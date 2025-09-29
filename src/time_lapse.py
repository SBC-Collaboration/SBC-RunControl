import os
import paramiko as pm
from functools import wraps
from pymodbus.client import ModbusTcpClient
import struct
import argparse
import time
import threading

# This standalone python script to periodically take images using multiple cameras
# to create a time-lapse video.
# It connects to the PLC and sets LED control voltage for the duration of image-taking.
# The images are saved to `rc-data/images/` folder on the NAS.

# Run this script in a screen using the following command:
# screen -S camera_time_lapse -dm python3 time_lapse.py -t 20 -n 0
# parameters:
# -t, --time: time interval between frames in seconds (default: 60)
# -n, --num_frames: number of frames to take (default: 1, use 0 for infinite)

config = {
    "modbus": {
        "hostname": "192.168.137.11",
        "port": 502,
        "registers": {
            "LED1_OUT": 16824,
            "LED2_OUT": 16826,
            "LED3_OUT": 16828,
            "LED_MAX": 16830,
        }
    },
    "led1_control": 0.05,
    "led2_control": 0.05,
    "led3_control": 0.05,
    "led_control_max": 0.3,
    "cam1": {
        "ip_addr": "192.168.137.101",
        "user": "pi"
    },
    "cam2": {
        "ip_addr": "192.168.137.102",
        "user": "pi"
    },
    "cam3": {
        "ip_addr": "192.168.137.103",
        "user": "pi"
    }
}

def safe_modbus(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            pos = kwargs.get('pos') if 'pos' in kwargs else args[1] if len(args) > 1 else '?'
            print(f"ERROR in {func.__name__} at register {pos}: {e}")
            return None
    return wrapper

@safe_modbus
def _write_float(client, pos, value, endian='<'):
    """Write a 32-bit float value to two words at a Modbus register.

    Args:
        pos (int): The register position to write to.
        value (float): The 32-bit float value to write.
        endian (str, optional): The byte order to use. Defaults to '<'.

    Returns:
        bool: True if the write was successful, None otherwise.
    """
    # PARAM_F
    fl = float(value)
    bytes = struct.pack(f'{endian}f', fl)
    words = struct.unpack(f'{endian}HH', bytes)
    response = client.write_registers(pos, words)
    return True

def _ssh_cam(cam_config):
    ip_addr = cam_config["ip_addr"]
    user = cam_config["user"]
    ssh_client = pm.client.SSHClient()
    ssh_client.set_missing_host_key_policy(pm.AutoAddPolicy())

    # run the command to take a single frame
    try:
        print(f"Connecting to camera at {ip_addr}...")
        ssh_client.connect(ip_addr, username=user, timeout=30)
        command = "cd /home/pi/RPi_CameraServers && python3 imdaq.py -s"
        stdin, stdout, stderr = ssh_client.exec_command(command, get_pty=True)

        for line in stdout:
            print(line.rstrip("\r\n"))
    except Exception as e:
        print(f"ERROR in _ssh_cam for {ip_addr}: {e}")
    finally:
        ssh_client.close()

def take_frame():
    # set up symlink
    current_path = "/mnt/nas/rc-data/current_event"
    event_dir = "/mnt/nas/rc-data/images/"
    if os.path.islink(current_path):
        os.unlink(current_path)
    os.symlink(event_dir, current_path, target_is_directory=True)

    # connect to PLC modbus
    modbus_config = config["modbus"]
    modbus_client = ModbusTcpClient(modbus_config["hostname"], port=modbus_config["port"])
    try:
        connected = modbus_client.connect()
        print(f"Beckoff PLC connected: {str(connected)}.")
    except Exception as e:
        print(f"Beckoff PLC connection failed: {e}.")

    # turn on LEDs
    registers = modbus_config["registers"]
    ret = True
    ret = ret and _write_float(modbus_client, registers["LED_MAX"], config["led_control_max"])
    ret = ret and _write_float(modbus_client, registers["LED1_OUT"],
        min(config["led1_control"], config["led_control_max"]))
    ret = ret and _write_float(modbus_client, registers["LED2_OUT"],
        min(config["led2_control"], config["led_control_max"]))
    ret = ret and _write_float(modbus_client, registers["LED3_OUT"],
        min(config["led3_control"], config["led_control_max"]))
    if ret:
        print(f"Writing of LED control voltages successful.")
    else:
        print(f"Writing of LED control voltages failed.")

    # set up ssh connection in threads
    cam_threads = []
    for cam in ["cam1", "cam2", "cam3"]:
        thread = threading.Thread(target=_ssh_cam, args=(config[cam],))
        cam_threads.append(thread)
        thread.start()

    # wait for all camera threads to finish
    for thread in cam_threads:
        thread.join()

    # turn off LEDs
    ret = True
    ret = ret and _write_float(modbus_client, registers["LED1_OUT"], 0)
    ret = ret and _write_float(modbus_client, registers["LED2_OUT"], 0)
    ret = ret and _write_float(modbus_client, registers["LED3_OUT"], 0)
    if ret:
        print(f"LED control voltages successfully changed to 0.")
    else:
        print(f"Writing of LED control voltages failed.")

    # close modbus connection
    modbus_client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run time-lapse frame capture.")
    parser.add_argument("-t", "--time", type=int, default=60, help="Interval in seconds between frames")
    parser.add_argument("-n", "--num_frames", type=int, default=1, help="Number of frames taken")
    args = parser.parse_args()
    time_interval = args.time
    num_frames = args.num_frames
    frame_count = 0
    interrupted = False
    print(f"Starting time-lapse capture: {num_frames} frames at {time_interval} second intervals.")

    try:
        while num_frames == 0 or frame_count < num_frames and not interrupted:
            timestamp = time.monotonic()
            print("Taking frame...")
            take_frame()
            print(f"Frame {frame_count+1}/{num_frames} taken.\n")
            frame_count += 1

            # wait until next frame
            if num_frames == 0 or frame_count < num_frames:
                print(f"Waiting {time_interval} seconds until next frame...")
                while time.monotonic() - timestamp < time_interval and not interrupted:
                    time.sleep(0.01)
    except KeyboardInterrupt:
        # If currently during capture, will wait until it finishes.
        interrupted = True
        print("Capture interrupted.")
