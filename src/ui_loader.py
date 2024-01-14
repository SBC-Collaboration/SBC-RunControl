import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile, Qt
import logging
from enum import Enum
import time
from ui.settingswindow import Ui_SettingsWindow
from ui.logwindow import Ui_LogWindow
from src.config import *
from src.workers import *


# Loads settings window
class SettingsWindow(QMainWindow):
    def __init__(self, main_window):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

    def select_config_path(self):
        config_path, _ = QFileDialog.getOpenFileName(self)
        self.ui.config_path_edit.setText(config_path)

    def select_data_path(self):
        data_path, _ = QFileDialog.getOpenFileName(self)
        self.ui.data_path_edit.setText(data_path)


# Loads log window
class LogWindow(QMainWindow):
    def __init__(self, main_window):
        super(LogWindow, self).__init__()
        self.ui = Ui_LogWindow()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.load_log()

    def load_log(self):
        log = open(self.main_window.log_filename).read()
        self.ui.log_box.setPlainText(log)
        if self.ui.hold_end_box.isChecked():
            self.ui.log_box.moveCursor(QTextCursor.End)
