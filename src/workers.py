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
    finished = Signal()

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
        self.finished.emit()

    def start_run(self):
        """Processes to start run"""
        self.main.create_run_directory()
        self.state.emit("Starting")
        self.main.ev_number = None
        run_json_path = os.path.join(self.main.run_dir, f"{self.main.run_number}.json")
        self.main.config_class.save_config(run_json_path)
        time.sleep(1)
        self.main.run_livetime = 0
        self.finished.emit()


class StartProgramWorker(QObject):
    """
    Worker class for starting up Run Control.
    """
    state = Signal(str)
    finished = Signal()

    def __init__(self, main_window):
        super(StartProgramWorker, self).__init__()
        self.main = main_window

    def start_program(self):
        """Processes to start program"""
        self.state.emit("Preparing")
        self.main.stopping_run = False
        # for arduino in ["trigger", "clock", "position"]:
        #     self.main_window.arduinos_class.upload_sketch(arduino)

        time.sleep(1)
        self.state.emit("Idle")
        self.finished.emit()


class StartRunWorker(QObject):
    """
    Worker class for starting a run. It will change the run state into "starting", then initialize each DAQ modules.
    Then it changes the state to "active".
    """
    state = Signal(str)
    finished = Signal()

    def __init__(self, main_window):
        super(StartRunWorker, self).__init__()
        self.main = main_window

    def start_run(self):
        """Processes to start run"""
        self.main.create_run_directory()
        self.state.emit("Starting")
        self.main.ev_number = None
        run_json_path = os.path.join(self.main.run_dir, f"{self.main.run_number}.json")
        self.main.config_class.save_config(run_json_path)
        time.sleep(1)
        self.main.run_livetime = 0
        self.finished.emit()


class StopRunWorker(QObject):
    """
    Worker class for stopping a run. It will change the run state into "stopping", then wait for each DAQ modules to
    end. Then it changes the run state to "idle".
    """
    state = Signal(str)
    finished = Signal()

    def __init__(self, main_window):
        super(StopRunWorker, self).__init__()
        self.main = main_window

    def stop_run(self):
        """Processes to start run"""
        self.state.emit("Stopping")
        self.main.stopping_run = False
        time.sleep(1)
        self.state.emit("Idle")
        self.finished.emit()


class StartEventWorker(QObject):
    """
    Worker class for starting a run. It will change the run state into "starting", then initialize each DAQ modules.
    Then it changes the state to "active".
    """
    state = Signal(str)
    ev_number = Signal()
    finished = Signal()

    def __init__(self, main_window):
        super(StartEventWorker, self).__init__()
        self.main = main_window

    def start_event(self):
        """Processes to start run"""
        if self.main.ev_number is not None:
            self.main.ev_number += 1
        else:
            self.main.ev_number = 0
        self.ev_number.emit()
        event_dir = os.path.join(self.main.run_dir, str(self.main.ev_number))
        if not os.path.exists(event_dir):
            os.mkdir(event_dir)
        self.state.emit("Expanding")
        time.sleep(1)

        self.main.event_timer.start()
        self.state.emit("Active")
        self.finished.emit()


class StopEventWorker(QObject):
    """
    Worker class for stopping a run. It will change the run state into "stopping", then wait for each DAQ modules to
    end. Then it changes the run state to "idle".
    """
    state = Signal(str)
    next = Signal()
    finished = Signal()

    def __init__(self, main_window):
        super(StopEventWorker, self).__init__()
        self.main = main_window

    def stop_event(self):
        """Processes to stop event"""
        if self.main.ev_number + 1 >= self.main.config_class.config["run"]["max_num_evs"]:
            self.main.stopping_run = True
        self.next.emit()

        self.main.run_livetime += self.main.event_timer.elapsed()
        self.state.emit("Compressing")
        time.sleep(1)
        self.finished.emit()
