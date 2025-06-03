import os.path
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal
import logging
from sbcbinaryformat import Writer as SBCWriter

class Writer(QObject):

    event_data_saved = Signal(str)

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
    def write_event_data(self, last_trigger):
        self.event_data = {
            "run_id": self.main.run_id,  # run id (str) e.g. 20240101_0
            "event_id": self.main.event_id,  # event id (int) e.g. 0
            "ev_livetime": self.main.event_livetime,  # event livetime (ms)
            "cum_livetime": self.main.run_livetime,  # cumulative livetime (ms)
            "pset": self.main.config_class.event_pressure["setpoint"],  # pressure setpoint (float)
            "pset_hi": self.main.config_class.event_pressure["setpoint_hi"],  # pressure setpoint high (float)
            "pset_slope": self.main.config_class.event_pressure["slope"],  # pressure setpoint slope (float)
            "pset_period": self.main.config_class.event_pressure["period"],  # pressure setpoint period (float)
            "trigger_source": last_trigger,  # trigger source (str)
        }
        headers = ["run_id", "event_id", "ev_exit_code", "ev_livetime", "cum_livetime", \
                   "pset", "pset_hi", "pset_slope", "pset_period", \
                   "start_time", "end_time", "trigger_source"]
        dtypes = ["U100", "u4", "u1", "u8", "u8", "f4", "f4", "f4", "f4", "U100"]
        shapes = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
        with SBCWriter(
                os.path.join(self.main.event_dir, f"event_info.sbc"),
                headers, dtypes, shapes,
        ) as event_writer:
            event_writer.write(self.event_data)
    
    @Slot()
    def write_run_data(self):
        run_data = {
            "run_id": self.main.run_id,
            "run_exit_code": self.main.run_exit_code,
            "num_events": self.main.num_events,
            "run_livetime": self.main.run_livetime,
            "run_start_time": self.main.run_start_time.timestamp(),
            "run_end_time": self.main.run_end_time.timestamp(),
        }
        headers = ["run_id", "run_exit_code", "num_events", "run_livetime", "run_start_time", "run_end_time"]
        dtypes = ["U100", "u1", "u4", "u8", "f8", "f8"]
        shapes = [[1], [1], [1], [1], [1], [1]]
        with SBCWriter(
                os.path.join(
                    self.main.run_dir, f"run_info.sbc"
                ),
                headers, dtypes, shapes
        ) as run_writer:
            run_writer.write(run_data)