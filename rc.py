# # recompile UI files before starting
# import os
# os.system('for ui in ui/*.ui; do name="${ui%%.*}"; pyside6-uic $ui -o "$name.py"; done')

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QObject, QThread, Signal, Slot, QElapsedTimer, QTimer, Qt, QMutex, QWaitCondition
from PySide6.QtGui import QPixmap
import pyqtgraph as pg
from ui.mainwindow import Ui_MainWindow
from src.config import Config
from src.ui_loader import SettingsWindow, LogWindow
from src.arduinos import Arduino
from src.caen import Caen
from src.acoustics import Acoustics
from src.modbus import Modbus
from src.cameras import Camera
from src.sipm_amp import SiPMAmp
from src.sql import SQL
from src.niusb import NIUSB
from src.writer import Writer
import logging
from logging.handlers import TimedRotatingFileHandler
from enum import Enum
import subprocess
import datetime
import time
import re
import sys
import os
import fcntl
from sbcbinaryformat import Streamer


# Loads Main window
class MainWindow(QMainWindow):
    # Declare all relevant signals
    program_starting = Signal()
    run_starting = Signal()
    run_stopping = Signal()
    event_starting = Signal()
    event_stopping = Signal()
    send_trigger = Signal(str)
    program_stopping = Signal()

    def __init__(self):
        super(MainWindow, self).__init__()

        # Acquire a lock to prevent multiple instances of the program
        os.umask(0o000) # allow r/w for all users
        self.lock_file = "/tmp/runcontrol.lock"
        self.lock_fd = open(self.lock_file, 'w+')
        try:
            fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            self.logger.error("Run Control is already running. Exiting.")
            sys.exit(1)

        self.run_id = ""
        self.event_id = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widgets = self.ui.__dict__

        # initialize config class
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        self.config_class = Config(self, path)
        self.config_class.load_config()
        self.config_class.load_config_to_mainwindow()
        self.stopping_run = False

        # logger initialization
        self.logger = logging.getLogger("rc")
        self.logger.setLevel(logging.DEBUG)
        # console handler
        self.console_format = "%(asctime)s > %(message)s"
        self.console_formatter = logging.Formatter(self.console_format, datefmt="%H:%M:%S")
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.console_formatter)
        self.logger.addHandler(self.console_handler)
        # file handler
        self.log_dir = self.config_class.config["general"]["log_dir"]
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
        self.log_filename = os.path.join(self.log_dir, "rc.log")
        self.log_format = "%(asctime)s %(levelname)s > %(message)s"
        self.log_formatter = logging.Formatter(self.log_format)
        self.file_handler = TimedRotatingFileHandler(
            filename=self.log_filename,
            when='midnight',        # Rotate at midnight
            interval=1,             # Daily rotation
            encoding='utf-8',
            delay=False
        )
        self.file_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(self.file_handler)

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

        # List populated by ready modules at each state. After all modules are ready, it will proceed to the next state
        self.all_modules = ["config", "niusb", "modbus", "sql", "writer", 
                            "cam1", "cam2", "cam3", "clock", "trigger", "position",
                            "amp1", "amp2", "amp3", "caen", "gage"]
        self.starting_program_modules = []
        self.starting_run_modules = ["amp1", "amp2", "amp3", "cam1", "cam2", "cam3",
                                     "clock", "position", "trigger", "niusb", "caen", "modbus", "sql"]
        self.stopping_run_modules = ["amp1", "amp2", "amp3", "cam1", "cam2", "cam3",
                                     "sql", "niusb", "caen", "modbus", "writer"]
        self.starting_event_modules = ["cam1", "cam2", "cam3", "niusb", "caen", "gage", "modbus", "sql"]
        self.stopping_event_modules = ["cam1", "cam2", "cam3", "niusb", "caen", "gage", "modbus", "sql", "writer"]
        
        self.update_state("preparing")

        self.starting_program_ready = []
        self.starting_run_ready = []
        self.stopping_run_ready = []
        self.starting_event_ready = []
        self.stopping_event_ready = []
        self.set_up_workers()

        self.setup_caen_plot()
        self.setup_acous_plot()

        # timer for event loop
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update)
        self.timer.start()

        # event timer
        self.event_timer = QElapsedTimer()
        self.run_livetime = 0
        self.event_livetime = 0
        self.start_program()

    def set_up_workers(self):
        # set up run handling thread and the worker
        d = self.__dict__
        for cam in ["cam1", "cam2", "cam3"]:
            d[f"{cam}_worker"] = Camera(self, cam)
            d[f"{cam}_worker"].camera_started.connect(self.starting_run_wait)
            d[f"{cam}_worker"].camera_closed.connect(self.stopping_run_wait)
            d[f"{cam}_thread"] = QThread()
            d[f"{cam}_thread"].setObjectName(f"{cam}_thread")
            d[f"{cam}_worker"].moveToThread(d[f"{cam}_thread"])
            d[f"{cam}_thread"].started.connect(d[f"{cam}_worker"].run)
            self.run_starting.connect(d[f"{cam}_worker"].start_camera)
            self.run_stopping.connect(d[f"{cam}_worker"].stop_camera)
            d[f"{cam}_thread"].start()
            time.sleep(0.001)

        for amp in ["amp1", "amp2", "amp3"]:
            d[f"{amp}_worker"] = SiPMAmp(self, amp)
            d[f"{amp}_worker"].sipm_biased.connect(self.starting_run_wait)
            d[f"{amp}_worker"].sipm_unbiased.connect(self.stopping_run_wait)
            d[f"{amp}_thread"] = QThread()
            d[f"{amp}_thread"].setObjectName(f"{amp}_thread")
            d[f"{amp}_worker"].moveToThread(d[f"{amp}_thread"])
            d[f"{amp}_thread"].started.connect(d[f"{amp}_worker"].run)
            self.run_starting.connect(d[f"{amp}_worker"].bias_sipm)
            self.run_stopping.connect(d[f"{amp}_worker"].unbias_sipm)
            d[f"{amp}_thread"].start()
            time.sleep(0.001)

        for ino in ["trigger", "clock", "position"]:
            d[f"arduino_{ino}_worker"] = Arduino(self, ino)
            d[f"arduino_{ino}_worker"].sketch_uploaded.connect(self.starting_run_wait)
            d[f"arduino_{ino}_thread"] = QThread()
            d[f"arduino_{ino}_thread"].setObjectName(f"arduino_{ino}_thread")
            d[f"arduino_{ino}_worker"].moveToThread(d[f"arduino_{ino}_thread"])
            d[f"arduino_{ino}_thread"].started.connect(d[f"arduino_{ino}_worker"].run)
            self.run_starting.connect(d[f"arduino_{ino}_worker"].upload_sketch)
            d[f"arduino_{ino}_thread"].start()
            time.sleep(0.001)

        self.caen_worker = Caen(self)
        self.caen_worker.run_started.connect(self.starting_run_wait)
        self.caen_worker.run_stopped.connect(self.stopping_run_wait)
        self.caen_worker.event_started.connect(self.starting_event_wait)
        self.caen_worker.event_stopped.connect(self.stopping_event_wait)
        self.caen_worker.data_retrieved.connect(self.update_caen_plot)
        self.caen_thread = QThread()
        self.caen_thread.setObjectName("caen_thread")
        self.caen_worker.moveToThread(self.caen_thread)
        self.caen_thread.started.connect(self.caen_worker.run)
        self.run_starting.connect(self.caen_worker.start_run)
        self.event_starting.connect(self.caen_worker.start_event)
        self.event_stopping.connect(self.caen_worker.stop_event)
        self.run_stopping.connect(self.caen_worker.stop_run)
        self.caen_thread.start()
        time.sleep(0.001)

        self.acous_worker = Acoustics(self)
        self.acous_worker.event_started.connect(self.starting_event_wait)
        self.acous_worker.event_stopped.connect(self.stopping_event_wait)
        self.acous_worker.event_stopped.connect(self.update_acous_plot)
        self.acous_thread = QThread()
        self.acous_thread.setObjectName("acous_thread")
        self.acous_worker.moveToThread(self.acous_thread)
        self.acous_thread.started.connect(self.acous_worker.run)
        self.event_starting.connect(self.acous_worker.start_event)
        self.event_stopping.connect(self.acous_worker.stop_event)
        self.acous_thread.start()
        time.sleep(0.001)

        self.modbus_worker = Modbus(self)
        self.modbus_worker.run_started.connect(self.starting_run_wait)
        self.modbus_worker.run_stopped.connect(self.stopping_run_wait)
        self.modbus_worker.event_started.connect(self.starting_event_wait)
        self.modbus_worker.event_stopped.connect(self.stopping_event_wait)
        self.modbus_thread = QThread()
        self.modbus_thread.setObjectName("modbus_thread")
        self.modbus_worker.moveToThread(self.modbus_thread)
        self.modbus_thread.started.connect(self.modbus_worker.run)
        self.run_starting.connect(self.modbus_worker.start_run)
        self.event_starting.connect(self.modbus_worker.start_event)
        self.event_stopping.connect(self.modbus_worker.stop_event)
        self.run_stopping.connect(self.modbus_worker.stop_run)
        self.modbus_thread.start()
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
        self.run_starting.connect(self.niusb_worker.start_run)
        self.event_starting.connect(self.niusb_worker.start_event)
        self.event_stopping.connect(self.niusb_worker.stop_event)
        self.run_stopping.connect(self.niusb_worker.stop_run)
        self.send_trigger.connect(self.niusb_worker.send_trigger)
        self.niusb_thread.start()
        time.sleep(0.001)

        self.writer_worker = Writer(self)
        self.writer_worker.event_stopped.connect(self.stopping_event_wait)
        self.writer_worker.run_stopped.connect(self.stopping_run_wait)
        self.writer_thread = QThread()
        self.writer_thread.setObjectName("writer_thread")
        self.writer_worker.moveToThread(self.writer_thread)
        self.writer_thread.started.connect(self.writer_worker.run)
        self.event_stopping.connect(self.writer_worker.write_event_data)
        self.run_stopping.connect(self.writer_worker.write_run_data)
        self.writer_thread.start()
        time.sleep(0.001)

        self.sql_worker = SQL(self)
        self.sql_worker.run_started.connect(self.starting_run_wait)
        self.sql_worker.run_stopped.connect(self.stopping_run_wait)
        self.sql_worker.event_started.connect(self.starting_event_wait)
        self.sql_worker.event_stopped.connect(self.stopping_event_wait)
        self.sql_thread = QThread()
        self.sql_thread.setObjectName("sql_thread")
        self.sql_worker.moveToThread(self.sql_thread)
        self.sql_thread.started.connect(self.sql_worker.run)
        self.run_starting.connect(self.sql_worker.start_run)
        self.event_starting.connect(self.sql_worker.start_event)
        self.event_stopping.connect(self.sql_worker.stop_event)
        self.run_stopping.connect(self.sql_worker.stop_run)
        self.sql_thread.start()

        # establish mutex and wait conditions for syncing
        self.trigff_mutex = QMutex()
        self.trigff_wait = QWaitCondition()
        self.trigff_ready = False

    # TODO: handle closing during run
    def closeEvent(self, event):
        """
        Custom function overriding the close event behavior. It will close both log and settings window, and also leave message in the logger.
        """
        self.logger.info("Quitting run control.")

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
        modules = ["cam1", "cam2", "cam3", "amp1", "amp2", "amp3",
                   "arduino_trigger", "arduino_clock", "arduino_position", 
                   "caen", "acous", "modbus", "niusb", "writer", "sql"]
        for m in modules:
            worker = getattr(self, f"{m}_worker", None)
            thread = getattr(self, f"{m}_thread", None)
            self.logger.debug(f"Stopping {worker}.")
            thread.quit()
            if not thread.wait(1000):  # 1 sec timeout
                self.logger.error(f"Thread {m} failed to stop")
            
            worker.deleteLater()
            thread.deleteLater()
        
        self.logger.info("All threads stopped.")

        # Cleanup resources
        QApplication.processEvents()
        event.accept()
        QApplication.quit()

        # Optional, release the lock file
        try:
            fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
            self.lock_fd.close()
            os.remove(self.lock_file)
        except BlockingIOError:
            self.logger.error("Failed to release the lock file.")

        self.logger.info("Run control successfully stopped.\n")
        

    def open_settings_window(self):
        """Create and show the settings window.
        """
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()

    def open_log_window(self):
        """Create and show the logs window.
        """
        self.log_window = LogWindow(self)
        self.log_window.show()

    def select_file(self):
        """Open a file dialog to select a file. The selected file path will be set in the file_path line edit.
        """
        filename, _ = QFileDialog.getOpenFileName(self)
        self.ui.file_path.setText(filename)

    def format_time(self, t):
        """
        Time formatting helper function for event time display. t is in milliseconds
        If time is under a minute, it will return "12s 345"
        If time ie between a minute and an hour, it will return "12m 34s 567"
        If time is more than an hour, it will return "12h 34m 56s 789"

        :param t: Time in milliseconds
        :type t: int
        :return: formatted time string
        :rtype: str
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
        Event loop function. This function will run every 100ms.
        In the active state, it will update event and run timer, and check if max event time is reached. If so, it will end the event.
        In the starting_run, stopping_run, starting_event, and stopping_event states, it will check if all modules are ready to proceed to the next state.
        """
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
                self.send_trigger.emit("Timeout")
        elif self.run_state == self.run_states["starting_run"]:
            # SiPM amp 1/2/3, Cam 1/2/3, clock/position/trigger arduino, NI USB, CAEN, MODBUS #change for RC-PLC comm.
            if len(self.starting_run_ready) >= len(self.starting_run_modules):
                self.logger.info(f"Run {self.run_id} started.")
                self.logger.debug(f"Modules started for run: {self.starting_run_ready}\n")
                self.start_event()
        elif self.run_state == self.run_states["starting_event"]:
            # cam 1/2/3, *PLC, NIUSB, CAEN, GaGe, MODBUS
            self.event_timer.start()
            if len(self.starting_event_ready) >= len(self.starting_event_modules):
                self.logger.info(f"Event {self.event_id} started.")
                self.logger.debug(f"Modules started for event: {self.starting_event_ready}\n")
                self.update_state("active")
        elif self.run_state == self.run_states["stopping_event"]:
            # SQL, cam 1/2/3, NIUSB, CAEN, GaGe, MODBUS
            if len(self.stopping_event_ready) >= len(self.stopping_event_modules):
                self.logger.info(f"Event {self.event_id} stopped.")
                self.logger.debug(f"Modules stopped for event: {self.stopping_event_ready}\n")
                self.start_event()
        elif self.run_state == self.run_states["stopping_run"]:
            # SQL, cam 1/2/3, sipm amp 1/2/3, NIUSB, CAEN, MODBUS
            if len(self.stopping_run_ready) >= len(self.stopping_run_modules):
                self.logger.info(f"Run {self.run_id} stopped.")
                self.logger.debug(f"Modules stopped for run: {self.stopping_run_ready}\n")

                # check for autorun condition
                autorun = self.ui.autorun_box.isChecked() and not self.manual_stop_run
                if autorun:
                    self.start_run()
                else:
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
        if module not in self.starting_program_ready:
            self.starting_program_ready.append(module)
            self.starting_program_ready.sort()

    @Slot(str)
    def starting_run_wait(self, module):
        """
        A slot method to append ready module names to the list. It will add the module to a list and change the status light.
        The update function will check the length of the list. When all modules are ready, it will proceed to the start_event state.
        """
        if "disabled" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.debug(f"Starting Run: {name} is disabled")
            self.widgets[f"status_{name}"].disabled()
        elif "error" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.error(f"Starting Run: {name} has an error")
            self.widgets[f"status_{name}"].error()
        else:
            self.logger.debug(f"Starting Run: {module} is complete")
            # change status lights
            self.widgets[f"status_{module}"].active()

        if module not in self.starting_run_ready:
            self.starting_run_ready.append(module)
            self.starting_run_ready.sort()

    @Slot(str)
    def stopping_run_wait(self, module):
        """
        A slot method to append ready module names to the list. It will add the module to a list and change the status light.
        The update function will check the length of the list. When all modules are ready, it will proceed to the idle state.
        """
        if "disabled" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.debug(f"Stopping Run: {name} is disabled")
            self.widgets[f"status_{name}"].idle()
        elif "error" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.error(f"Stopping Run: {name} has an error")
            self.widgets[f"status_{name}"].error()
        else:
            self.logger.debug(f"Stopping Run: {module} is complete")
            # change status lights
            self.widgets[f"status_{module}"].idle()

        if module not in self.stopping_run_ready:
            self.stopping_run_ready.append(module)
            self.stopping_run_ready.sort()

    @Slot(str)
    def starting_event_wait(self, module):
        """
        A slot method to append ready module names to the list. It will add the module to a list and change the status light.
        The update function will check the length of the list. When all modules are ready, it will proceed to the active state.
        """
        if "disabled" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.debug(f"Starting Event: {name} is disabled")
            self.widgets[f"status_{name}"].disabled()
        elif "error" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.error(f"Starting Event: {name} has an error")
            self.widgets[f"status_{name}"].error()
        else:
            self.logger.debug(f"Starting Event: {module} is complete")
            # change status lights
            self.widgets[f"status_{module}"].active()

        if module not in self.starting_event_ready:
            self.starting_event_ready.append(module)
            self.starting_event_ready.sort()

    @Slot(str)
    def stopping_event_wait(self, module):
        """
        A slot method to append ready module names to the list. It will add the module to a list and change the status light.
        The update function will check the length of the list. When all modules are ready, it will proceed to next event or stopping run.
        """
        if "disabled" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.debug(f"Stopping Event: {name} is disabled")
            self.widgets[f"status_{name}"].disabled()
        elif "error" in module:
            name = re.search(r'^(.*?)-', module).group(1)
            self.logger.error(f"Stopping Event: {name} has an error")
            self.widgets[f"status_{name}"].error()
        else:
            self.logger.debug(f"Stopping Event: {module} is complete")
            # change status lights
            self.widgets[f"status_{module}"].active()

        if module not in self.stopping_event_ready:
            self.stopping_event_ready.append(module)
            self.stopping_event_ready.sort()

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

        current_run_path = os.path.join(self.config_class.config["general"]["data_dir"], "current_run")
        if os.path.islink(current_run_path):
            os.unlink(current_run_path)
        os.symlink(self.run_dir, current_run_path, target_is_directory=True)

    def start_program(self):
        self.program_starting.emit()
        self.update_state("idle")

    def start_run(self):
        """
        Start a new run. Copies configuration into run-specific config. Creates run directory. Initializes data submodules.
        """
        self.create_run_directory()
        self.run_start_time = datetime.datetime.now()
        self.starting_run_ready = []

        # reset event number and livetimes
        self.run_exit_code = 255
        self.event_id = -1
        self.event_livetime = 0
        self.run_livetime = 0
        self.manual_stop_run = False
        self.ui.event_id_edit.setText(f"{self.event_id:2d}")
        self.ui.event_time_edit.setText(self.format_time(self.event_livetime))
        self.ui.run_live_time_edit.setText(self.format_time(self.run_livetime))
        self.ui.trigger_edit.setText("")

        self.run_log_dir = os.path.join(self.run_dir, f"rc.log")
        self.widgets["status_config"].working()
        self.config_class.start_run()
        self.widgets["status_config"].active()

        file_handler = logging.FileHandler(self.run_log_dir, mode="a")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(file_handler)
        for m in self.all_modules:
            if m in self.starting_run_modules:
                self.widgets[f"status_{m}"].working()
            else:
                self.widgets[f"status_{m}"].idle()

        self.update_state("starting_run")
        self.run_starting.emit()

    def stop_run(self):
        # set up multithreading thread and workers
        self.run_end_time = datetime.datetime.now()
        self.stopping_run_ready = []
        self.stopping_run = False
        self.run_exit_code = 0

        for m in self.all_modules:
            if m in self.stopping_run_modules:
                self.widgets[f"status_{m}"].working()
            else:
                self.widgets[f"status_{m}"].idle()

        self.run_stopping.emit()
        self.update_state("stopping_run")

    def start_event(self):
        """
        Main RC function to start an event. First it checks if the max number of events has been reached. If so, it will stop the run.
        Then, it will start the event timer, set the numbers on main window, and create the event directory.
        Finally, it will send out the event_starting signal to all modules.
        """
        # if the max number of events is reached, stop the run
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
        self.event_start_time = datetime.datetime.now()
        self.event_exit_code = 255
        self.starting_event_ready = []
        self.update_state("starting_event")
        self.event_livetime = 0
        self.ui.event_id_edit.setText(f"{self.event_id:2d}")
        self.ui.event_time_edit.setText(self.format_time(0))
        self.event_dir = os.path.join(self.run_dir, str(self.event_id))

        self.widgets["status_config"].working()
        self.config_class.start_event()
        if not os.path.exists(self.event_dir):
            os.mkdir(self.event_dir)

        status = bool(self.config_class.run_pressure_profiles)
        ev_pressure = self.config_class.event_pressure
        self.ui.ev_pset_box.setValue(ev_pressure["setpoint"] or 0)
        self.ui.ev_pset_hi_box.setValue(ev_pressure["setpoint_high"] or 0)
        self.ui.ev_pset_slope_box.setValue(ev_pressure["slope"] or 0)
        self.ui.ev_pset_period_box.setValue(ev_pressure["period"] or 0)
        self.ui.ev_pset_box.setEnabled(status)
        self.ui.ev_pset_hi_box.setEnabled(status)
        self.ui.ev_pset_slope_box.setEnabled(status)
        self.ui.ev_pset_period_box.setEnabled(status)
        for m in self.all_modules:
            if m in self.starting_event_modules:
                self.widgets[f"status_{m}"].working()
            else:
                self.widgets[f"status_{m}"].idle()

        self.current_path = os.path.join(self.config_class.config["general"]["data_dir"], "current_event")
        if os.path.islink(self.current_path):
            os.unlink(self.current_path)
        os.symlink(self.event_dir, self.current_path,target_is_directory=True)
        self.widgets["status_config"].active()
        self.event_starting.emit()

    def stop_event(self):
        """
        Stop the event. Enter into compressing state. If the "Stop Run" button is pressed or the max number of events
        are reached, then it will enter into "stopping" state. Otherwise, it will start another event.
        """
        self.event_end_time = datetime.datetime.now()
        self.stopping_event_ready = []
        self.event_livetime = self.event_timer.elapsed()
        self.run_livetime += self.event_livetime
        self.event_exit_code = 0
        for m in self.all_modules:
            if m in self.stopping_event_modules:
                self.widgets[f"status_{m}"].working()
            else:
                self.widgets[f"status_{m}"].idle()

        self.event_stopping.emit()
        self.update_state("stopping_event")

    def stop_run_but_pressed(self):
        self.stopping_run = True
        self.manual_stop_run = True
        self.ui.stop_run_but.setEnabled(False)

    def sw_trigger(self):
        self.send_trigger.emit("Software")

    def open_data_folder(self):
        path = self.run_dir if "run_dir" in self.__dict__ \
            else self.config_class.config["general"]["data_dir"]
        subprocess.Popen(["nemo", path])
        self.logger.debug(f"Opened data folder: {path}")

    def setup_caen_plot(self):
        """
        Set up the CAEN plot widgets. It will create the plot and text items for each plot, and set up basic properties.
        """
        # plot and text items for each plot
        self.caen_plots = [self.ui.caen_plot_0, self.ui.caen_plot_1, self.ui.caen_plot_2, self.ui.caen_plot_3]
        self.caen_texts = [pg.TextItem(text="Event: 0", color='k', anchor=(0,0)) for _ in self.caen_plots]
        self.caen_curves = []
        # one pen for each channel in a group
        self.caen_pens = [pg.mkPen(color=c, width=2) for c in ["green", "red", "blue", "orange","violet","brown","pink","gray"]] 

        for i in range(len(self.caen_plots)):
            p = self.caen_plots[i]
            t = self.caen_texts[i]

            # setup some basic plot properties
            p.setBackground("w")
            p.showGrid(x=True, y=True)
            p.setTitle(f"CAEN Waveforms G{i}", color='k')
            p.setLabel('left', "Amplitude (ADC)", color='k')
            p.setLabel('bottom', "Time (ns)", color='k')
            p.addLegend()

            # setup text counter
            t.setParentItem(p.getViewBox())
            t.setPos(0, 1)

            # create curves for each channel
            curves = []
            for j in range(8):
                c = p.plot(x=[], y=[], pen=self.caen_pens[j], name=f"Ch{i*8+j}")
                curves.append(c)
            self.caen_curves.append(curves)

    @Slot(dict)
    def update_caen_plot(self, data):
        """
        Update the CAEN plot widgets every time data is retrieved
        """
        def get_ch_index(mask, ch):
            """
            Get the index of the channel in list using mask
            Count number of 1s in all bits lower than the desired bit
            """
            lower_mask = (1 << ch) - 1
            return bin(mask & lower_mask).count("1")

        caen_configs = self.config_class.config["caen"]
        for i in range(len(self.caen_plots)):
            p = self.caen_plots[i]
            t = self.caen_texts[i]
            curves = self.caen_curves[i]

            # update text and curves
            t.setText(f"Event: {data['EventCounter'][-1]}")
            # frequency is 62.5MHz
            time_axis = [i*16 for i in range(data["Waveforms"].shape[2])]
            for j in range(8):
                if not caen_configs[f"group{i}"]["enabled"] or \
                  not caen_configs[f"group{i}"]["acq_mask"][j] or \
                  not caen_configs[f"group{i}"]["plot_mask"][j]:
                    curves[j].setData(x=[], y=[])
                else:
                    ind = get_ch_index(data["AcquisitionMask"], 8*i+j)
                    curves[j].setData(x=time_axis, y=data['Waveforms'][-1][ind])

    def setup_acous_plot(self):
        """
        Set up the Acous plot widgets. It will create the plot and text items for each plot, and set up basic properties.
        """
        # plot and text items for each plot
        self.acous_plot = self.ui.acous_plot
        self.acous_curves = []
        self.acous_text = pg.TextItem(text="Event: 0", color='k', anchor=(0,0))

        # one pen for each channel in a group
        self.acous_pens = [pg.mkPen(color=c, width=2) for c in ["green", "red", "blue", "orange","violet","brown","pink","gray"]] 

        # setup some basic plot properties
        self.acous_plot.setBackground("w")
        self.acous_plot.showGrid(x=True, y=True)
        self.acous_plot.setTitle(f"Acous Waveforms", color='k')
        self.acous_plot.setLabel('left', "Amplitude (ADC)", color='k')
        self.acous_plot.setLabel('bottom', "Time (us)", color='k')
        self.acous_plot.addLegend()

        # setup text counter
        self.acous_text.setParentItem(self.acous_plot.getViewBox())
        self.acous_text.setPos(0, 1)

        # create curves for each channel
        for i in range(8):
            c = self.acous_plot.plot(x=[], y=[], pen=self.acous_pens[i], name=f"Ch{i+1}")
            self.acous_curves.append(c)

    @Slot(dict)
    def update_acous_plot(self):
        """
        Update the acous plot widgets every time data is retrieved
        """
        acous_configs = self.config_class.config["acous"]
        if not acous_configs["enabled"]:
            return
        
        try:
            data = Streamer(os.path.join(self.current_path, "acoustics.sbc")).to_dict()
        except FileNotFoundError:
            self.logger.warning("Acoustics data file not found.")
            return
        sample_rate = self.acous_worker.sample_rate_conversion[acous_configs["sample_rate"]]/1e6
        time_axis = [i/sample_rate for i in range(data["Waveforms"].shape[2])]
        for i in range(8):
            if not acous_configs[f"ch{i+1}"]["plot"]:
                self.acous_curves[i].setData(x=[], y=[])
            else:
                self.acous_curves[i].setData(x=time_axis, y=data['Waveforms'][-1][i])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())