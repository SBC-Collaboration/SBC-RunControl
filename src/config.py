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
        self.logger = logging.getLogger("rc")

        self.logger.debug("Config class initialized.")

    def load_config(self):
        with open(self.path, "r") as file:
            self.config = json.load(file)

    def load_config_to_window(self, ui):
        general_config = self.config["general"]
        ui.config_path_edit.setText(general_config["config_path"])
        ui.log_path_edit.setText(general_config["log_path"])
        ui.data_dir_edit.setText(general_config["data_dir"])
        ui.max_ev_time_box.setValue(general_config["max_ev_time"])
        ui.max_num_ev_box.setValue(general_config["max_num_evs"])

        sipm_config = self.config["scint"]["amp"]
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

        caen_g0_config = self.config["scint"]["caen_g0"]
        ui.caen_g0_enable_box.setChecked(caen_g0_config["enabled"])
        ui.caen_g0_thres_box.setValue(caen_g0_config["threshold"])
        ui.caen_g0_trig_mask_0.setChecked(caen_g0_config["trig_mask"][0])
        ui.caen_g0_trig_mask_1.setChecked(caen_g0_config["trig_mask"][1])
        ui.caen_g0_trig_mask_2.setChecked(caen_g0_config["trig_mask"][2])
        ui.caen_g0_trig_mask_3.setChecked(caen_g0_config["trig_mask"][3])
        ui.caen_g0_trig_mask_4.setChecked(caen_g0_config["trig_mask"][4])
        ui.caen_g0_trig_mask_5.setChecked(caen_g0_config["trig_mask"][5])
        ui.caen_g0_trig_mask_6.setChecked(caen_g0_config["trig_mask"][6])
        ui.caen_g0_trig_mask_7.setChecked(caen_g0_config["trig_mask"][7])
        ui.caen_g0_acq_mask_0.setChecked(caen_g0_config["acq_mask"][0])
        ui.caen_g0_acq_mask_1.setChecked(caen_g0_config["acq_mask"][1])
        ui.caen_g0_acq_mask_2.setChecked(caen_g0_config["acq_mask"][2])
        ui.caen_g0_acq_mask_3.setChecked(caen_g0_config["acq_mask"][3])
        ui.caen_g0_acq_mask_4.setChecked(caen_g0_config["acq_mask"][4])
        ui.caen_g0_acq_mask_5.setChecked(caen_g0_config["acq_mask"][5])
        ui.caen_g0_acq_mask_6.setChecked(caen_g0_config["acq_mask"][6])
        ui.caen_g0_acq_mask_7.setChecked(caen_g0_config["acq_mask"][7])
        ui.caen_g0_offset_0.setValue(caen_g0_config["offsets"][0])
        ui.caen_g0_offset_1.setValue(caen_g0_config["offsets"][1])
        ui.caen_g0_offset_2.setValue(caen_g0_config["offsets"][2])
        ui.caen_g0_offset_3.setValue(caen_g0_config["offsets"][3])
        ui.caen_g0_offset_4.setValue(caen_g0_config["offsets"][4])
        ui.caen_g0_offset_5.setValue(caen_g0_config["offsets"][5])
        ui.caen_g0_offset_6.setValue(caen_g0_config["offsets"][6])
        ui.caen_g0_offset_7.setValue(caen_g0_config["offsets"][7])

        acous_config = self.config["acous"]

        cam_config = self.config["cam"]
        cam1_config = cam_config["cam1"]
        ui.cam1_rc_config_path.setText(cam1_config["rc_config_path"])
        ui.cam1_config_path.setText(cam1_config["config_path"])
        ui.cam1_data_path.setText(cam1_config["data_path"])
        ui.cam1_ip_addr.setText(cam1_config["ip_addr"])
        ui.cam1_mode.setValue(cam1_config["mode"])
        ui.cam1_trig_wait.setValue(cam1_config["trig_wait"])
        ui.cam1_exposure.setValue(cam1_config["exposure"])
        ui.cam1_buffer_len.setValue(cam1_config["buffer_len"])
        ui.cam1_post_trig_len.setValue(cam1_config["post_trig"])
        ui.cam1_adc_threshold.setValue(cam1_config["adc_threshold"])
        ui.cam1_pix_threshold.setValue(cam1_config["pix_threshold"])
        ui.cam1_image_format.setCurrentText(cam1_config["image_format"])
        ui.cam1_date_format.setText(cam1_config["date_format"])
        ui.cam1_state_comm_pin.setValue(cam1_config["state_comm_pin"])
        ui.cam1_trig_enbl_pin.setValue(cam1_config["trig_en_pin"])
        ui.cam1_trig_latch_pin.setValue(cam1_config["trig_latch_pin"])
        ui.cam1_state_pin.setValue(cam1_config["state_pin"])
        ui.cam1_trig_pin.setValue(cam1_config["trig_pin"])

        cam2_config = cam_config["cam2"]
        ui.cam2_rc_config_path.setText(cam2_config["rc_config_path"])
        ui.cam2_config_path.setText(cam2_config["config_path"])
        ui.cam2_data_path.setText(cam2_config["data_path"])
        ui.cam2_ip_addr.setText(cam2_config["ip_addr"])
        ui.cam2_mode.setValue(cam2_config["mode"])
        ui.cam2_trig_wait.setValue(cam2_config["trig_wait"])
        ui.cam2_exposure.setValue(cam2_config["exposure"])
        ui.cam2_buffer_len.setValue(cam2_config["buffer_len"])
        ui.cam2_post_trig_len.setValue(cam2_config["post_trig"])
        ui.cam2_adc_threshold.setValue(cam2_config["adc_threshold"])
        ui.cam2_pix_threshold.setValue(cam2_config["pix_threshold"])
        ui.cam2_image_format.setCurrentText(cam2_config["image_format"])
        ui.cam2_date_format.setText(cam2_config["date_format"])
        ui.cam2_state_comm_pin.setValue(cam2_config["state_comm_pin"])
        ui.cam2_trig_enbl_pin.setValue(cam2_config["trig_en_pin"])
        ui.cam2_trig_latch_pin.setValue(cam2_config["trig_latch_pin"])
        ui.cam2_state_pin.setValue(cam2_config["state_pin"])
        ui.cam2_trig_pin.setValue(cam2_config["trig_pin"])

        cam3_config = cam_config["cam3"]
        ui.cam3_rc_config_path.setText(cam3_config["rc_config_path"])
        ui.cam3_config_path.setText(cam3_config["config_path"])
        ui.cam3_data_path.setText(cam3_config["data_path"])
        ui.cam3_ip_addr.setText(cam3_config["ip_addr"])
        ui.cam3_mode.setValue(cam3_config["mode"])
        ui.cam3_trig_wait.setValue(cam3_config["trig_wait"])
        ui.cam3_exposure.setValue(cam3_config["exposure"])
        ui.cam3_buffer_len.setValue(cam3_config["buffer_len"])
        ui.cam3_post_trig_len.setValue(cam3_config["post_trig"])
        ui.cam3_adc_threshold.setValue(cam3_config["adc_threshold"])
        ui.cam3_pix_threshold.setValue(cam3_config["pix_threshold"])
        ui.cam3_image_format.setCurrentText(cam3_config["image_format"])
        ui.cam3_date_format.setText(cam3_config["date_format"])
        ui.cam3_state_comm_pin.setValue(cam3_config["state_comm_pin"])
        ui.cam3_trig_enbl_pin.setValue(cam3_config["trig_en_pin"])
        ui.cam3_trig_latch_pin.setValue(cam3_config["trig_latch_pin"])
        ui.cam3_state_pin.setValue(cam3_config["state_pin"])
        ui.cam3_trig_pin.setValue(cam3_config["trig_pin"])

        arduinos_config = self.config["dio"]["arduinos"]
        ui.trigger_port_edit.setText(arduinos_config["trigger"]["port"])
        ui.trigger_sketch_edit.setText(arduinos_config["trigger"]["sketch"])
        ui.clock_port_edit.setText(arduinos_config["clock"]["port"])
        ui.clock_sketch_edit.setText(arduinos_config["clock"]["sketch"])
        ui.position_port_edit.setText(arduinos_config["position"]["port"])
        ui.position_sketch_edit.setText(arduinos_config["position"]["sketch"])

        self.logger.info("Configuration loaded from file.")

        # TODO: implement loading and saving for more settings components

    def apply_config(self, ui):
        # apply general config
        general_config = {
            "config_path": ui.config_path_edit.text(),
            "log_path": ui.log_path_edit.text(),
            "data_dir": ui.data_dir_edit.text(),
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

        caen_g0_config = {
            "enabled": ui.caen_g0_enable_box.isChecked(),
            "threshold": ui.caen_g0_thres_box.value(),
            "trig_mask": [
                ui.caen_g0_trig_mask_0.isChecked(),
                ui.caen_g0_trig_mask_1.isChecked(),
                ui.caen_g0_trig_mask_2.isChecked(),
                ui.caen_g0_trig_mask_3.isChecked(),
                ui.caen_g0_trig_mask_4.isChecked(),
                ui.caen_g0_trig_mask_5.isChecked(),
                ui.caen_g0_trig_mask_6.isChecked(),
                ui.caen_g0_trig_mask_7.isChecked(),
            ],
            "acq_mask": [
                ui.caen_g0_acq_mask_0.isChecked(),
                ui.caen_g0_acq_mask_1.isChecked(),
                ui.caen_g0_acq_mask_2.isChecked(),
                ui.caen_g0_acq_mask_3.isChecked(),
                ui.caen_g0_acq_mask_4.isChecked(),
                ui.caen_g0_acq_mask_5.isChecked(),
                ui.caen_g0_acq_mask_6.isChecked(),
                ui.caen_g0_acq_mask_7.isChecked(),
            ],
            "offsets": [
                ui.caen_g0_offset_0.value(),
                ui.caen_g0_offset_1.value(),
                ui.caen_g0_offset_2.value(),
                ui.caen_g0_offset_3.value(),
                ui.caen_g0_offset_4.value(),
                ui.caen_g0_offset_5.value(),
                ui.caen_g0_offset_6.value(),
                ui.caen_g0_offset_7.value(),
            ],
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

        cam_config = {
            "cam1": {
                "rc_config_path": ui.cam1_rc_config_path.text(),
                "config_path": ui.cam1_config_path.text(),
                "data_path": ui.cam1_data_path.text(),
                "ip_addr": ui.cam1_ip_addr.text(),
                "mode": ui.cam1_mode.value(),
                "trig_wait": ui.cam1_trig_wait.value(),
                "exposure": ui.cam1_exposure.value(),
                "buffer_len": ui.cam1_buffer_len.value(),
                "post_trig": ui.cam1_post_trig_len.value(),
                "adc_threshold": ui.cam1_adc_threshold.value(),
                "pix_threshold": ui.cam1_pix_threshold.value(),
                "image_format": ui.cam1_image_format.currentText(),
                "date_format": ui.cam1_date_format.text(),
                "state_comm_pin": ui.cam1_state_comm_pin.value(),
                "trig_en_pin": ui.cam1_trig_enbl_pin.value(),
                "trig_latch_pin": ui.cam1_trig_latch_pin.value(),
                "state_pin": ui.cam1_state_pin.value(),
                "trig_pin": ui.cam1_trig_pin.value()
            },
            "cam2": {
                "rc_config_path": ui.cam2_rc_config_path.text(),
                "config_path": ui.cam2_config_path.text(),
                "data_path": ui.cam2_data_path.text(),
                "ip_addr": ui.cam2_ip_addr.text(),
                "mode": ui.cam2_mode.value(),
                "trig_wait": ui.cam2_trig_wait.value(),
                "exposure": ui.cam2_exposure.value(),
                "buffer_len": ui.cam2_buffer_len.value(),
                "post_trig": ui.cam2_post_trig_len.value(),
                "adc_threshold": ui.cam2_adc_threshold.value(),
                "pix_threshold": ui.cam2_pix_threshold.value(),
                "image_format": ui.cam2_image_format.currentText(),
                "date_format": ui.cam2_date_format.text(),
                "state_comm_pin": ui.cam2_state_comm_pin.value(),
                "trig_en_pin": ui.cam2_trig_enbl_pin.value(),
                "trig_latch_pin": ui.cam2_trig_latch_pin.value(),
                "state_pin": ui.cam2_state_pin.value(),
                "trig_pin": ui.cam2_trig_pin.value()
            },
            "cam3": {
                "rc_config_path": ui.cam3_rc_config_path.text(),
                "config_path": ui.cam3_config_path.text(),
                "data_path": ui.cam3_data_path.text(),
                "ip_addr": ui.cam3_ip_addr.text(),
                "mode": ui.cam3_mode.value(),
                "trig_wait": ui.cam3_trig_wait.value(),
                "exposure": ui.cam3_exposure.value(),
                "buffer_len": ui.cam3_buffer_len.value(),
                "post_trig": ui.cam3_post_trig_len.value(),
                "adc_threshold": ui.cam3_adc_threshold.value(),
                "pix_threshold": ui.cam3_pix_threshold.value(),
                "image_format": ui.cam3_image_format.currentText(),
                "date_format": ui.cam3_date_format.text(),
                "state_comm_pin": ui.cam3_state_comm_pin.value(),
                "trig_en_pin": ui.cam3_trig_enbl_pin.value(),
                "trig_latch_pin": ui.cam3_trig_latch_pin.value(),
                "state_pin": ui.cam3_state_pin.value(),
                "trig_pin": ui.cam3_trig_pin.value()
            },
        }

        arduinos_config = {
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
            "scint": {
                "amp": sipm_config,
                "caen": caen_config,
                "caen_g0": caen_g0_config,
            },
            "acous": {"general": acous_general_config, "per_channel": acous_ch_config},
            "cam": cam_config,
            "dio": {"arduinos": arduinos_config},
        }

        self.logger.info("Configuration applied.")

    def save_config_from_ui(self, ui, path):
        self.apply_config(ui)
        with open(path, "w") as file:
            json.dump(self.config, file, indent=2)
        self.logger.info("Configuration saved to file.")

    def save_config(self, path):
        with open(path, "w") as file:
            json.dump(self.config, file, indent=2)
        self.logger.info("Configuration saved to file.")