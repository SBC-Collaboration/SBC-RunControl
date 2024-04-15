import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import paramiko as pm
import logging
import os
import json
import time
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal
import subprocess


class Camera(QObject):
    camera_started = Signal(str)
    camera_connected = Signal(str)
    camera_closed = Signal(str)

    def __init__(self, mainwindow, cam_name):
        super().__init__()
        self.main = mainwindow
        self.cam_name = cam_name
        self.config = mainwindow.config_class.config["cam"][self.cam_name]
        self.logger = logging.getLogger("rc")
        os.putenv("PATH", "/home/sbc/packages")
        self.username = "pi"
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Camera {self.cam_name} module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def test_rpi(self):
        if not self.config["enabled"]:
            return
        host = self.config["ip_addr"]

        # ping with 1 packet, and 1s timeout
        command = ["ping", "-c", "1", "-W", "1", host]
        if not subprocess.call(command):
            self.logger.debug(f"Camera {self.cam_name} connected.")
        else:
            self.logger.error(f"Camera {self.cam_name} at {host} not connected.")
            raise ConnectionError

    def save_config(self):
        # skip camera if not enabled
        if not self.config["enabled"]:
            return
        cam_config = self.config.copy()
        cam_config["data_path"] = os.path.join(cam_config["data_path"], self.main.run_id, str(self.main.event_id))
        with open(cam_config["rc_config_path"], "w") as file:
            json.dump(cam_config, file, indent=2)
        self.logger.info(f"Configuration file saved for {self.cam_name}")

    @Slot()
    def start_camera(self):
        if not self.config["enabled"]:
            self.logger.info(f"Camera {self.cam_name} disabled.")
            return
        else:
            self.test_rpi()
        self.save_config()
        self.logger.info(f"Starting camera {self.cam_name}")
        # make ssh connection
        self.client.connect(self.config["ip_addr"], username=self.username)
        self.camera_started.emit(self.cam_name)
        time.sleep(3)

        # start executing command
        commands = ["cd /home/pi/RPi_CameraServers && python3 imdaq.py"]
        for command in commands:
            _stdin, _stdout, _stderr = self.client.exec_command(command)
            self.logger.debug(_stdout.read())
            self.logger.debug(_stderr.read())
        self.client.close()
        self.camera_closed.emit(self.cam_name)

