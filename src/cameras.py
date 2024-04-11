import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import paramiko as pm
import logging
import os
import json
from PySide6.QtCore import QTimer, QObject, Slot


class Cameras(QObject):
    def __init__(self, main_window, cam_name):
        super().__init__()
        self.main = main_window
        self.cam_name = cam_name
        self.config = main_window.config_class.config
        self.logger = logging.getLogger("rc")
        os.putenv("PATH", "/home/sbc/packages")
        self.username = "pi"
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
        self.logger.debug(f"Cameras class {self.cam_name} initialized.")
        self.timer = QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.periodic_task)

    def run(self):
        self.timer.start()

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def start_run(self):
        self.start_camera()

    def exec_commands(self, host, commands):
        self.client.connect(host, username=self.username)
        for command in commands:
            _stdin, _stdout, _stderr = self.client.exec_command(command)
            self.logger.info(_stdout.read())
        self.client.close()

    def save_config(self):
        cam_config = self.config["cam"][self.cam_name].copy()
        # skip camera if not enabled
        if not cam_config["enabled"]:
            return
        cam_config["data_path"] = os.path.join(cam_config["data_path"], self.main.run_id, str(self.main.event_id))
        with open(cam_config["rc_config_path"], "w") as file:
            json.dump(cam_config, file, indent=2)
        self.logger.info(f"Configuration file saved for {self.cam_name}")

    def start_camera(self):
        self.save_config()
        commands = ["cd /home/pi/RPi_CameraServers", "python3 imdaq.py"]
        cam_config = self.config["cam"][self.cam_name]
        if not cam_config["enabled"]:
            return
        self.exec_commands(cam_config["ip_addr"], commands)
