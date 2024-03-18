import json
import os


class Config:
    """
    Class object to load and save run config files
    """

    def __init__(self, main_window, path):
        self.main_window = main_window
        self.path = path
        self.config = {}

    def load_config(self):
        with open(self.path, "r") as file:
            self.config = json.load(file)

    def load_config_to_window(self, settings_ui):
        self.load_config()

        general_config = self.config["general"]
        settings_ui.config_path_edit.setText(general_config["config_path"])
        settings_ui.log_path_edit.setText(general_config["log_path"])
        settings_ui.data_dir_edit.setText(general_config["data_dir"])

        run_config = self.config["run"]
        settings_ui.max_ev_time_box.setValue(run_config["max_ev_time"])
        settings_ui.max_num_ev_box.setValue(run_config["max_num_evs"])

        # TODO: implement loading and saving for more settings components

    def apply_config(self, settings_ui):
        self.config = {}

        # apply general config
        self.config["general"] = {}
        self.config["general"]["config_path"] = settings_ui.config_path_edit.text()
        self.config["general"]["log_path"] = settings_ui.log_path_edit.text()
        self.config["general"]["data_dir"] = settings_ui.data_dir_edit.text()

        # apply run config
        self.config["run"] = {}
        self.config["run"]["source"] = settings_ui.source_box.currentText()
        self.config["run"]["pressure_setpoint"] = settings_ui.pressure_setpoint_box.value()
        self.config["run"]["max_ev_time"] = settings_ui.max_ev_time_box.value()
        self.config["run"]["max_num_evs"] = settings_ui.max_num_ev_box.value()

        self.config["scint"] = {}
        self.config["scint"]["sipm"] = {}
        self.config["scint"]["sipm"]["ip_addr"] = settings_ui.sipm_ip_addr_edit.text()
        self.config["scint"]["sipm"]["bias"] = settings_ui.sipm_bias_box.value()
        self.config["scint"]["sipm"]["qp"] = settings_ui.sipm_qp_box.value()

        self.config["scint"]["caen"] = {}
        logging.info("Settings applied")

    def save_config(self, settings_ui):
        self.apply_config(settings_ui)
        with open(self.path, "w") as file:
            json.dump(self.config, file, indent=2)
