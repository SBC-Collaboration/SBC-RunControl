import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from enum import Enum
import logging
import time
from workers import *


class MainWindow(QMainWindow):
    states = Enum("State", ["Idle", "Starting", "Active", "Stopping"])

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SBC Run Control")
        self.resize(1200, 750)

        # logger initialization
        log_filename = "test-rc.log"
        log_format = '%(asctime)s %(levelname)s > %(message)s'
        logging.basicConfig(filename=log_filename, format=log_format, level=logging.INFO)
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.info("Run control starting.")

        # initialize run state
        self.state = self.states["Idle"]

        layout = QGridLayout()

        self.quit_but = QPushButton("Quit")
        self.quit_but.clicked.connect(self.quit)
        layout.addWidget(self.quit_but, 0, 0)

        # start run button
        self.start_run_but = QPushButton("Start Run")
        # self.start_run_but.setCheckable(True)
        # self.start_run_but.toggled.connect(self.start_run)
        self.start_run_but.clicked.connect(self.start_run)
        layout.addWidget(self.start_run_but, 1, 0)

        # stop run button
        self.stop_run_but = QPushButton("Stop Run")
        # self.stop_run_but.setCheckable(True)
        self.stop_run_but.clicked.connect(self.stop_run)
        layout.addWidget(self.stop_run_but, 2, 0)

        self.state_label = QLabel(self)
        self.state_label.setText("State")
        layout.addWidget(self.state_label, 3, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def quit(self):
        logging.info("Quitting run control.\n")
        self.close()

    def start_run(self):
        if self.state == self.states["Idle"]:
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
        if self.state == self.states["Active"]:
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
        self.state = self.states[s]
        logging.info(f"Run state: {s}.")
        self.state_label.setText(self.state.name)
        state_colors = ["lightgrey", "lightblue", "lightgreen", "lightpink"]
        self.state_label.setStyleSheet(f"background-color: {state_colors[self.state.value-1]}")


app = QApplication(sys.argv)
win = MainWindow()
win.show()

sys.exit(app.exec())
