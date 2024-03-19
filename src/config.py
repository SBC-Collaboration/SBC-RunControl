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

        caen_config = self.config["scint"]["caen"]
        ui.caen_model_box.setCurrentText(caen_config["model"])
        ui.caen_port_box.setValue(caen_config["port"])
        ui.caen_conn_box.setCurrentText(caen_config["connection"])
        ui.caen_evs_box.setValue(caen_config["evs_per_read"])
        ui.caen_length_box.setValue(caen_config["rec_length"])
        ui.caen_post_trig_box.setValue(caen_config["post_trig"])
        ui.caen_trigin_box.setChecked(caen_config["trig_in"])
        ui.caen_decimation_box.setValue(caen_config["decimation"])
        ui.caen_overlap_box.setChecked(caen_config["overlap"])
        ui.caen_polarity_box.setCurrentText(caen_config["polarity"])
        ui.caen_io_box.setCurrentText(caen_config["io_level"])
        ui.caen_ext_trig_box.setCurrentText(caen_config["ext_trig"])
        ui.caen_sw_trig_box.setCurrentText(caen_config["sw_trig"])

        acous_config = self.config["acous"]

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
        general_config = {
            "config_path": ui.config_path_edit.text(),
            "log_path": ui.log_path_edit.text(),
            "data_dir": ui.data_dir_edit.text(),
        }

        # apply run config
        run_config = {
            "source": ui.source_box.currentText(),
            "pressure_setpoint": ui.pressure_setpoint_box.value(),
            "max_ev_time": ui.max_ev_time_box.value(),
            "max_num_evs": ui.max_num_ev_box.value(),
        }

        sipm_config = {
            "ip_addr": ui.sipm_ip_addr_edit.text(),
            "bias": ui.sipm_bias_box.value(),
            "qp": ui.sipm_qp_box.value(),
        }

        caen_config = {
            "model": ui.caen_model_box.currentText(),
            "port": ui.caen_port_box.value(),
            "connection": ui.caen_conn_box.currentText(),
            "evs_per_read": ui.caen_evs_box.value(),
            "rec_length": ui.caen_length_box.value(),
            "post_trig": ui.caen_post_trig_box.value(),
            "trig_in": ui.caen_trigin_box.isChecked(),
            "decimation": ui.caen_decimation_box.value(),
            "overlap": ui.caen_overlap_box.isChecked(),
            "polarity": ui.caen_polarity_box.currentText(),
            "io_level": ui.caen_io_box.currentText(),
            "ext_trig": ui.caen_ext_trig_box.currentText(),
            "sw_trig": ui.caen_sw_trig_box.currentText(),
        }

        acous_general_config = {
            "sample_rate": ui.acous_sample_rate_box.currentText(),
            "pre_trig_len": ui.acous_pre_trig_box.value(),
            "post_trig_len": ui.acous_post_trig_box.value(),
            "trig_timeout": ui.acous_trig_timeout_box.value(),
            "trig_delay": ui.acous_trig_delay_box.value(),
        }

        acous_ch_config = {
            "ch1": {
                "enabled": ui.acous_enable_ch1.isChecked(),
                "range": ui.acous_range_ch1.value(),
                "offset": ui.acous_dc_offset_ch1.value(),
                "trig": ui.acous_trig_ch1.isChecked(),
                "polarity": ui.acous_polarity_ch1.currentText(),
                "threshold": ui.acous_threshold_ch1.value(),
            },
            "ch2": {
                "enabled": ui.acous_enable_ch2.isChecked(),
                "range": ui.acous_range_ch2.value(),
                "offset": ui.acous_dc_offset_ch2.value(),
                "trig": ui.acous_trig_ch2.isChecked(),
                "polarity": ui.acous_polarity_ch2.currentText(),
                "threshold": ui.acous_threshold_ch2.value(),
            },
            "ch3": {
                "enabled": ui.acous_enable_ch3.isChecked(),
                "range": ui.acous_range_ch3.value(),
                "offset": ui.acous_dc_offset_ch3.value(),
                "trig": ui.acous_trig_ch3.isChecked(),
                "polarity": ui.acous_polarity_ch3.currentText(),
                "threshold": ui.acous_threshold_ch3.value(),
            },
            "ch4": {
                "enabled": ui.acous_enable_ch4.isChecked(),
                "range": ui.acous_range_ch4.value(),
                "offset": ui.acous_dc_offset_ch4.value(),
                "trig": ui.acous_trig_ch4.isChecked(),
                "polarity": ui.acous_polarity_ch4.currentText(),
                "threshold": ui.acous_threshold_ch4.value(),
            },
            "ch5": {
                "enabled": ui.acous_enable_ch5.isChecked(),
                "range": ui.acous_range_ch5.value(),
                "offset": ui.acous_dc_offset_ch5.value(),
                "trig": ui.acous_trig_ch5.isChecked(),
                "polarity": ui.acous_polarity_ch5.currentText(),
                "threshold": ui.acous_threshold_ch5.value(),
            },
            "ch6": {
                "enabled": ui.acous_enable_ch6.isChecked(),
                "range": ui.acous_range_ch6.value(),
                "offset": ui.acous_dc_offset_ch6.value(),
                "trig": ui.acous_trig_ch6.isChecked(),
                "polarity": ui.acous_polarity_ch6.currentText(),
                "threshold": ui.acous_threshold_ch6.value(),
            },
            "ch7": {
                "enabled": ui.acous_enable_ch7.isChecked(),
                "range": ui.acous_range_ch7.value(),
                "offset": ui.acous_dc_offset_ch7.value(),
                "trig": ui.acous_trig_ch7.isChecked(),
                "polarity": ui.acous_polarity_ch7.currentText(),
                "threshold": ui.acous_threshold_ch7.value(),
            },
            "ch8": {
                "enabled": ui.acous_enable_ch8.isChecked(),
                "range": ui.acous_range_ch8.value(),
                "offset": ui.acous_dc_offset_ch8.value(),
                "trig": ui.acous_trig_ch8.isChecked(),
                "polarity": ui.acous_polarity_ch8.currentText(),
                "threshold": ui.acous_threshold_ch8.value(),
            },
        }

        dio_general_config = {
            "trigger": {
                "port": ui.trigger_port_edit.text(),
                "sketch": ui.trigger_sketch_edit.text(),
            },
            "clock": {
                "port": ui.clock_port_edit.text(),
                "sketch": ui.clock_sketch_edit.text(),
            },
            "position": {
                "port": ui.position_port_edit.text(),
                "sketch": ui.position_sketch_edit.text(),
            },
        }

        self.config = {
            "general": general_config,
            "run": run_config,
            "scint": {"sipm": sipm_config, "caen": caen_config},
            "acous": {"general": acous_general_config, "per_channel": acous_ch_config},
            "dio": {"general": dio_general_config},
        }

        self.logger.info("Configuration applied.")

    def save_config(self, ui):
        self.apply_config(ui)
        with open(self.path, "w") as file:
            json.dump(self.config, file, indent=2)
        self.logger.info("Configuration saved to file.")
