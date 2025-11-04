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

    col_headers = ['FPGAframes_ntrans','cRIOframes_ntrans','ix','t_ticks','dt_ticks','DI']
    col_dtypes = ['i4','i4','u4','u4','u4','u4']
    col_dsizes = [1,1,1,1,1,2]

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.config = self.main.config_class.config["digiscope"]
        self.client = None

        self.timer = QTimer(self)
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.periodic_task)

    def poll(self):
        if self.client is not None:
            try:
                self.client.send(b'x')
                records_cRIO = np.frombuffer(self.client.recv(4, socket.MSG_WAITALL),
                                             '>i4')
                records_ready = np.frombuffer(self.client.recv(4, socket.MSG_WAITALL),
                                              '>i4')
                datachunk = np.frombuffer(self.client.recv(20*records_ready[0], socket.MSG_WAITALL),
                                          '>u4').reshape((records_ready[0],5))
                datapreamble0 = np.zeros((records_ready[0]), dtype=np.int32)
                datapreamble0[0] = records_cRIO
                datapreamble1 = np.zeros((records_ready[0]), dtype=np.int32)
                datapreamble1[0] = records_ready
                datadict = {self.col_headers[0]: datapreamble0,
                            self.col_headers[1]: datapreamble1,
                            self.col_headers[2]: datachunk[:,0].astype(np.uint32),
                            self.col_headers[3]: datachunk[:,1].astype(np.uint32),
                            self.col_headers[4]: datachunk[:,2].astype(np.uint32),
                            self.col_headers[5]: datachunk[:,3:].astype(np.uint32)}
                self.digiscope_data.append(datadict)
            except Exception as e:
                self.logger.error(f"Digiscope TCP data poll failed: {e}.")

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Digiscope module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        if (self.enabled and self.poll_active):
            self.poll()

    @Slot()
    def start_run(self):
        self.config = self.main.config_class.run_config["digiscope"]
        self.enabled = self.config["enabled"]
        if not self.enabled:
            self.run_started.emit("digiscope-disabled")
            return
            
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.config["hostname"], self.config["port"]))
        except Exception as e:
            self.logger.error(f"Digiscope TCP connection failed to open: {e}.")
        self.run_started.emit("digiscope")


    @Slot()                                                                      
    def start_event(self):
        if not self.enabled:
            self.event_started.emit("digiscope-disabled")
            return
        self.digiscope_data.clear()
        self.poll() # make initial poll
        self.poll_active = True
        self.event_started.emit("digiscope")

    @Slot()
    def stop_event(self):
        if not self.enabled:
            self.event_stopped.emit("digiscope-disabled")
            return
        self.poll_active = False
        self.poll() # make final poll
        # write the digiscope data in a file
        with SBCWriter(
                os.path.join(
                    self.main.event_dir, "digiscope.sbc"
                ),
                self.col_headers, self.col_dtypes, self.col_shapes
        ) as digiscope_writer:
            digiscope_writer.write(self.digiscope_data)

        self.digiscope_data.clear()
        self.event_stopped.emit("digiscope")

    @Slot()
    def stop_run(self):
        if not self.enabled:
            self.run_stopped.emit("digiscope-disabled")
            return
        try:
            self.client.close()
        except Exception as e:
            self.logger.error(f"Digiscope TCP connection failed to close: {e}.")
        self.client = None
        self.run_stopped.emit("digiscope")
    
