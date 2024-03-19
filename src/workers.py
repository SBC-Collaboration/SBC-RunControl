import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from enum import Enum
import logging
import time


class StartProgramWorker(QObject):
    """
    Worker class for starting up Run Control.
    """
    state = Signal(str)
    finished = Signal()

    def __init__(self, main_window):
        super(StartProgramWorker, self).__init__()
        self.main_window = main_window

    def run(self):
        """Processes to start run"""
        self.state.emit("Starting")
        time.sleep(1)
        self.state.emit("Active")
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
        self.main_window = main_window

    def run(self):
        """Processes to start run"""
        self.state.emit("Starting")
        time.sleep(1)
        self.state.emit("Active")
        self.finished.emit()


class StopRunWorker(QObject):
    """
    Worker class for stopping a run. It will change the run state into "stopping", then wait for each DAQ modules to
    end. Then it changes the run state to "idle".
    """
    state = Signal(str)
    finished = Signal()

    def run(self):
        """Processes to start run"""
        self.state.emit("Stopping")
        time.sleep(1)
        self.state.emit("Idle")
        self.finished.emit()
    