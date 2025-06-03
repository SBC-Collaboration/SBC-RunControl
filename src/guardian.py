from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread

class SQL(QObject):
    run_started = Signal(str)
    run_stopped = Signal(str)
    event_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"SQL module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def start_run(self):
        pass

    @Slot()
    def stop_run(self):
        pass
    
    @Slot()
    def start_event(self):
        pass

    @Slot()
    def stop_event(self):
        pass