import paramiko as pm
import logging
import os


class SiPMAmp:
    daq_mapping = {  # the two numbers are DAC address and DAC channel number
        1: [5, 0],
        2: [5, 1],
        3: [5, 2],
        4: [5, 3],
        5: [5, 4],
        6: [5, 5],
        7: [5, 6],
        8: [5, 7],
        9: [2, 0],
        10: [2, 1],
        11: [2, 2],
        12: [2, 3],
        13: [2, 4],
        14: [2, 5],
        15: [2, 6],
        16: [2, 7],
    }

    adc_mapping = {  # the three numbers are ADC address and ADC POS/NEG channel number
        1: [6, 0, 1],
        2: [6, 4, 5],
        3: [6, 6, 7],
        4: [6, 2, 3],
        5: [4, 0, 1],
        6: [4, 4, 5],
        7: [4, 6, 7],
        8: [4, 2, 3],
        9: [3, 0, 1],
        10: [3, 4, 5],
        11: [3, 6, 7],
        12: [3, 2, 3],
        13: [1, 0, 1],
        14: [1, 4, 5],
        15: [1, 6, 7],
        16: [1, 2, 3],
    }

    def __init__(self, main_window):
        self.main = main_window
        self.config = main_window.config_class.config
        self.logger = logging.getLogger("rc")
        os.putenv("PATH", "/home/sbc/packages")
        self.username = "pi"
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
        self.save_config()
        self.logger.debug("SiPM amp class initialized.")

    def exec_commands(self, host, command):
        self.client.connect(host, username=self.username)
        _stdin, _stdout, _stderr = self.client.exec_command(command)
        print(_stdout.read().decode())
        self.client.close()

    def bias_sipm_amp(self):
        for amp in ["amp1", "amp2"]:
            amp_config = self.config["scint"][amp]
            if not amp_config["enabled"]:
                continue
            commands = [
                "dactest -v hv 1 0",  # set HV rail to 0V
                "setPin ENQP hi",  # enable charge pump
                f"dactest -v hv 0 {amp_config['qp']}",  # set charge pump voltage
                "enhv enable",  # enable HV rail
                f"dactest -v hv 1 {amp_config['bias']}",  # set HV rail voltage
                "adctest -l 1000 -r 8 hv 1 0",  # readback HV rail voltage
            ]
            self.exec_commands(amp_config["ip_addr"], commands)

    def unbias_sipm_amp(self):
        for amp in ["amp1", "amp2"]:
            amp_config = self.config["scint"][amp]
            if not amp_config["enabled"]:
                continue
            commands = [
                "dactest -v hv 1 0",  # set HV rail to 0V
                "enhv disable",  # disable HV rails
                "setPin ENQP lo"  # enable charge pump
            ]
            self.exec_commands(amp_config["ip_addr"], commands)
