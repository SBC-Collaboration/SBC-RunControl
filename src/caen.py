import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
from collections import namedtuple
import copy
import json


class Caen(QObject):
    caen_started = Signal(str)
    caen_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.scint_config = self.main.config_class.config["scint"]

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Caen module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def start_event(self):
        self.config = {}

        # translate between run control config keys and caen config keys
        self.scint_config = self.main.config_class.run_config["scint"]
        caen_config = self.scint_config["caen"]
        trig_code = {"Disabled": 0, "ACQ Only": 1, "EXT Only": 2, "ACQ+EXT": 3}
        io_code = {"NIM": 0, "TTL": 1}
        self.config["CAEN"] = {
            "Model": caen_config["model"],
            "Port": caen_config["port"],
            "ConnectionType": caen_config["connection"],
            "RecordLength": caen_config["rec_length"],
            "DecimationFactor": caen_config["decimation"],
            "MaxEventsPerRead": caen_config["evs_per_read"],
            "PostBufferPercentage": caen_config["post_trig"],
            "OverlappingRejection": caen_config["overlap_rej"],
            "TRGINasGate": caen_config["trig_in_as_gate"],
            "ExternalTrigger": trig_code[caen_config["ext_trig"]],
            "SoftwareTrigger": trig_code[caen_config["sw_trig"]],
            "Polarity": caen_config["polarity"],
            "IOLevel": io_code[caen_config["io_level"]],
        }
        for gp in range(4):
            gp_config = self.scint_config[f"caen_g{gp}"]
            self.config["CAEN"][f"group{gp}"] = {
                "Enabled": gp_config["enabled"],
                "TrigMask": gp_config["trig_mask"],
                "AcqMask": gp_config["acq_mask"],
                "Offset": gp_config["offset"],
                "Corrections": gp_config["ch_offset"],
                "Threshold": gp_config["threshold"],
            }
        caen_config_path = self.scint_config["caen"]["config_path"]
        with open(caen_config_path, "w") as file:
            json.dump(self.config, file, indent=2)

        self.caen_started.emit("caen")
