import os
import subprocess
import glob
import hashlib
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal


class Arduino(QObject):
    # A map of pin number to port in Arduino Mega 2560
    # Pin number is digital pin number (number on board)
    # The letter is port name, and the number is location in the port
    # It is ordered roughly according to the placement on the board
    arduino_port_map = {
        13: "B7",
        12: "B6",
        11: "B5",
        10: "B4",
        9:  "H6",
        8:  "H5",
        7:  "H4",
        6:  "H3",
        5:  "E3",
        4:  "G5",
        3:  "E5",
        2:  "E4",
        1:  "E1",
        0:  "E0",
        14: "J1",
        15: "J0",
        16: "H1",
        17: "H0",
        18: "D3",
        19: "D2",
        20: "D1",
        21: "D0",
        22: "A0",
        23: "A1",
        24: "A2",
        25: "A3",
        26: "A4",
        27: "A5",
        28: "A6",
        29: "A7",
        30: "C7",
        31: "C6",
        32: "C5",
        33: "C4",
        34: "C3",
        35: "C2",
        36: "C1",
        37: "C0",
        38: "D7",
        39: "G2",
        40: "G1",
        41: "G0",
        42: "L7",
        43: "L6",
        44: "L5",
        45: "L4",
        46: "L3",
        47: "L2",
        48: "L1",
        49: "L0",
        50: "B3",
        51: "B2",
        52: "B1",
        53: "B0",
    }
    reverse_port_map = {}

    sketch_uploaded = Signal(str)

    def __init__(self, mainwindow, arduino):
        super().__init__()
        self.main = mainwindow
        self.arduino = arduino
        self.config = mainwindow.config_class.config["dio"][arduino]
        self.logger = logging.getLogger("rc")
        os.putenv("PATH", "/home/sbc/packages")
        # create reverse port map
        for pin, port in self.arduino_port_map.items():
            self.reverse_port_map[port] = pin
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
        self.config = self.main.config_class.run_config["dio"][self.arduino]
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

        # check if hash of new archive is the same as the old
        if (archives := glob.glob(os.path.join(build_path, "*.zip"))) and len(archives)==1:
            with open(archives[0], "rb") as f:
                if checksum == hashlib.sha256(f.read()).digest():
                    self.logger.info(f"Sketch for {self.arduino} arduino not changed. Skipping upload.")
                    self.sketch_uploaded.emit(self.arduino)
                    return

        # if not the same, compile and upload
        command = (f"cd {sketch_path} && "
                   f"arduino-cli compile -b {fqbn} --build-path {build_path} {sketch_path} && "
                   f"arduino-cli upload -p {port} -b {fqbn} --input-dir {build_path}")
        result = subprocess.run(command, shell=True, capture_output=True)
        if result.returncode:
            self.logger.error(f"Sketch upload for {self.arduino} failed.")
            self.logger.error(result.stderr.decode("utf-8"))
            command = f"cd {sketch_path} && rm -f {build_path}/*.zip"
            result = subprocess.run(command, shell=True, capture_output=True)
            return
        self.logger.info(f"Sketch successfully uploaded for {self.arduino} arduino.")
        self.sketch_uploaded.emit(self.arduino)
