from dependencies.NI_USB6501.ni_usb_6501 import *
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal

class NIUSB(QObject):
    pin_definition = { # input / output from run control
        "trig": "out", #trigger
        "latch": "in", # trigger latch
        "reset": "out", # trigger reset
        "state_cam1": "in", # state confirmation from pi
        "comm_cam1": "out", # state comm to pi
        "trigen-cam1": "out", # trigger enable signal
        "state_cam2": "in",
        "comm_cam2": "out",
        "trigen_cam2": "out",
        "state_cam3": "in",
        "comm_cam3": "out",
        "trigen_cam3": "out",
        "trigff_rc": "in", # trigger first fault, run control
        "trigff_p": "in", # pressure
        "trigff_but": "in", # external button
        "trigff_cam1": "in", # camera video trigger
        "trigff_cam2": "in",
        "trigff_cam3": "in",
        "trigff_piezo": "in", # piezo acoustic trigger
        "trigff_ar": "in", # Kulite trigger for Ar
        "trigff_cf4": "in", # kulite trigger for CF4
        # and more ...
    }

    event_started = Signal(str)

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
            except:
                self.logger.error(f"Pin {k} {self.config[k]} invalid.")
        # convert an array of 1s and 0s to binary mask
        io_mask = [int("".join(str(bit) for bit in mask),2) for mask in io]

        self.dev.set_io_mode(*io_mask)
        io_set.emit("nuisb")

    @Slot()
    def start_event(self):
        pass
