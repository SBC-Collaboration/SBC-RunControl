import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread, QProcess
import signal
from configparser import ConfigParser
import ctypes
from src.guardian import ErrorCodes

class Acoustics(QObject):
    event_started = Signal(str)
    event_stopped = Signal(str)
    error = Signal(int)

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
    
    range_conversion = {
        "±5 V": 10000,
        "±2 V": 4000,
        "±1 V": 2000,
        "±500 mV": 1000,
        "±200 mV": 400,
        "±100 mV": 200,
    }

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.config = self.main.config_class.config["acous"]
        self.process = None

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Acoustics module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        if (self.main.run_state == self.main.run_states["active"] and self.gage_process):
            if not self.gage_process.is_alive():
                self.logger.debug(f"Acous: GaGe process not alive. Starting new thread.")
                self.gage_process = Process(target=self.start_gage)
                self.gage_process.start()

    def save_config(self):
        n_trig = 1
        config = {}

        config["Acquisition"] = {
            "Mode": self.config["mode"],
            "SampleRate": self.sample_rate_conversion[self.config["sample_rate"]],
            "Depth": self.config["depth"],
            "SegmentSize": self.config["segment_size"],
            "SegmentCount": self.config["acq_seg_count"],
            "TriggerDelay": self.config["trig_delay"],
            "TriggerTimeout": self.config["trig_timeout"],
            "TriggerHoldOff": self.config["trig_holdoff"],
            "TimeStampMode": self.config["timestamp_mode"],
            "TimeStampClock": self.config["timestamp_clock"],
            "PreTrigLen": self.config["pre_trig_len"],
            "PostTrigLen": self.config["post_trig_len"],
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
                "Range": self.range_conversion[self.config[f"ch{ch}"]["range"]],
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
        parser.optionxform = str
        parser.read_dict(config)
        with open("SBCAcquisition.ini", "w") as f:
            parser.write(f)
    
    def start_gage_process(self):
        """Helper method to start/restart the GaGe process"""
        if self.process is not None and self.process.state() != QProcess.ProcessState.NotRunning:
            self.logger.warning("GaGe process already running")
            return False
        
        # Clean up old process if it exists
        if self.process is not None:
            self.process.deleteLater()

        # Create new process
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.finished.connect(self.process_finished)

        # Start with error checking
        rc_path = os.path.join(os.path.dirname(__file__), '..')
        self.process.setWorkingDirectory(rc_path)
        self.logger.debug(f"RC path: {rc_path}")
        self.process.start(os.path.join(rc_path, self.config["driver_path"]))
        if not self.process.waitForStarted(3000):  # 3 second timeout
            self.logger.error(f"Failed to start GaGe process: {self.process.errorString()}")
            return False
        
        return True

    @Slot()                                                                      
    def start_event(self):
        self.config = self.main.config_class.run_config["acous"]
        if not self.config["enabled"]:
            self.event_started.emit(f"acous-disabled")
            return
        self.save_config()
        
        self.logger.debug(f"Acous: Data acquisition starting.")
        self.gage_process = Process(target=self.start_gage)
        self.gage_process.start()
        self.event_started.emit("acous")

    @Slot()
    def handle_stdout(self):
        if self.process:
            data = self.process.readAllStandardOutput()
            text = data.data().decode('utf-8')
            self.logger.debug(f"GaGe: {text.strip()}")
    
    @Slot()
    def process_finished(self, exit_code, exit_status):
        self.handle_stdout()
        self.logger.debug(f"GaGe process finished with exit code {exit_code} and status {exit_status}.")
        if self.process and self.main.run_state == self.main.run_states["active"]:
            self.logger.info(f"Restarting GaGe process.")
            self.process.start(self.config["driver_path"])
        else:
            self.process = None

    @Slot()
    def stop_event(self):
        if not self.config["enabled"]:
            self.event_stopped.emit(f"acous-disabled")
            return
        
        if self.process and \
            self.process and self.process.state() != QProcess.ProcessState.NotRunning:
            self.logger.debug("Terminating GaGe process.")
            self.process.terminate()
            if not self.process.waitForFinished(self.config["driver_timeout"] * 1000):
                self.logger.warning("GaGe process did not terminate gracefully, killing it.")
                self.process.kill()
                
        self.process = None
        self.event_stopped.emit("acous")
