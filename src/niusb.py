from dependencies.NI_USB6501.ni_usb_6501 import *
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal
import numpy as np
import os

class NIUSB(QObject):
    pin_definition = {  # input / output from run control
        "trig": "output",  # trigger
        "latch": "input",  # trigger latch
        "reset": "output",  # trigger reset
        "state_cam1": "input",  # state confirmation from pi
        "comm_cam1": "output",  # state comm to pi
        "trigen-cam1": "output",  # trigger enable signal
        "state_cam2": "input",
        "comm_cam2": "output",
        "trigen_cam2": "output",
        "state_cam3": "input",
        "comm_cam3": "output",
        "trigen_cam3": "output",
        "trigff_rc": "input",  # trigger first fault, run control
        "trigff_p": "input",  # pressure
        "trigff_but": "input",  # external button
        "trigff_cam1": "input",  # camera video trigger
        "trigff_cam2": "input",
        "trigff_cam3": "input",
        "trigff_piezo": "input",  # piezo acoustic trigger
        "trigff_ar": "input",  # Kulite trigger for Ar
        "trigff_cf4": "input",  # kulite trigger for CF
        "": "input",
        # and more ...
    }

    pins_set = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.config = mainwindow.config_class.config
        self.logger = logging.getLogger("rc")

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"NI_USB class initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def check_niusb(self):
        try:
            os.stat(self.config["dio"]["port"])
        except:
            self.logger.error(f"NIUSB not connected.")
        self.logger.debug(f"Arduino connected")

    @Slot()
    def set_pins(self):
        self.check_niusb()
        self.dev = get_adapter()
        if not self.dev:
            self.logger.error("NI USB device not found!")

        self.config = self.main.config_class.config["dio"]["niusb"]
        self.reverse_config = {}
        io = np.zeros([3,8], dtype=int)
        # use output/input table to get io mask
        # if undefined, set as input
        for k in self.config.keys():
            port, pin = [int(s) for s in k.split(".")]
            try:
                self.reverse_config[self.config[k]] = (port, pin)
                if self.pin_definition[self.config[k]] == "output":
                    io[port, pin] = 1
                else:
                    io[port, pin] = 0  # check again to make sure port, pin in range
            except IndexError:
                self.logger.error(f"Pin {k} {self.config[k]} invalid.")
                continue
        # convert an array of 1s and 0s to binary mask
        io_mask = [int("".join(str(bit) for bit in mask),2) for mask in io]

        self.dev.set_io_mode(*io_mask)
        self.pins_set.emit("nuisb")

    @Slot()
    def start_event(self):
        pass
