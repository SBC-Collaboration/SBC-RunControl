import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui.mainwindow import Ui_MainWindow
import logging
from enum import Enum
import time
from config import *
from workers import *

class MainWindow(QMainWindow):
    # define four run states
    run_states = Enum("State", ["Idle", "Starting", "Active", "Stopping"])
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        # logger initialization
        log_filename = "test-rc.log"
        log_format = '%(asctime)s %(levelname)s > %(message)s'
        logging.basicConfig(filename=log_filename, format=log_format, level=logging.INFO)
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.info("Starting run control.")

        # initialize run state
        # self.update_state("Idle")

    def quit(self):
        logging.info("Quitting run control.\n")
        self.close()

    def start_run(self):
        if self.state == self.run_states["Idle"]:
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
        if self.state == self.run_states["Active"]:
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
        self.state = self.run_states[s]
        logging.info(f"Run state: {s}.")
        self.run_state_label.setText(self.state.name)
        run_state_colors = ["lightgrey", "lightblue", "lightgreen", "lightpink"]
        self.run_state_label.setStyleSheet(f"background-color: {run_state_colors[self.state.value-1]}")
        if self.state == self.run_states["Idle"]:
            self.start_run_but.setEnabled(True)
            self.stop_run_but.setEnabled(False)
        elif self.state == self.run_states["Active"]:
            self.start_run_but.setEnabled(False)
            self.stop_run_but.setEnabled(True)
        else:
            self.start_run_but.setEnabled(False)
            self.stop_run_but.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())