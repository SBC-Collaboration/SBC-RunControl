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
    CAEN_DISABLED = 2200
    CAEN_NOT_CONNECTED = 2201
    SIPM_AMP_DISABLED = 2300
    SIPM_AMP_NOT_CONNECTED = 2301
    SIPM_AMP_COMMAND_FAILED = 2310
    SIPM_AMP_HV_COMMAND_FAILED = 2311
    SIPM_AMP_QP_COMMAND_FAILED = 2312
    SIPM_AMP_CH_COMMAND_FAILED = 2313
    DIGISCOPE_DISABLED = 2400
    DIGISCOPE_NOT_CONNECTED = 2401

class Guardian(QObject):
    error_messages = {
        ErrorCodes.RC_SUCCESS: "Success - Run control exited successfully.",
        ErrorCodes.LOCKFILE_LOCKED: "Run Control - Failed to acquire lock file.",
        ErrorCodes.LOCKFILE_FAILED_TO_RELEASE: "Run Control - Failed to release lock file.",
        ErrorCodes.CONFIG_SAVE_FAILED: "Config - Failed to save config file to disk",
        ErrorCodes.CONFIG_INVALID_PRESSURE: "Config - Invalid pressure setting.",
        ErrorCodes.PLC_DISABLED: "PLC - Modbus disabled.",
        ErrorCodes.PLC_CONNECTION_FAILED: "PLC - Connection failed.",
        ErrorCodes.PLC_SMB_PERMISSION_FILE_MISSING: "PLC - SMB permission file missing.",
        ErrorCodes.PLC_PRESSURE_CYCLE_START_FAILED: "PLC - PPressure cycle start failed.",
        ErrorCodes.PLC_PRESSURE_CYCLE_STOP_FAILED: "PLC - PPressure cycle stop failed.",
        ErrorCodes.PLC_LED_ON_FAILED: "PLC - LED on failed.",
        ErrorCodes.PLC_LED_OFF_FAILED: "PLC - LED off failed.",
        ErrorCodes.PLC_SLOWDAQ_START_FAILED: "PLC - SLOW DAQ start failed.",
        ErrorCodes.PLC_SLOWDAQ_STOP_FAILED: "PLC - SLOW DAQ stop failed.",
        ErrorCodes.PLC_PSET_FAILED: "PLC - PSET write failed.",
        ErrorCodes.NIUSB_DISABLED: "NIUSB - NIUSB disabled.",
        ErrorCodes.NIUSB_NOT_CONNECTED: "NIUSB - NIUSB not connected.",
        ErrorCodes.NIUSB_CANNOT_RETRIEVE_HANDLE: "NIUSB - Cannot retrieve NIUSB handle.",
        ErrorCodes.NIUSB_NO_FIRST_FAULT: "NIUSB - No first fault detected.",
        ErrorCodes.NIUSB_MULTIPLE_FIRST_FAULT: "NIUSB - Multiple first fault detected.",
        ErrorCodes.NIUSB_INVALID_PIN: "NIUSB - Invalid NIUSB pin setting.",
        ErrorCodes.ARDUINO_DISABLED: "Arduino - Arduinos disabled.",
        ErrorCodes.ARDUINO_NOT_CONNECTED: "Arduino - Arduino not connected.",
        ErrorCodes.ARDUINO_SKETCH_ARCHIVAL_FAILED: "Arduino - Arduino sketch archival failed.",
        ErrorCodes.ARDUINO_SKETCH_COMPILE_UPLOAD_FAILED: "Arduino - Arduino sketch compilation or upload failed.",
        ErrorCodes.WRITER_DISABLED: "Writer - Writer disabled.",
        ErrorCodes.WRITER_NOT_MOUNTED: "Writer - Data folder not mounted.",
        ErrorCodes.SQL_DISABLED: "SQL - SQL disabled.",
        ErrorCodes.SQL_NOT_CONNECTED: "SQL - Cannot reach SQL server.",
        ErrorCodes.CAMERA_DISABLED: "Camera - Camera disabled.",
        ErrorCodes.CAMERA_NOT_CONNECTED: "Camera - Camera not connected",
        ErrorCodes.ACOUSTIC_DISABLED: "Acoustic - GaGe digitizer disabled.",
        ErrorCodes.ACOUSTIC_NOT_CONNECTED: "Acoustic - GaGe digitizer not connected.",
        ErrorCodes.CAEN_DISABLED: "CAEN - CAEN digitizer disabled.",
        ErrorCodes.CAEN_NOT_CONNECTED: "CAEN - CAEN digitizer not connected.",
        ErrorCodes.SIPM_AMP_DISABLED: "SiPM Amp - SiPM Amp disabled.",
        ErrorCodes.SIPM_AMP_NOT_CONNECTED: "SiPM Amp - SiPM Amp not connected.",
        ErrorCodes.SIPM_AMP_COMMAND_FAILED: "SiPM Amp - Command execution failed.",
        ErrorCodes.SIPM_AMP_HV_COMMAND_FAILED: "SiPM Amp - HV command execution failed.",
        ErrorCodes.SIPM_AMP_QP_COMMAND_FAILED: "SiPM Amp - QP command execution failed.",
        ErrorCodes.SIPM_AMP_CH_COMMAND_FAILED: "SiPM Amp - CH command execution failed.",
        ErrorCodes.DIGISCOPE_DISABLED: "Digiscope - Digiscope disabled.",
        ErrorCodes.DIGISCOPE_NOT_CONNECTED: "Digiscope - Digiscope not connected.",
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
        
        match error:
            case 2:
                pass
