import os
import logging

class Arduino:
    def __init__(self, main_window):
        self.main_window = main_window
        self.config = main_window.config_class.config
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.StreamHandler())
        os.system("whoami")
        os.putenv("PATH", "/home/sbc/packages")
        self.upload_sketch("clock")

        self.logger.debug("Arduino class initialized.")

    def upload_sketch(self, name):
        fqbn = "arduino:avr:mega"
        port = self.config["dio"]["general"][name]["port"]
        sketch_path = self.config["dio"]["general"][name]["sketch"]
        build_path = os.path.join(sketch_path, "build")

        os.system(f"arduino-cli compile -b {fqbn} --build-path {build_path} {sketch_path}")
        os.system(f"arduino-cli upload -p {port} -b {fqbn} --input-dir {build_path}")

