# # recompile UI files before starting
# import os
# os.system('for ui in ui/*.ui; do name="${ui%%.*}"; pyside6-uic $ui -o "$name.py"; done')

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QObject, QThread, Signal, Slot, QElapsedTimer, QTimer, Qt, QMutex, QWaitCondition
from PySide6.QtGui import QPixmap
from ui.mainwindow import Ui_MainWindow
from src.config import Config
from src.ui_loader import SettingsWindow, LogWindow
from src.arduinos import Arduino
from src.caen import Caen
from src.cameras import Camera
from src.sipm_amp import SiPMAmp
from src.sql import SQL
from src.niusb import NIUSB
from src.writer import Writer
import logging
from enum import Enum
import subprocess
import datetime
import time
import re
import sys
import os


class MainSignals(QObject):
    # initialize signals
    program_starting = Signal()
    run_starting = Signal()
    run_stopping = Signal()
    event_starting = Signal()
    event_stopping = Signal()
    send_trigger = Signal(str)
    program_stopping = Signal()


# Loads Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.run_id = ""
        self.event_id = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize config class
        self.config_class = Config(self, "config.json")
        self.config_class.load_config()
        self.stopping_run = False

        # logger initialization
        self.logger = logging.getLogger("rc")
        self.log_filename = self.config_class.config["general"]["log_path"]
        self.log_format = "%(asctime)s %(levelname)s > %(message)s"
        self.log_formatter = logging.Formatter(self.log_format)
        logging.basicConfig(
            filename=self.log_filename, format=self.log_format, level=logging.DEBUG
        )
        self.logger.addHandler(logging.StreamHandler())

        # define four run states
        self.run_states = Enum(
            "State",
            [
                "idle",
                "preparing",
                "active",
                "starting_run",
                "stopping_run",
                "starting_event",
                "stopping_event",
            ],
        )

        self.update_state("preparing")

        # List populated by ready modules at each state. After all modules are ready, it will proceed to the next state
        self.starting_program_ready = []
        self.starting_run_ready = []
        self.stopping_run_ready = []
        self.starting_event_ready = []
        self.stopping_event_ready = []
        self.set_up_workers()

        # timer for event loop
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update)
        self.timer.start()
        # event timer
        self.event_timer = QElapsedTimer()
        self.run_livetime = 0
        self.ev_livetime = 0

        # initialize writer for sbc binary format
        # sbc_writer = Writer()

        self.start_program()

    def set_up_workers(self):
        self.signals = MainSignals()

        # set up run handling thread and the worker
        vars = self.__dict__
        ui_vars = self.ui.__dict__
        for cam in ["cam1", "cam2", "cam3"]:
            vars[f"{cam}_worker"] = Camera(self, cam)
            vars[f"{cam}_worker"].camera_started.connect(self.starting_run_wait)
            vars[f"{cam}_worker"].camera_closed.connect(self.stopping_run_wait)
            vars[f"{cam}_thread"] = QThread()
            vars[f"{cam}_thread"].setObjectName(f"{cam}_thread")
            vars[f"{cam}_worker"].moveToThread(vars[f"{cam}_thread"])
            vars[f"{cam}_thread"].started.connect(vars[f"{cam}_worker"].run)
            self.signals.run_starting.connect(vars[f"{cam}_worker"].start_camera)
            self.signals.run_starting.connect(ui_vars[f"gen_status_{cam}"].working)
            self.signals.run_stopping.connect(vars[f"{cam}_worker"].stop_camera)
            vars[f"{cam}_thread"].start()
            time.sleep(0.001)

        for amp in ["amp1", "amp2"]:
            vars[f"{amp}_worker"] = SiPMAmp(self, amp)
            vars[f"{amp}_worker"].sipm_biased.connect(self.starting_run_wait)
            vars[f"{amp}_worker"].sipm_unbiased.connect(self.stopping_run_wait)
            vars[f"{amp}_thread"] = QThread()
            vars[f"{amp}_thread"].setObjectName(f"{amp}_thread")
            vars[f"{amp}_worker"].moveToThread(vars[f"{amp}_thread"])
            vars[f"{amp}_thread"].started.connect(vars[f"{amp}_worker"].run)
            self.signals.run_starting.connect(vars[f"{amp}_worker"].bias_sipm)
            self.signals.run_stopping.connect(vars[f"{amp}_worker"].unbias_sipm)
            vars[f"{amp}_thread"].start()
            time.sleep(0.001)

        for ino in ["trigger", "clock", "position"]:
            vars[f"arduino_{ino}_worker"] = Arduino(self, ino)
            vars[f"arduino_{ino}_worker"].sketch_uploaded.connect(self.starting_run_wait)
            vars[f"arduino_{ino}_thread"] = QThread()
            vars[f"arduino_{ino}_thread"].setObjectName(f"arduino_{ino}_thread")
            vars[f"arduino_{ino}_worker"].moveToThread(vars[f"arduino_{ino}_thread"])
            vars[f"arduino_{ino}_thread"].started.connect(vars[f"arduino_{ino}_worker"].run)
            self.signals.run_starting.connect(vars[f"arduino_{ino}_worker"].upload_sketch)
            vars[f"arduino_{ino}_thread"].start()
            time.sleep(0.001)

        self.caen_worker = Caen(self)

        self.caen_thread = QThread()
        self.caen_thread.setObjectName("caen_thread")
        self.caen_worker.moveToThread(self.caen_thread)
        self.caen_thread.started.connect(self.caen_worker.run)
        self.caen_thread.start()
        time.sleep(0.001)

        self.niusb_worker = NIUSB(self)
        self.niusb_worker.run_started.connect(self.starting_run_wait)
        self.niusb_worker.event_started.connect(self.starting_event_wait)
        self.niusb_worker.event_stopped.connect(self.stopping_event_wait)
        self.niusb_worker.run_stopped.connect(self.stopping_run_wait)
        self.niusb_worker.trigger_detected.connect(self.stop_event)
        self.niusb_worker.trigger_ff.connect(self.ui.trigger_edit.setText)
        self.niusb_thread = QThread()
        self.niusb_thread.setObjectName("niusb_thread")
        self.niusb_worker.moveToThread(self.niusb_thread)
        self.niusb_thread.started.connect(self.niusb_worker.run)
        self.signals.run_starting.connect(self.niusb_worker.start_run)
        self.signals.event_starting.connect(self.niusb_worker.start_event)
        self.signals.event_stopping.connect(self.niusb_worker.stop_event)
        self.signals.run_stopping.connect(self.niusb_worker.stop_run)
        self.signals.send_trigger.connect(self.niusb_worker.send_trigger)
        self.niusb_thread.start()
        time.sleep(0.001)

        self.writer_worker = Writer(self)
        self.writer_worker.event_data_saved.connect(self.starting_event_wait)
        self.writer_thread = QThread()
        self.writer_thread.setObjectName("writer_thread")
        self.writer_worker.moveToThread(self.writer_thread)
        self.writer_thread.started.connect(self.writer_worker.run)
        self.signals.event_stopping.connect(self.writer_worker.write_event_data)
        self.writer_thread.start()
        time.sleep(0.001)

        self.sql_worker = SQL(self)
        self.sql_worker.run_started.connect(self.starting_run_wait)
        self.sql_worker.run_stopped.connect(self.stopping_run_wait)
        self.sql_worker.event_stopped.connect(self.stopping_event_wait)
        self.sql_thread = QThread()
        self.sql_thread.setObjectName("sql_thread")
        self.sql_worker.moveToThread(self.sql_thread)
        self.sql_thread.started.connect(self.sql_worker.run)
        self.signals.run_starting.connect(self.sql_worker.start_run)
        self.signals.event_stopping.connect(self.sql_worker.stop_event)
        self.signals.run_stopping.connect(self.sql_worker.stop_run)
        self.sql_thread.start()

        # establish mutex and wait conditions for syncing
        self.config_mutex = QMutex()
        self.config_wait = QWaitCondition()
        self.trigff_mutex = QMutex()
        self.trigff_wait = QWaitCondition()

    # TODO: handle closing during run
    def closeEvent(self, event):
        """
        Custom function overriding the close event behavior. It will close both log and settings window, and also leave message in the logger.
        """
        # close other opened windows before closing
        try:
            self.log_window.close()
        except AttributeError:
            pass
        try:
            self.settings_window.close()
        except AttributeError:
            pass

        # quit all created workers and threads
        vars = self.__dict__
        for name, var in vars.items():
            if name.endswith("_worker"):
                var.deleteLater()
            elif name.endswith("_thread"):
                var.quit()
                var.wait()

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
        Time formatting helper function for event time display. t is in milliseconds
        If time is under a minute, it will return "12s 345"
        If time ie between a minute and an hour, it will return "12m 34s 567"
        If time is more than an hour, it will return "12h 34m 56s 789"
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
        """
        Function that controls image display of last event
        """
        # display image when checkbox checked
        # TODO: make it only render when checkbox changed
        if checked:
            image = QPixmap(path)
            aspect_ratio = image.height() / image.width()
            image = image.scaled(500, 500 * aspect_ratio, aspectMode=Qt.KeepAspectRatio)
            label.setPixmap(image)
        else:
            label.clear()


    def update_state(self, s):
        """
        The update_state function will change the self.run_state variable to the current state, and also change the GUI
        to reflect it. The "Start Run" and "Stop Run" buttons are enabled and disabled accordingly. The states are:
        - "Preparing": The program is starting up. Initializing necessary variables.
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
            "lightblue",
            "lightsalmon",
        ]
        self.ui.run_state_label.setStyleSheet(
            f"background-color: {run_state_colors[self.run_state.value-1]}"
        )

        start_run_but_available = False
        stop_run_but_available = False

        self.ui.stop_run_but.setEnabled(False)
        if self.run_state == self.run_states["idle"]:
            self.logger.info(f"Entering into Idle state.")
            start_run_but_available = True
        elif self.run_state == self.run_states["preparing"]:
            self.logger.info(f"Run control starting.")
        elif self.run_state == self.run_states["active"]:
            self.logger.info(f"Event {self.event_id} active.")
            stop_run_but_available = True
        elif self.run_state == self.run_states["starting_run"]:
            self.logger.info(f"Starting Run {self.run_id}.")
            stop_run_but_available = True
        elif self.run_state == self.run_states["stopping_run"]:
            self.logger.info(f"Stopping Run {self.run_id}.")
        elif self.run_state == self.run_states["starting_event"]:
            self.logger.info(f"Event {self.event_id} starting")
            stop_run_but_available = True
        elif self.run_state == self.run_states["stopping_event"]:
            self.logger.info(f"Event {self.event_id} stopping")
            stop_run_but_available = True
        else:
            pass

        if start_run_but_available:
            self.ui.start_run_but.setEnabled(True)
        else:
            self.ui.start_run_but.setEnabled(False)
        if stop_run_but_available and not self.stopping_run:
            self.ui.stop_run_but.setEnabled(True)
        else:
            self.ui.stop_run_but.setEnabled(False)

    # event loop
    @Slot()
    def update(self):
        """
        Event loop function. Every 100ms this function will run.
        In the active state, it will update event and run timer, and check if max event time is reached. If so, it will end the event.

        """
        vars = self.ui.__dict__

        if self.run_state == self.run_states["active"]:
            self.ui.event_time_edit.setText(
                self.format_time(self.event_timer.elapsed())
            )
            self.ui.run_live_time_edit.setText(
                self.format_time(self.event_timer.elapsed() + self.run_livetime)
            )
            if (
                self.event_timer.elapsed()
                > self.config_class.run_config["general"]["max_ev_time"] * 1000
            ):
                self.signals.send_trigger.emit("Timeout")
        elif self.run_state == self.run_states["starting_run"]:
            if len(self.starting_run_ready) >= 10:
                self.start_event()
        elif self.run_state == self.run_states["starting_event"]:
            self.event_timer.start()
            if len(self.starting_event_ready) >= 4:
                self.update_state("active")
        elif self.run_state == self.run_states["stopping_event"]:
            if len(self.stopping_event_ready) >= 4:
                self.start_event()
        elif self.run_state == self.run_states["stopping_run"]:
            if len(self.stopping_run_ready) >= 1:
                self.update_state("idle")

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

    @Slot(str)
    def starting_program_wait(self, module):
        self.starting_program_ready.append(module)

    @Slot(str)
    def starting_run_wait(self, module):
        """
        A slot method to append ready module names to the list. When the length of the list reaches the threshold, the run can start.
        """
        vars = self.ui.__dict__
        if "disabled" in module:
            name = re.sub(r'^.*?-', "", module)
            self.logger.info(f"Starting Run: {name} is disabled")
            vars[f"gen_status_{name}"].idle()
            self.starting_run_ready.append(module)
            return

        self.logger.info(f"Starting Run: {module} is complete")
        # change status lights

        vars[f"gen_status_{module}"].active()
        self.starting_run_ready.append(module)

    @Slot(str)
    def stopping_run_wait(self, module):
        vars = self.ui.__dict__
        if "disabled" in module:
            name = re.sub(r'^.*?-', "", module)
            self.logger.info(f"Stopping Run: {name} is disabled")
            vars[f"gen_status_{name}"].idle()
            self.stopping_run_ready.append(module)
            return

        self.logger.info(f"Stopping Run: {module} is complete")
        # change status lights
        vars[f"gen_status_{module}"].idle()
        self.stopping_run_ready.append(module)

    @Slot(str)
    def starting_event_wait(self, module):
        vars = self.ui.__dict__
        if "disabled" in module:
            name = re.sub(r'^.*?-', "", module)
            self.logger.info(f"Starting Event: {name} is disabled")
            vars[f"gen_status_{name}"].idle()
            self.starting_event_ready.append(module)
            return

        self.logger.info(f"Starting Event: {module} is complete")

        # change status lights
        vars[f"gen_status_{module}"].active()
        self.starting_event_ready.append(module)

    @Slot(str)
    def stopping_event_wait(self, module):
        vars = self.ui.__dict__
        if "disabled" in module:
            name = re.sub(r'^.*?-', "", module)
            self.logger.info(f"Stopping Event: {name} is disabled")
            vars[f"gen_status_{name}"].idle()
            self.stopping_event_ready.append(module)
            return

        self.logger.info(f"Stopping Event: {module} is complete")

        # change status lights
        vars[f"gen_status_{module}"].idle()
        self.stopping_event_ready.append(module)

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
        # self.run_id = f"{today}_{num:02d}" # minimum two digits
        self.run_id = f"{today}_{num}"

        self.run_dir = os.path.join(data_dir, self.run_id)
        if not os.path.exists(self.run_dir):
            os.mkdir(self.run_dir)
        self.ui.run_id_edit.setText(self.run_id)

    def start_program(self):
        self.signals.program_starting.emit()
        self.update_state("idle")

    def start_run(self):
        """
        Start a new run. Copies configuration into run-specific config. Creates run directory. Initializes data submodules.
        """
        self.create_run_directory()
        self.run_start_time = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
        self.starting_run_ready = []
        vars = self.ui.__dict__
        for v in vars.keys():
            if v.startswith("gen_status"):
                vars[v].idle()

        # reset event number and livetimes
        self.event_id = -1
        self.ev_livetime = 0
        self.run_livetime = 0
        self.ui.event_id_edit.setText(f"{self.event_id:2d}")
        self.ui.event_time_edit.setText(self.format_time(self.ev_livetime))
        self.ui.run_live_time_edit.setText(self.format_time(self.run_livetime))
        self.ui.trigger_edit.setText("")

        self.run_log_path = os.path.join(self.run_dir, f"{self.run_id}.log")
        self.config_class.start_run()

        file_handler = logging.FileHandler(self.run_log_path, mode="a")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(file_handler)
        self.update_state("starting_run")

        self.signals.run_starting.emit()

    def stop_run(self):
        # set up multithreading thread and workers
        self.run_end_time = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
        self.stopping_run_ready = []
        self.stopping_run = False

        self.signals.run_stopping.emit()
        self.update_state("stopping_run")

    def start_event(self):
        # check if stopping run now or start new event
        self.event_id += 1
        if (
                self.event_id
                >= self.config_class.config["general"]["max_num_evs"]
        ):
            self.stopping_run = True
        if self.stopping_run:
            self.stop_run()
            return

        self.event_timer.start()
        self.event_start_time = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
        self.starting_event_ready = []
        self.update_state("starting_event")
        self.ev_livetime = 0
        self.ui.event_id_edit.setText(f"{self.event_id:2d}")
        self.ui.event_time_edit.setText(self.format_time(0))
        self.event_dir = os.path.join(self.run_dir, str(self.event_id))
        self.config_class.start_event()
        if not os.path.exists(self.event_dir):
            os.mkdir(self.event_dir)

        current_path = os.path.join(self.config_class.config["general"]["data_dir"], "current_event")
        if os.path.islink(current_path):
            os.unlink(current_path)
        os.symlink(self.event_dir, current_path)
        self.signals.event_starting.emit()

    def stop_event(self):
        """
        Stop the event. Enter into compressing state. If the "Stop Run" button is pressed or the max number of events
        are reached, then it will enter into "stopping" state. Otherwise, it will start another event.
        """
        self.event_end_time = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
        self.stopping_event_ready = []
        self.event_livetime = self.event_timer.elapsed()
        self.run_livetime += self.event_livetime
        self.signals.event_stopping.emit()
        self.update_state("stopping_event")

    def stop_run_but_pressed(self):
        self.stopping_run = True
        self.ui.stop_run_but.setEnabled(False)

    def sw_trigger(self):
        self.signals.send_trigger.emit("Software")

    def open_data_folder(self):
        path = self.run_dir if "run_dir" in self.__dict__ \
            else self.config_class.config["general"]["data_dir"]
        subprocess.Popen(["nemo", path])
        self.logger.info(f"Opened data folder: {path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
