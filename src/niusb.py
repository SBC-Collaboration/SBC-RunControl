from dependencies.NI_USB6501.ni_usb_6501 import *
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal

class NIUSB(QObject):
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
    def start_run(self):
        self.check_niusb()
        self.dev = get_adapter()
        if not self.dev:
            self.logger.error("NI USB device not found!")

        self.dev.set_io_mode(0b11111111, 0b11111111, 0b00000000)
        self.dev.write_port(0, 0b11001100)
        pass

    @Slot()
    def start_event(self):
        pass
