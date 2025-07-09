import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import QTimer, Qt, QObject, QSignalBlocker, QStringListModel, Signal, Slot
import logging
from enum import Enum
import time
from ui.settingswindow import Ui_SettingsWindow
from ui.logwindow import Ui_LogWindow
import re
import numpy as np
from src.config import Config


# initialize class for syncing the status of two checkboxes
class CheckBoxPairBinder(QObject):
    def __init__(self, checkbox1, checkbox2):
        super(CheckBoxPairBinder, self).__init__()
        self.checkbox1 = checkbox1
        self.checkbox2 = checkbox2

        self.checkbox1.stateChanged.connect(self.sync_checkboxes)
        self.checkbox2.stateChanged.connect(self.sync_checkboxes)

    def sync_checkboxes(self, state):
        sender = self.sender()
        if sender == self.checkbox1:
            with QSignalBlocker(self.checkbox2):
                self.checkbox2.setCheckState(Qt.CheckState(state))
        elif sender == self.checkbox2:
            with QSignalBlocker(self.checkbox1):
                self.checkbox1.setCheckState(Qt.CheckState(state))


# Class for handling group checkbox synchronization (group checkbox with multiple individual checkboxes)
class CheckBoxGroupBinder(QObject):
    def __init__(self, group_checkbox, individual_checkboxes):
        super(CheckBoxGroupBinder, self).__init__()
        self.group_checkbox = group_checkbox
        self.individual_checkboxes = individual_checkboxes
        self._updating_group = False  # Flag to prevent infinite loops
        
        # Enable tristate for the group checkbox
        self.group_checkbox.setTristate(True)
        
        # Connect signals
        self.group_checkbox.stateChanged.connect(self.group_changed)
        for checkbox in self.individual_checkboxes:
            checkbox.stateChanged.connect(self.individual_changed)
        
        # Initialize the group state
        self.update_group_state()

    def group_changed(self, state):
        """When group checkbox changes, update all individual checkboxes"""
        if self._updating_group or Qt.CheckState(state) == Qt.PartiallyChecked:
            # Don't change individual checkboxes when we're updating the group state
            # or when partially checked
            return
            
        new_state = Qt.CheckState(state)
        # Don't use QSignalBlocker here - let the signals propagate to pair binders
        for checkbox in self.individual_checkboxes:
            checkbox.setCheckState(new_state)

    def individual_changed(self, state):
        """When any individual checkbox changes, update the group checkbox"""
        if not self._updating_group:
            self.update_group_state()

    def update_group_state(self):
        """Update group checkbox state based on individual checkboxes"""
        self._updating_group = True  # Set flag to prevent recursion
        
        checked_count = sum(1 for cb in self.individual_checkboxes if cb.isChecked())
        total_count = len(self.individual_checkboxes)
        
        with QSignalBlocker(self.group_checkbox):
            if checked_count == 0:
                self.group_checkbox.setCheckState(Qt.Unchecked)
            elif checked_count == total_count:
                self.group_checkbox.setCheckState(Qt.Checked)
            else:
                self.group_checkbox.setCheckState(Qt.PartiallyChecked)
        
        self._updating_group = False  # Reset flag


# Loads settings window
class SettingsWindow(QMainWindow):
    def __init__(self, mainwindow):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.main = mainwindow
        self.config_class = self.main.config_class
        self.config = self.config_class.config
        self.logger = logging.getLogger("rc")

        self.widgets = self.ui.__dict__
        for group in ["g0", "g1", "g2", "g3"]:
            for ch in range(8):
                self.widgets[f"caen_{group}_trig_mask_{ch}"].stateChanged.connect(self.caen_individual_changed)
                self.widgets[f"caen_{group}_acq_mask_{ch}"].stateChanged.connect(self.caen_individual_changed)
                self.widgets[f"caen_{group}_plot_mask_{ch}"].stateChanged.connect(self.caen_individual_changed)
            self.widgets[f"caen_{group}_trig_box"].stateChanged.connect(self.caen_group_changed)
            self.widgets[f"caen_{group}_acq_box"].stateChanged.connect(self.caen_group_changed)
            self.widgets[f"caen_{group}_plot_box"].stateChanged.connect(self.caen_group_changed)
        self.caen_individual_changed()

        # connect upload sketch signals, force upload
        self.ui.trigger_upload_but.clicked.connect(
            lambda: self.main.arduino_trigger_worker.upload_sketch(check_archive=False))
        self.ui.clock_upload_but.clicked.connect(
            lambda: self.main.arduino_clock_worker.upload_sketch(check_archive=False))
        self.ui.position_upload_but.clicked.connect(
            lambda: self.main.arduino_position_worker.upload_sketch(check_archive=False))

        # set up checkboxes pairs and groups
        # Individual checkbox pairs (general tab <-> specific tab)
        self.checkpair_pressure = CheckBoxPairBinder(self.widgets["active_plc"], self.widgets["plc_enabled_box"])
        self.checkpair_sql = CheckBoxPairBinder(self.widgets["active_sql"], self.widgets["sql_enabled_box"])
        self.checkpair_writer = CheckBoxPairBinder(self.widgets["active_writer"], self.widgets["writer_enabled_box"])
        self.checkpair_acoustic = CheckBoxPairBinder(self.widgets["active_acous"], self.widgets["acous_enabled_box"])
        
        # Camera checkboxes
        self.checkpair_cam1 = CheckBoxPairBinder(self.widgets["active_cam1"], self.widgets["cam1_enabled_box"])
        self.checkpair_cam2 = CheckBoxPairBinder(self.widgets["active_cam2"], self.widgets["cam2_enabled_box"])
        self.checkpair_cam3 = CheckBoxPairBinder(self.widgets["active_cam3"], self.widgets["cam3_enabled_box"])
        
        # SiPM amp checkboxes
        self.checkpair_amp1 = CheckBoxPairBinder(self.widgets["active_amp1"], self.widgets["sipm_amp1_enabled_box"])
        self.checkpair_amp2 = CheckBoxPairBinder(self.widgets["active_amp2"], self.widgets["sipm_amp2_enabled_box"])
        self.checkpair_amp3 = CheckBoxPairBinder(self.widgets["active_amp3"], self.widgets["sipm_amp3_enabled_box"])
        
        # CAEN checkboxes
        self.checkpair_caen = CheckBoxPairBinder(self.widgets["active_caen"], self.widgets["caen_enabled_box"])
        self.checkpair_caen0 = CheckBoxPairBinder(self.widgets["active_caen_g0"], self.widgets["caen_g0_enable_box"])
        self.checkpair_caen1 = CheckBoxPairBinder(self.widgets["active_caen_g1"], self.widgets["caen_g1_enable_box"])
        self.checkpair_caen2 = CheckBoxPairBinder(self.widgets["active_caen_g2"], self.widgets["caen_g2_enable_box"])
        self.checkpair_caen3 = CheckBoxPairBinder(self.widgets["active_caen_g3"], self.widgets["caen_g3_enable_box"])

        # Group checkboxes (group checkbox controls multiple individual checkboxes)
        # Cameras group - "active_cams" controls cam1, cam2, cam3 AND also syncs with "cams_enabled_box"
        cam_individual_checkboxes = [self.widgets["cam1_enabled_box"], 
                                     self.widgets["cam2_enabled_box"], 
                                     self.widgets["cam3_enabled_box"]]
        self.checkgroup_cams = CheckBoxGroupBinder(self.widgets["cams_enabled_box"], cam_individual_checkboxes)

        # set up shared combo boxes
        self.sipm_names = QStringListModel(["NC",
                                            "SiPM11", "SiPM12", "SiPM14", "SiPM15",
                                            "SiPM22", "SiPM23", "SiPM25", "SiPM26",
                                            "SiPM31", "SiPM32", "SiPM34", "SiPM35",
                                            "SiPM42", "SiPM43", "SiPM45", "SiPM46",
                                            "SiPM51", "SiPM52", "SiPM54", "SiPM55",
                                            "SiPM62", "SiPM63", "SiPM65", "SiPM66",
                                            "SiPM71", "SiPM72", "SiPM74", "SiPM75",
                                            "SiPM82", "SiPM83", "SiPM85", "SiPM86"])
        
        for amp in ["amp1", "amp2", "amp3"]:
            for ch in range(1, 17):
                self.widgets[f"sipm_{amp}_name_ch{ch}"].setModel(self.sipm_names)

        self.amp_names = QStringListModel(["NC",
                                           "1-01", "1-02", "1-03", "1-04", "1-05", "1-06", "1-07", "1-08",
                                           "1-09", "1-10", "1-11", "1-12", "1-13", "1-14", "1-15", "1-16",
                                           "2-01", "2-02", "2-03", "2-04", "2-05", "2-06", "2-07", "2-08",
                                           "2-09", "2-10", "2-11", "2-12", "2-13", "2-14", "2-15", "2-16",
                                           "3-01", "3-02", "3-03", "3-04", "3-05", "3-06", "3-07", "3-08",
                                           "3-09", "3-10", "3-11", "3-12", "3-13", "3-14", "3-15", "3-16"])
        for gp in ["g0", "g1", "g2", "g3"]:
            for ch in range(8):
                self.widgets[f"caen_{gp}_name_{ch}"].setModel(self.amp_names)

        self.load_config()
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

    def select_log_dir(self):
        log_dir = QFileDialog.getExistingDirectory(self, self.config["general"]["log_dir"])
        self.ui.log_dir_edit.setText(log_dir)

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
            caption="SiPM Amp2 IV Data Directory",
            dir=self.config["scint"]["amp2"]["iv_rc_dir"])
        self.ui.sipm_amp2_iv_rc_data_dir_edit.setText(amp2_iv_dir)
    
    def select_amp3_iv_dir(self):
        amp3_iv_dir = QFileDialog.getExistingDirectory(
            self,
            caption="SiPM Amp3 IV Data Directory",
            dir=self.config["scint"]["amp3"]["iv_rc_dir"])
        self.ui.sipm_amp3_iv_rc_data_dir_edit.setText(amp3_iv_dir)

    def select_caen_data_path(self):
        caen_data_path = QFileDialog.getExistingDirectory(
            self,
            caption="CAEN Data Directory",
            dir=self.config["scint"]["caen"]["data_path"]
        )
        self.ui.caen_data_path_box.setText(caen_data_path)

    def caen_individual_changed(self):
        if self.sender():
            sender = self.sender().objectName()
            pattern = r"_g[0-3]_(trig|acq|plot)_"
            match = re.search(pattern, sender)
            settings = [match.group(0)[1:-1]]  # g0-3_trig/acq/plot
        else:
            settings = [f"{group}_{mode}" for group in ["g0", "g1", "g2", "g3"] for mode in ["trig", "acq", "plot"]]

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
            pattern = r"_g[0-3]_(trig|acq|plot)_"
            match = re.search(pattern, sender)
            setting = match.group(0)[1:-1] # g0-3_trig/acq/plot
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
