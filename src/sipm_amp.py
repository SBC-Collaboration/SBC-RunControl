import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import paramiko as pm
import logging
import os
import re
import datetime as dt
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import subprocess
from sbcbinaryformat import Writer

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

    hv_dac_mapping = {
        "QPout": "hv 0",
        "HVout": "hv 1",
        "Enable HVout": "hv 3"
    }

    hv_adc_mapping = {
        "HVout": "hv 1 0",
        "+QPout": "hv 3 2",
        "-QPout": "hv 4 5"
    }

    run_started = Signal(str)
    run_stopped = Signal(str)

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

        # ping with 1 packet, and 1s timeout
        if not subprocess.call(f"ping -c 1 -W 1 {self.config['ip_addr']}", shell=True):
            self.logger.debug(f"SiPM {self.amp} connected.")
        else:
            self.logger.error(f"SiPM {self.amp} at {self.config['ip_addr']} not connected.")
            raise ConnectionError

    def exec_commands(self, commands):
        already_connected = False
        if self.client.get_transport() and self.client.get_transport().is_active():
            already_connected = True
        else:
            self.client.connect(self.config['ip_addr'], username=self.config["user"])
        command = "; ".join(commands)
        _stdin, _stdout, _stderr = self.client.exec_command(command)
        self.logger.error(_stderr.read().decode())
        self.logger.debug(_stdout.read().decode())
        if not already_connected:
            self.client.close()

    @Slot()
    def bias_sipm(self):
        commands = [
            "/root/nanopi/dactest -v hv 1 0",  # set HV rail to 0V
            "/root/nanopi/setPin ENQP hi",  # enable charge pump
            f"/root/nanopi/dactest -v hv 0 {self.config['qp']}",  # set charge pump voltage
            "/root/nanopi/enhv enable",  # enable HV rail
            f"/root/nanopi/dactest -v hv 1 {self.config['bias']}",  # set HV rail voltage
            "/root/nanopi/adctest -l 1000 -r 8 hv 1 0",  # readback HV rail voltage
        ]
        self.exec_commands(self.config["ip_addr"], commands)

    @Slot()
    def unbias_sipm(self):
        commands = [
            "/root/nanopi/dactest -v hv 1 0",  # set HV rail to 0V
            "/root/nanopi/enhv disable",  # disable HV rails
            "/root/nanopi/setPin ENQP lo",  # disable charge pump
        ]
        self.exec_commands(self.config["ip_addr"], commands)

    @Slot()
    def run_iv_curve(self):
        """ tell the SiPM amplifier to do an IV curve measurement"""
        start_v = self.config["iv_start"]
        stop_v = self.config["iv_stop"]
        step = self.config["iv_step"]
        adc_rate = 4 # 80 sps
        num_readings =  6
        now = dt.date.today().strftime("%Y%m%d%H%M")
        filename = os.path.join(self.config["iv_data_dir"], f"{self.amp}-{str(now)}.csv")
        commands = [
            "cd /root/nanopi",
            f"iv_cmd.py --start_v {start_v} --stop_v {stop_v} --step {step} --adc_rate {adc_rate} --num_readings {num_readings} --file {filename}"
        ]
        self.exec_commands(self.config["ip_addr"], commands)

    def check_iv_interval(self):
        """ return the time stamp of last IV curve measurement"""
        if not self.config["enabled"] or not self.config["iv_enabled"]:
            return False
        
        data_dir = self.config["iv_rc_dir"]
        files = os.listdir(data_dir)
        valid_dates = []
        now = dt.datetime.now()
        pattern = re.compile(rf"^{self.amp}-\d{{12}}\.csv$")  # ampN - 12 digit time followed by .csv
        for file in files:
            if pattern.match(file):
                try:
                    datetime_str = file[5:17]  # extract datetime part from filename
                    timestamp = dt.datetime.strptime(datetime_str, "%Y%m%d%H%M")
                    if timestamp > now:
                        self.logger.error("IV curve data timestamp in the future.")
                        raise ValueError
                    valid_dates.append(timestamp)
                except ValueError:
                    # error if pattern doesn't match or time in the future
                    continue

        # check if latest time is more than interval
        interval = self.config["iv_interval"]
        if not valid_dates or now - max(valid_dates) > dt.timedelta(hours=interval):
            return True  # return if we need a new measurement
        else:
            return False
    
    def _parse_hv_output(output):
        """
        Parse the ADC test output and extract relevant data
        """
        data = {}
        voltage_conversion = {
            'nV': 1e-9,
            'uV': 1e-6,
            'mV': 1e-3,
            'V': 1
        }
        
        # Extract channels
        channels_match = re.search(r'Measuring between channels (\d+) and (\d+)', output)
        if channels_match:
            channels = (int(channels_match.group(1)), int(channels_match.group(2)))
            if channels == (1, 0):
                ch = "hv"
            elif channels == (3, 2):
                ch = "qp"
            elif channels == (4, 5):
                ch = "-qp"
            else:
                raise ValueError(f"Unexpected channel pair for HV readback: {channels}")

        # Extract ADC statistics
        adcvalue_match = re.search(r'ADCValue:\s+mean: ([\d.]+), stdev: ([\d.]+)', output)
        if adcvalue_match:
            data[f'{ch}_mean_adc'] = float(adcvalue_match.group(1))
            data[f'{ch}_stdev_adc'] = float(adcvalue_match.group(2))
        else:
            data[f'{ch}_mean_adc'] = None
            data[f'{ch}_stdev_adc'] = None

        # Extract Converted statistics
        converted_match = re.search(r'Converted:\s*mean:\s*([\d.]+)\s*(nV|uV|mV|V),\s*stdev:\s*([\d.]+)\s*(nV|uV|mV|V)', output)
        if converted_match:
            mean_value = float(converted_match.group(1))
            mean_unit = converted_match.group(2)
            stdev_value = float(converted_match.group(3))
            stdev_unit = converted_match.group(4)
            
            # Convert both to volts
            data[f'{ch}_mean_v'] = mean_value * voltage_conversion[mean_unit]
            data[f'{ch}_stdev_v'] = stdev_value * voltage_conversion[stdev_unit]
        else:
            data[f'{ch}_mean_v'] = None
            data[f'{ch}_stdev_v'] = None

        return data

    def _parse_dac_output(output):
        values_match = re.findall(r'V\[\d+\] = (\d+)', output)
        values = [int(v) for v in values_match]
        return values
    
    @Slot()
    def read_voltages(self):
        rate = 8
        n_samples = 100
        hv_command = f"/root/nanopi/adctest -l {n_samples} -r {rate} hv 1 0"
        qp_command = f"/root/nanopi/adctest -l {n_samples} -r {rate} hv 3 2"
        ch_command_1 = f"/root/nanopi/dactest -r 5" # first half of the channels
        ch_command_2 = f"/root/nanopi/dactest -r 2" # second half of the channels

        readback = {'amp': self.amp, 
                    'timestamp': dt.datetime.now().timestamp()}
        _stdin, _stdout, _stderr = self.exec_command(hv_command)
        readback.update(self._parse_hv_output(_stdout.read().decode()))
        _stdin, _stdout, _stderr = self.exec_command(qp_command)
        readback.update(self._parse_hv_output(_stdout.read().decode()))

        _stdin, _stdout, _stderr = self.exec_command(ch_command_1)
        offsets1 = self._parse_dac_output(_stdout.read().decode())
        _stdin, _stdout, _stderr = self.exec_command(ch_command_2)
        offsets2 = self._parse_dac_output(_stdout.read().decode())
        dac_offsets = offsets1 + offsets2
        readback["ch_offsets_adc"] = dac_offsets
        scale_v = 5.0 / 2**16
        readback["ch_offsets_v"] = [offset * scale_v for offset in dac_offsets]

        return readback
    
    @Slot()
    def measure_and_write_voltages(self):
        voltages = self.read_voltages()
        self.logger.debug(f"SiPM {self.amp} bias readback: {voltages['hv_mean_v']} V")

        # TODO: Add mutex lock
        headers = ["amp", "timestamp", "hv_mean_adc", "hv_stdev_adc", "hv_mean_v", "hv_stdev_v", "qp_mean_adc", "qp_stdev_adc", 
                   "qp_mean_v", "qp_stdev_v", "ch_offsets_adc", "ch_offsets_v"]
        dtypes = ["U10", "f", "f", "f", "f", "f", "f", "f", "f", "f", "i4", "f"]
        shapes = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [16], [16]]
        writer = Writer(
            os.path.join(self.main.event_dir, f"sipm_amp.sbc"), 
            headers, dtypes, shapes)
        writer.write(voltages)

    @Slot()
    def start_run(self):
        self.config = self.main.config_class.run_config["scint"][self.amp]
        if not self.config["enabled"]:
            self.run_started.emit(f"{self.amp}-disabled")
            return
        self.client.connect(self.config["ip_addr"], username=self.config["user"])
        self.logger.debug(f"SiPM {self.amp} connected to {self.config['ip_addr']}.")
        if self.check_iv_interval():
            self.run_iv_curve()
            self.logger.debug(f"SiPM {self.amp} IV curve measurement executed.")
        self.bias_sipm()
        self.logger.debug(f"SiPM {self.amp} bias command executed.")
        self.measure_and_write_voltages()
        self.run_started.emit(self.amp)
    

    @Slot()
    def stop_run(self):
        if not self.config["enabled"]:
            self.run_stopped.emit(f"{self.amp}-disabled")
            return
        self.measure_and_write_voltages()
        self.unbias_sipm()
        if self.client.get_transport() and self.client.get_transport().is_active():
            self.client.close()
            self.logger.debug(f"SiPM {self.amp} disconnected from {self.config['ip_addr']}.")
        self.logger.debug(f"SiPM {self.amp} unbias command executed.")
        self.run_stopped.emit(self.amp)