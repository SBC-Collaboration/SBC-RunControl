from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import logging

# Error code list: https://docs.google.com/spreadsheets/d/1l-7dthFAcyHkQRA3YD875fsAcTKyn0Vgf3X5fvdhq5I/edit?gid=0#gid=0

class Guardian(QObject):
    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")

        self.timer = QTimer(self)
        self.timer.setInterval(100)  # ms
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Guardian module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def error_handler(self, error_message):
        self.logger.error(f"Error received: {error_message}")
