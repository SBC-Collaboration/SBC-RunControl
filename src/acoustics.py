import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
from collections import namedtuple
import copy
import json
from ctypes import *
import src.global_variable  as gv #BM
import subprocess
import signal
import time
from configparser import ConfigParser


class Acoustics(QObject):
    acous_started = Signal(str)
    acous_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.config = self.main.config_class.config["acous"]

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Acoustics module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    def save_config(self):
        n_trig = 1
        config = {}

        # convert sample_rate to a number
        sample_rate_conversion = {
            "100 MS/s": 100000000,
            "50 MS/s": 50000000,
            "25 MS/s": 25000000,
            "12.5 MS/s": 12500000,
            "10 MS/s": 10000000,
            "5 MS/s": 5000000,
            "2 MS/s": 2000000,
            "1 MS/s": 1000000,
            "500 kS/s": 500000,
            "200 kS/s": 200000,
            "100 kS/s": 100000,
            "50 kS/s": 50000,
            "20 kS/s": 20000,
            "10 kS/s": 10000,
            "5 kS/s": 5000,
            "2 kS/s": 2000,
            "1 kS/s": 1000,
        }

        # convert range to a number
        range_conversion = {
            "±5 V": 10000,
            "±2 V": 4000,
            "±1 V": 2000,
            "±500 mV": 1000,
            "±200 mV": 400,
            "±100 mV": 200,
        }

        config["Acquisition"] = {
            "Mode": self.config["mode"],
            "SampleRate": sample_rate_conversion[self.config["sample_rate"]],
            "Depth": self.config["post_trig_len"],
            "SegmentSize": self.config["pre_trig_len"] + self.config["post_trig_len"],
            "SegmentCount": self.config["acq_seg_count"],
            "TriggerDelay": self.config["trig_delay"],
            "TriggerTimeout": self.config["trig_timeout"],
            "TriggerHoldOff": self.config["trig_holdoff"],
            "TimeStampMode": self.config["timestamp_mode"],
            "TimeStampClock": self.config["timestamp_clock"],
        }

        config["Application"] = {
            "StartPosition": self.config["start_pos"],
            "TransferLength": self.config["transfer_len"],
            "SegmentStart": self.config["seg_start"],
            "SegmentCount": self.config["seg_count"],
            "SaveFileFormat": self.config["file_format"],
            "SaveFileName": os.path.join(self.config["data_dir"], self.config["file_name"]),
        }

        for ch in range(1, 9):
            if self.config[f"ch{ch}"]["enabled"]:
                config[f"Channel{ch}"] = {
                    "Range": range_conversion[self.config[f"ch{ch}"]["range"]],
                    "Coupling": self.config[f"ch{ch}"]["coupling"],
                    "Impedance": 50 if self.config[f"ch{ch}"]["impedance"]=="50 Ω" else 1000000,
                }
        
        for ch in range(1, 9):
            if self.config[f"ch{ch}"]["trig"]:
                config[f"Trigger{n_trig}"] = {
                    "Condition": self.config[f"ch{ch}"]["polarity"],
                    "Level": self.config[f"ch{ch}"]["threshold"],
                    "Source": n_trig,
                }
                n_trig += 1
        
        if self.config["ext"]["trig"]:
            config[f"Trigger{n_trig}"] = {
                "Condition": self.config["ext"]["polarity"],
                "Level": self.config["ext"]["threshold"],
                "Source": -1,
            }
            n_trig += 1
        
        if n_trig == 1: # if no other trigger is enabled
            config[f"Trigger{n_trig}"] = {
                "Source": 0, # use disabled trigger
            }

        parser = ConfigParser()
        parser.read_dict(config)
        with open("SBCAcquisition.ini", "w") as f:
            parser.write(f)

    @Slot(str)                                                                      
    def start_event(self,module):

        self.config = self.main.config_class.run_config[module]
        if not self.config["enabled"]:
            self.event_stopped.emit(f"disabled-acous")
            return
        self.save_config()
        
        self.logger.info(f"Acoustic data acquisition starting.")                    
        process = subprocess.Popen(['python', '/home/sbc/packages/gati-linux-driver/Sdk/SBC-Piezo-Base-Code/sbc_reader_dll_wrapper.py'])             
        while True:
            if(gv.TRIG_LATCH==1):
                process.send_signal(signal.SIGINT)
                break                                                         
            if process.poll() != None:                                            
                process = subprocess.Popen(['python', '/home/sbc/packages/gati-linux-driver/Sdk/SBC-Piezo-Base-Code/sbc_reader_dll_wrapper.py']) 
            time.sleep(0.001) #time.sleep(0.0005)  # Sleep for 0.5 milliseconds
                                        
        self.logger.info(f"Acoustic data acquisition ended.")

    @Slot()
    def stop_event(self):
        self.client.close()
