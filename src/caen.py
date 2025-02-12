import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
from collections import namedtuple
import copy
import json
import red_caen
from sbcbinaryformat import Writer

class Caen(QObject):
    caen_started = Signal(str)
    caen_stopped = Signal(str)
    event_started = Signal(str)
    event_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.scint_config = self.main.config_class.config["scint"]
        self.caen = None

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

    def set_config(self):
        self.config = self.main.config_class.run_config["scint"]["caen"]

        # set global config from dict to class attributes
        self.global_config = red_caen.CAENGlobalConfig()
        self.global_config.MaxEventsPerRead = self.config["evs_per_read"]
        self.global_config.RecordLength = self.config["rec_length"]
        self.global_config.PostTriggerPorcentage = self.config["post_trig"]
        self.global_config.EXTTriggerMode = getattr(red_caen.CAEN_DGTZ_TriggerMode, self.config["ext_trig"])
        self.global_config.SWTriggerMode = getattr(red_caen.CAEN_DGTZ_TriggerMode, self.config["sw_trig"])
        self.global_config.CHTriggerMode = getattr(red_caen.CAEN_DGTZ_TriggerMode, self.config["ch_trig"])
        self.global_config.TriggerPolarity = getattr(red_caen.CAEN_DGTZ_TriggerPolarity, self.config["polarity"])
        self.global_config.IOLevel = getattr(red_caen.CAEN_DGTZ_IOLevel, self.config["io_level"])
        self.global_config.TrgInAsGate = self.config["trig_in_as_gate"]
        self.global_config.TriggerOverlappingEn = self.config["overlap_en"]
        self.global_config.MemoryFullMode = self.config["memory_full"]
        self.global_config.DecimationFactor = self.config["decimation"]
        self.global_config.MajorityLevel = self.config["majority_level"]
        self.global_config.MajorityWindow = self.config["majority_window"]

        self.group_configs = [red_caen.CAENGroupConfig() for _ in range(8)]
        for i in range(4):
            group_config = self.main.config_class.run_config["scint"][f"caen_g{i}"]
            acq_mask = red_caen.ChannelMask()
            trg_mask = red_caen.ChannelMask()
            for ch in range(8):
                acq_mask[ch] = group_config["acq_mask"][ch]
                trg_mask[ch] = group_config["trg_mask"][ch]
            self.group_configs[i].AcquisitionMask = acq_mask
            self.group_configs[i].TriggerMask = trg_mask
            self.group_configs[i].Enabled = group_config["enabled"]
            self.group_configs[i].DCOffset = group_config["offset"]
            self.group_configs[i].DCCorrections = group_config["ch_offset"]
            self.group_configs[i].DCRange = 0 if group_config["range"]=="2Vpp" else 1 # 0: 2Vpp, 1: 0.5Vpp
            self.group_configs[i].TriggerThreshold = group_config["threshold"]
        
        self.caen.Setup(self.global_config, self.group_configs)

        self.buffer = []

    @Slot()
    def start_run(self):
        self.config = self.main.config_class.run_config["scint"]["caen"]

        self.caen = red_caen.CAEN(
            red_caen.iostream_wrapper(), 
            getattr(red_caen.CAENDigitizerModel, self.config["model"]),
            getattr(red_caen.CAENConnectionType, self.config["connection"]),
            self.config["link"],
            0,
            0)
        if self.caen.IsConnected():
            self.logger.info("CAEN connection successful.\n")
        else:
            self.logger.error("CAEN connection failed.\n")
            raise ConnectionError("CAEN connection failed.\n")

        self.set_config()
        self.run_started.emit("caen")

    @Slot()
    def start_event(self):
        # Check connection status
        if not self.caen or not self.caen.IsConnected():
            self.logger.error("CAEN not connected.")
        
        self.buffer = [] # create a list for data dictionaries
        # create writer
        self.writer = Writer(
            
        )

        self.caen.EnableAcquisition()

        self.event_started.emit("caen")

    @Slot()
    def stop_event(self):
        self.caen.DisableAcquisition()
        # retrieve more data
        self.caen.ClearData()

        # write data to file
        for b in self.buffer:
            self.writer.write(b)
        
        self.event_stopped.emit("caen")

    @Slot()
    def stop_run(self):
        del self.caen
        del self.buffer
        del self.global_config
        del self.group_configs
