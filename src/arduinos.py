import os
import subprocess
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
        elif not (archives := glob.glob(os.path.join(build_path, "*.zip"))):
            # check if a zip file exists in the build folder, without in the filename
            checksum = 0
            self.logger.debug(f"Sketch archive doesn't exist for {self.arduino} arduino.")
        elif len(archives)==1:
            # generate checksum for old zip file
            with open(archives[0], "rb") as f:
                checksum = hashlib.sha256(f.read()).digest()
        else:
            self.logger.error(f"More than one sketch archive for {self.arduino} arduino.")
            cheskum = 0

        # generate a new zip archive of sketch
        os.environ["PATH"] += os.pathsep + os.path.join(os.path.dirname(os.path.dirname(__file__)), "dependencies")
        command = (f"cd {sketch_path} && rm -f {build_path}/*.zip && "
                   f"arduino-cli sketch archive {sketch_path} {build_path}")
        result = subprocess.run(command, shell=True, capture_output=True)
        # self.logger.debug(result.stdout)

        # check if hash of new archive is the same as the old
        if (archives := glob.glob(os.path.join(build_path, "*.zip"))) and len(archives)==1:
            with open(archives[0], "rb") as f:
                if checksum == hashlib.sha256(f.read()).digest():
                    self.logger.info(f"Sketch for {self.arduino} arduino not changed. Skipping upload.")
                    self.arduino_sketch_uploaded.emit(self.arduino)
                    return

        # if not the same, compile and upload
        command = (f"cd {sketch_path} && "
                   f"arduino-cli compile -b {fqbn} --build-path {build_path} {sketch_path} && "
                   f"arduino-cli upload -p {port} -b {fqbn} --input-dir {build_path}")
        result = subprocess.run(command, shell=True, capture_output=True)
        self.logger.info(f"Sketch successfully uploaded for {self.arduino} arduino.")

        self.arduino_sketch_uploaded.emit(self.arduino)
