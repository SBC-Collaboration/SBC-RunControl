import os.path
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal
import logging
from sbcbinaryformat import Writer as SBCWriter
import red_caen, ni_usb_6501, sbcbinaryformat

class Writer(QObject):

    event_stopped = Signal(str)
    run_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.config = mainwindow.config_class.config["general"]
        self.logger = logging.getLogger("rc")
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Writer module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def write_event_data(self):
        # wait until trig ff is ready
        self.main.trigff_mutex.lock()
        while not self.main.trigff_ready:
            self.main.trigff_wait.wait(self.main.trigff_mutex)
        self.main.trigff_mutex.unlock()

        self.event_data = {
            "run_id": self.main.run_id,  # run id (str) e.g. 20240101_0
            "event_id": self.main.event_id,  # event id (int) e.g. 0
            "ev_exit_code": self.main.event_exit_code,  # event exit code (int) e.g. 0
            "ev_livetime": self.main.event_livetime,  # event livetime (ms)
            "cum_livetime": self.main.run_livetime,  # cumulative livetime (ms)
            "pset": self.main.config_class.event_pressure["setpoint"],  # pressure setpoint (float)
            "pset_hi": self.main.config_class.event_pressure["setpoint_high"],  # pressure setpoint high (float)
            "pset_slope": self.main.config_class.event_pressure["slope"],  # pressure setpoint slope (float)
            "pset_period": self.main.config_class.event_pressure["period"],  # pressure setpoint period (float)
            "start_time": self.main.event_start_time.timestamp(),  # event start time (float)
            "end_time": self.main.event_end_time.timestamp(),  # event end time (float)
            "trigger_source": self.main.ui.trigger_edit.text(),  # trigger source (str)
        }
        headers = ["run_id", "event_id", "ev_exit_code", "ev_livetime", "cum_livetime",
                   "pset", "pset_hi", "pset_slope", "pset_period",
                   "start_time", "end_time", "trigger_source"]
        dtypes = ["U100", "u4", "u1", "u8", "u8", "f", "f", "f", "f", "d", "d", "U100"]
        shapes = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
        with SBCWriter(
                os.path.join(self.main.event_dir, f"event_info.sbc"),
                headers, dtypes, shapes,
        ) as event_writer:
            event_writer.write(self.event_data)
        
        self.event_stopped.emit("writer")
    
    @Slot()
    def write_run_data(self):
        run_data = {
            "run_id": self.main.run_id,
            "run_exit_code": self.main.run_exit_code,
            "num_events": self.main.event_id,
            "run_livetime": self.main.run_livetime,
            "comment": self.main.ui.comment_edit.toPlainText() or "",
            "run_start_time": self.main.run_start_time.timestamp(),
            "run_end_time": self.main.run_end_time.timestamp(),
            "active_datastreams": "", 
            "pset_mode": self.main.config_class.run_pressure_mode,
            "pset": self.main.config_class.run_pressure_profiles[0]["setpoint"]
                if len(self.main.config_class.run_pressure_profiles)==1 else None, 
            "source1_ID": self.main.ui.source_box.currentText() or "",
            "source1_location": self.main.ui.source_location_box.currentText() or "",
            "red_caen_ver": red_caen.__version__,
            "niusb_ver": ni_usb_6501.__version__,
            "sbc_binary_ver": sbcbinaryformat.__version__,
        }
        comment_len = len(run_data["comment"]) if run_data["comment"] else 1
        headers = ["run_id", "run_exit_code", "num_events", "run_livetime", "comment", 
                   "run_start_time", "run_end_time", "active_datastreams", "pset_mode", "pset",
                   "source1_ID", "source1_location", "red_caen_ver", "niusb_ver", "sbc_binary_ver"]
        dtypes = ["U100", "u1", "u4", "u8", f"U{comment_len}", 
                  "d", "d", "U100", "U100", "f",
                  "U100", "U100", "U100", "U100", "U100"]
        shapes = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
        with SBCWriter(
                os.path.join(
                    self.main.run_dir, f"run_info.sbc"
                ),
                headers, dtypes, shapes
        ) as run_writer:
            run_writer.write(run_data)

        self.run_stopped.emit("writer")
