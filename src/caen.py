import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
from collections import namedtuple
import copy
import json
import red_caen

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
        print(f"buffer: {caen.GetEventsInBuffer()}, retrieved: {caen.GetNumberOfEvents()}")
        caen.RetrieveDataUntilNEvents(500)
        caen.DecodeEvents()
        for i in range(0,500):
            data_array_temp = caen.GetWaveform(i)
            data_array_temp=data_array_temp.tolist()
            del data_array_temp[32:64]
            counter=counter + 1
            event = caen.GetEvent(i)
            eventsize_array.append(event.get_info().EventSize)
            boardid_array.append(event.get_info().BoardId)
            pattern_array.append(event.get_info().Pattern)
            channelmask_array.append(event.get_info().ChannelMask)
            eventcounter_array.append(event.get_info().EventCounter)
            triggertimetag_array.append(event.get_info().TriggerTimeTag)
            data_array.append(data_array_temp)
        if counter >= 1000: 
            data_array=np.array(data_array)
            eventsize_array=np.array(eventsize_array)
            boardid_array=np.array(boardid_array)
            pattern_array=np.array(pattern_array)
            channelmask_array=np.array(channelmask_array)
            eventcounter_array=np.array(eventcounter_array)
            triggertimetag_array=np.array(triggertimetag_array)
            data = {
                'Event Size': eventsize_array,
                'Board Id':boardid_array,
                'Pattern': pattern_array,
                'Channel Mask':channelmask_array,
                'Event Counter':eventcounter_array,
                'Trigger Time Tag':triggertimetag_array,
                'data_array': data_array}
            caen_writer.write(data)
            eventsize_array=[]
            boardid_array=[]
            pattern_array=[]
            channelmask_array=[]
            eventcounter_array=[]
            triggertimetag_array=[]
            data_array_temp=[]
            data_array=[]
            counter = 0

    @Slot()
    def start_run(self):
        model_constants = red_caen.GetCAENDigitizerModelConstants()
        caen = red_caen.CAEN(
            red_caen.iostream_wrapper(), 
            red_caen.CAENDigitizerModel.DT5740D, 
            red_caen.CAENConnectionType.USB,
            0,
            0,
            0)
        if caen.IsConnected():
            print("CAEN connection successful.\n")
        else:
            print("CAEN connection not successful.\n")

        self.run_started.emit("caen")


    @Slot()
    def start_event(self):
        file_name = "caen.sbc.bin"

        column_names = ["Event Size","Board Id","Pattern","Channel Mask","Event Counter","Trigger Time Tag","data_array"]
        data_types = ['u4','u4','u4','u4','u4','u4','i8']
        sizes = [[1],[1],[1],[1],[1],[1],[32, 180]]
        caen_writer = Writer(file_name, column_names, data_types, sizes)

        eventsize_array=[]
        boardid_array=[]
        pattern_array=[]
        channelmask_array=[]
        eventcounter_array=[]
        triggertimetag_array=[]
        data_array_temp=[]
        data_array=[]



        # global config
        global_config = red_caen.CAENGlobalConfig()
        global_config.MaxEventsPerRead = 500
        global_config.RecordLength = 180
        global_config.PostTriggerPorcentage = 50
        global_config.EXTTriggerMode = red_caen.CAEN_DGTZ_TriggerMode.ACQ_ONLY
        global_config.SWTriggerMode = red_caen.CAEN_DGTZ_TriggerMode.ACQ_ONLY
        global_config.CHTriggerMode = red_caen.CAEN_DGTZ_TriggerMode.ACQ_ONLY
        global_config.TriggerPolarity = red_caen.CAEN_DGTZ_TriggerPolarity.Falling
        global_config.IOLevel = red_caen.CAEN_DGTZ_IOLevel.TTL
        global_config.EXTAsGate = False
        global_config.TriggerOverlappingEn = False
        global_config.MemoryFullModeSelection = True
        global_config.DecimationFactor = 0
        global_config.MajorityLevel = 0
        global_config.MajorityCoincidenceWindow = 0

        # group config (need length 8 for the wrapper, but only first 4 is used)
        group_configs = [red_caen.CAENGroupConfig() for i in range(8)]
        for i in range(8):
            acq_mask = red_caen.ChannelsMask()
            trg_mask = red_caen.ChannelsMask()
            for ch in range(8):
                acq_mask[ch] = True
                trg_mask[ch] = True
        #    acq_mask[0] = False # False meas data won't be recorded from these channels.
        #    print("acq_mask:",acq_mask)
            group_configs[i].Enabled = True
            group_configs[i].DCOffset = 0x8000
            group_configs[i].DCCorrections = [0,0,0,0,0,0,0,0]
            group_configs[i].DCRange = 0
            group_configs[i].TriggerThreshold = 0x800
            group_configs[i].AcquisitionMask = acq_mask
            group_configs[i].TriggerMask = trg_mask

        # set config
        caen.Setup(global_config, group_configs)

        global_back = caen.GetGlobalConfiguration()
        print(global_back)


        groups_back = caen.GetGroupConfigurations()

        caen.EnableAcquisition()
        counter = 0
        self.caen_started.emit("caen")

    @Slot()
    def stop_event(self):
        print(f"buffer_after_while_loop: {caen.GetEventsInBuffer()}, retrieved_after_while_loop: {caen.GetNumberOfEvents()}") #BM
        caen.RetrieveDataUntilNEvents(caen.GetEventsInBuffer()) #BM
        caen.DecodeEvents()   #BM
        caen.DisableAcquisition()

        print(f"buffer_final: {caen.GetEventsInBuffer()}, retrieved_final: {caen.GetNumberOfEvents()}") #BM

        data_array_temp=[]
        eventsize_array=[]
        boardid_array=[]
        pattern_array=[]
        channelmask_array=[]
        eventcounter_array=[]
        triggertimetag_array=[]
        data_array=[]   
        for i in range(0,caen.GetNumberOfEvents()):
            data_array_temp = caen.GetWaveform(i)
            data_array_temp=data_array_temp.tolist()
            del data_array_temp[32:64]
            event = caen.GetEvent(i)
            eventsize_array.append(event.get_info().EventSize)
            boardid_array.append(event.get_info().BoardId)
            pattern_array.append(event.get_info().Pattern)
            channelmask_array.append(event.get_info().ChannelMask)
            eventcounter_array.append(event.get_info().EventCounter)
            triggertimetag_array.append(event.get_info().TriggerTimeTag)
            data_array.append(data_array_temp)

        data_array=np.array(data_array)
        eventsize_array=np.array(eventsize_array)
        boardid_array=np.array(boardid_array)
        pattern_array=np.array(pattern_array)
        channelmask_array=np.array(channelmask_array)
        eventcounter_array=np.array(eventcounter_array)
        triggertimetag_array=np.array(triggertimetag_array)
        data = {
            'Event Size': eventsize_array,
            'Board Id':boardid_array,
            'Pattern': pattern_array,
            'Channel Mask':channelmask_array,
            'Event Counter':eventcounter_array,
            'Trigger Time Tag':triggertimetag_array,
            'data_array': data_array}
        caen_writer.write(data)

        caen.ClearData()

    @Slot()
    def stop_run(self):
        #stop CAEN connection
        del data_array_temp
        del ventsize_array
        del boardid_array
        del pattern_array
        del channelmask_array
        del eventcounter_array
        del triggertimetag_array
        del data_array

