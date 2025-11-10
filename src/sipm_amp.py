import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import paramiko as pm
import logging
import os
import re
import time
import datetime as dt
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import subprocess
from sbcbinaryformat import Writer
from src.guardian import ErrorCodes

class SiPMAmp(QObject):
    """
    SiPM amplifier module, responsible for controlling the SiPM amplifier boards.
    It handles the connection to the amplifier, reading and writing voltages, and performing IV curve measurements.
    """

    _dac_mapping = {  # the two numbers are DAC address and DAC channel number
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

    _adc_mapping = {  # the three numbers are ADC address and ADC POS/NEG channel number
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

    _hv_dac_mapping = {
        "QPout": "hv 0",
        "HVout": "hv 1",
        "Enable HVout": "hv 3"
    }

    _hv_adc_mapping = {
        "HVout": "hv 1 0",
        "+QPout": "hv 3 2",
        "-QPout": "hv 4 5"
    }

    run_started = Signal(str)
    run_stopped = Signal(str)
    event_started = Signal(str)
    event_stopped = Signal(str)
    error = Signal(int, str)

    def __init__(self, mainwindow, amp):
        super().__init__()
        self.main = mainwindow
        self.amp = amp
        self.config = mainwindow.config_class.config["scint"][amp]
        self.logger = logging.getLogger("rc")
        self.username = "root"
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
        self.offset_v = 0
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
        """
        Test if the SiPM amplifier is connected by pinging its IP address.

        :raises ConnectionError: If the SiPM amplifier is not connected
        """
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
        """
        Execute a list of commands on the SiPM amplifier via SSH. If no active connection exists, 
        it will establish one, and close connection when execution ends.

        :param commands: List of commands to execute
        :type commands: list
        :raises RuntimeError: If command execution fails
        """
        already_connected = False
        if self.client.get_transport() and self.client.get_transport().is_active():
            already_connected = True
        else:
            try:
                self.client.connect(self.config['ip_addr'], username=self.config["user"])
            except pm.ssh_exception.NoValidConnectionsError:
                self.error.emit(ErrorCodes.SIPM_AMP_NOT_CONNECTED, self.amp)
                return
        command = "; ".join(commands)
        _stdin, _stdout, _stderr = self.client.exec_command(command)
        exit_status = _stdout.channel.recv_exit_status()
        if exit_status != 0:
            error_message = _stderr.read().decode()
            self.logger.warning(f"SiPM {self.amp} command failed with exit status {exit_status}: {error_message}")
            raise RuntimeError(f"Command execution failed: {error_message}")
        if not already_connected:
            self.client.close()

    @Slot()
    def setup_sipm(self):
        """
        Setup SiPM amplifier HV rail and charge pump.
        """

        setup_commands = [
            "/root/nanopi/dactest -v hv 1 0",  # set HV rail to 0V
            "/root/nanopi/setPin ENQP hi",  # enable charge pump
            f"/root/nanopi/dactest -v hv 0 {self.config['qp']}",  # set charge pump voltage
            "/root/nanopi/enhv enable",  # enable HV rail
        ]
        # Retry until setup commands succeed
        while True:
            try:
                self.exec_commands(setup_commands)
                break
            except RuntimeError:
                continue

    @Slot()
    def bias_sipm(self, error=0.01, iterations=3, offset_v=0):
        """ 
        Bias SiPM amplifier, and then make small changes so the bias readback is close to target value 

        :param error: acceptable error in volts
        :type error: float
        :param iterations: number of iterations to adjust the bias. If 1, it will set only once
        :type iterations: int
        """

        # start feedback loop to set the bias voltage
        target_v = self.config["bias"]
        set_v = target_v - offset_v
        i = 0

        while True:
            i+=1
            bias_command = [f"/root/nanopi/dactest -v hv 1 {set_v}"]  # set HV rail voltage
            try:
                self.exec_commands(bias_command)
            except RuntimeError:
                continue

            readback_v = self.read_voltages()["hv_mean_v"]
            offset_v = readback_v - set_v
            diff_v = readback_v - target_v
            self.logger.debug(f"SiPM {self.amp} bias setting try {i}, readback: {readback_v:.3f} V, set: {set_v:.3f} V, target: {target_v:.3f} V, diff: {diff_v:.3f} V")
            if abs(diff_v) < error and i>=iterations:
                self.offset_v = offset_v
                break
            set_v = target_v - offset_v  # adjust target voltage

            if i >= max(5*iterations, 10):
                self.logger.error(f"SiPM {self.amp} bias cannot be set to target voltage.")
                self.error.emit(ErrorCodes.SIPM_AMP_BIASING_FAILED, self.amp)
                break

        self.logger.debug(f"SiPM {self.amp} bias set to {readback_v:.3f} V after {i} iterations, with target {target_v:.3f} V.")

    @Slot()
    def unbias_sipm(self):
        """
        Unbias SiPM amplifier HV rail, disable HV and charge pump.
        """
        unset_commands = [
            "/root/nanopi/dactest -v hv 1 0",  # set HV rail to 0V
            "/root/nanopi/enhv disable",  # disable HV rails
            "/root/nanopi/setPin ENQP lo",  # disable charge pump
        ]
        # Retry until unset commands succeed
        while True:
            try:
                self.exec_commands(unset_commands)
                break
            except RuntimeError:
                continue

    @Slot()
    def run_iv_curve(self):
        """
        Tell the SiPM amplifier to do an IV curve measurement
        """
        if self.main.run_state == self.main.run_states["idle"]:
            self.config = self.main.config_class.config["scint"][self.amp]
        elif self.main.run_state != self.main.run_states["starting_run"]:
            self.logger.error("Cannot run IV curve measurement during a run.")
            return

        start_v = self.config["iv_start"]
        stop_v = self.config["iv_stop"]
        step = self.config["iv_step"]
        adc_rate = 8  # 1000 sps
        num_readings =  1000
        now = dt.datetime.now().strftime("%Y%m%d-%H%M")
        filename = os.path.join(self.config["iv_data_dir"], f"{self.amp}-{str(now)}.csv")

        self.logger.info(f"SiPM {self.amp} starting IV curve measurement. Voltage from {start_v} V to {stop_v} V in steps of {step} V. Data will be saved to {filename}.")
        commands = [
            "cd /root/nanopi",
            f"/root/nanopi/iv_cmd.py --start_v {start_v} --stop_v {stop_v} --step {step} --adc_rate {adc_rate} --num_readings {num_readings} --file {filename}"
        ]
        # Retry until commands succeed
        while True:
            try:
                self.exec_commands(commands)
                break
            except RuntimeError:
                continue
        self.logger.debug(f"SiPM {self.amp} IV curve measurement command complete.")

    def check_iv_interval(self):
        """
        Return the time stamp of last IV curve measurement

        :return: True if a new IV measurement is needed, False if last one is still within the interval.
        :rtype: bool
        """
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
    
    def _parse_hv_output(self, output, channel="unknown"):
        """
        Parse the ADC test output and extract relevant data

        :param output: The output string from the ADC test command
        :type output: str
        :return: HV or QP readback data, both in ADC and converted voltages
        :rtype: dict
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
        else:
            if channel != "unknown":
                ch = channel
            else:
                self.logger.error(f"Could not find channel information in HV output: {output}")
                raise ValueError("Could not find channel information in HV output.")

        # Extract ADC statistics
        adcvalue_match = re.search(r'ADCValue:\s+mean: ([\d.e+-]+), stdev: ([\d.e+-]+)', output)
        if adcvalue_match:
            data[f'{ch}_mean_adc'] = float(adcvalue_match.group(1))
            data[f'{ch}_stdev_adc'] = float(adcvalue_match.group(2))
        else:
            self.logger.error(f"Could not find ADC values for {ch} in output: {output}")
            data[f'{ch}_mean_adc'] = None
            data[f'{ch}_stdev_adc'] = None

        # Extract Converted statistics
        converted_match = re.search(r'Converted:\s*mean:\s*([\d.e+-]+)\s*(nV|uV|mV|V),\s*stdev:\s*([\d.e+-]+)\s*(nV|uV|mV|V)', output)
        if converted_match:
            mean_value = float(converted_match.group(1))
            mean_unit = converted_match.group(2)
            stdev_value = float(converted_match.group(3))
            stdev_unit = converted_match.group(4)
            
            # Convert both to volts
            data[f'{ch}_mean_v'] = mean_value * voltage_conversion[mean_unit]
            data[f'{ch}_stdev_v'] = stdev_value * voltage_conversion[stdev_unit]
        else:
            self.logger.error(f"Could not find converted voltages for {ch} in output: {output}")
            data[f'{ch}_mean_v'] = None
            data[f'{ch}_stdev_v'] = None

        return data

    def _parse_dac_output(self, output):
        """
        Parse of DAC output of per-channel offset

        :param output: The output string from the DAC test readback command
        :type output: str
        :return: List of per-channel offsets in ADC counts
        :rtype: list
        """
        values_match = re.findall(r'V\[\d+\] = (\d+)', output)
        values = [int(v) for v in values_match]
        return values
    
    @Slot()
    def read_voltages(self):
        """
        Read the SiPM amplifier HV and QP voltages, and per-channel offsets.

        :return: Dictionary with HV, QP, and channel offsets in ADC counts and volts
        :rtype: dict
        """
        rate = 8
        n_samples = 100
        hv_command = f"/root/nanopi/adctest -l {n_samples} -r {rate} hv 1 0"
        qp_command = f"/root/nanopi/adctest -l {n_samples} -r {rate} hv 3 2"
        ch_command_1 = f"/root/nanopi/dactest -r 5" # first half of the channels
        ch_command_2 = f"/root/nanopi/dactest -r 2" # second half of the channels

        readback = {'amp': self.amp, 
                    'timestamp': dt.datetime.now().timestamp()}
        _stdin, _stdout, _stderr = self.client.exec_command(hv_command)
        exit_status = _stdout.channel.recv_exit_status()
        if exit_status != 0:
            error_message = _stderr.read().decode()
            self.logger.warning(f"SiPM {self.amp} HV readback command failed with exit status {exit_status}: {error_message}")
            return False

        out_message = _stdout.read().decode()
        try:
            readback.update(self._parse_hv_output(out_message, "hv"))
        except ValueError:
            self.logger.warning(f"SiPM {self.amp} HV readback parsing failed: {out_message}")
            return False

        _stdin, _stdout, _stderr = self.client.exec_command(qp_command)
        exit_status = _stdout.channel.recv_exit_status()
        if exit_status != 0:
            error_message = _stderr.read().decode()
            self.logger.warning(f"SiPM {self.amp} QP readback command failed with exit status {exit_status}: {error_message}")
            return False

        out_message = _stdout.read().decode()
        try:
            readback.update(self._parse_hv_output(out_message, "qp"))
        except ValueError:
            self.logger.warning(f"SiPM {self.amp} QP readback parsing failed: {out_message}")
            return False

        _stdin, _stdout, _stderr = self.client.exec_command(ch_command_1)
        exit_status = _stdout.channel.recv_exit_status()
        if exit_status != 0:
            error_message = _stderr.read().decode()
            self.logger.error(f"SiPM {self.amp} channel offset readback command failed with exit status {exit_status}: {error_message}")
            return False
        out_message = _stdout.read().decode()
        try:
            offsets1 = self._parse_dac_output(out_message)
        except ValueError:
            self.logger.error(f"SiPM {self.amp} channel offset readback parsing failed: {out_message}")
            return False

        _stdin, _stdout, _stderr = self.client.exec_command(ch_command_2)
        exit_status = _stdout.channel.recv_exit_status()
        if exit_status != 0:
            error_message = _stderr.read().decode()
            self.logger.error(f"SiPM {self.amp} channel offset readback command failed with exit status {exit_status}: {error_message}")
            return False
        out_message = _stdout.read().decode()
        try:
            offsets2 = self._parse_dac_output(out_message)
        except ValueError:
            self.logger.error(f"SiPM {self.amp} channel offset readback parsing failed: {out_message}")
            return False

        dac_offsets = offsets1 + offsets2
        readback["ch_offsets_adc"] = dac_offsets
        scale_v = 5.0 / 2**16
        readback["ch_offsets_v"] = [offset * scale_v for offset in dac_offsets]

        return readback
    
    @Slot()
    def write_voltages(self, voltages):
        """
        Read the SiPM amplifier HV and QP voltages, and per-channel offsets, and write the values to a binary file.

        :param voltages: Dictionary with HV, QP, and channel offsets in ADC counts and volts
        :type voltages: dict
        """
        self.logger.debug(f"SiPM {self.amp} bias readback: {voltages['hv_mean_v']} V")

        headers = ["amp", "timestamp", "hv_mean_adc", "hv_stdev_adc", "hv_mean_v", "hv_stdev_v", "qp_mean_adc", "qp_stdev_adc", 
                   "qp_mean_v", "qp_stdev_v", "ch_offsets_adc", "ch_offsets_v"]
        dtypes = ["U10", "f", "f", "f", "f", "f", "f", "f", "f", "f", "i4", "f"]
        shapes = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [16], [16]]
        
        # lock mutex before writing
        self.main.sipm_mutex.lock()
        try:
            with Writer(os.path.join(self.main.event_dir, f"sipm_amp.sbc"), 
                headers, dtypes, shapes) as writer:
                writer.write(voltages)
        finally:
            self.main.sipm_mutex.unlock()
        self.logger.debug(f"SiPM {self.amp} biases written to file.")

    @Slot()
    def start_run(self):
        """
        Prepare SiPM amplifier for a run. Connect to the device, and perform IV curve measurement if needed.
        """
        self.config = self.main.config_class.run_config["scint"][self.amp]
        if not self.config["enabled"]:
            self.run_started.emit(f"{self.amp}-disabled")
            return
        
        try:
            self.client.connect(self.config["ip_addr"], username=self.config["user"])
        except pm.ssh_exception.NoValidConnectionsError:
            self.error.emit(ErrorCodes.SIPM_AMP_NOT_CONNECTED, self.amp)
            return

        self.logger.debug(f"SiPM {self.amp} connected to {self.config['ip_addr']}.")
        if self.check_iv_interval():
            self.run_iv_curve()
            self.logger.debug(f"SiPM {self.amp} IV curve measurement executed.")
        
        # bias SiPMs
        self.setup_sipm()
        self.bias_sipm(offset_v=self.offset_v)
        self.logger.debug(f"SiPM {self.amp} bias command executed.")
        self.run_started.emit(self.amp)
    
    @Slot()
    def stop_run(self):
        """
        Unarm SiPM amplifier, and disconnect from the device.
        """
        if not self.config["enabled"]:
            self.run_stopped.emit(f"{self.amp}-disabled")
            return
        
        # unbias SiPMs
        self.unbias_sipm()
        self.logger.debug(f"SiPM {self.amp} unbias command executed.")

        if self.client.get_transport() and self.client.get_transport().is_active():
            self.client.close()
            self.logger.debug(f"SiPM {self.amp} disconnected from {self.config['ip_addr']}.")
        self.run_stopped.emit(self.amp)

    @Slot()
    def start_event(self):
        """
        Prepare SiPM amplifier for an event. Bias the SiPM, and write the readback voltages to a file.
        """
        if not self.config["enabled"]:
            self.event_started.emit(f"{self.amp}-disabled")
            return
        
        # bias SiPMs
        self.bias_sipm(iterations=1, offset_v=self.offset_v)
        self.logger.debug(f"SiPM {self.amp} bias command executed.")
        voltage_readback = self.read_voltages()
        # redo voltage readback if failed
        while not voltage_readback:
            voltage_readback = self.read_voltages()
        self.write_voltages(voltages=voltage_readback)
        self.event_started.emit(self.amp)
    
    @Slot()
    def stop_event(self):
        """
        At the end of event, unbias SiPM amplifier, and write the readback voltages to a file.
        """
        if not self.config["enabled"]:
            self.event_stopped.emit(f"{self.amp}-disabled")
            return
        
        voltage_readback = self.read_voltages()
        # redo voltage readback if failed
        while not voltage_readback:
            voltage_readback = self.read_voltages()
        self.write_voltages(voltages=voltage_readback)
        self.event_stopped.emit(self.amp)
