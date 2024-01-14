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


# Loads Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # logger initialization
        self.log_filename = "test-rc.log"
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

    def start_run(self):
        if self.run_state == self.run_states["Idle"]:
            self.run_number = datetime.date.today().strftime("%Y%m%d")+"_00"
            self.ui.run_edit.setText(self.run_number)

            # set up multithreading thread and workers
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

    def open_settings_window(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()

    def open_log_window(self):
        self.log_window = LogWindow(self)
        self.log_window.show()

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        self.ui.file_path.setText(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
