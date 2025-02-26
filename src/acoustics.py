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
        sample_rate = 0
        if self.config["sample_rate"] == "100 MS/s":
            sample_rate = 100000000
        elif self.config["sample_rate"] == "50 MS/s":
            sample_rate = 50000000
        elif self.config["sample_rate"] == "25 MS/s":
            sample_rate = 25000000
        elif self.config["sample_rate"] == "12.5 MS/s":
            sample_rate = 12500000
        elif self.config["sample_rate"] == "10 MS/s":
            sample_rate = 10000000
        elif self.config["sample_rate"] == "5 MS/s":
            sample_rate = 5000000
        elif self.config["sample_rate"] == "2 MS/s":
            sample_rate = 2000000
        elif self.config["sample_rate"] == "1 MS/s":
            sample_rate = 1000000
        elif self.config["sample_rate"] == "500 kS/s":
            sample_rate = 500000
        elif self.config["sample_rate"] == "200 kS/s":
            sample_rate = 200000
        elif self.config["sample_rate"] == "100 kS/s":
            sample_rate = 100000
        elif self.config["sample_rate"] == "50 kS/s":
            sample_rate = 50000
        elif self.config["sample_rate"] == "20 kS/s":
            sample_rate = 20000
        elif self.config["sample_rate"] == "10 kS/s":
            sample_rate = 10000
        elif self.config["sample_rate"] == "5 kS/s":
            sample_rate = 5000
        elif self.config["sample_rate"] == "2 kS/s":
            sample_rate = 2000
        elif self.config["sample_rate"] == "1 kS/s":
            sample_rate = 1000
        else:
            sample_rate = 1000000
            self.logger.warning("Acoustics: Invalid sample rate.")

        config["Acquisition"] = {
            "Mode": self.config["mode"],
            "SampleRate": sample_rate,
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
                    "Range": self.config[f"ch{ch}"]["range"],
                    "Coupling": self.config[f"ch{ch}"]["coupling"],
                    "Impedance": 50 if self.config[f"ch{ch}"]["impedance"]=="50 Ω" else 1000000,
                }
            if self.config[f"ch{ch}"]["trig"]:
                config[f"Trigger{ch}"] = {
                    "Condition": self.config[f"ch{ch}"]["polarity"],
                    "Level": self.config[f"ch{ch}"]["threshold"],
                    "Source": n_trig,
                }
                n_trig += 1
        
        if self.config["ext"]["trig"]:
            config[f"Trigger9"] = {
                "Condition": self.config["ext"]["polarity"],
                "Level": self.config["ext"]["threshold"],
                "Source": n_trig,
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
