import json
import os
import logging


class Config:
    """
    Class object to load and save run config files
    """

    def __init__(self, main_window, path):
        self.main_window = main_window
        self.path = path
        self.config = {}
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.StreamHandler())

        self.logger.info("Config class initialized.")

    def load_config(self):
        with open(self.path, "r") as file:
            self.config = json.load(file)

    def load_config_to_window(self, ui):
        self.load_config()

        general_config = self.config["general"]
        ui.config_path_edit.setText(general_config["config_path"])
        ui.log_path_edit.setText(general_config["log_path"])
        ui.data_dir_edit.setText(general_config["data_dir"])

        run_config = self.config["run"]
        ui.source_box.setCurrentText(run_config["source"])
        ui.pressure_setpoint_box.setValue(run_config["pressure_setpoint"])
        ui.max_ev_time_box.setValue(run_config["max_ev_time"])
        ui.max_num_ev_box.setValue(run_config["max_num_evs"])

        sipm_config = self.config["scint"]["sipm"]
        ui.sipm_ip_addr_edit.setText(sipm_config["ip_addr"])
        ui.sipm_bias_box.setValue(sipm_config["bias"])
        ui.sipm_qp_box.setValue(sipm_config["qp"])

        dio_general_config = self.config["dio"]["general"]
        ui.trigger_port_edit.setText(dio_general_config["trigger"]["port"])
        ui.trigger_sketch_edit.setText(dio_general_config["trigger"]["sketch"])
        ui.clock_port_edit.setText(dio_general_config["clock"]["port"])
        ui.clock_sketch_edit.setText(dio_general_config["clock"]["sketch"])
        ui.position_port_edit.setText(dio_general_config["position"]["port"])
        ui.position_sketch_edit.setText(dio_general_config["position"]["sketch"])

        self.logger.info("Configuration loaded from file.")

        # TODO: implement loading and saving for more settings components

    def apply_config(self, ui):
        # apply general config
        general_config = {"config_path": ui.config_path_edit.text(),
                          "log_path": ui.log_path_edit.text(),
                          "data_dir": ui.data_dir_edit.text()}

        # apply run config
        run_config = {"source": ui.source_box.currentText(),
                      "pressure_setpoint": ui.pressure_setpoint_box.value(),
                      "max_ev_time": ui.max_ev_time_box.value(),
                      "max_num_evs": ui.max_num_ev_box.value()}

        sipm_config = {"ip_addr": ui.sipm_ip_addr_edit.text(),
                       "bias": ui.sipm_bias_box.value(),
                       "qp": ui.sipm_qp_box.value()}

        caen_config = {}

        dio_general_config = {"trigger": {"port": ui.trigger_port_edit.text(),
                                          "sketch": ui.trigger_sketch_edit.text()},
                              "clock": {"port": ui.clock_port_edit.text(),
                                        "sketch": ui.clock_sketch_edit.text()},
                              "position": {"port": ui.position_port_edit.text(),
                                           "sketch": ui.position_sketch_edit.text()}}

        self.config = {"general": general_config,
                       "run": run_config,
                       "scint": {"sipm": sipm_config,
                                 "caen": caen_config},
                       "dio": {"general": dio_general_config}}

        self.logger.info("Configuration applied.")

    def save_config(self, ui):
        self.apply_config(ui)
        with open(self.path, "w") as file:
            json.dump(self.config, file, indent=2)
        self.logger.info("Configuration saved to file.")
