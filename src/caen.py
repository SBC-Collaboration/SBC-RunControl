import os
import numpy as np
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import red_caen
from sbcbinaryformat import Writer

class Caen(QObject):
    run_started = Signal(str)
    run_stopped = Signal(str)
    event_started = Signal(str)
    event_stopped = Signal(str)
    data_retrieved = Signal(dict)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.scint_config = self.main.config_class.config["caen"]
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
        """
        This periodic task is controlled by a timer set to 100 ms.
        When the run state is active and CAEN is enabled, it tries to retrieve data from the CAEN digitizer.
        If the number of triggers on the on-board buffer is greater than the number of events per read,
        it retrieves the data, decodes the events, and appends the data dictionary to the buffer.
        It then updates the CAEN plot on main window with the latest data.
        """
        if (self.main.run_state == self.main.run_states["active"] and self.caen):
            if self.caen.RetrieveDataUntilNEvents(self.evs_per_read):
                self.logger.info(f"Retrieving {self.evs_per_read} CAEN events.")
                self.caen.DecodeEvents()
                self.buffer.append(self.caen.GetDataDict())
                self.data_retrieved.emit(self.buffer[-1])


    def set_config(self):
        """
        Setup configuration into CAENGlobalConfig and CAENGroupConfig objects.
        It reads from the config dictionary and sets the attributes accordingly.
        The CAENGlobalConfig and CAENGroupConfig objects are then passed to the CAEN instance.
        Then the configuration is read back from the CAEN instance, so we would catch 
        any discrepancies like the record length.
        """
        self.config = self.main.config_class.run_config["caen"]["global"]

        # set global config from dict to class attributes
        self.global_config.MaxEventsPerRead = self.config["evs_per_read"]
        self.global_config.RecordLength = self.config["rec_length"]
        self.global_config.PostTriggerPorcentage = self.config["post_trig"]
        self.global_config.EXTTriggerMode = getattr(red_caen.CAEN_DGTZ_TriggerMode, self.config["ext_trig"])
        self.global_config.SWTriggerMode = getattr(red_caen.CAEN_DGTZ_TriggerMode, self.config["sw_trig"])
        self.global_config.CHTriggerMode = getattr(red_caen.CAEN_DGTZ_TriggerMode, self.config["ch_trig"])
        self.global_config.TriggerPolarity = getattr(red_caen.CAEN_DGTZ_TriggerPolarity, self.config["polarity"])
        self.global_config.IOLevel = getattr(red_caen.CAEN_DGTZ_IOLevel, self.config["io_level"])
        self.global_config.TrigInAsGate = self.config["trig_in_as_gate"]
        self.global_config.TriggerOverlappingEn = self.config["overlap_en"]
        self.global_config.MemoryFullMode = False if self.config["memory_full"]=="Normal" else True
        self.global_config.TriggerCountingMode = False if self.config["counting_mode"]=="Accepted Only" else True
        self.global_config.DecimationFactor = self.config["decimation"]
        self.global_config.MajorityLevel = self.config["majority_level"]
        self.global_config.MajorityWindow = self.config["majority_window"]

        for i in range(4):
            group_config = self.main.config_class.run_config["caen"][f"group{i}"]
            acq_mask = red_caen.ChannelsMask()
            trg_mask = red_caen.ChannelsMask()
            for ch in range(8):
                acq_mask[ch] = group_config["acq_mask"][ch]
                trg_mask[ch] = group_config["trig_mask"][ch]
            self.group_configs[i].AcquisitionMask = acq_mask
            self.group_configs[i].TriggerMask = trg_mask
            self.group_configs[i].Enabled = group_config["enabled"]
            self.group_configs[i].DCOffset = group_config["offset"]
            self.group_configs[i].DCCorrections = group_config["ch_offset"]
            self.group_configs[i].DCRange = 0 if group_config["range"]=="2Vpp" else 1 # 0: 2Vpp, 1: 0.5Vpp
            self.group_configs[i].TriggerThreshold = group_config["threshold"]
        
        self.caen.Setup(self.global_config, self.group_configs)

        # get configurations back from CAEN
        self.real_global_config = self.caen.GetGlobalConfiguration()
        self.real_group_configs = self.caen.GetGroupConfigurations()
        self.logger.info("CAEN configuration set.")

    @Slot()
    def start_run(self):
        """
        Initialize CAEN class for the run.
        It creates CAENGlobalConfig and CAENGroupConfig objects, and establishes connection 
        to the CAEN digitizer, and then sets the configuration.

        :raises ConnectionError: If the CAEN digitizer connection fails.
        """
        self.global_config = red_caen.CAENGlobalConfig()
        self.group_configs = [red_caen.CAENGroupConfig() for _ in range(8)]
        self.config = self.main.config_class.run_config["caen"]["global"]
        self.evs_per_read = self.config["evs_per_read"] # save value for reading data

        if not self.config["enabled"]:
            self.run_started.emit(f"caen-disabled")
            return

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
        """
        This function will initialize the writer, and start the acquisition on the CAEN digitizer.
        """
        if not self.config["enabled"]:
            self.event_started.emit(f"caen-disabled")
            return

        # Check connection status
        if not self.caen or not self.caen.IsConnected():
            self.logger.error("CAEN not connected.")
            self.event_started.emit("caen-error")
            raise ConnectionError("CAEN not connected.")
        
        self.buffer = [] # create a list for data dictionaries

        # create writer
        en_chs = np.sum([self.real_group_configs[i].AcquisitionMask for i in range(4) 
                         if self.real_group_configs[i].Enabled ]) # number of enabled channels
        rec_len = self.real_global_config.RecordLength
        self.writer = Writer(
            os.path.join(self.config["data_path"], "scintillation.sbc"), # file path
            ["EventCounter","TriggerSource","GroupMask","TriggerMask","AcquisitionMask","TriggerTimeTag","Waveforms"], # column names
            ['u4','u1','u1','u4','u4','u4','u2'], # data types
            [[1],[1],[1],[1],[1],[1],[en_chs, rec_len]] # data shapes
        )

        self.caen.EnableAcquisition()
        self.logger.info("CAEN acquisition enabled.")

        self.event_started.emit("caen")

    @Slot()
    def stop_event(self):
        """
        At the end of the event, this function will disable the acquisition, retrieve data from CAEN 
        until the buffer is empty, decode the events, and write the data to file.
        """
        if not self.config["enabled"]:
            self.event_stopped.emit(f"caen-disabled")
            return

        self.caen.DisableAcquisition()
        self.logger.info("CAEN acquisition disabled.")

        self.caen.RetrieveData()
        self.caen.DecodeEvents()
        if self.caen.GetNumberOfEvents() > 0:
            self.buffer.append(self.caen.GetDataDict())
            self.data_retrieved.emit(self.buffer[-1])

        # write data to file
        for b in self.buffer:
            self.writer.write(b)
        
        self.logger.info("CAEN data written to file.")
        self.event_stopped.emit("caen")

    @Slot()
    def stop_run(self):
        """
        At the end of the run, this function will delete all buffers and handles.
        """
        if not self.config["enabled"]:
            self.run_stopped.emit(f"caen-disabled")
            return
        
        del self.caen
        del self.buffer
        del self.global_config
        del self.group_configs
        self.run_stopped.emit("caen")
