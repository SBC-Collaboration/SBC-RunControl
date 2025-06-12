import os
import logging
from PySide6.QtCore import QTimer, QElapsedTimer, QObject, Slot, Signal, QThread
from sbcbinaryformat import Writer as SBCWriter
import socket
import struct
import numpy as np

class Digiscope(QObject):
    poll_active = False
    digiscope_data = []
    run_started = Signal(str)
    run_stopped = Signal(str)
    event_started = Signal(str)
    event_stopped = Signal(str)
    error_msg = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.config = self.main.config_class.config["digiscope"]
        self.client = None

        self.timer = QTimer(self)
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Digiscope module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        if (self.enabled and self.poll_active):
            pass # poll as needed

    @Slot()
    def start_run(self):
        self.config = self.main.config_class.run_config["digiscope"]
        self.enabled = self.config["enabled"]
        if not self.enabled:
            self.run_started.emit("digiscope-disabled")
            return

        self.client = socket.create_connection((self.config["hostname"], self.config["port"]))
        try:
            pass
        except Exception as e:
            self.logger.error(f"Digiscope TPC connection failed: {e}.")
        self.run_started.emit("digiscope")


    @Slot()                                                                      
    def start_event(self):
        if not self.enabled:
            self.event_started.emit("digiscope-disabled")
            return
        # make first poll here
        self.poll_active = True
        self.event_started.emit("digiscope")

    @Slot()
    def stop_event(self):
        if not self.enabled:
            self.event_stopped.emit("digiscope-disabled")
            return
        
        self.poll_active = False
        # write the digiscope data in a file
        with SBCWriter(
                os.path.join(
                    self.main.event_dir, "digiscope.sbc"
                ),
                headers, dtypes, shapes
        ) as digiscope_writer:
            digiscope_writer.write(self.digiscope_data)
                    

        self.event_stopped.emit("digiscope")

    @Slot()
    def stop_run(self):
        if not self.enabled:
            self.run_stopped.emit("digiscope-disabled")
            return
        
        self.client.close()
        self.run_stopped.emit("digiscope")
    