from dependencies.NI_USB6501.ni_usb_6501 import *
import logging

class NIUSB:
    def __init__(self, main_window):
        self.main = main_window
        self.config = main_window.config_class.config
        self.logger = logging.getLogger("rc")
        self.logger.debug("NI_USB class initialized.")
        self.dev = get_adapter()
        if not self.dev:
            self.logger.error("NI USB device not found!")

        self.dev.set_io_mode(0b11111111, 0b11111111, 0b00000000)

        self.dev.write_port(0, 0b11001100)

        print(f"Channel 0: {self.dev.read_port(0):08b}")
