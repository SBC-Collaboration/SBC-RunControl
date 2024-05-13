import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal
import copy


class Config(QObject):
    """
    Class object to load and save run config files
    """
    run_config_saved = Signal()

    def __init__(self, mainwindow, path):
        super().__init__()
        self.main = mainwindow
        self.path = path
        self.config = {}
        self.run_config = {}  # A copy of config for the run
        self.cam_config_saved = False  # flag for syncing
        self.logger = logging.getLogger("rc")
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

        self.logger.debug("Config class initialized.")

    def periodic_task(self):
        pass

    @Slot()
    def load_config(self):
        with open(self.path, "r") as file:
            self.config = json.load(file)

    @Slot()
    def load_config_to_window(self, ui):
        widgets = ui.__dict__

        general_config = self.config["general"]
        ui.config_path_edit.setText(general_config["config_path"])
        ui.log_path_edit.setText(general_config["log_path"])
        ui.data_dir_edit.setText(general_config["data_dir"])
        ui.max_ev_time_box.setValue(general_config["max_ev_time"])
        ui.max_num_ev_box.setValue(general_config["max_num_evs"])

        pressure_config = self.config["general"]["pressure"]
        if pressure_config["mode"] == "random":
            ui.p_random_but.setChecked(True)
        elif pressure_config["mode"] == "cycle":
            ui.p_cycle_but.setChecked(True)
        elif pressure_config["mode"] == "interpolate":
            ui.p_interpolate_but.setChecked(True)
        else:
            self.logger.error("Invalid pressure mode.")
        for i in range(1,7):
            profile = pressure_config[f"profile{i}"]
            widgets[f"pressure{i}_enable"].setChecked(profile["enabled"])
            widgets[f"pressure{i}_set"].setValue(profile["setpoint"])
            widgets[f"pressure{i}_high"].setValue(profile["setpoint_high"])
            widgets[f"pressure{i}_slope"].setValue(profile["slope"])
            widgets[f"pressure{i}_period"].setValue(profile["period"])

        sql_config = self.config["general"]["sql"]
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

        dio_config = self.config["dio"]
        trigger_config = dio_config["trigger"]
        ui.trigger_port_edit.setText(trigger_config["port"])
        ui.trigger_sketch_edit.setText(trigger_config["sketch"])
        ui.trig_reset_pin_box.setValue(trigger_config["reset"])
        ui.trig_or_pin_box.setValue(trigger_config["or"])
        ui.trig_on_time_pin_box.setValue(trigger_config["on_time"])
        ui.trig_heartbeat_pin_box.setValue(trigger_config["heartbeat"])

        trig_in_ports = ["A", "C"]
        trig_ff_ports = ["B", "L"]
        speed = ["fast", "slow"]
        for i in range(1, 17):
            in_port_name = trig_in_ports[(i - 1) // 8] + str((i - 1) % 8)
            in_pin = self.main.arduino_trigger_worker.reverse_port_map[in_port_name]
            ff_port_name = trig_ff_ports[(i - 1) // 8] + str((i - 1) % 8)
            ff_pin = self.main.arduino_trigger_worker.reverse_port_map[ff_port_name]

            conf = trigger_config[f"trig{i}"]
            widgets[f"trig{i}_enabled"].setChecked(conf["enabled"]),
            widgets[f"trig_pin{i}_name_edit"].setText(conf["name"]),
            widgets[f"trig_in_pin{i}_box"].setValue(in_pin)
            widgets[f"trig_ff_pin{i}_box"].setValue(ff_pin)
            widgets[f"trig{i}_compression"].setText(speed[(i - 1) // 8])

        for i in range(1, 14):
            latch_pin = self.main.arduino_trigger_worker.latch_pins[i-1]
            widgets[f"trig_latch_pin{i}_box"].setValue(latch_pin)

        clock_ports = ["C", "L"]
        clock_config = dio_config["clock"]
        ui.clock_port_edit.setText(clock_config["port"])
        ui.clock_sketch_edit.setText(clock_config["sketch"])
        for i in range(1, 17):
            w = f"wave{i}"
            clock_port_name = clock_ports[(i - 1) // 8] + str((i - 1) % 8)
            clock_pin = self.main.arduino_clock_worker.reverse_port_map[clock_port_name]
            config = clock_config[w]
            widgets[f"{w}_enabled"].setChecked(config["enabled"])
            widgets[f"clock_name_{w}"].setText(config["name"])
            widgets[f"clock_pin_{w}"].setValue(clock_pin)
            widgets[f"clock_period_{w}"].setValue(config["period"])
            widgets[f"clock_phase_{w}"].setValue(config["phase"])
            widgets[f"clock_duty_{w}"].setValue(config["duty"])
            widgets[f"clock_polarity_{w}"].setCurrentText("Normal" if config["polarity"] else "Reverse")

        position_config = dio_config["position"]
        ui.position_port_edit.setText(position_config["port"])
        ui.position_sketch_edit.setText(position_config["sketch"])
        ui.position_mac_edit.setText(position_config["mac_addr"])
        ui.position_ip_edit.setText(position_config["ip_addr"])
        ui.position_gateway_edit.setText(position_config["gateway"])
        ui.position_subnet_edit.setText(position_config["subnet"])

        niusb_config = dio_config["niusb"]
        for port in range(3):
            for pin in range(8):
                try:
                    ui.niusb_table.item(port, pin).setText(niusb_config[f"{port}.{pin}"])
                except:
                    pass

        self.logger.info("Configuration loaded from file.")

        # TODO: implement loading and saving for more settings components

    @Slot()
    def apply_config(self, ui):
        widgets = ui.__dict__

        # get mode from radio buttons
        if ui.p_random_but.isChecked():
            mode = "random"
        elif ui.p_cycle_but.isChecked():
            mode = "cycle"
        elif ui.p_interpolate_but.isChecked():
            mode = "interpolate"
        else:
            self.logger.error("No pressure mode selected.")
            mode = ""
        # check at least one profile is enabled
        enabled_profiles = 0

        pressure_config = {
            "mode": mode,
        }
        for i in range(1,7):
            profile = {}
            profile["enabled"] = widgets[f"pressure{i}_enable"].isChecked()
            if profile["enabled"]: enabled_profiles += 1
            profile["setpoint"] = widgets[f"pressure{i}_set"].value()
            profile["setpoint_high"] = widgets[f"pressure{i}_high"].value()
            profile["slope"] = widgets[f"pressure{i}_slope"].value()
            profile["period"] = widgets[f"pressure{i}_period"].value()
            pressure_config[f"profile{i}"] = profile
        if enabled_profiles <= 0:
            self.logger.error("No pressure profile is enabled.")

        # apply general config
        sql_config = {
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
            "pressure": pressure_config,
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

        acous_config = {
            "sample_rate": ui.acous_sample_rate_box.currentText(),
            "pre_trig_len": ui.acous_pre_trig_box.value(),
            "post_trig_len": ui.acous_post_trig_box.value(),
            "trig_timeout": ui.acous_trig_timeout_box.value(),
            "trig_delay": ui.acous_trig_delay_box.value(),
        }

        for i in range(1,9):
            ch_config = {}
            ch = f"ch{i}"
            ch_config["enabled"] = widgets[f"acous_enable_{ch}"].isChecked()
            ch_config["range"] = widgets[f"acous_range_{ch}"].currentText()
            ch_config["offset"] = widgets[f"acous_offset_{ch}"].value()
            ch_config["impedance"] = widgets[f"acous_impedance_{ch}"].currentText()
            ch_config["coupling"] = widgets[f"acous_coupling_{ch}"].currentText()
            ch_config["trig"] = widgets[f"acous_trig_{ch}"].isChecked()
            ch_config["slope"] = widgets[f"acous_slope_{ch}"].currentText()
            ch_config["threshold"] = widgets[f"acous_threshold_{ch}"].value()
            acous_config[ch] = ch_config

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
        for i in range(1, 17):
            w = f"wave{i}"
            clock_config[w] = {
                "enabled": widgets[f"{w}_enabled"].isChecked(),
                "name": widgets[f"clock_name_{w}"].text(),
                "period": widgets[f"clock_period_{w}"].value(),
                "phase": widgets[f"clock_phase_{w}"].value(),
                "duty": widgets[f"clock_duty_{w}"].value(),
                "polarity": widgets[f"clock_polarity_{w}"].currentText() == "Normal"
            }

        trigger_config = {
            "port": ui.trigger_port_edit.text(),
            "sketch": ui.trigger_sketch_edit.text(),
            "reset": ui.trig_reset_pin_box.value(),
            "or": ui.trig_or_pin_box.value(),
            "on_time": ui.trig_on_time_pin_box.value(),
            "heartbeat": ui.trig_heartbeat_pin_box.value(),
        }
        for i in range(1, 17):
            trigger_config[f"trig{i}"] = {
                "enabled": widgets[f"trig{i}_enabled"].isChecked(),
                "name": widgets[f"trig_pin{i}_name_edit"].text(),
                "compression": widgets[f"trig{i}_compression"].text(),
                "in": widgets[f"trig_in_pin{i}_box"].value(),
                "first_fault": widgets[f"trig_ff_pin{i}_box"].value(),
            }

        position_config = {
            "port": ui.position_port_edit.text(),
            "sketch": ui.position_sketch_edit.text(),
            "mac_addr": ui.position_mac_edit.text(),
            "ip_addr": ui.position_ip_edit.text(),
            "gateway": ui.position_gateway_edit.text(),
            "subnet": ui.position_subnet_edit.text(),
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
            "acous": acous_config,
            "cam": cam_config,
            "dio": {"trigger": trigger_config,
                    "clock": clock_config,
                    "position": position_config,
                    "niusb": niusb_config},
        }

        self.logger.info("Configuration applied.")

    @Slot()
    def save_config_from_ui(self, ui, path):
        self.apply_config(ui)
        with open(path, "w") as file:
            json.dump(self.config, file, indent=2)
        self.logger.info("Configuration saved to file.")

    @Slot()
    def save_config(self, path):
        with open(path, "w") as file:
            json.dump(self.config, file, indent=2)
        self.logger.info("Configuration saved to file.")

    @Slot()
    def start_run(self):
        self.run_config = copy.deepcopy(self.config)
        run_json_path = os.path.join(self.main.run_dir, f"{self.main.run_id}.json")
        # save run config file
        with open(run_json_path, "w") as file:
            json.dump(self.run_config, file, indent=2)

        # save arduino json files
        for ino in ["trigger", "clock", "position"]:
            ino_config = self.run_config["dio"][ino]
            json_file = os.path.join(ino_config["sketch"], f"{ino}_config.json")

            # comparing json file with config, and save if they are different
            if os.path.exists(json_file):
                with open(json_file, "r") as file:
                    config_temp = json.load(file)
            else:
                config_temp = {}

            if not ino_config == config_temp:
                with open(json_file, "w") as file:
                    json.dump(ino_config, file, indent=2)

        self.logger.info(f"Configuration saved to file for run {self.main.run_id}.")
        self.run_config_saved.emit()

    @Slot()
    def start_event(self):
        # save camera json files
        for cam in ["cam1", "cam2", "cam3"]:
            cam_config = copy.deepcopy(self.run_config["cam"][cam])
            if not cam_config["enabled"]:
                continue
            cam_config["data_path"] = os.path.join(cam_config["data_path"], self.main.run_id, str(self.main.event_id))
            with open(cam_config["rc_config_path"], "w") as file:
                json.dump(cam_config, file, indent=2)
            self.logger.debug(f"Configuration file saved for {cam}")

        self.cam_config_saved = True

    @Slot()
    def stop_run(self):
        self.run_config = self.config
