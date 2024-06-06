import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
from collections import namedtuple
import copy


class Caen(QObject):
    caen_started = Signal(str)
    caen_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.config = mainwindow.config_class.config["scint"]["caen"]
        self.gp_config = {
            "g0": mainwindow.config_class.config["scint"]["caen_g0"],
            "g1": mainwindow.config_class.config["scint"]["caen_g1"],
            "g2": mainwindow.config_class.config["scint"]["caen_g2"],
            "g3": mainwindow.config_class.config["scint"]["caen_g3"]
        }

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Caen module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass