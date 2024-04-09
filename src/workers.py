import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from enum import Enum
import logging
import time
from src.ui_loader import SettingsWindow
from dependencies.SBCBinaryFormat.python.sbcbinaryformat.files import Writer


class StartProgramWorker(QObject):
    state = Signal(str)
    program_started = Signal()

    def __init__(self, main_window):
        super(RunHandlingWorker, self).__init__()
        self.main = main_window
        self.logger = logging.getLogger("rc")
        self.logger.debug("Start program worker class initialized.")

    @Slot()
    def start_program(self):
        """Processes to start program"""
        # for arduino in ["trigger", "clock", "position"]:
        #     self.main_window.arduinos_class.upload_sketch(arduino)

        time.sleep(1)
        self.state.emit("Idle")
        self.program_started.emit()


class StartRunWorker(QObject):
    state = Signal(str)
    run_started = Signal()
    run_json_path = Signal(str)
    run_log_path = Signal(str)
    file_handler = Signal(logging.FileHandler)

    def __init__(self, main_window):
        super(RunHandlingWorker, self).__init__()
        self.main = main_window
        self.logger = logging.getLogger("rc")
        self.logger.debug("Start run worker class initialized.")

    def run(self):
        """Processes to start run"""
        self.main.create_run_directory()
        self.state.emit("Starting")
        run_json_path = os.path.join(self.main.run_dir, f"{self.main.run_id}.json")
        self.run_json_path.emit(run_json_path)
        run_log_path = os.path.join(self.main.run_dir, f"{self.main.run_id}.log")
        self.run_log_path.emit(run_log_path)

        file_handler = logging.FileHandler(run_log_path, mode="a")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self.main.log_formatter)
        self.logger.addHandler(file_handler)

        # initialize run data structure
        self.run_data = []

        time.sleep(1)
        self.run_started.emit()


class StopRunWorker(QObject):
    state = Signal(str)
    run_stopped = Signal()

    def __init__(self, main_window):
        super(RunHandlingWorker, self).__init__()
        self.main = main_window
        self.logger = logging.getLogger("rc")
        self.logger.debug("Stop run worker class initialized.")

    def run(self):
        """Processes to start run"""
        self.state.emit("Stopping")

        time.sleep(1)
        self.logger.removeHandler(self.logger.handlers[-1])
        self.state.emit("Idle")
        self.run_stopped.emit()


class StartEventWorker(QObject):
    state = Signal(str)
    event_started = Signal()

    def __init__(self, main_window):
        super(RunHandlingWorker, self).__init__()
        self.main = main_window
        self.logger = logging.getLogger("rc")
        self.logger.debug("Start event worker class initialized.")

    def run(self):
        """Processes to start run"""

        self.state.emit("Expanding")

        self.main.event_dir = os.path.join(self.main.run_dir, str(self.main.ev_number))
        if not os.path.exists(self.main.event_dir):
            os.mkdir(self.main.event_dir)
        self.main.camera_class.start_camera()

        time.sleep(1)

        self.main.event_timer.start()
        self.state.emit("Active")
        self.event_started.emit()


class RunHandlingWorker(QObject):
    """
    Woeker class for starting the program, starting and stopping a run, and starting and stopping each individual
    events.
    """

    state = Signal(str)
    event_stopped = Signal()
    run_stopped = Signal()
    stopping = Signal()
    continuing = Signal()

    def __init__(self, main_window):
        super(RunHandlingWorker, self).__init__()
        self.main = main_window
        self.logger = logging.getLogger("rc")
        self.logger.debug("Worker class initialized.")

    def stop_event(self):
        """Processes to stop event"""
        self.event_livetime = self.main.event_timer.elapsed()
        self.main.run_livetime += self.event_livetime
        self.state.emit("Compressing")
        self.trigger_source = "cam1"  # TODO: implement trigger source logic
        self.trigger_dict = {
            "cam1": 0,
            "cam2": 1,
            "cam3": 2,
            "RC_Timeout": 3,
            "RC_But": 4,
            "PLC": 5,
            "Kulite_Ar": 6,
            "Kulite_CF4": 7,
            "Button": 8,
            "Unknown": 9,
        }

        # event data tuple and save data to disk
        ev_number = [int(i) for i in self.main.run_id.split("_")]
        ev_number.append(self.main.ev_number)
        self.event_data = {
            "ev_number": ev_number,
            # list of date, run number, event number: [20240101, 0, 0]
            "ev_livetime": self.event_livetime,  # event livetime (ms)
            "run_livetime": self.main.run_livetime,  # event livetime (ms)
            "trigger_source": self.trigger_dict[
                self.trigger_source
            ],  # trigger source (dict)
        }
        with Writer(
            os.path.join(
                self.main.event_dir, f"{self.main.run_id}_{self.main.ev_number}.sbc"
            ),
            ["ev_number", "ev_livetime", "run_livetime", "trigger_source"],
            ["u4", "u8", "u8", "u1"],
            [[3], [1], [1], [1]],
        ) as event_writer:
            event_writer.write(self.event_data)
        self.run_data.append(self.event_data)
        self.main.sipm_amp_class.unbias_sipm_amp()

        time.sleep(1)
        self.event_stopped.emit()

    def check_event(self):
        """Check between events to stop or continue"""
        self.main.ev_number += 1

        # check if needs to stop run
        if (
            self.main.ev_number
            >= self.main.config_class.config["general"]["max_num_evs"]
        ):
            self.main.stopping_run = True

        if self.main.stopping_run:
            self.stopping.emit()
        else:
            self.continuing.emit()
