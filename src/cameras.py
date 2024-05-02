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
        if not subprocess.call(f"ping -c 1 -W 1 {host}", shell=True):
            self.logger.debug(f"Camera {self.cam_name} connected.")
        else:
            self.logger.error(f"Camera {self.cam_name} at {host} not connected.")
            # raise ConnectionError

    @Slot()
    def start_camera(self):
        # use run config, which is stable during a run
        self.config = self.main.config_class.run_config["cam"][self.cam_name]

        if not self.config["enabled"]:
            self.logger.info(f"Camera {self.cam_name} disabled.")
            return
        else:
            self.test_rpi()
        # self.save_config()
        self.logger.info(f"Starting camera {self.cam_name}")
        # make ssh connection
        self.client.connect(self.config["ip_addr"], username=self.username)
        time.sleep(2)

        # start executing command
        command = "cd /home/pi/RPi_CameraServers && python3 imdaq.py"
        transport = self.client.get_transport()
        channel = transport.open_session()
        channel.exec_command(command)
        self.camera_started.emit(self.cam_name)

    @Slot()
    def stop_camera(self):
        self.client.close()
        self.camera_closed.emit(self.cam_name)
