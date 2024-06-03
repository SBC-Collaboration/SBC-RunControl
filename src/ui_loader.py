import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import QTimer
import logging
from enum import Enum
import time
from ui.settingswindow import Ui_SettingsWindow
from ui.logwindow import Ui_LogWindow
from src.config import Config


# Loads settings window
class SettingsWindow(QMainWindow):
    def __init__(self, mainwindow):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.main = mainwindow
        self.config_class = self.main.config_class
        self.config = self.config_class.config
        self.load_config()
        self.logger = logging.getLogger("rc")

        self.logger.debug("Settings window loaded.")

    def load_config(self):
        self.config_class.load_config_to_window(self.ui)

    def apply_config(self):
        self.config_class.apply_config(self.ui)

    def save_config(self):
        self.config_class.save_config_from_ui(self.ui, self.main.config_class.path)

    def select_config_path(self):
        config_path, _ = QFileDialog.getOpenFileName(self, self.config["general"]["config_path"])
        self.ui.config_path_edit.setText(config_path)

    def select_log_path(self):
        log_path = QFileDialog.getExistingDirectory(self, self.config["general"]["log_path"])
        self.ui.log_path_edit.setText(log_path)

    def select_data_dir(self):
        data_dir = QFileDialog.getExistingDirectory(self, self.config["general"]["data_dir"])
        self.ui.data_dir_edit.setText(data_dir)

    def select_trigger_sketch_dir(self):
        trigger_dir = QFileDialog.getExistingDirectory(
            self,
            caption="Trigger Arduino Sketch Directory",
            dir=self.config["dio"]["trigger"]["sketch"])
        self.ui.trigger_sketch_edit.setText(trigger_dir)

    def select_clock_sketch_dir(self):
        clock_dir = QFileDialog.getExistingDirectory(
            self,
            caption="Clock Arduino Sketch Directory",
            dir=self.config["dio"]["clock"]["sketch"])
        self.ui.clock_sketch_edit.setText(clock_dir)

    def select_position_sketch_dir(self):
        position_dir = QFileDialog.getExistingDirectory(
            self,
            caption="Position Arduino Sketch Directory",
            dir=self.config["dio"]["position"]["sketch"])
        self.ui.position_sketch_edit.setText(position_dir)

    def select_amp1_iv_dir(self):
        amp1_iv_dir = QFileDialog.getExistingDirectory(
            self,
            caption="SiPM Amp1 IV Data Directory",
            dir=self.config["scint"]["amp1"]["iv_rc_dir"])
        self.ui.sipm_amp1_iv_rc_data_dir_edit.setText(amp1_iv_dir)

    def select_amp2_iv_dir(self):
        amp2_iv_dir = QFileDialog.getExistingDirectory(
            self,
            caption="SiPM Amp1 IV Data Directory",
            dir=self.config["scint"]["amp2"]["iv_rc_dir"])
        self.ui.sipm_amp2_iv_rc_data_dir_edit.setText(amp2_iv_dir)


# Loads log window
class LogWindow(QMainWindow):
    def __init__(self, main_window):
        super(LogWindow, self).__init__()
        self.ui = Ui_LogWindow()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.load_log()
        self.logger = logging.getLogger("rc")

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)
        self.timer.start()

        self.logger.info("Log window loaded.")

    def periodic_task(self):
        self.load_log()

    def load_log(self):
        log = open(self.main_window.log_filename).read()
        self.ui.log_box.setPlainText(log)
        if self.ui.hold_end_box.isChecked():
            self.ui.log_box.moveCursor(QTextCursor.End)
