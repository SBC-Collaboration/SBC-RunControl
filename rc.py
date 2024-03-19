from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QElapsedTimer, QTimer, Qt
from PySide6.QtGui import QPixmap
from ui.mainwindow import Ui_MainWindow
from src.config import *
from src.workers import *
from src.ui_loader import *
from src.arduinos import *
from src.cameras import *
import logging
from enum import Enum
import datetime
import time
import re


# Loads Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.run_number = ""
        self.ev_number = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize config class
        self.config_class = Config(self, "config.json")
        self.config_class.load_config()

        # logger initialization
        self.logger = logging.getLogger(__name__)
        self.log_filename = self.config_class.config["general"]["log_path"]
        log_format = "%(asctime)s %(levelname)s > %(message)s"
        logging.basicConfig(
            filename=self.log_filename, format=log_format, level=logging.INFO
        )
        self.logger.addHandler(logging.StreamHandler())

        # initialize arduino class
        self.arduinos_class = Arduinos(self)

        # timer for event loop
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update)
        self.timer.timeout.connect(self.active_monitor)
        self.timer.start()
        # event timer
        self.event_timer = QElapsedTimer()
        self.run_livetime = 0

        # set up run handling thread
        self.run_handling_thread = QThread()

        # define four run states
        self.run_states = Enum(
            "State",
            ["Idle", "Preparing", "Active", "Starting", "Stopping", "Expanding", "Compressing"],
        )

        self.start_program_worker = StartProgramWorker(self)
        self.start_program_worker.moveToThread(self.run_handling_thread)
        self.run_handling_thread.started.connect(self.start_program_worker.run)
        self.start_program_worker.finished.connect(self.start_program_worker.deleteLater)
        self.start_program_worker.finished.connect(self.run_handling_thread.quit)
        self.start_program_worker.state.connect(self.update_state)
        self.run_handling_thread.start()


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
        self.logger.info("Quitting run control.\n")

    def open_settings_window(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()

    def open_log_window(self):
        self.log_window = LogWindow(self)
        self.log_window.show()

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        self.ui.file_path.setText(filename)

    def format_time(self, t):
        """
        Time formatting helper function for event time display
        """
        seconds, milliseconds = divmod(t, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours > 0:
            return f"{hours}h {minutes:02d}m {seconds:02d}s{milliseconds//100:1d}"
        elif minutes > 0:
            return f"{minutes}m {seconds:02d}s {milliseconds:03d}"
        else:
            return f"{seconds}s {milliseconds:03d}"

    def display_image(self, path, label, checked=True):
        # display image when checkbox checked
        # TODO: make it only render when checkbox changed
        if checked:
            image = QPixmap(path)
            aspect_ratio = image.height() / image.width()
            image = image.scaled(500, 500 * aspect_ratio, aspectMode=Qt.KeepAspectRatio)
            label.setPixmap(image)
        else:
            label.clear()

    # event loop
    def update(self):
        if self.run_state == self.run_states.Active:
            self.ui.event_time_edit.setText(
                self.format_time(self.event_timer.elapsed())
            )
            self.ui.run_live_time_edit.setText(
                self.format_time(self.event_timer.elapsed() + self.run_livetime)
            )
        self.display_image(
            "resources/cam1.png",
            self.ui.cam1_image,
            self.ui.cam1_image_check.isChecked(),
        )
        self.display_image(
            "resources/cam2.png",
            self.ui.cam2_image,
            self.ui.cam2_image_check.isChecked(),
        )
        self.display_image(
            "resources/cam3.png",
            self.ui.cam3_image,
            self.ui.cam3_image_check.isChecked(),
        )

    def create_run_directory(self):
        """
        Get all runs in the data directory, get the run numbers
        using regex to handle 2/3 digits of run number and possible suffix at the end
        would handle folder names like "20240101_00", "20240101_0001",
        "20240101_03 cf252", "20240101_04.252", non_continuous folder numbers
        it also handles the case that there's no runs today yet
        """
        data_dir = self.config_class.config["general"]["data_dir"]
        today = datetime.date.today().strftime("%Y%m%d")
        todays_runs = [
            int(re.search(r"\d+", r[9:])[0]) for r in os.listdir(data_dir) if today in r
        ]
        num = 0 if len(todays_runs) == 0 else max(todays_runs) + 1
        self.run_number = f"{today}_{num:02d}"

        self.run_dir = os.path.join(data_dir, self.run_number)
        if not os.path.exists(self.run_dir):
            os.mkdir(self.run_dir)
        self.ui.run_edit.setText(self.run_number)

    def active_monitor(self):
        if self.run_state == self.run_states.Active:
            if (
                self.event_timer.elapsed()
                > self.config_class.config["run"]["max_ev_time"] * 1000
            ):
                self.stop_event()

    def start_event(self):
        event_dir = os.path.join(self.run_dir, str(self.ev_number))
        if not os.path.exists(event_dir):
            os.mkdir(event_dir)

        def set_ev_num():
            self.ui.event_num_edit.setText(f"{self.ev_number:2d}")

        self.start_event_worker = StartEventWorker(self)
        self.start_event_worker.moveToThread(self.run_handling_thread)
        self.run_handling_thread.started.connect(self.start_event_worker.run)
        self.start_event_worker.finished.connect(self.start_event_worker.deleteLater)
        self.start_event_worker.finished.connect(self.run_handling_thread.quit)
        self.start_event_worker.state.connect(self.update_state)
        self.start_event_worker.ev_number.connect(set_ev_num)
        self.run_handling_thread.start()

    def stop_event(self):
        """
        Stop the event. Enter into compressing state. If the "Stop Run" button is pressed or the max number of events
        are reached, then it will enter into "stopping" state. Otherwise it will start another event.
        """

        # TODO: move this check into worker
        if (
            self.ui.stop_run_but.isChecked()
            or self.ev_number + 1 >= self.config_class.config["run"]["max_num_evs"]
        ):
            stop_run = True
        else:
            stop_run = False

        self.stop_event_worker = StopEventWorker(self)
        self.stop_event_worker.moveToThread(self.run_handling_thread)
        self.run_handling_thread.started.connect(self.stop_event_worker.run)
        self.stop_event_worker.finished.connect(self.stop_event_worker.deleteLater)
        self.stop_event_worker.finished.connect(self.run_handling_thread.quit)
        if stop_run: self.stop_event_worker.finished.connect(self.stop_run)
        else: self.stop_event_worker.finished.connect(self.start_event)
        self.stop_event_worker.state.connect(self.update_state)
        self.run_handling_thread.start()

    def start_run(self):
        if self.run_state == self.run_states["Idle"]:
            self.ui.event_time_edit.setText(self.format_time(0))
            # self.ui.run_live_time_edit.setText(self.format_time(self.run_livetime))
            self.create_run_directory()
            self.ev_number = 0

            # set up multithreading thread and workers
            self.start_run_worker = StartRunWorker(self)
            self.start_run_worker.moveToThread(self.run_handling_thread)
            self.run_handling_thread.started.connect(self.start_run_worker.run)
            self.start_run_worker.finished.connect(self.start_run_worker.deleteLater)
            self.start_run_worker.finished.connect(self.run_handling_thread.quit)
            self.start_run_worker.finished.connect(self.start_event)
            self.start_run_worker.state.connect(self.update_state)
            self.run_handling_thread.start()

    def stop_run(self):
        # set up multithreading thread and workers

        self.stop_run_worker = StopRunWorker(self)
        self.stop_run_worker.moveToThread(self.run_handling_thread)
        self.run_handling_thread.started.connect(self.stop_run_worker.run)
        self.stop_run_worker.finished.connect(self.stop_run_worker.deleteLater)
        self.stop_run_worker.finished.connect(self.run_handling_thread.quit)
        self.stop_run_worker.state.connect(self.update_state)
        self.run_handling_thread.start()

    def update_state(self, s):
        """
        The update_state function will change the self.run_state variable to the current state, and also change the GUI
        to reflect it. The "Start Run" and "Stop Run" buttons are enabled and disabled accordingly. The states are:
        - Idle: The program is idling. Settings can be changed and a new run can be started
        - Starting: The run is starting. A configuration file is used for the entire run.
        - Stopping: The running is stopping.
        - Expanding: An event is starting. The pump is expanding the chamber and all components are starting up,
        ready to take data
        - Compressing: The event is stopping. The pump is compressing back to non-superheated state, and all components
        are saving data to file.
        - Active: All components are actively taking data to buffer.
        """
        self.run_state = self.run_states[s]
        self.ui.run_state_label.setText(self.run_state.name)
        run_state_colors = [
            "lightgrey",
            "khaki",
            "lightgreen",
            "lightskyblue",
            "lightpink",
            "lightsalmon",
            "lightblue",
        ]
        self.ui.run_state_label.setStyleSheet(
            f"background-color: {run_state_colors[self.run_state.value-1]}"
        )
        self.ui.start_run_but.setEnabled(False)
        self.ui.stop_run_but.setEnabled(False)
        if self.run_state == self.run_states["Idle"]:
            self.logger.info(f"Entering into Idle state.")
            self.ui.start_run_but.setEnabled(True)
        elif self.run_state == self.run_states["Preparing"]:
            self.logger.info(f"Run control starting.")
        elif self.run_state == self.run_states["Active"]:
            self.logger.info(f"Event {self.ev_number} active.")
            self.ui.stop_run_but.setEnabled(True)
        elif self.run_state == self.run_states["Starting"]:
            self.logger.info(f"Starting Run {self.run_number}.")
            self.ui.stop_run_but.setEnabled(True)
        elif self.run_state == self.run_states["Stopping"]:
            self.logger.info(f"Stopping Run {self.run_number}.")
        elif self.run_state == self.run_states["Expanding"]:
            self.logger.info(f"Event {self.ev_number} expanding")
            self.ui.stop_run_but.setEnabled(True)
        elif self.run_state == self.run_states["Compressing"]:
            self.logger.info(f"Event {self.ev_number} compressing")
            self.ui.stop_run_but.setEnabled(True)
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
