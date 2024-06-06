import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import QTimer, Qt
import logging
from enum import Enum
import time
from ui.settingswindow import Ui_SettingsWindow
from ui.logwindow import Ui_LogWindow
import re
import numpy as np
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

        self.widgets = self.ui.__dict__
        for group in ["g0", "g1", "g2", "g3"]:
            for ch in range(8):
                self.widgets[f"caen_{group}_trig_mask_{ch}"].stateChanged.connect(self.caen_individual_changed)
                self.widgets[f"caen_{group}_acq_mask_{ch}"].stateChanged.connect(self.caen_individual_changed)
            self.widgets[f"caen_{group}_trig_box"].stateChanged.connect(self.caen_group_changed)
            self.widgets[f"caen_{group}_acq_box"].stateChanged.connect(self.caen_group_changed)
        self.caen_individual_changed()

        self.logger.debug("Settings window loaded.")

    def load_config(self):
        self.config_class.load_config_to_window(self.ui)

    def load_config_from_file(self):
        config_path, _ = QFileDialog.getOpenFileName(
            self,
            caption="Config file to load",
            dir=self.config["general"]["config_path"]
        )
        self.config_class.load_config_from_file(config_path, self.ui)

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

    def select_caen_exec_path(self):
        caen_exec_path, _ = QFileDialog.getOpenFileName(
            self,
            caption="CAEN Software Executable Location",
            dir=self.config["scint"]["caen"]["exec_path"]
        )
        self.ui.caen_exec_path_edit.setText(caen_exec_path)

    def select_caen_config_path(self):
        caen_config_path, _ = QFileDialog.getOpenFileName(
            self,
            caption="CAEN Configuration File Location",
            dir=self.config["scint"]["caen"]["config_path"]
        )
        self.ui.caen_config_path_edit.setText(caen_config_path)

    def caen_individual_changed(self):
        if self.sender():
            sender = self.sender().objectName()
            pattern = r"_g[0-3]_(trig|acq)_"
            match = re.search(pattern, sender)
            settings = [match.group(0)[1:-1]]  # g0-3_trig/acq
        else:
            settings = [f"{group}_{mode}" for group in ["g0", "g1", "g2", "g3"] for mode in ["trig", "acq"]]

        for setting in settings:
            trigger_enabled = [self.widgets[f"caen_{setting}_mask_{ch}"].isChecked() for ch in range(8)]
            if np.sum(trigger_enabled) == 0:
                self.widgets[f"caen_{setting}_box"].setCheckState(Qt.Unchecked)
            elif np.sum(trigger_enabled) == 8:
                self.widgets[f"caen_{setting}_box"].setCheckState(Qt.Checked)
            else:
                self.widgets[f"caen_{setting}_box"].setCheckState(Qt.PartiallyChecked)

    def caen_group_changed(self, state):
        if self.sender():
            sender = self.sender().objectName()
            pattern = r"_g[0-3]_(trig|acq)_"
            match = re.search(pattern, sender)
            setting = match.group(0)[1:-1] # g0-3_trig/acq
        else:
            return

        if Qt.CheckState(state) == Qt.Unchecked:
            for ch in range(8):
                self.widgets[f"caen_{setting}_mask_{ch}"].setChecked(False)
        elif Qt.CheckState(state) == Qt.Checked:
            for ch in range(8):
                self.widgets[f"caen_{setting}_mask_{ch}"].setChecked(True)
        else:
            return  # if partially checked, do nothing


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
