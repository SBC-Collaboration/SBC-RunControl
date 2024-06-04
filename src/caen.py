import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal
from collections import namedtuple
import copy


class Caen(QObject):
    caen_started = Signal(str)
    caen_stopped = Signal(str)

    def __init__(self, mainwindow, cam_name):
        super().__init__()
        self.main = mainwindow
        self.config = mainwindow.config_class.config["scint"]["caen"]
        self.gp_config = {
            "g0": mainwindow.config_class.config["scint"]["caen_g0"],
            "g1": mainwindow.config_class.config["scint"]["caen_g1"],
            "g2": mainwindow.config_class.config["scint"]["caen_g2"],
            "g3": mainwindow.config_class.config["scint"]["caen_g3"]
        }