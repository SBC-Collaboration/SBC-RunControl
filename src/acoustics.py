import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import signal
from configparser import ConfigParser
from multiprocessing import Process
import ctypes

class Acoustics(QObject):
    event_started = Signal(str)
    event_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.config = self.main.config_class.config["acous"]

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

        self.gage_process = None

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Acoustics module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        if (self.main.run_state == self.main.run_states["active"] and self.gage_process):
            if not self.gage_process.is_alive():
                self.logger.debug(f"GaGe process not alive. Starting new thread.")
                self.gage_process = Process(target=self.start_gage)
                self.gage_process.start()

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
            # All 8 channels must be enabled
            config[f"Channel{ch}"] = {
                "Range": range_conversion[self.config[f"ch{ch}"]["range"]],
                "Coupling": self.config[f"ch{ch}"]["coupling"],
                "Impedance": 50 if self.config[f"ch{ch}"]["impedance"]=="50 Ω" else 1000000,
                "DCOffset": self.config[f"ch{ch}"]["offset"],
            }
        
        # trigger fields must be after channel fields
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
        
        # Must have one or more trigger fields
        if n_trig == 1: # if no other trigger is enabled
            config[f"Trigger{n_trig}"] = {
                "Source": 0, # use disabled trigger
            }

        parser = ConfigParser()
        parser.read_dict(config)
        with open("SBCAcquisition.ini", "w") as f:
            parser.write(f)
    
    def start_gage(self):
        lib = ctypes.cdll.LoadLibrary(self.config["driver_path"])
        lib.main()

    @Slot()                                                                      
    def start_event(self):
        self.config = self.main.config_class.run_config["acous"]
        if not self.config["enabled"]:
            self.event_started.emit(f"gage-disabled")
            return
        self.save_config()
        
        self.logger.debug(f"Acoustic data acquisition starting.")
        self.gage_process = Process(target=self.start_gage)
        self.gage_process.start()
        self.event_started.emit("gage")

    @Slot()
    def stop_event(self):
        if not self.config["enabled"]:
            self.event_stopped.emit(f"gage-disabled")
            return

        if self.gage_process and self.gage_process.is_alive():
            os.kill(self.gage_process.pid, signal.SIGINT)
            self.gage_process.join()
            self.gage_process = None
        
        self.event_stopped.emit("gage")
