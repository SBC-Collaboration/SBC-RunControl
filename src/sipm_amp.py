import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import paramiko as pm
import logging
import os
import re
import datetime
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import subprocess

class SiPMAmp(QObject):
    daq_mapping = {  # the two numbers are DAC address and DAC channel number
        1: "5 0",
        2: "5 1",
        3: "5 2",
        4: "5 3",
        5: "5 4",
        6: "5 5",
        7: "5 6",
        8: "5 7",
        9: "2 0",
        10: "2 1",
        11: "2 2",
        12: "2 3",
        13: "2 4",
        14: "2 5",
        15: "2 6",
        16: "2 7",
    }

    adc_mapping = {  # the three numbers are ADC address and ADC POS/NEG channel number
        1: "6 0 1",
        2: "6 4 5",
        3: "6 6 7",
        4: "6 2 3",
        5: "4 0 1",
        6: "4 4 5",
        7: "4 6 7",
        8: "4 2 3",
        9: "3 0 1",
        10: "3 4 5",
        11: "3 6 7",
        12: "3 2 3",
        13: "1 0 1",
        14: "1 4 5",
        15: "1 6 7",
        16: "1 2 3",
    }

    sipm_biased = Signal(str)
    sipm_unbiased = Signal(str)

    def __init__(self, mainwindow, amp):
        super().__init__()
        self.main = mainwindow
        self.amp = amp
        self.config = mainwindow.config_class.config["scint"][amp]
        self.logger = logging.getLogger("rc")
        self.username = "root"
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"SiPM {self.amp} module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot()
    def test_sipm_amp(self):
        if not self.config["enabled"]:
            self.logger.debug(f"SiPM {self.amp} disabled.")
            return
        host = self.config["ip_addr"]

        # ping with 1 packet, and 1s timeout
        if not subprocess.call(f"ping -c 1 -W 1 {host}", shell=True):
            self.logger.debug(f"SiPM {self.amp} connected.")
        else:
            self.logger.error(f"SiPM {self.amp} at {host} not connected.")
            raise ConnectionError

    def exec_commands(self, host, commands):
        self.client.connect(host, username=self.username)
        command = "; ".join(commands)
        _stdin, _stdout, _stderr = self.client.exec_command(command)
        print(_stdout.read().decode())
        self.client.close()

    @Slot()
    def bias_sipm(self):
        self.test_sipm_amp()
        if not self.config["enabled"]:
            self.sipm_biased.emit(f"{self.amp}-disabled")
            return
        commands = [
            "dactest -v hv 1 0",  # set HV rail to 0V
            "setPin ENQP hi",  # enable charge pump
            f"dactest -v hv 0 {self.config['qp']}",  # set charge pump voltage
            "enhv enable",  # enable HV rail
            f"dactest -v hv 1 {self.config['bias']}",  # set HV rail voltage
            "adctest -l 1000 -r 8 hv 1 0",  # readback HV rail voltage
        ]
        self.exec_commands(self.config["ip_addr"], commands)
        self.sipm_biased.emit(self.amp)

    @Slot()
    def unbias_sipm(self):
        """
        if not enabled, try pinging the IP address
        if ping successes, still unbias. if not, quit
        ping with only 1 packet, with 1s timeout
        """
        if not self.config["enabled"]:
            self.sipm_unbiased.emit(f"{self.amp}-disabled")
            return
            if subprocess.call(f"ping -c 1 -W 1 {self.config["ip_addr"]}", shell=True):
                self.logger.debug(f"SiPM {self.amp} is disabled and not connected")
                self.sipm_unbiased.emit(f"{self.amp}-disabled")
                return

        commands = [
            "dactest -v hv 1 0",  # set HV rail to 0V
            "enhv disable",  # disable HV rails
            "setPin ENQP lo",  # enable charge pump
        ]
        self.exec_commands(self.config["ip_addr"], commands)
        self.sipm_unbiased.emit(self.amp)

    @Slot()
    def run_iv_curve(self):
        """ tell the SiPM amplifier to do an IV curve measurement"""
        if not self.config["enabled"] or not self.config["iv_enabled"]:
            return
        start_v = self.config["iv_start"]
        stop_v = self.config["iv_stop"]
        step = self.config["iv_step"]
        adc_rate = 4 # 80 sps
        num_readings =  6
        now = datetime.date.today().strftime("%Y%m%d%H%M")
        filename = os.path.join(self.config["iv_data_dir"], f"{self.amp}-{str(now)}.csv")
        commands = [
            "cd /root/nanopi",
            f"iv_cmd.py --start_v {start_v} --stop_v {stop_v} --step {step} --adc_rate {adc_rate} --num_readings {num_readings} --file {filename}"
        ]
        self.exec_commands(self.config["ip_addr"], commands)

    def check_iv_interval(self):
        """ return the time stamp of last IV curve measurement"""
        data_dir = self.config["iv_rc_data_dir"]
        files = os.listdir(data_dir)
        valid_dates = []
        now = datetime.now()
        pattern = re.compile(rf"^{self.amp}-\d{{12}}\.csv$")  # ampN - 12 digit time followed by .csv
        for file in files:
            if pattern.match(file):
                try:
                    datetime_str = file[5:17]  # extract datetime part from filename
                    timestamp = datetime.strptime(datetime_str, "%Y%m%d%H%M")
                    if timestamp > now:
                        self.logger.error("IV curve data timestamp in the future.")
                        raise ValueError
                    valid_dates.append(timestamp)
                except ValueError:
                    # error if pattern doesn't match or time in the future
                    continue

        # check if latest time is more than interval
        interval = self.config["iv_interval"]
        if now - max(valid_dates) > datetime.timedelta(hours=interval):
            return True  # return if we need a new measurement
        else:
            return False

    @Slot()
    def start_run(self):
        self.config = self.main.config_class.run_config["scint"][self.amp]
        if not self.config["enabled"]:
            self.sipm_biased.emit(f"{self.amp}-disabled")
            return
        if self.check_iv_interval():
            self.run_iv_curve
        self.bias_sipm()