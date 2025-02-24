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
        config_data = {
            "Acquisition": {
                "Mode": "Octal",
                "SampleRate": "1000000",  # 1 MHz
                "Depth": "25000000",      # e.g. for eight channels
                "SegmentSize": "25000000",
                "SegmentCount": "1",
                "TriggerHoldOff": "0",
                "TriggerTimeout": "0",    # 10 ms would be '100000' etc.
                "TimeStampMode": "Free",
                "TimeStampClock": "Fixed"
            },
            "Channel1": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Channel2": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Channel3": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Channel4": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Channel5": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Channel6": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Channel7": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Channel8": {
                "Range": "2000",
                "Coupling": "DC",
                "Impedance": "50"
            },
            "Trigger1": {
                "Condition": "Rising",
                "Level": "10",
                "Source": "2"
            },
            "Application": {
                "StartPosition": "0",
                "TransferLength": "25000000",
                "SegmentStart": "1",
                "SegmentCount": "1",
                "SaveFileName": "/home/sbc/packages/gati-linux-driver/Sdk/SBC-Piezo-Base-Code/test/Acquire-",
                "SaveFileFormat": "TYPE_DEC"
            }
        }
        parser = ConfigParser()
        parser.read_dict(config_data)
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
