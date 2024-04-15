import os
import glob
import hashlib
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal

class Arduino(QObject):
    arduino_sketch_uploaded = Signal(str)

    def __init__(self, mainwindow, arduino):
        super().__init__()
        self.main = mainwindow
        self.arduino = arduino
        self.config = mainwindow.config_class.config["dio"]["arduinos"][arduino]
        self.logger = logging.getLogger("rc")
        os.putenv("PATH", "/home/sbc/packages")
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Arduino {self.arduino} module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def check_arduino(self):
        try:
            os.stat(self.config["port"])
        except:
            self.logger.error(f"Arduino {self.arduino} not connected.")
            return 1
        self.logger.debug(f"Arduino {self.arduino} connected")
        return 0

    @Slot()
    def upload_sketch(self):
        if self.check_arduino():
            return
        # TODO: copy json
        fqbn = "arduino:avr:mega"
        port = self.config["port"]
        sketch_path = self.config["sketch"]
        build_path = os.path.join(sketch_path, "build")
        if not os.path.exists(build_path):
            os.mkdir(build_path)
            checksum = 0
        elif not (hex_files := glob.glob(os.path.join(build_path, "*.ino.hex"))):
            # check if a .hex file exists in the build folder, without "bootloader" in the filename
            checksum = 0
            self.logger.debug(f"Binary file doesn't exist for {self.arduino} arduino.")
        elif len(hex_files)==1:
            # generate checksum for old binary file
            with open(hex_files[0], "rb") as f:
                checksum = hashlib.sha256(f.read()).digest()
        else:
            self.logger.error(f"More than one compiled binary files for {self.arduino} arduino.")

        os.environ["PATH"] += os.pathsep + os.path.join(os.path.dirname(os.path.dirname(__file__)), "dependencies")
        os.system(f"cd {sketch_path} && arduino-cli compile -b {fqbn} --build-path {build_path} {sketch_path}")
        hex_files_new = glob.glob(os.path.join(build_path, "*.ino.hex"))
        with open(hex_files_new[0], "rb") as f:
            # comparing the new compiled binary file with old checksum
            # if there is no difference, then skip uploading
            checksum_new = hashlib.sha256(f.read()).digest()
            if checksum == checksum_new:
                self.logger.info(f"Sketch for {self.arduino} arduino not changed. Skipping upload.")
            else:
                os.system(f"arduino-cli upload -p {port} -b {fqbn} --input-dir {build_path}")
                self.logger.info(f"Sketch successfully uploaded for {self.arduino} arduino.")

        self.arduino_sketch_uploaded.emit(self.arduino)
