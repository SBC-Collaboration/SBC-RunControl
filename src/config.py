import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal
import copy
import random


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
        self.run_pressure_profiles = []

        self.logger = logging.getLogger("rc")
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

        self.logger.debug("Config class initialized.")

    def periodic_task(self):
        pass

    def update_dict(self, original, new):
        """
        recursive helper function to update config dictionary with new settings.
        Prevents overwriting keys in the same level that is written.
        """
        for key, value in new.items():
            if isinstance(value, dict) and key in original:
                self.update_dict(original[key], value)
            else:
                original[key] = value

    @Slot()
    def load_config(self):
        with open(self.path, "r") as file:
            self.new_config = json.load(file)

        # update existing dict with new settings
        self.update_dict(self.config, self.new_config)

    @Slot()
    def load_config_from_file(self, path, ui):
        """
        Updates the config dict with new json dict. The new json has to follow the same structure,
        but doesn't need to have all the values
        """
        with open(path, "r") as file:
            self.new_config = json.load(file)

        # update existing dict with new settings
        self.update_dict(self.config, self.new_config)
        self.load_config_to_window(ui)

    @Slot()
    def load_config_to_window(self, ui):
        widgets = ui.__dict__

        # general
        general_config = self.config["general"]
        ui.config_path_edit.setText(general_config["config_path"])
        ui.log_dir_edit.setText(general_config["log_dir"])
        ui.data_dir_edit.setText(general_config["data_dir"])
        ui.max_ev_time_box.setValue(general_config["max_ev_time"])
        ui.max_num_ev_box.setValue(general_config["max_num_evs"])

        # PLC
        plc_config = self.config["plc"]
        ui.plc_enabled_box.setChecked(plc_config["enabled"])
        ui.plc_hostname_edit.setText(plc_config["hostname"])
        ui.plc_modbus_port_box.setValue(plc_config["port"])
        ui.smb_share_edit.setText(plc_config["smb_share"])
        ui.smb_filename_edit.setText(plc_config["smb_filename"])
        ui.pc_trig_timeout_box.setValue(plc_config["trig_timeout"])
        ui.pc_stop_timeout_box.setValue(plc_config["stop_timeout"])
        ui.pc_abort_timeout_box.setValue(plc_config["abort_timeout"])

        # pressure
        pressure_config = self.config["plc"]["pressure"]
        ui.p_enabled_box.setChecked(pressure_config["enabled"])
        if pressure_config["mode"] == "random":
            ui.p_random_but.setChecked(True)
        elif pressure_config["mode"] == "cycle":
            ui.p_cycle_but.setChecked(True)
        else:
            self.logger.error("Invalid pressure mode.")
        for i in range(1,7):
            profile = pressure_config[f"profile{i}"]
            widgets[f"pressure{i}_enable"].setChecked(profile["enabled"])
            widgets[f"pressure{i}_set"].setValue(profile["setpoint"])
            widgets[f"pressure{i}_high"].setValue(profile["setpoint_high"])
            widgets[f"pressure{i}_slope"].setValue(profile["slope"])
            widgets[f"pressure{i}_period"].setValue(profile["period"])
        
        plc_registers = self.config["plc"]["registers"]
        ui.PCYCLE_PSET_box.setValue(plc_registers["PCYCLE_PSET"])
        ui.PCYCLE_EXPTIME_box.setValue(plc_registers["PCYCLE_EXPTIME"])
        ui.PCYCLE_MAXEXPTIME_box.setValue(plc_registers["PCYCLE_MAXEXPTIME"])
        ui.PCYCLE_MAXEQTIME_box.setValue(plc_registers["PCYCLE_MAXEQTIME"])
        ui.PCYCLE_MAXEQPDIFF_box.setValue(plc_registers["PCYCLE_MAXEQPDIFF"])
        ui.PCYCLE_MAXACCTIME_box.setValue(plc_registers["PCYCLE_MAXACCTIME"])
        ui.PCYCLE_MAXACCDPDT_box.setValue(plc_registers["PCYCLE_MAXACCDPDT"])
        ui.PCYCLE_MAXBLEEDTIME_box.setValue(plc_registers["PCYCLE_MAXBLEEDTIME"])
        ui.PCYCLE_MAXBLEEDDPDT_box.setValue(plc_registers["PCYCLE_MAXBLEEDDPDT"])
        ui.PCYCLE_SLOWCOMP_SET_box.setValue(plc_registers["PCYCLE_SLOWCOMP_SET"])
        ui.WRITE_SLOWDAQ_box.setValue(plc_registers["WRITE_SLOWDAQ"])
        ui.PRESSURE_CYCLE_box.setValue(plc_registers["PRESSURE_CYCLE"])
        ui.TS_ADDREM_FF_box.setValue(plc_registers["TS_ADDREM_FF"])
        ui.TS_EMPTY_FF_box.setValue(plc_registers["TS_EMPTY_FF"])
        ui.TS_EMPTYALL_FF_box.setValue(plc_registers["TS_EMPTYALL_FF"])
        ui.SLOWDAQ_FF_box.setValue(plc_registers["SLOWDAQ_FF"])
        ui.PCYCLE_ABORT_FF_box.setValue(plc_registers["PCYCLE_ABORT_FF"])
        ui.PCYCLE_FASTCOMP_FF_box.setValue(plc_registers["PCYCLE_FASTCOMP_FF"])
        ui.PCYCLE_SLOWCOMP_FF_box.setValue(plc_registers["PCYCLE_SLOWCOMP_FF"])
        ui.PCYCLE_CYLEQ_FF_box.setValue(plc_registers["PCYCLE_CYLEQ_FF"])
        ui.PCYCLE_CYLBLEED_FF_box.setValue(plc_registers["PCYCLE_CYLBLEED_FF"])
        ui.PCYCLE_ACCHARGE_FF_box.setValue(plc_registers["PCYCLE_ACCHARGE_FF"])

        # SQL
        sql_config = self.config["sql"]
        ui.sql_enabled_box.setChecked(sql_config["enabled"])
        ui.sql_hostname_edit.setText(sql_config["hostname"])
        ui.sql_port_box.setValue(sql_config["port"])
        ui.sql_user_edit.setText(sql_config["user"])
        ui.sql_database_edit.setText(sql_config["database"])
        ui.sql_run_table_edit.setText(sql_config["run_table"])
        ui.sql_event_table_edit.setText(sql_config["event_table"])

        # SiPM amplifiers
        sipm_amp1_config = self.config["scint"]["amp1"]
        ui.sipm_amp1_enabled_box.setChecked(sipm_amp1_config["enabled"])
        ui.sipm_amp1_ip_addr_edit.setText(sipm_amp1_config["ip_addr"])
        ui.sipm_amp1_bias_box.setValue(sipm_amp1_config["bias"])
        ui.sipm_amp1_qp_box.setValue(sipm_amp1_config["qp"])
        ui.sipm_amp1_iv_enabled_box.setChecked(sipm_amp1_config["iv_enabled"])
        ui.sipm_amp1_iv_data_dir_edit.setText(sipm_amp1_config["iv_data_dir"])
        ui.sipm_amp1_iv_rc_data_dir_edit.setText(sipm_amp1_config["iv_rc_dir"])
        ui.sipm_amp1_iv_interval_box.setValue(sipm_amp1_config["iv_interval"])
        ui.sipm_amp1_iv_start_box.setValue(sipm_amp1_config["iv_start"])
        ui.sipm_amp1_iv_stop_box.setValue(sipm_amp1_config["iv_stop"])
        ui.sipm_amp1_iv_step_box.setValue(sipm_amp1_config["iv_step"])
        for ch in range(1, 16):
            widgets[f"sipm_amp1_ch{ch}_offset"].setValue(sipm_amp1_config["ch_offset"][ch-1])
            widgets[f"sipm_amp1_name_ch{ch}"].setCurrentText(sipm_amp1_config["name"][ch-1])

        sipm_amp2_config = self.config["scint"]["amp2"]
        ui.sipm_amp2_enabled_box.setChecked(sipm_amp2_config["enabled"])
        ui.sipm_amp2_ip_addr_edit.setText(sipm_amp2_config["ip_addr"])
        ui.sipm_amp2_bias_box.setValue(sipm_amp2_config["bias"])
        ui.sipm_amp2_qp_box.setValue(sipm_amp2_config["qp"])
        ui.sipm_amp2_iv_enabled_box.setChecked(sipm_amp2_config["iv_enabled"])
        ui.sipm_amp2_iv_data_dir_edit.setText(sipm_amp2_config["iv_data_dir"])
        ui.sipm_amp2_iv_rc_data_dir_edit.setText(sipm_amp2_config["iv_rc_dir"])
        ui.sipm_amp2_iv_interval_box.setValue(sipm_amp2_config["iv_interval"])
        ui.sipm_amp2_iv_start_box.setValue(sipm_amp2_config["iv_start"])
        ui.sipm_amp2_iv_stop_box.setValue(sipm_amp2_config["iv_stop"])
        ui.sipm_amp2_iv_step_box.setValue(sipm_amp2_config["iv_step"])
        for ch in range(1, 16):
            widgets[f"sipm_amp2_ch{ch}_offset"].setValue(sipm_amp2_config["ch_offset"][ch-1])
            widgets[f"sipm_amp2_name_ch{ch}"].setCurrentText(sipm_amp2_config["name"][ch-1])

        sipm_amp3_config = self.config["scint"]["amp3"]
        ui.sipm_amp3_enabled_box.setChecked(sipm_amp3_config["enabled"])
        ui.sipm_amp3_ip_addr_edit.setText(sipm_amp3_config["ip_addr"])
        ui.sipm_amp3_bias_box.setValue(sipm_amp3_config["bias"])
        ui.sipm_amp3_qp_box.setValue(sipm_amp3_config["qp"])
        ui.sipm_amp3_iv_enabled_box.setChecked(sipm_amp3_config["iv_enabled"])
        ui.sipm_amp3_iv_data_dir_edit.setText(sipm_amp3_config["iv_data_dir"])
        ui.sipm_amp3_iv_rc_data_dir_edit.setText(sipm_amp3_config["iv_rc_dir"])
        ui.sipm_amp3_iv_interval_box.setValue(sipm_amp3_config["iv_interval"])
        ui.sipm_amp3_iv_start_box.setValue(sipm_amp3_config["iv_start"])
        ui.sipm_amp3_iv_stop_box.setValue(sipm_amp3_config["iv_stop"])
        ui.sipm_amp3_iv_step_box.setValue(sipm_amp3_config["iv_step"])
        for ch in range(1, 16):
            widgets[f"sipm_amp3_ch{ch}_offset"].setValue(sipm_amp3_config["ch_offset"][ch-1])
            widgets[f"sipm_amp3_name_ch{ch}"].setCurrentText(sipm_amp3_config["name"][ch-1])

        # CAEN
        caen_config = self.config["caen"]["global"]
        ui.caen_enabled_box.setChecked(caen_config["enabled"])
        ui.caen_data_path_box.setText(caen_config["data_path"])
        ui.caen_model_box.setCurrentText(caen_config["model"])
        ui.caen_link_box.setValue(caen_config["link"])
        ui.caen_conn_box.setCurrentText(caen_config["connection"])
        ui.caen_evs_box.setValue(caen_config["evs_per_read"])
        ui.caen_length_box.setValue(caen_config["rec_length"])
        ui.caen_post_trig_box.setValue(caen_config["post_trig"])
        ui.caen_trigin_gate_box.setChecked(caen_config["trig_in_as_gate"])
        ui.caen_decimation_box.setValue(caen_config["decimation"])
        ui.caen_overlap_box.setChecked(caen_config["overlap_en"])
        ui.caen_mem_full_box.setCurrentText(caen_config["memory_full"])
        ui.caen_counting_box.setCurrentText(caen_config["counting_mode"])
        ui.caen_polarity_box.setCurrentText(caen_config["polarity"])
        ui.caen_majority_box.setValue(caen_config["majority_level"])
        ui.caen_majority_window_box.setValue(caen_config["majority_window"])
        ui.caen_clock_box.setCurrentText(caen_config["clock_source"])
        ui.caen_acq_box.setCurrentText(caen_config["acq_mode"])
        ui.caen_io_box.setCurrentText(caen_config["io_level"])
        ui.caen_ext_trig_box.setCurrentText(caen_config["ext_trig"])
        ui.caen_sw_trig_box.setCurrentText(caen_config["sw_trig"])
        ui.caen_ch_trig_box.setCurrentText(caen_config["ch_trig"])

        for g in range(4):
            gp = f"g{g}"
            gp_config = self.config["caen"][f"group{g}"]
            widgets[f"caen_{gp}_enable_box"].setChecked(gp_config["enabled"])
            widgets[f"caen_{gp}_thres_box"].setValue(gp_config["threshold"])
            widgets[f"caen_{gp}_offset_box"].setValue(gp_config["offset"])
            widgets[f"caen_{gp}_range_box"].setCurrentText(gp_config["range"])
            for ch in range(8):
                widgets[f"caen_{gp}_name_{ch}"].setCurrentText(gp_config["name"][ch])
                widgets[f"caen_{gp}_trig_mask_{ch}"].setChecked(gp_config["trig_mask"][ch])
                widgets[f"caen_{gp}_acq_mask_{ch}"].setChecked(gp_config["acq_mask"][ch])
                widgets[f"caen_{gp}_plot_mask_{ch}"].setChecked(gp_config["plot_mask"][ch])
                widgets[f"caen_{gp}_offset_{ch}"].setValue(gp_config["ch_offset"][ch])

        # acoustics
        acous_config = self.config["acous"]
        # Acquisition settings
        ui.acous_enabled_box.setChecked(acous_config["enabled"])
        ui.acous_data_dir_edit.setText(acous_config["data_dir"])
        ui.acous_driver_path_edit.setText(acous_config["driver_path"])
        ui.acous_mode_box.setCurrentText(acous_config["mode"])
        ui.acous_sample_rate_box.setCurrentText(acous_config["sample_rate"])
        ui.acous_timestamp_mode_box.setCurrentText(acous_config["timestamp_mode"])
        ui.acous_timestamp_clock_box.setCurrentText(acous_config["timestamp_clock"])
        ui.acous_pre_trig_box.setValue(acous_config["pre_trig_len"])
        ui.acous_post_trig_box.setValue(acous_config["post_trig_len"])
        ui.acous_acq_seg_count_box.setValue(acous_config["acq_seg_count"])
        ui.acous_trig_timeout_box.setValue(acous_config["trig_timeout"])
        ui.acous_trig_delay_box.setValue(acous_config["trig_delay"])
        ui.acous_trig_holdoff_box.setValue(acous_config["trig_holdoff"])

        # Application settings
        ui.acous_start_pos_box.setValue(acous_config["start_pos"])
        ui.acous_transfer_len_box.setValue(acous_config["transfer_len"])
        ui.acous_seg_start_box.setValue(acous_config["seg_start"])
        ui.acous_seg_count_box.setValue(acous_config["seg_count"])
        ui.acous_page_size_box.setValue(acous_config["page_size"])
        ui.acous_file_format_box.setCurrentText(acous_config["file_format"])
        ui.acous_file_name_edit.setText(acous_config["file_name"])

        # Channel settings
        for i in range(1,9):
            ch = f"ch{i}"
            ch_config = acous_config[ch]
            widgets[f"acous_name_{ch}"].setText(ch_config["name"])
            widgets[f"acous_range_{ch}"].setCurrentText(ch_config["range"])
            widgets[f"acous_offset_{ch}"].setValue(ch_config["offset"])
            widgets[f"acous_impedance_{ch}"].setCurrentText(ch_config["impedance"])
            widgets[f"acous_coupling_{ch}"].setCurrentText(ch_config["coupling"])
            widgets[f"acous_trig_{ch}"].setChecked(ch_config["trig"])
            widgets[f"acous_polarity_{ch}"].setCurrentText(ch_config["polarity"])
            widgets[f"acous_threshold_{ch}"].setValue(ch_config["threshold"])

        # external trigger settings
        acous_ext_config = acous_config["ext"]
        widgets[f"acous_range_ext"].setCurrentText(acous_ext_config["range"])
        widgets[f"acous_trig_ext"].setChecked(acous_ext_config["trig"])
        widgets[f"acous_polarity_ext"].setCurrentText(acous_ext_config["polarity"])
        widgets[f"acous_threshold_ext"].setValue(acous_ext_config["threshold"])

        # cameras
        cam_config = self.config["cams"]
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
        ui.trig_loop_box.setValue(trigger_config["loop"])
        ui.trig_reset_pin_box.setValue(trigger_config["reset"])
        ui.trig_or_pin_box.setValue(trigger_config["or"])
        ui.trig_on_time_pin_box.setValue(trigger_config["on_time"])
        ui.trig_heartbeat_pin_box.setValue(trigger_config["heartbeat"])
        ui.trig_led_gate_pin_box.setValue(trigger_config["led_gate_pin"])
        ui.trig_led_gate_cycles_box.setValue(trigger_config["led_gate"])

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
        ui.clock_loop_box.setValue(clock_config["loop"])
        for i in range(1, 17):
            w = f"wave{i}"
            clock_port_name = clock_ports[(i - 1) // 8] + str((i - 1) % 8)
            clock_pin = self.main.arduino_clock_worker.reverse_port_map[clock_port_name]
            config = clock_config[w]
            widgets[f"{w}_enabled"].setChecked(config["enabled"])
            widgets[f"clock_name_{w}"].setText(config["name"])
            widgets[f"clock_pin_{w}"].setValue(clock_pin)
            widgets[f"clock_gate_{w}"].setChecked(config["gated"])
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

        general_config = {
            "config_path": ui.config_path_edit.text(),
            "data_dir": ui.data_dir_edit.text(),
            "log_dir": ui.log_dir_edit.text(),
            "max_ev_time": ui.max_ev_time_box.value(),
            "max_num_evs": ui.max_num_ev_box.value(),
        }

        # apply plc config
        plc_config = {
            "enabled": ui.plc_enabled_box.isChecked(),
            "hostname": ui.plc_hostname_edit.text(),
            "port": ui.plc_modbus_port_box.value(),
            "smb_share": ui.smb_share_edit.text(),
            "smb_filename": ui.smb_filename_edit.text(),
            "trig_timeout": ui.pc_trig_timeout_box.value(),
            "stop_timeout": ui.pc_stop_timeout_box.value(),
            "abort_timeout": ui.pc_abort_timeout_box.value(),
        }

        # get mode from radio buttons
        if ui.p_random_but.isChecked():
            mode = "random"
        elif ui.p_cycle_but.isChecked():
            mode = "cycle"
        else:
            self.logger.error("No pressure mode selected.")
            mode = ""

        pressure_config = {
            "enabled": ui.p_enabled_box.isChecked(),
            "mode": mode,
        }

        for i in range(1,7):
            profile = {}
            profile["enabled"] = widgets[f"pressure{i}_enable"].isChecked()
            profile["setpoint"] = widgets[f"pressure{i}_set"].value()
            profile["setpoint_high"] = widgets[f"pressure{i}_high"].value()
            profile["slope"] = widgets[f"pressure{i}_slope"].value()
            profile["period"] = widgets[f"pressure{i}_period"].value()
            pressure_config[f"profile{i}"] = profile
        plc_config["pressure"] = pressure_config

        plc_registers = {
            "PCYCLE_PSET": ui.PCYCLE_PSET_box.value(),
            "PCYCLE_EXPTIME": ui.PCYCLE_EXPTIME_box.value(),
            "PCYCLE_MAXEXPTIME": ui.PCYCLE_MAXEXPTIME_box.value(),
            "PCYCLE_MAXEQTIME": ui.PCYCLE_MAXEQTIME_box.value(),
            "PCYCLE_MAXEQPDIFF": ui.PCYCLE_MAXEQPDIFF_box.value(),
            "PCYCLE_MAXACCTIME": ui.PCYCLE_MAXACCTIME_box.value(),
            "PCYCLE_MAXACCDPDT": ui.PCYCLE_MAXACCDPDT_box.value(),
            "PCYCLE_MAXBLEEDTIME": ui.PCYCLE_MAXBLEEDTIME_box.value(),
            "PCYCLE_MAXBLEEDDPDT": ui.PCYCLE_MAXBLEEDDPDT_box.value(),
            "PCYCLE_SLOWCOMP_SET": ui.PCYCLE_SLOWCOMP_SET_box.value(),
            "WRITE_SLOWDAQ": ui.WRITE_SLOWDAQ_box.value(),
            "PRESSURE_CYCLE": ui.PRESSURE_CYCLE_box.value(),
            "TS_ADDREM_FF": ui.TS_ADDREM_FF_box.value(),
            "TS_EMPTY_FF": ui.TS_EMPTY_FF_box.value(),
            "TS_EMPTYALL_FF": ui.TS_EMPTYALL_FF_box.value(),
            "SLOWDAQ_FF": ui.SLOWDAQ_FF_box.value(),
            "PCYCLE_ABORT_FF": ui.PCYCLE_ABORT_FF_box.value(),
            "PCYCLE_FASTCOMP_FF": ui.PCYCLE_FASTCOMP_FF_box.value(),
            "PCYCLE_SLOWCOMP_FF": ui.PCYCLE_SLOWCOMP_FF_box.value(),
            "PCYCLE_CYLEQ_FF": ui.PCYCLE_CYLEQ_FF_box.value(),
            "PCYCLE_CYLBLEED_FF": ui.PCYCLE_CYLBLEED_FF_box.value(),
            "PCYCLE_ACCHARGE_FF": ui.PCYCLE_ACCHARGE_FF_box.value(),
        }
        plc_config["registers"] = plc_registers

        # apply general config
        sql_config = {
            "enabled": ui.sql_enabled_box.isChecked(),
            "hostname": ui.sql_hostname_edit.text(),
            "port": ui.sql_port_box.value(),
            "user": ui.sql_user_edit.text(),
            "database": ui.sql_database_edit.text(),
            "run_table": ui.sql_run_table_edit.text(),
            "event_table": ui.sql_event_table_edit.text(),
        }

        sipm_amp1_config = {
            "enabled": ui.sipm_amp1_enabled_box.isChecked(),
            "ip_addr": ui.sipm_amp1_ip_addr_edit.text(),
            "bias": ui.sipm_amp1_bias_box.value(),
            "qp": ui.sipm_amp1_qp_box.value(),
            "iv_enabled": ui.sipm_amp1_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp1_iv_data_dir_edit.text(),
            "iv_rc_dir": ui.sipm_amp1_iv_rc_data_dir_edit.text(),
            "iv_interval": ui.sipm_amp1_iv_interval_box.value(),
            "iv_start": ui.sipm_amp1_iv_start_box.value(),
            "iv_stop": ui.sipm_amp1_iv_stop_box.value(),
            "iv_step": ui.sipm_amp1_iv_step_box.value(),
            "ch_offset": [widgets[f"sipm_amp1_ch{ch}_offset"].value() for ch in range(1,16)],
            "name": [widgets[f"sipm_amp1_name_ch{ch}"].currentText() for ch in range(1,16)],
        }

        sipm_amp2_config = {
            "enabled": ui.sipm_amp2_enabled_box.isChecked(),
            "ip_addr": ui.sipm_amp2_ip_addr_edit.text(),
            "bias": ui.sipm_amp2_bias_box.value(),
            "qp": ui.sipm_amp2_qp_box.value(),
            "iv_enabled": ui.sipm_amp2_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp2_iv_data_dir_edit.text(),
            "iv_rc_dir": ui.sipm_amp2_iv_rc_data_dir_edit.text(),
            "iv_interval": ui.sipm_amp2_iv_interval_box.value(),
            "iv_start": ui.sipm_amp2_iv_start_box.value(),
            "iv_stop": ui.sipm_amp2_iv_stop_box.value(),
            "iv_step": ui.sipm_amp2_iv_step_box.value(),
            "ch_offset": [widgets[f"sipm_amp2_ch{ch}_offset"].value() for ch in range(1, 16)],
            "name": [widgets[f"sipm_amp2_name_ch{ch}"].currentText() for ch in range(1,16)],
        }

        sipm_amp3_config = {
            "enabled": ui.sipm_amp3_enabled_box.isChecked(),
            "ip_addr": ui.sipm_amp3_ip_addr_edit.text(),
            "bias": ui.sipm_amp3_bias_box.value(),
            "qp": ui.sipm_amp3_qp_box.value(),
            "iv_enabled": ui.sipm_amp3_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp3_iv_data_dir_edit.text(),
            "iv_rc_dir": ui.sipm_amp3_iv_rc_data_dir_edit.text(),
            "iv_interval": ui.sipm_amp3_iv_interval_box.value(),
            "iv_start": ui.sipm_amp3_iv_start_box.value(),
            "iv_stop": ui.sipm_amp3_iv_stop_box.value(),
            "iv_step": ui.sipm_amp3_iv_step_box.value(),
            "ch_offset": [widgets[f"sipm_amp3_ch{ch}_offset"].value() for ch in range(1, 16)],
            "name": [widgets[f"sipm_amp3_name_ch{ch}"].currentText() for ch in range(1,16)],
        }

        caen_config = {
            "enabled": ui.caen_enabled_box.isChecked(),
            "data_path": ui.caen_data_path_box.text(),
            "model": ui.caen_model_box.currentText(),
            "link": ui.caen_link_box.value(),
            "connection": ui.caen_conn_box.currentText(),
            "evs_per_read": ui.caen_evs_box.value(),
            "rec_length": ui.caen_length_box.value(),
            "post_trig": ui.caen_post_trig_box.value(),
            "trig_in_as_gate": ui.caen_trigin_gate_box.isChecked(),
            "decimation": ui.caen_decimation_box.value(),
            "overlap_en": ui.caen_overlap_box.isChecked(),
            "memory_full": ui.caen_mem_full_box.currentText(),
            "counting_mode": ui.caen_counting_box.currentText(),
            "polarity": ui.caen_polarity_box.currentText(),
            "majority_level": ui.caen_majority_box.value(),
            "majority_window": ui.caen_majority_window_box.value(),
            "clock_source": ui.caen_clock_box.currentText(),
            "acq_mode": ui.caen_acq_box.currentText(),
            "io_level": ui.caen_io_box.currentText(),
            "ext_trig": ui.caen_ext_trig_box.currentText(),
            "sw_trig": ui.caen_sw_trig_box.currentText(),
            "ch_trig": ui.caen_ch_trig_box.currentText(),
        }


        caen_g0_config = {
            "enabled": ui.caen_g0_enable_box.isChecked(),
            "threshold": ui.caen_g0_thres_box.value(),
            "offset": ui.caen_g0_offset_box.value(),
            "range": ui.caen_g0_range_box.currentText(),
            "name": [widgets[f"caen_g0_name_{ch}"].currentText() for ch in range(8)],
            "trig_mask": [widgets[f"caen_g0_trig_mask_{ch}"].isChecked() for ch in range(8)],
            "acq_mask": [widgets[f"caen_g0_acq_mask_{ch}"].isChecked() for ch in range(8)],
            "plot_mask": [widgets[f"caen_g0_plot_mask_{ch}"].isChecked() for ch in range(8)],
            "ch_offset": [widgets[f"caen_g0_offset_{ch}"].value() for ch in range(8)],
        }

        caen_g1_config = {
            "enabled": ui.caen_g1_enable_box.isChecked(),
            "threshold": ui.caen_g1_thres_box.value(),
            "offset": ui.caen_g1_offset_box.value(),
            "range": ui.caen_g1_range_box.currentText(),
            "name": [widgets[f"caen_g1_name_{ch}"].currentText() for ch in range(8)],
            "trig_mask": [widgets[f"caen_g1_trig_mask_{ch}"].isChecked() for ch in range(8)],
            "acq_mask": [widgets[f"caen_g1_acq_mask_{ch}"].isChecked() for ch in range(8)],
            "plot_mask": [widgets[f"caen_g1_plot_mask_{ch}"].isChecked() for ch in range(8)],
            "ch_offset": [widgets[f"caen_g1_offset_{ch}"].value() for ch in range(8)],
        }

        caen_g2_config = {
            "enabled": ui.caen_g2_enable_box.isChecked(),
            "threshold": ui.caen_g2_thres_box.value(),
            "offset": ui.caen_g2_offset_box.value(),
            "range": ui.caen_g2_range_box.currentText(),
            "name": [widgets[f"caen_g2_name_{ch}"].currentText() for ch in range(8)],
            "trig_mask": [widgets[f"caen_g2_trig_mask_{ch}"].isChecked() for ch in range(8)],
            "acq_mask": [widgets[f"caen_g2_acq_mask_{ch}"].isChecked() for ch in range(8)],
            "plot_mask": [widgets[f"caen_g2_plot_mask_{ch}"].isChecked() for ch in range(8)],
            "ch_offset": [widgets[f"caen_g2_offset_{ch}"].value() for ch in range(8)],
        }

        caen_g3_config = {
            "enabled": ui.caen_g3_enable_box.isChecked(),
            "threshold": ui.caen_g3_thres_box.value(),
            "offset": ui.caen_g3_offset_box.value(),
            "range": ui.caen_g3_range_box.currentText(),
            "name": [widgets[f"caen_g3_name_{ch}"].currentText() for ch in range(8)],
            "trig_mask": [widgets[f"caen_g3_trig_mask_{ch}"].isChecked() for ch in range(8)],
            "acq_mask": [widgets[f"caen_g3_acq_mask_{ch}"].isChecked() for ch in range(8)],
            "plot_mask": [widgets[f"caen_g3_plot_mask_{ch}"].isChecked() for ch in range(8)],
            "ch_offset": [widgets[f"caen_g3_offset_{ch}"].value() for ch in range(8)],
        }

        acous_config = {
            "enabled": ui.acous_enabled_box.isChecked(),
            "data_dir": ui.acous_data_dir_edit.text(),
            "driver_path": ui.acous_driver_path_edit.text(),
            "mode": ui.acous_mode_box.currentText(),
            "sample_rate": ui.acous_sample_rate_box.currentText(),
            "timestamp_mode": ui.acous_timestamp_mode_box.currentText(),
            "timestamp_clock": ui.acous_timestamp_clock_box.currentText(),
            "pre_trig_len": ui.acous_pre_trig_box.value(),
            "post_trig_len": ui.acous_post_trig_box.value(),
            "acq_seg_count": ui.acous_acq_seg_count_box.value(),
            "trig_timeout": ui.acous_trig_timeout_box.value(),
            "trig_delay": ui.acous_trig_delay_box.value(),
            "trig_holdoff": ui.acous_trig_holdoff_box.value(),
            "start_pos": ui.acous_start_pos_box.value(),
            "transfer_len": ui.acous_transfer_len_box.value(),
            "seg_start": ui.acous_seg_start_box.value(),
            "seg_count": ui.acous_seg_count_box.value(),
            "page_size": ui.acous_page_size_box.value(),
            "file_format": ui.acous_file_format_box.currentText(),
            "file_name": ui.acous_file_name_edit.text(),
        }

        for i in range(1,9):
            ch_config = {}
            ch = f"ch{i}"
            ch_config["name"] = widgets[f"acous_name_{ch}"].text()
            ch_config["range"] = widgets[f"acous_range_{ch}"].currentText()
            ch_config["offset"] = widgets[f"acous_offset_{ch}"].value()
            ch_config["impedance"] = widgets[f"acous_impedance_{ch}"].currentText()
            ch_config["coupling"] = widgets[f"acous_coupling_{ch}"].currentText()
            ch_config["trig"] = widgets[f"acous_trig_{ch}"].isChecked()
            ch_config["polarity"] = widgets[f"acous_polarity_{ch}"].currentText()
            ch_config["threshold"] = widgets[f"acous_threshold_{ch}"].value()
            acous_config[ch] = ch_config

        acous_config["ext"] = {
            "range": widgets["acous_range_ext"].currentText(),
            "trig": widgets["acous_trig_ext"].isChecked(),
            "polarity": widgets[f"acous_polarity_ext"].currentText(),
            "threshold": widgets[f"acous_threshold_ext"].value(),
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
            "loop": ui.clock_loop_box.value(),
        }
        for i in range(1, 17):
            w = f"wave{i}"
            clock_config[w] = {
                "enabled": widgets[f"{w}_enabled"].isChecked(),
                "name": widgets[f"clock_name_{w}"].text(),
                "gated": widgets[f"clock_gate_{w}"].isChecked(),
                "period": widgets[f"clock_period_{w}"].value(),
                "phase": widgets[f"clock_phase_{w}"].value(),
                "duty": widgets[f"clock_duty_{w}"].value(),
                "polarity": widgets[f"clock_polarity_{w}"].currentText() == "Normal"
            }

        trigger_config = {
            "port": ui.trigger_port_edit.text(),
            "sketch": ui.trigger_sketch_edit.text(),
            "loop": ui.trig_loop_box.value(),
            "reset": ui.trig_reset_pin_box.value(),
            "or": ui.trig_or_pin_box.value(),
            "on_time": ui.trig_on_time_pin_box.value(),
            "heartbeat": ui.trig_heartbeat_pin_box.value(),
            "led_gate_pin": ui.trig_led_gate_pin_box.value(),
            "led_gate": ui.trig_led_gate_cycles_box.value(),
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
            "plc": plc_config,
            "sql": sql_config,
            "scint": {
                "amp1": sipm_amp1_config,
                "amp2": sipm_amp2_config,
                "amp3": sipm_amp3_config,
            },
            "caen": {
                "global": caen_config,
                "group0": caen_g0_config,
                "group1": caen_g1_config,
                "group2": caen_g2_config,
                "group3": caen_g3_config
            },
            "acous": acous_config,
            "cams": cam_config,
            "dio": {"trigger": trigger_config,
                    "clock": clock_config,
                    "position": position_config,
                    "niusb": niusb_config},
        }

        self.logger.info("Configuration applied.")

    @Slot()
    def save_config_from_ui(self, ui, path):
        self.apply_config(ui)
        self.save_config(path)

    @Slot()
    def save_config(self, path):
        with open(path, "w") as file:
            json.dump(self.config, file, indent=2)
        self.logger.info("Configuration saved to file.")

    @Slot()
    def start_run(self):
        # self.apply_config(self.main.settings_window.ui)
        self.run_config = copy.deepcopy(self.config)
        run_json_path = os.path.join(self.main.run_dir, f"rc.json")
        # save run config file
        with open(run_json_path, "w") as file:
            json.dump(self.run_config, file, indent=2)

        # check at least one profile is enabled
        pressure_profiles = self.run_config["plc"]["pressure"]
        self.run_pressure_mode = pressure_profiles["mode"]

        enabled_profiles = 0
        self.run_pressure_profiles = []
        if pressure_profiles["enabled"]:
            for k, v in pressure_profiles.items():
                if ("profile" in k) and v["enabled"]:
                    self.run_pressure_profiles.append(v)

        # save arduino json files
        for ino in ["trigger", "clock", "position"]:
            ino_config = copy.deepcopy(self.run_config["dio"][ino])
            # remove name field in clock config to save space
            if ino=="clock":
                for w in range(1, 17):
                    ino_config[f"wave{w}"].pop("name")
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

        # save camera json files
        for cam in ["cam1", "cam2", "cam3"]:
            cam_config = copy.deepcopy(self.run_config["cams"][cam])
            if not cam_config["enabled"]:
                continue
            with open(cam_config["rc_config_path"], "w") as file:
                json.dump(cam_config, file, indent=2)
            self.logger.debug(f"Configuration file saved for {cam}")

        self.main.niusb_worker.cam_config_mutex.lock()
        self.main.niusb_worker.cam_config_ready = True
        self.main.niusb_worker.cam_config_wait.wakeOne()
        self.main.niusb_worker.cam_config_mutex.unlock()

        self.logger.info(f"Configuration saved to file for run {self.main.run_id}.\n")
        self.run_config_saved.emit()

    @Slot()
    def start_event(self):
        if not self.run_pressure_profiles:
            self.logger.debug("No pressure profiles enabled.")
            self.event_pressure = {
                "setpoint": None, 
                "setpoint_high": None, 
                "slope": None, 
                "period": None
                }
        elif self.run_pressure_mode == "random":
            self.event_pressure = random.choice(self.run_pressure_profiles)
        elif self.run_pressure_mode == "cycle":
            self.event_pressure = self.run_pressure_profiles[0]
            self.run_pressure_profiles.append(self.run_pressure_profiles.pop(0))
        else:
            self.logger.error("No pressure mode selected.")
            self.event_pressure = {}
            return
        self.logger.info(f"Event pressure: Pset: {self.event_pressure["setpoint"]}, "
                         f"Pset_high: {self.event_pressure['setpoint_high']}, "
                         f"Slope: {self.event_pressure['slope']}, "
                         f"Period: {self.event_pressure['period']}")

    @Slot()
    def stop_run(self):
        self.run_config = self.config

        self.cam_config_mutex.lock()
        self.cam_config_ready = False
        self.cam_config_mutex.unlock()
