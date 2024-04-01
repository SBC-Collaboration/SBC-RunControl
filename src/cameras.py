import paramiko as pm
import logging
import os

class Cameras:
    def __init__(self, main_window):
        self.main = main_window
        self.config = main_window.config_class.config
        self.logger = logging.getLogger("rc")
        os.putenv("PATH", "/home/sbc/packages")
        self.username = "pi"
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
        self.save_config()
        self.logger.debug("Cameras class initialized.")

    def connect_camera(self, host, command):
        self.client.connect(host, username=self.username)
        _stdin, _stdout, _stderr = self.client.exec_command(command)
        # print(_stdout.read().decode())
        self.client.close()

    def save_config(self):
        for cam in ["cam1", "cam2", "cam3"]:
            cam_config = self.main.config_class.config["cam"][cam]
            # print(cam_config)