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
    NIUSB_DISABLED = 1400
    NIUSB_NOT_CONNECTED = 1401
    NIUSB_CANNOT_RETRIEVE_HANDLE = 1402
    NIUSB_NO_FIRST_FAULT = 1403
    NIUSB_MULTIPLE_FIRST_FAULT = 1404
    NIUSB_INVALID_PIN = 1405
    ARDUINO_DISABLED = 1500
    ARDUINO_NOT_CONNECTED = 1501
    ARDUINO_SKETCH_COMPILE_FAILED = 1502
    ARDUINO_SKETCH_UPLOAD_FAILED = 1503
    WRITER_DISABLED = 1600
    WRITER_NOT_MOUNTED = 1601
    SQL_DISABLED = 1700
    SQL_NOT_CONNECTED = 1701
    CAMERA_DISABLED = 2000
    CAMERA_NOT_CONNECTED = 2001
    ACOUSTIC_DISABLED = 2100
    ACOUSTIC_NOT_CONNECTED = 2101
    CAEN_DISABLED = 2200
    CAEN_NOT_CONNECTED = 2201
    SIPM_AMP_DISABLED = 2300
    SIPM_AMP_NOT_CONNECTED = 2301
    DIGISCOPE_DISABLED = 2400
    DIGISCOPE_NOT_CONNECTED = 2401

class Guardian(QObject):
    error_messages = {
        ErrorCodes.RC_SUCCESS:    "Success - Run control exited successfully.",
        ErrorCodes.RC_DUPLICATE_INSTANCE:    "Run Control - Another instance of RC is running. Program exited.",
        ErrorCodes.RC_RUN_ENDED_SUCCESSFULLY: "Run Control - Run ended successfully.",
        ErrorCodes.RC_RUN_ENDED_UNSUCCESSFULLY: "Run Control - Run ended unsuccessfully.",
        ErrorCodes.RC_LOCKFILE_LOCKED: "Run Control - Failed to acquire lock file.",
        ErrorCodes.RC_LOCKFILE_FAILED_TO_RELEASE: "Run Control - Failed to release lock file.",
        ErrorCodes.RC_CONFIG_SAVE_FAILED: "Config - Failed to save config file to disk",
        ErrorCodes.RC_CONFIG_INVALID_PRESSURE: "Config - Invalid pressure setting.",
        ErrorCodes.RC_PLC_DISABLED: "PLC - PLC Modbus disabled.",
        ErrorCodes.RC_NIUSB_DISABLED: "NIUSB - NIUSB disabled.",
        ErrorCodes.RC_NIUSB_NOT_CONNECTED: "NIUSB - NIUSB not connected.",
        ErrorCodes.RC_NIUSB_CANNOT_RETRIEVE_HANDLE: "NIUSB - Cannot retrieve NIUSB handle.",
        ErrorCodes.RC_NIUSB_NO_FIRST_FAULT: "NIUSB - No first fault detected.",
        ErrorCodes.RC_NIUSB_MULTIPLE_FIRST_FAULT: "NIUSB - Multiple first fault detected.",
        ErrorCodes.RC_NIUSB_INVALID_PIN: "NIUSB - Invalid NIUSB pin setting.",
        ErrorCodes.RC_ARDUINO_DISABLED: "Arduino - Arduinos disabled.",
        ErrorCodes.RC_ARDUINO_NOT_CONNECTED: "Arduino - Arduino not connected.",
        ErrorCodes.RC_ARDUINO_SKETCH_COMPILE_FAILED: "Arduino - Arduino sketch compile failed.",
        ErrorCodes.RC_ARDUINO_SKETCH_UPLOAD_FAILED: "Arduino - Arduino sketch upload failed.",
        ErrorCodes.RC_WRITER_DISABLED: "Writer - Writer disabled.",
        ErrorCodes.RC_WRITER_NOT_MOUNTED: "Writer - Data folder not mounted.",
        ErrorCodes.RC_SQL_DISABLED: "SQL - SQL disabled.",
        ErrorCodes.RC_SQL_NOT_CONNECTED: "SQL - Cannot reach SQL server.",
        ErrorCodes.RC_CAMERA_DISABLED: "Camera - Camera disabled.",
        ErrorCodes.RC_CAMERA_NOT_CONNECTED: "Camera - Camera not connected",
        ErrorCodes.RC_ACOUSTIC_DISABLED: "Acoustic - GaGe digitizer disabled.",
        ErrorCodes.RC_ACOUSTIC_NOT_CONNECTED: "Acoustic - GaGe digitizer not connected.",
        ErrorCodes.RC_CAEN_DISABLED: "CAEN - CAEN digitizer disabled.",
        ErrorCodes.RC_CAEN_NOT_CONNECTED: "CAEN - CAEN digitizer not connected.",
        ErrorCodes.RC_SIPM_AMP_DISABLED: "SiPM Amp - SiPM Amp disabled.",
        ErrorCodes.RC_SIPM_AMP_NOT_CONNECTED: "SiPM Amp - SiPM Amp not connected.",
        ErrorCodes.RC_DIGISCOPE_DISABLED: "Digiscope - Digiscope disabled.",
        ErrorCodes.RC_DIGISCOPE_NOT_CONNECTED: "Digiscope - Digiscope not connected.",
    }

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")

        with open(os.path.expanduser("~/.config/runcontrol/slack_token"), "r") as f:
            token = f.read().strip()
        self.client = WebClient(token=token)
        self.channel_id = "C01A549VDHS"

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
        self.client.chat_postMessage(channel=self.channel_id, text=f"RC TEST E{error}: {message}")
        self.logger.error(f"Error {error}: {message}")

    @Slot()
    def error_handler(self, error):
        match error:
            case 2:
                self.logger.error("Error 0002: Lock file cannot be released.")
            case 1101:
                self.logger.error("Error 1101: Failed to save config file to disk.")
            case _:
                self.logger.error(f"Unknown error code: {error}")
