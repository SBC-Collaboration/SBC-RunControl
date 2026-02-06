import os
import numpy as np
import time
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread

class Wait(QObject):
    event_started = Signal(str)
    event_stopped = Signal(str)
    error = Signal(int)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.stop_event_wait = 60*1000  #ms

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

        self.wait_timer = QTimer(self)
        self.wait_timer.setSingleShot(True)
        self.wait_timer.timeout.connect(self.finish_stop_event)
    
    @Slot() 
    def run(self):
        self.timer.start()
        self.logger.debug(f"Wait: Module initialized in {QThread.currentThread().objectName()}.")
    
    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def stop_event(self):
        self.logger.debug("Wait: Stopping event, starting wait timer.")
        self.wait_timer.start(self.stop_event_wait)
        
    @Slot()
    def finish_stop_event(self):
        self.logger.debug("Wait: Wait timer finished.")
        self.event_stopped.emit("wait")
