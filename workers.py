import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from enum import Enum
import logging
import time


class StartRunWorker(QObject):
    state = Signal(str)
    finished = Signal()

    def run(self):
        """Processes to start run"""
        self.state.emit("Starting")
        time.sleep(1)
        self.state.emit("Active")
        self.finished.emit()


class StopRunWorker(QObject):
    state = Signal(str)
    finished = Signal()

    def run(self):
        """Processes to start run"""
        self.state.emit("Stopping")
        time.sleep(1)
        self.state.emit("Idle")
        self.finished.emit()