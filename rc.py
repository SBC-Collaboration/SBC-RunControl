import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile
from ui.mainwindow import Ui_MainWindow
from src.config import *
from src.workers import *
from src.ui_loader import SettingsWindow, LogWindow
import logging
from enum import Enum
import time, datetime
import re


# Loads Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize config class
        self.start_config()

        # logger initialization
        self.log_filename = self.config.config["general"]["log_path"]
        log_format = "%(asctime)s %(levelname)s > %(message)s"
        logging.basicConfig(
            filename=self.log_filename, format=log_format, level=logging.INFO
        )
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.info("Starting run control.")

        # define four run states
        self.run_states = Enum("State", ["Idle", "Starting", "Active", "Stopping"])
        # initialize run state
        self.update_state("Idle")

    # TODO: handle closing during run
    def closeEvent(self, event):
        # close other opened windows before closing
        try:
            self.log_window.close()
        except AttributeError:
            pass
        try:
            self.settings_window.close()
        except AttributeError:
            pass
        logging.info("Quitting run control.\n")

    def start_config(self):
        self.config = Config(self, "config.json")
        self.config.load_config()

    def open_settings_window(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()

    def open_log_window(self):
        self.log_window = LogWindow(self)
        self.log_window.show()

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        self.ui.file_path.setText(filename)

    def create_run_directory(self):
        # get all runs in the data directory, get the run numbers
        # using regex to handle 2/3 digits of run number and possible suffix at the end
        # would handle folder names like "20240101_00", "20240101_0001", "20240101_03 cf252", ""20240101_04.252", non_continuous folder numbers
        # it also handles the case that there's no runs today yet
        data_dir = self.config.config["general"]["data_dir"]
        today = datetime.date.today().strftime("%Y%m%d")
        todays_runs = [int(re.search(r"\d+", r[9:])[0]) for r in os.listdir(data_dir) if today in r]
        num = 0 if len(todays_runs)==0 else max(todays_runs)+1
        self.run_number = f"{today}_{num:02d}"

        os.mkdir(os.path.join(data_dir, self.run_number))
        self.ui.run_edit.setText(self.run_number)

    def start_run(self):
        if self.run_state == self.run_states["Idle"]:
            self.create_run_directory()

            # set up multithreading thread and workers
            # TODO: check if thread can persist between runs while worker rerun every time
            # TODO: implement event timer / livetime timer
            self.start_run_thread = QThread()
            self.start_run_worker = StartRunWorker()
            self.start_run_worker.moveToThread(self.start_run_thread)
            self.start_run_thread.started.connect(self.start_run_worker.run)
            self.start_run_worker.finished.connect(self.start_run_thread.quit)
            self.start_run_worker.finished.connect(self.start_run_worker.deleteLater)
            self.start_run_thread.finished.connect(self.start_run_thread.deleteLater)
            self.start_run_worker.state.connect(self.update_state)
            self.start_run_thread.start()

    def stop_run(self):
        if self.run_state == self.run_states["Active"]:
            # set up multithreading thread and workers
            self.stop_run_thread = QThread()
            self.stop_run_worker = StopRunWorker()
            self.stop_run_worker.moveToThread(self.stop_run_thread)
            self.stop_run_thread.started.connect(self.stop_run_worker.run)
            self.stop_run_worker.finished.connect(self.stop_run_thread.quit)
            self.stop_run_worker.finished.connect(self.stop_run_worker.deleteLater)
            self.stop_run_thread.finished.connect(self.stop_run_thread.deleteLater)
            self.stop_run_worker.state.connect(self.update_state)
            self.stop_run_thread.start()

    def update_state(self, s):
        self.run_state = self.run_states[s]
        self.ui.run_state_label.setText(self.run_state.name)
        run_state_colors = ["lightgrey", "lightblue", "lightgreen", "lightpink"]
        self.ui.run_state_label.setStyleSheet(
            f"background-color: {run_state_colors[self.run_state.value-1]}"
        )
        if self.run_state == self.run_states["Idle"]:
            logging.info(f"Entering into Idle state.")
            self.ui.start_run_but.setEnabled(True)
            self.ui.stop_run_but.setEnabled(False)
        elif self.run_state == self.run_states["Active"]:
            logging.info(f"Run {self.run_number} active.")
            self.ui.start_run_but.setEnabled(False)
            self.ui.stop_run_but.setEnabled(True)
        elif self.run_state == self.run_states["Starting"]:
            logging.info(f"Starting Run {self.run_number}.")
            self.ui.start_run_but.setEnabled(False)
            self.ui.stop_run_but.setEnabled(False)
        elif self.run_state == self.run_states["Stopping"]:
            logging.info(f"Stopping Run {self.run_number}.")
            self.ui.start_run_but.setEnabled(False)
            self.ui.stop_run_but.setEnabled(False)
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
