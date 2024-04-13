import os
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

        os.system(f"arduino-cli compile -b {fqbn} --build-path {build_path} {sketch_path}")
        os.system(f"arduino-cli upload -p {port} -b {fqbn} --input-dir {build_path}")
        self.logger.info(f"Sketch uploaded for {self.arduino} is completed.")

