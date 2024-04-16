from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QElapsedTimer, QTimer
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from ui.mainwindow import Ui_MainWindow
from src.config import *
from src.workers import *
from src.ui_loader import *
from src.arduinos import *
from src.cameras import *
from src.sipm_amp import *
from src.sql import *
from src.niusb import *
from src.writer import *
import logging
from enum import Enum
import datetime
import time
import re

class MainSignals(QObject):
    # initialize signals
    program_starting = Signal()
    run_starting = Signal()
    run_stopping = Signal()
    event_starting = Signal()
    event_stopping = Signal()
    send_trigger = Signal()
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
        self.timer.setInterval(100)
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
        self.cam1_worker = Camera(self, "cam1")
        self.cam1_worker.camera_connected.connect(self.starting_run_wait)
        self.cam1_worker.camera_started.connect(self.starting_event_wait)
        self.cam1_worker.camera_closed.connect(self.stopping_event_wait)
        self.cam1_thread = QThread()
        self.cam1_thread.setObjectName("cam1_thread")
        self.cam1_worker.moveToThread(self.cam1_thread)
        self.cam1_thread.started.connect(self.cam1_worker.run)
        self.signals.run_starting.connect(self.cam1_worker.test_rpi)
        self.signals.event_starting.connect(self.cam1_worker.start_camera)
        self.cam1_thread.start()
        time.sleep(0.001) # 1ms separation of worker and thread initialization so that the log is easier to read

        self.cam2_worker = Camera(self, "cam2")
        self.cam2_worker.camera_connected.connect(self.starting_run_wait)
        self.cam2_worker.camera_started.connect(self.starting_event_wait)
        self.cam2_worker.camera_closed.connect(self.stopping_event_wait)
        self.cam2_thread = QThread()
        self.cam2_thread.setObjectName("cam2_thread")
        self.cam2_worker.moveToThread(self.cam2_thread)
        self.cam2_thread.started.connect(self.cam2_worker.run)
        self.signals.run_starting.connect(self.cam2_worker.test_rpi)
        self.signals.event_starting.connect(self.cam2_worker.start_camera)
        self.cam2_thread.start()
        time.sleep(0.001)

        self.cam3_worker = Camera(self, "cam3")
        self.cam3_worker.camera_connected.connect(self.starting_run_wait)
        self.cam3_worker.camera_started.connect(self.starting_event_wait)
        self.cam3_worker.camera_closed.connect(self.stopping_event_wait)
        self.cam3_thread = QThread()
        self.cam3_thread.setObjectName("cam3_thread")
        self.cam3_worker.moveToThread(self.cam3_thread)
        self.cam3_thread.started.connect(self.cam3_worker.run)
        self.signals.run_starting.connect(self.cam3_worker.test_rpi)
        self.signals.event_starting.connect(self.cam3_worker.start_camera)
        self.cam3_thread.start()
        time.sleep(0.001)

        self.amp1_worker = SiPMAmp(self, "amp1")
        self.amp1_worker.sipm_biased.connect(self.starting_run_wait)
        self.amp1_worker.sipm_unbiased.connect(self.stopping_run_wait)
        self.amp1_thread = QThread()
        self.amp1_thread.setObjectName('sipm_amp1_thread')
        self.amp1_worker.moveToThread(self.amp1_thread)
        self.amp1_thread.started.connect(self.amp1_worker.run)
        self.signals.run_starting.connect(self.amp1_worker.bias_sipm)
        self.signals.run_stopping.connect(self.amp1_worker.unbias_sipm)
        self.amp1_thread.start()
        time.sleep(0.001)

        self.amp2_worker = SiPMAmp(self, "amp2")
        self.amp2_worker.sipm_biased.connect(self.starting_run_wait)
        self.amp2_worker.sipm_unbiased.connect(self.stopping_run_wait)
        self.amp2_thread = QThread()
        self.amp2_thread.setObjectName('sipm_amp2_thread')
        self.amp2_worker.moveToThread(self.amp2_thread)
        self.amp2_thread.started.connect(self.amp2_worker.run)
        self.signals.run_starting.connect(self.amp2_worker.bias_sipm)
        self.signals.run_stopping.connect(self.amp2_worker.unbias_sipm)
        self.amp2_thread.start()
        time.sleep(0.001)

        self.arduino_trig_worker = Arduino(self, "trigger")
        self.arduino_trig_worker.arduino_sketch_uploaded.connect(self.starting_run_wait)
        self.arduino_trig_thread = QThread()
        self.arduino_trig_thread.setObjectName('arduino_trig_thread')
        self.arduino_trig_worker.moveToThread(self.arduino_trig_thread)
        self.arduino_trig_thread.started.connect(self.arduino_trig_worker.run)
        self.signals.run_starting.connect(self.arduino_trig_worker.upload_sketch)
        self.arduino_trig_thread.start()
        time.sleep(0.001)

        self.arduino_clock_worker = Arduino(self, "clock")
        self.arduino_clock_worker.arduino_sketch_uploaded.connect(self.starting_run_wait)
        self.arduino_clock_thread = QThread()
        self.arduino_clock_thread.setObjectName('arduino_clock_thread')
        self.arduino_clock_worker.moveToThread(self.arduino_clock_thread)
        self.arduino_clock_thread.started.connect(self.arduino_clock_worker.run)
        self.signals.run_starting.connect(self.arduino_clock_worker.upload_sketch)
        self.arduino_clock_thread.start()
        time.sleep(0.001)

        self.arduino_position_worker = Arduino(self, "position")
        self.arduino_position_worker.arduino_sketch_uploaded.connect(self.starting_run_wait)
        self.arduino_position_thread = QThread()
        self.arduino_position_thread.setObjectName('arduino_position_thread')
        self.arduino_position_worker.moveToThread(self.arduino_position_thread)
        self.arduino_position_thread.started.connect(self.arduino_position_worker.run)
        self.signals.run_starting.connect(self.arduino_position_worker.upload_sketch)
        self.arduino_position_thread.start()
        time.sleep(0.001)

        self.niusb_worker = NIUSB(self)
        self.niusb_worker.pins_set.connect(self.starting_event_wait)
        self.niusb_worker.trigger_received.connect(self.stop_event)
        self.niusb_worker.pins_read.connect(self.stopping_event_wait)
        self.niusb_thread = QThread()
        self.niusb_thread.setObjectName("niusb_thread")
        self.niusb_worker.moveToThread(self.niusb_thread)
        self.niusb_thread.started.connect(self.niusb_worker.run)
        self.signals.event_starting.connect(self.niusb_worker.start_event)
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

        # quit all created threads
        self.cam1_thread.quit()
        self.cam2_thread.quit()
        self.cam3_thread.quit()
        self.amp1_thread.quit()
        self.amp2_thread.quit()
        self.arduino_trig_thread.quit()
        self.arduino_clock_thread.quit()
        self.arduino_position_thread.quit()
        self.niusb_thread.quit()
        self.writer_thread.quit()

        self.cam1_thread.wait()
        self.cam2_thread.wait()
        self.cam3_thread.wait()
        self.amp1_thread.wait()
        self.amp2_thread.wait()
        self.arduino_trig_thread.wait()
        self.arduino_clock_thread.wait()
        self.arduino_position_thread.wait()
        self.niusb_thread.wait()
        self.writer_thread.wait()

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

    # event loop
    @Slot()
    def update(self):
        """
        Event loop function. Every 100ms this function will run.
        In the active state, it will update event and run timer, and check if max event time is reached. If so, it will end the event.

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
                > self.config_class.config["general"]["max_ev_time"] * 1000
            ):
                self.stop_event()
        elif self.run_state == self.run_states["starting_run"]:
            if len(self.starting_run_ready) >= 3:
                self.start_event()
        elif self.run_state == self.run_states["starting_event"]:
            if len(self.starting_event_ready) >= 3:
                self.update_state("active")
        elif self.run_state == self.run_states["stopping_event"]:
            if len(self.starting_event_ready) >= 1:
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
        self.starting_run_ready.append(module)

    @Slot(str)
    def stopping_run_wait(self, module):
        self.stopping_run_ready.append(module)

    @Slot(str)
    def starting_event_wait(self, module):
        self.starting_event_ready.append(module)

    @Slot(str)
    def stopping_event_wait(self, module):
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
        self.create_run_directory()
        self.starting_run_ready = []
        self.update_state("starting_run")
        # reset event number and livetimes
        self.event_id = 0
        self.ev_livetime = 0
        self.run_livetime = 0
        self.ui.event_id_edit.setText(f"{self.event_id:2d}")
        self.ui.event_time_edit.setText(self.format_time(self.ev_livetime))
        self.ui.run_live_time_edit.setText(self.format_time(self.run_livetime))
        self.run_json_path = os.path.join(self.run_dir, f"{self.run_id}.json")
        self.run_log_path = os.path.join(self.run_dir, f"{self.run_id}.log")

        self.config = self.config_class.config
        # self.run_dev_counts =
        #     self.config[""]

        file_handler = logging.FileHandler(self.run_log_path, mode="a")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(file_handler)

        self.signals.run_starting.emit()

    def stop_run(self):
        self.update_state("stopping_run")
        # set up multithreading thread and workers
        self.stopping_run = False
        self.update_state("idle")
        self.signals.run_stopping.emit()

    def start_event(self):
        self.starting_event_ready = []
        self.update_state("starting_event")
        self.ev_livetime = 0
        self.ui.event_id_edit.setText(f"{self.event_id:2d}")
        self.ui.event_time_edit.setText(self.format_time(0))
        self.event_dir = os.path.join(self.run_dir, str(self.event_id))
        if not os.path.exists(self.event_dir):
            os.mkdir(self.event_dir)
        self.signals.event_starting.emit()

    def stop_event(self):
        """
        Stop the event. Enter into compressing state. If the "Stop Run" button is pressed or the max number of events
        are reached, then it will enter into "stopping" state. Otherwise, it will start another event.
        """
        self.signals.event_stopping.emit()
        self.stopping_event_ready = []
        self.update_state("stopping_event")

        # check if stopping run now or start new event
        self.event_id += 1
        if (
                self.event_id
                >= self.config_class.config["general"]["max_num_evs"]
        ):
            self.stopping_run = True
        if self.stopping_run:
            self.stop_run()
        else:
            self.start_event()

    def stop_run_but_pressed(self):
        self.stopping_run = True
        self.ui.stop_run_but.setEnabled(False)

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
            self.event_timer.start()
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

    def sw_trigger(self):
        self.signals.send_trigger.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
