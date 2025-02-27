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
        ev_number = [int(i) for i in self.main.run_id.split("_")]
        ev_number.append(self.main.event_id)
        self.event_data = {
            "event_id": ev_number,
            # list of date, run number, event number: [20240101, 0, 0]
            "ev_livetime": self.main.event_livetime,  # event livetime (ms)
            "run_livetime": self.main.run_livetime,  # event livetime (ms)
            "trigger_source": last_trigger,  # trigger source (str)
        }
        with SBCWriter(
                os.path.join(
                    self.main.event_dir, f"event_info.sbc"
                ),
                ["event_id", "ev_livetime", "run_livetime", "trigger_source"],
                ["u4", "u8", "u8", "U100"],
                [[3], [1], [1], [1]],
        ) as event_writer:
            event_writer.write(self.event_data)