import os
from slack_sdk import WebClient
import os

with open(os.path.expanduser("~/.config/runcontrol/slack_token"), "r") as f:
    token = f.read().strip()
client = WebClient(token=token)
channel_id = "C01A549VDHS"

#edited dictionary to incldue all errors (log and inform)
error_dict = {
    0:    "Success - Run control exited successfully.",
    1:    "Run Control - Another instance of RC is running. Program exited.",
    1000: "Run Control - Run ended successfully.",
    1001: "Run Control - Another instance of RC is running. Program exited.",
    1002: "Run Control - Failed to release lock file.",
    1101: "Config - Failed to save config file to disk",
    1102: "Config - Invalid pressure setting.",
    1300: "PLC - PLC Modbus disabled.",
    1400: "NIUSB - NIUSB disabled.",
    1401: "NIUSB - NIUSB not connected.",
    1402: "NIUSB - Cannot retrieve NIUSB handle.",
    1403: "NIUSB - No first fault detected.",
    1404: "NIUSB - Multiple first fault detected.",
    1405: "NIUSB - Invalid NIUSB pin setting.",
    1500: "Arduino - Arduinos disabled.",
    1501: "Arduino - Arduino not connected.",
    1502: "Arduino - Arduino sketch compile failed.",
    1503: "Arduino - Arduino sketch upload failed.",
    1600: "Writer - Writer disabled.",
    1601: "Writer - Data folder not mounted.",
    1700: "SQL - SQL disabled.",
    1701: "SQL - Cannot reach SQL server.",
    2000: "Camera - Camera disabled.",
    2001: "Camera - Camera not connected",
    2100: "Acoustic - GaGe digitizer disabled.",
    2101: "Acoustic - GaGe digitizer not connected.",
    2200: "CAEN - CAEN digitizer disabled.",
    2201: "CAEN - CAEN digitizer not connected.",
    2300: "SiPM Amp - SiPM Amp disabled.",
    2301: "SiPM Amp - SiPM Amp not connected.",
    2400: "Digiscope - Digiscope disabled."
}

def error_handling(error_code):
    if error_code not in error_dict:
        print(f"Invalid error code: {error_code}.")
        return

    value = error_dict[error_code]
    slack_message = f"Run Control: Error code {error_code}: {value}."
    result = client.chat_postMessage(channel=channel_id, text=str(slack_message))
    print("slackalarm", result)

error_code = 2300
# will end up being error code = what is returned from the run control
# what if more than one error?
error_handling(error_code)
