from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import logging
from enum import IntEnum
import os
from slack_sdk import WebClient

# Error code list: https://docs.google.com/spreadsheets/d/1l-7dthFAcyHkQRA3YD875fsAcTKyn0Vgf3X5fvdhq5I/edit?gid=0#gid=0

class ErrorCodes(IntEnum):
    RC_SUCCESS = 1000
    LOCKFILE_LOCKED = 1001
    LOCKFILE_FAILED_TO_RELEASE = 1002
    CONFIG_SAVE_FAILED = 1101
    CONFIG_INVALID_PRESSURE = 1102
    PLC_DISABLED = 1300
    PLC_CONNECTION_FAILED = 1301
    PLC_SMB_PERMISSION_FILE_MISSING = 1302
    PLC_PRESSURE_CYCLE_START_FAILED = 1303
    PLC_PRESSURE_CYCLE_STOP_FAILED = 1304
    PLC_LED_ON_FAILED = 1305
    PLC_LED_OFF_FAILED = 1306
    PLC_SLOWDAQ_START_FAILED = 1307
    PLC_SLOWDAQ_STOP_FAILED = 1308
    PLC_PSET_FAILED = 1309
    NIUSB_DISABLED = 1400
    NIUSB_NOT_CONNECTED = 1401
    NIUSB_CANNOT_RETRIEVE_HANDLE = 1402
    NIUSB_NO_FIRST_FAULT = 1403
    NIUSB_MULTIPLE_FIRST_FAULT = 1404
    NIUSB_INVALID_PIN = 1405
    ARDUINO_DISABLED = 1500
    ARDUINO_NOT_CONNECTED = 1501
    ARDUINO_SKETCH_ARCHIVAL_FAILED = 1502
    ARDUINO_SKETCH_COMPILE_UPLOAD_FAILED = 1503
    WRITER_DISABLED = 1600
    WRITER_NOT_MOUNTED = 1601
    SQL_DISABLED = 1700
    SQL_NOT_CONNECTED = 1701
    CAMERA_DISABLED = 2000
    CAMERA_NOT_CONNECTED = 2001
    ACOUSTIC_DISABLED = 2100
    ACOUSTIC_NOT_CONNECTED = 2101
    ACOUSTIC_FAILED_TO_START = 2102
    ACOUSTIC_FAILED_TO_END = 2103
    CAEN_DISABLED = 2200
    CAEN_NOT_CONNECTED = 2201
    SIPM_AMP_DISABLED = 2300
    SIPM_AMP_NOT_CONNECTED = 2301
    SIPM_AMP_COMMAND_FAILED = 2310
    SIPM_AMP_BIASING_FAILED = 2311
    DIGISCOPE_DISABLED = 2400
    DIGISCOPE_NOT_CONNECTED = 2401
    UNKNOWN_ERROR = 9999

class Guardian(QObject):
    error_messages = {
        ErrorCodes.RC_SUCCESS: "Success - Run control exited successfully.",
        ErrorCodes.LOCKFILE_LOCKED: "Run Control - Failed to acquire lock file.",
        ErrorCodes.LOCKFILE_FAILED_TO_RELEASE: "Run Control - Failed to release lock file.",
        ErrorCodes.CONFIG_SAVE_FAILED: "Config - Failed to save config file to disk",
        ErrorCodes.CONFIG_INVALID_PRESSURE: "Config - Invalid pressure setting.",
        ErrorCodes.PLC_DISABLED: "PLC - Disabled.",
        ErrorCodes.PLC_CONNECTION_FAILED: "PLC - Connection failed.",
        ErrorCodes.PLC_SMB_PERMISSION_FILE_MISSING: "PLC - SMB permission file missing.",
        ErrorCodes.PLC_PRESSURE_CYCLE_START_FAILED: "PLC - Pressure cycle start failed.",
        ErrorCodes.PLC_PRESSURE_CYCLE_STOP_FAILED: "PLC - Pressure cycle stop failed.",
        ErrorCodes.PLC_LED_ON_FAILED: "PLC - LED on failed.",
        ErrorCodes.PLC_LED_OFF_FAILED: "PLC - LED off failed.",
        ErrorCodes.PLC_SLOWDAQ_START_FAILED: "PLC - SLOWDAQ start failed.",
        ErrorCodes.PLC_SLOWDAQ_STOP_FAILED: "PLC - SLOWDAQ stop failed.",
        ErrorCodes.PLC_PSET_FAILED: "PLC - PSET write failed.",
        ErrorCodes.NIUSB_DISABLED: "NIUSB - Disabled.",
        ErrorCodes.NIUSB_NOT_CONNECTED: "NIUSB - Not connected.",
        ErrorCodes.NIUSB_CANNOT_RETRIEVE_HANDLE: "NIUSB - Cannot retrieve handle.",
        ErrorCodes.NIUSB_NO_FIRST_FAULT: "NIUSB - No first fault detected.",
        ErrorCodes.NIUSB_MULTIPLE_FIRST_FAULT: "NIUSB - Multiple first faults detected.",
        ErrorCodes.NIUSB_INVALID_PIN: "NIUSB - Invalid pin setting.",
        ErrorCodes.ARDUINO_DISABLED: "Arduino - Disabled.",
        ErrorCodes.ARDUINO_NOT_CONNECTED: "Arduino - Not connected.",
        ErrorCodes.ARDUINO_SKETCH_ARCHIVAL_FAILED: "Arduino - Sketch archival failed.",
        ErrorCodes.ARDUINO_SKETCH_COMPILE_UPLOAD_FAILED: "Arduino - Sketch compilation or upload failed.",
        ErrorCodes.WRITER_DISABLED: "Writer - Disabled.",
        ErrorCodes.WRITER_NOT_MOUNTED: "Writer - Data folder not mounted.",
        ErrorCodes.SQL_DISABLED: "SQL - Disabled.",
        ErrorCodes.SQL_NOT_CONNECTED: "SQL - Not connected.",
        ErrorCodes.CAMERA_DISABLED: "Camera - Disabled.",
        ErrorCodes.CAMERA_NOT_CONNECTED: "Camera - Not connected.",
        ErrorCodes.ACOUSTIC_DISABLED: "Acoustic - Disabled.",
        ErrorCodes.ACOUSTIC_NOT_CONNECTED: "Acoustic - Not connected.",
        ErrorCodes.ACOUSTIC_FAILED_TO_START: "Acoustic - GaGe driver failed to start.",
        ErrorCodes.ACOUSTIC_FAILED_TO_END: "Acoustic - GaGe driver failed to stop.",
        ErrorCodes.CAEN_DISABLED: "CAEN - Disabled.",
        ErrorCodes.CAEN_NOT_CONNECTED: "CAEN - Not connected.",
        ErrorCodes.SIPM_AMP_DISABLED: "SiPM Amp - Disabled.",
        ErrorCodes.SIPM_AMP_NOT_CONNECTED: "SiPM Amp - Not connected.",
        ErrorCodes.SIPM_AMP_COMMAND_FAILED: "SiPM Amp - Command execution failed.",
        ErrorCodes.SIPM_AMP_BIASING_FAILED: "SiPM Amp - Biasing to target voltage failed.",
        ErrorCodes.DIGISCOPE_DISABLED: "Digiscope - Disabled.",
        ErrorCodes.DIGISCOPE_NOT_CONNECTED: "Digiscope - Not connected.",
        ErrorCodes.UNKNOWN_ERROR: "Unknown Error."
    }

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")

        with open(os.path.expanduser("~/.config/runcontrol/slack_token"), "r") as f:
            token = f.read().strip()
        self.client = WebClient(token=token)

        self.timer = QTimer(self)
        self.timer.setInterval(100)  # ms
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Guardian module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    def send_message(self, error):
        message = self.error_messages.get(error, "Unknown Error.")
        self.logger.error(f"Error {error}: {message}")
        config = self.main.config_class.run_config["general"]
        if config.get("slack_alarm", False):
            try:
                channel_id = config["slack_channel_id"]
                self.client.chat_postMessage(channel=channel_id, text=f"RC E{error}: {message}")
            except Exception as e:
                self.logger.error(f"Failed to send Slack message: {e}")

    @Slot()
    def error_handler(self, error):
        if error in ErrorCodes:
            self.send_message(error)
            self.main.run_exit_code = error
            self.main.event_exit_code = error
        else:
            self.send_message(ErrorCodes.UNKNOWN_ERROR)
            self.main.run_exit_code = ErrorCodes.UNKNOWN_ERROR
            self.main.event_exit_code = ErrorCodes.UNKNOWN_ERROR

        match error:
            case ErrorCodes.CAMERA_NOT_CONNECTED:
                pass
