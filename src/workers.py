import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from enum import Enum
import logging
import time

from src.ui_loader import SettingsWindow


class RunHandlingWorker(QObject):
    """
    Woeker class for starting the program, starting and stopping a run, and starting and stopping each individual
    events.
    """

    state = Signal(str)
    program_started = Signal()
    run_started = Signal()
    event_started = Signal()
    event_stopped = Signal()
    run_stopped = Signal()
    stopping = Signal()
    continuing = Signal()

    def __init__(self, main_window):
        super(RunHandlingWorker, self).__init__()
        self.main = main_window

    def start_program(self):
        """Processes to start program"""
        self.state.emit("Preparing")
        # for arduino in ["trigger", "clock", "position"]:
        #     self.main_window.arduinos_class.upload_sketch(arduino)

        time.sleep(1)
        self.state.emit("Idle")
        self.program_started.emit()

    def start_run(self):
        """Processes to start run"""
        self.main.create_run_directory()
        self.state.emit("Starting")
        self.main.ev_number = 0
        run_json_path = os.path.join(self.main.run_dir, f"{self.main.run_number}.json")
        self.main.config_class.save_config(run_json_path)
        time.sleep(1)
        self.main.run_livetime = 0
        self.run_started.emit()

    def stop_run(self):
        """Processes to start run"""
        self.state.emit("Stopping")
        self.main.stopping_run = False
        time.sleep(1)
        self.state.emit("Idle")
        self.run_stopped.emit()

    def start_event(self):
        """Processes to start run"""

        self.state.emit("Expanding")

        event_dir = os.path.join(self.main.run_dir, str(self.main.ev_number))
        if not os.path.exists(event_dir):
            os.mkdir(event_dir)

        time.sleep(1)

        self.main.event_timer.start()
        self.state.emit("Active")
        self.event_started.emit()

    def stop_event(self):
        """Processes to stop event"""
        self.main.run_livetime += self.main.event_timer.elapsed()
        self.state.emit("Compressing")
        time.sleep(1)
        self.event_stopped.emit()

    def check_event(self):
        """Check between events to stop or continue"""
        self.main.ev_number += 1

        # check if needs to stop run
        if self.main.ev_number >= self.main.config_class.config["run"]["max_num_evs"]:
            self.main.stopping_run = True

        if self.main.stopping_run:
            self.stopping.emit()
        else:
            self.continuing.emit()
