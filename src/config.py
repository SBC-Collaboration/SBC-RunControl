import json
import os
import logging


class Config:
    """
    Class object to load and save run config files
    """

    def __init__(self, mainwindow, path):
        self.main = mainwindow
        self.path = path
        self.config = {}
        self.logger = logging.getLogger("rc")

        self.logger.debug("Config class initialized.")

    def load_config(self):
        with open(self.path, "r") as file:
            self.config = json.load(file)

    def load_config_to_window(self, ui):
        widgets = ui.__dict__

        general_config = self.config["general"]
        ui.config_path_edit.setText(general_config["config_path"])
        ui.log_path_edit.setText(general_config["log_path"])
        ui.data_dir_edit.setText(general_config["data_dir"])
        ui.max_ev_time_box.setValue(general_config["max_ev_time"])
        ui.max_num_ev_box.setValue(general_config["max_num_evs"])

        sql_config = self.config["general"]["sql"]
        ui.sql_ssh_host_edit.setText(sql_config["ssh_host"])
        ui.sql_ssh_port_box.setValue(sql_config["ssh_port"])
        ui.sql_ssh_user_edit.setText(sql_config["ssh_user"])
        ui.sql_ssh_pkey_edit.setText(sql_config["ssh_pkey"])
        ui.sql_hostname_edit.setText(sql_config["hostname"])
        ui.sql_port_box.setValue(sql_config["port"])
        ui.sql_user_edit.setText(sql_config["user"])
        ui.sql_token_edit.setText(sql_config["token"])
        ui.sql_database_edit.setText(sql_config["database"])
        ui.sql_run_table_edit.setText(sql_config["run_table"])
        ui.sql_event_table_edit.setText(sql_config["event_table"])

        sipm_amp1_config = self.config["scint"]["amp1"]
        ui.sipm_amp1_enabled_box.setChecked(sipm_amp1_config["enabled"])
        ui.sipm_amp1_ip_addr_edit.setText(sipm_amp1_config["ip_addr"])
        ui.sipm_amp1_bias_box.setValue(sipm_amp1_config["bias"])
        ui.sipm_amp1_qp_box.setValue(sipm_amp1_config["qp"])
        ui.sipm_amp1_iv_enabled_box.setChecked(sipm_amp1_config["iv_enabled"])
        ui.sipm_amp1_iv_data_dir_edit.setText(sipm_amp1_config["iv_data_dir"])
        ui.sipm_amp1_iv_start_box.setValue(sipm_amp1_config["iv_start"])
        ui.sipm_amp1_iv_stop_box.setValue(sipm_amp1_config["iv_stop"])
        ui.sipm_amp1_iv_step_box.setValue(sipm_amp1_config["iv_step"])

        sipm_amp2_config = self.config["scint"]["amp2"]
        ui.sipm_amp2_enabled_box.setChecked(sipm_amp2_config["enabled"])
        ui.sipm_amp2_ip_addr_edit.setText(sipm_amp2_config["ip_addr"])
        ui.sipm_amp2_bias_box.setValue(sipm_amp2_config["bias"])
        ui.sipm_amp2_qp_box.setValue(sipm_amp2_config["qp"])
        ui.sipm_amp2_iv_enabled_box.setChecked(sipm_amp2_config["iv_enabled"])
        ui.sipm_amp2_iv_data_dir_edit.setText(sipm_amp2_config["iv_data_dir"])
        ui.sipm_amp2_iv_start_box.setValue(sipm_amp2_config["iv_start"])
        ui.sipm_amp2_iv_stop_box.setValue(sipm_amp2_config["iv_stop"])
        ui.sipm_amp2_iv_step_box.setValue(sipm_amp2_config["iv_step"])

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
        for ch in range(8):
            widgets[f"caen_g0_trig_mask_{ch}"].setChecked(caen_g0_config["trig_mask"][ch])
            widgets[f"caen_g0_acq_mask_{ch}"].setChecked(caen_g0_config["acq_mask"][ch])
            widgets[f"caen_g0_offset_{ch}"].setValue(caen_g0_config["offsets"][ch])

        acous_config = self.config["acous"]

        cam_config = self.config["cam"]
        for cam in ["cam1", "cam2", "cam3"]:
            config = cam_config[cam]
            widgets[f"{cam}_enabled_box"].setChecked(config["enabled"])
            widgets[f"{cam}_rc_config_path"].setText(config["rc_config_path"])
            widgets[f"{cam}_config_path"].setText(config["config_path"])
            widgets[f"{cam}_data_path"].setText(config["data_path"])
            widgets[f"{cam}_ip_addr"].setText(config["ip_addr"])
            widgets[f"{cam}_mode"].setValue(config["mode"])
            widgets[f"{cam}_trig_wait"].setValue(config["trig_wait"])
            widgets[f"{cam}_exposure"].setValue(config["exposure"])
            widgets[f"{cam}_buffer_len"].setValue(config["buffer_len"])
            widgets[f"{cam}_post_trig_len"].setValue(config["post_trig"])
            widgets[f"{cam}_adc_threshold"].setValue(config["adc_threshold"])
            widgets[f"{cam}_pix_threshold"].setValue(config["pix_threshold"])
            widgets[f"{cam}_image_format"].setCurrentText(config["image_format"])
            widgets[f"{cam}_date_format"].setText(config["date_format"])
            widgets[f"{cam}_state_comm_pin"].setValue(config["state_comm_pin"])
            widgets[f"{cam}_trig_enbl_pin"].setValue(config["trig_en_pin"])
            widgets[f"{cam}_trig_latch_pin"].setValue(config["trig_latch_pin"])
            widgets[f"{cam}_state_pin"].setValue(config["state_pin"])
            widgets[f"{cam}_trig_pin"].setValue(config["trig_pin"])

        arduinos_config = self.config["dio"]["arduinos"]
        trigger_config = arduinos_config["trigger"]
        ui.trigger_port_edit.setText(trigger_config["port"])
        ui.trigger_sketch_edit.setText(trigger_config["sketch"])

        clock_config = arduinos_config["clock"]
        ui.clock_port_edit.setText(clock_config["port"])
        ui.clock_sketch_edit.setText(clock_config["sketch"])
        for w in [f"wave{i}" for i in range(1,17)]:
            config = clock_config[w]
            widgets[f"{w}_enabled"].setChecked(config["enabled"])
            widgets[f"clock_name_{w}"].setText(config["name"])
            widgets[f"clock_period_{w}"].setValue(config["period"])
            widgets[f"clock_phase_{w}"].setValue(config["phase"])
            widgets[f"clock_duty_{w}"].setValue(config["duty"])
            widgets[f"clock_polarity_{w}"].setCurrentText("Normal" if config["polarity"] else "Reverse")

        position_config = arduinos_config["position"]
        ui.position_port_edit.setText(position_config["port"])
        ui.position_sketch_edit.setText(position_config["sketch"])

        niusb_config = self.config["dio"]["niusb"]
        for port in range(3):
            for pin in range(8):
                try:
                    ui.niusb_table.item(port, pin).setText(niusb_config[f"{port}.{pin}"])
                except:
                    pass

        self.logger.info("Configuration loaded from file.")

        # TODO: implement loading and saving for more settings components

    def apply_config(self, ui):
        widgets = ui.__dict__

        # apply general config
        sql_config = {
            "ssh_host": ui.sql_ssh_host_edit.text(),
            "ssh_port": ui.sql_ssh_port_box.value(),
            "ssh_user": ui.sql_ssh_user_edit.text(),
            "ssh_pkey": ui.sql_ssh_pkey_edit.text(),
            "hostname": ui.sql_hostname_edit.text(),
            "port": ui.sql_port_box.value(),
            "user": ui.sql_user_edit.text(),
            "token": ui.sql_token_edit.text(),
            "database": ui.sql_database_edit.text(),
            "run_table": ui.sql_run_table_edit.text(),
            "event_table": ui.sql_event_table_edit.text(),
        }

        general_config = {
            "config_path": ui.config_path_edit.text(),
            "log_path": ui.log_path_edit.text(),
            "data_dir": ui.data_dir_edit.text(),
            "max_ev_time": ui.max_ev_time_box.value(),
            "max_num_evs": ui.max_num_ev_box.value(),
            "sql": sql_config
        }

        sipm_amp1_config = {
            "enabled": ui.sipm_amp1_enabled_box.isChecked(),
            "ip_addr": ui.sipm_amp1_ip_addr_edit.text(),
            "bias": ui.sipm_amp1_bias_box.value(),
            "qp": ui.sipm_amp1_qp_box.value(),
            "iv_enabled": ui.sipm_amp1_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp1_iv_data_dir_edit.text(),
            "iv_start": ui.sipm_amp1_iv_start_box.value(),
            "iv_stop": ui.sipm_amp1_iv_stop_box.value(),
            "iv_step": ui.sipm_amp1_iv_step_box.value(),
        }

        sipm_amp2_config = {
            "enabled": ui.sipm_amp2_enabled_box.isChecked(),
            "ip_addr": ui.sipm_amp2_ip_addr_edit.text(),
            "bias": ui.sipm_amp2_bias_box.value(),
            "qp": ui.sipm_amp2_qp_box.value(),
            "iv_enabled": ui.sipm_amp2_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp2_iv_data_dir_edit.text(),
            "iv_start": ui.sipm_amp2_iv_start_box.value(),
            "iv_stop": ui.sipm_amp2_iv_stop_box.value(),
            "iv_step": ui.sipm_amp2_iv_step_box.value(),
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
            "trig_mask": [widgets[f"caen_g0_trig_mask_{ch}"].isChecked() for ch in range(8)],
            "acq_mask": [widgets[f"caen_g0_acq_mask_{ch}"].isChecked() for ch in range(8)],
            "offsets": [widgets[f"caen_g0_offset_{ch}"].value() for ch in range(8)],
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

        cam_config = {}
        for cam in ["cam1", "cam2", "cam3"]:
            cam_config[f"{cam}"] = {
                "enabled": widgets[f"{cam}_enabled_box"].isChecked(),
                "rc_config_path": widgets[f"{cam}_rc_config_path"].text(),
                "config_path": widgets[f"{cam}_config_path"].text(),
                "data_path": widgets[f"{cam}_data_path"].text(),
                "ip_addr": widgets[f"{cam}_ip_addr"].text(),
                "mode": widgets[f"{cam}_mode"].value(),
                "trig_wait": widgets[f"{cam}_trig_wait"].value(),
                "exposure": widgets[f"{cam}_exposure"].value(),
                "buffer_len": widgets[f"{cam}_buffer_len"].value(),
                "post_trig": widgets[f"{cam}_post_trig_len"].value(),
                "adc_threshold": widgets[f"{cam}_adc_threshold"].value(),
                "pix_threshold": widgets[f"{cam}_pix_threshold"].value(),
                "image_format": widgets[f"{cam}_image_format"].currentText(),
                "date_format": widgets[f"{cam}_date_format"].text(),
                "state_comm_pin": widgets[f"{cam}_state_comm_pin"].value(),
                "trig_en_pin": widgets[f"{cam}_trig_enbl_pin"].value(),
                "trig_latch_pin": widgets[f"{cam}_trig_latch_pin"].value(),
                "state_pin": widgets[f"{cam}_state_pin"].value(),
                "trig_pin": widgets[f"{cam}_trig_pin"].value(),
            }

        clock_config = {
            "port": ui.clock_port_edit.text(),
            "sketch": ui.clock_sketch_edit.text(),
        }
        for w in [f"wave{i}" for i in range(1,17)]:
            clock_config[w] = {
                "enabled": widgets[f"{w}_enabled"].isChecked(),
                "name": widgets[f"clock_name_{w}"].text(),
                "period": widgets[f"clock_period_{w}"].value(),
                "phase": widgets[f"clock_phase_{w}"].value(),
                "duty": widgets[f"clock_duty_{w}"].value(),
                "polarity": widgets[f"clock_polarity_{w}"].currentText() == "Normal"
            }

        arduinos_config = {
            "trigger": {
                "port": ui.trigger_port_edit.text(),
                "sketch": ui.trigger_sketch_edit.text(),
            },
            "clock": clock_config,
            "position": {
                "port": ui.position_port_edit.text(),
                "sketch": ui.position_sketch_edit.text(),
            },
        }

        niusb_config = {}
        for port in range(3):
            for pin in range(8):
                niusb_config[f"{port}.{pin}"] = ui.niusb_table.item(port, pin).text()

        self.config = {
            "general": general_config,
            "scint": {
                "amp1": sipm_amp1_config,
                "amp2": sipm_amp2_config,
                "caen": caen_config,
                "caen_g0": caen_g0_config,
            },
            "acous": {"general": acous_general_config, "per_channel": acous_ch_config},
            "cam": cam_config,
            "dio": {"arduinos": arduinos_config, "niusb": niusb_config},
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
