import paramiko as pm
import logging
import os
import json

class Cameras:
    def __init__(self, main_window):
        self.main = main_window
        self.config = main_window.config_class.config
        self.logger = logging.getLogger("rc")
        os.putenv("PATH", "/home/sbc/packages")
        self.username = "pi"
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
        self.logger.debug("Cameras class initialized.")

    def exec_commands(self, host, commands):
        self.client.connect(host, username=self.username)
        for command in commands:
            _stdin, _stdout, _stderr = self.client.exec_command(command)
            self.logger.info(_stdout.read())
        self.client.close()

    def save_config(self):
        for cam in ["cam1", "cam2", "cam3"]:
            cam_config = self.config["cam"][cam].copy()
            # skip camera if not enabled
            if not cam_config["enabled"]:
                continue
            cam_config["data_path"] = os.path.join(cam_config["data_path"], self.main.run_id, str(self.main.ev_number))
            with open(cam_config["rc_config_path"], "w") as file:
                json.dump(cam_config, file, indent=2)
            self.logger.info(f"Configuration file saved for {cam}")

    def start_camera(self):
        self.save_config()
        commands = ["cd /home/pi/RPi_CameraServers", "python3 imdaq.py"]
        for cam in ["cam1", "cam2", "cam3"]:
            cam_config = self.config["cam"][cam]
            if not cam_config["enabled"]:
                continue
            self.exec_commands(cam_config["ip_addr"], commands)
