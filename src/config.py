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

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.path = os.path.join(os.path.expanduser("~"), ".config", "runcontrol", "config.json")
        self.config = {}
        self.run_config = {}  # A copy of config for the run
        self.run_pressure_profiles = []
        self.load_config()
        self.run_config = copy.deepcopy(self.config)

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
        # check if the config file exists, if not, copy the template
        if not os.path.isfile(self.path):
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            self.logger.info(f"Config file not found. Created a new one at {self.path}")
            self.new_config = {}
        else:
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
        self.load_config()
        self.load_config_to_window(ui)
    
    @Slot()
    def load_config_to_mainwindow(self):
        main_ui = self.main.ui
        config = self.config["general"]
        main_ui.autorun_box.setChecked(config["autorun"])
        main_ui.source_box.setCurrentText(config["source"])
        main_ui.source_location_box.setCurrentText(config["source_location"])


    @Slot()
    def load_config_to_window(self, ui):
        # settings window
        widgets = ui.__dict__

        # general
        general_config = self.config["general"]
        ui.config_path_edit.setText(general_config.get("config_path", ""))
        ui.log_dir_edit.setText(general_config.get("log_dir", ""))
        ui.data_dir_edit.setText(general_config.get("data_dir", ""))
        ui.writer_enabled_box.setChecked(general_config.get("writer_enabled", False))
        ui.max_ev_time_box.setValue(general_config.get("max_ev_time", 0))
        ui.max_num_ev_box.setValue(general_config.get("max_num_evs", 0))

        # PLC
        plc_config = self.config["plc"]
        ui.plc_enabled_box.setChecked(plc_config.get("enabled", False))
        ui.plc_hostname_edit.setText(plc_config.get("hostname", ""))
        ui.plc_modbus_port_box.setValue(plc_config.get("port", 0))
        ui.smb_share_edit.setText(plc_config.get("smb_share", ""))
        ui.smb_filename_edit.setText(plc_config.get("smb_filename", ""))
        ui.pc_trig_timeout_box.setValue(plc_config.get("trig_timeout", 0))
        ui.pc_stop_timeout_box.setValue(plc_config.get("stop_timeout", 0))
        ui.pc_abort_timeout_box.setValue(plc_config.get("abort_timeout", 0))
        ui.led1_control_box.setValue(plc_config.get("led1_control", 0))
        ui.led2_control_box.setValue(plc_config.get("led2_control", 0))
        ui.led3_control_box.setValue(plc_config.get("led3_control", 0))
        ui.led_control_max_box.setValue(plc_config.get("led_control_max", 0))

        # pressure
        pressure_config = self.config["plc"]["pressure"]
        ui.p_mode_box.setCurrentText(pressure_config.get("mode", ""))
        for i in range(1,7):
            profile = pressure_config[f"profile{i}"]
            widgets[f"pressure{i}_enable"].setChecked(profile.get("enabled", False))
            widgets[f"pressure{i}_set"].setValue(profile.get("setpoint", 0))
            widgets[f"pressure{i}_high"].setValue(profile.get("setpoint_high", 0))
            widgets[f"pressure{i}_slope"].setValue(profile.get("slope", 0))
            widgets[f"pressure{i}_period"].setValue(profile.get("period", 0))

        plc_registers = self.config["plc"]["registers"]
        ui.PCYCLE_PSET_box.setValue(plc_registers.get("PCYCLE_PSET", 0))
        ui.PCYCLE_EXPTIME_box.setValue(plc_registers.get("PCYCLE_EXPTIME", 0))
        ui.PCYCLE_MAXEXPTIME_box.setValue(plc_registers.get("PCYCLE_MAXEXPTIME", 0))
        ui.PCYCLE_MAXEQTIME_box.setValue(plc_registers.get("PCYCLE_MAXEQTIME", 0))
        ui.PCYCLE_MAXEQPDIFF_box.setValue(plc_registers.get("PCYCLE_MAXEQPDIFF", 0))
        ui.PCYCLE_MAXACCTIME_box.setValue(plc_registers.get("PCYCLE_MAXACCTIME", 0))
        ui.PCYCLE_MAXACCDPDT_box.setValue(plc_registers.get("PCYCLE_MAXACCDPDT", 0))
        ui.PCYCLE_MAXBLEEDTIME_box.setValue(plc_registers.get("PCYCLE_MAXBLEEDTIME", 0))
        ui.PCYCLE_MAXBLEEDDPDT_box.setValue(plc_registers.get("PCYCLE_MAXBLEEDDPDT", 0))
        ui.PCYCLE_SLOWCOMP_SET_box.setValue(plc_registers.get("PCYCLE_SLOWCOMP_SET", 0))
        ui.LED1_OUT_box.setValue(plc_registers.get("LED1_OUT", 0))
        ui.LED2_OUT_box.setValue(plc_registers.get("LED2_OUT", 0))
        ui.LED3_OUT_box.setValue(plc_registers.get("LED3_OUT", 0))
        ui.LED_MAX_box.setValue(plc_registers.get("LED_MAX", 0))
        ui.WRITE_SLOWDAQ_box.setValue(plc_registers.get("WRITE_SLOWDAQ", 0))
        ui.PRESSURE_CYCLE_box.setValue(plc_registers.get("PRESSURE_CYCLE", 0))
        ui.TS_ADDREM_FF_box.setValue(plc_registers.get("TS_ADDREM_FF", 0))
        ui.TS_EMPTY_FF_box.setValue(plc_registers.get("TS_EMPTY_FF", 0))
        ui.TS_EMPTYALL_FF_box.setValue(plc_registers.get("TS_EMPTYALL_FF", 0))
        ui.SLOWDAQ_FF_box.setValue(plc_registers.get("SLOWDAQ_FF", 0))
        ui.PCYCLE_ABORT_FF_box.setValue(plc_registers.get("PCYCLE_ABORT_FF", 0))
        ui.PCYCLE_FASTCOMP_FF_box.setValue(plc_registers.get("PCYCLE_FASTCOMP_FF", 0))
        ui.PCYCLE_SLOWCOMP_FF_box.setValue(plc_registers.get("PCYCLE_SLOWCOMP_FF", 0))
        ui.PCYCLE_CYLEQ_FF_box.setValue(plc_registers.get("PCYCLE_CYLEQ_FF", 0))
        ui.PCYCLE_CYLBLEED_FF_box.setValue(plc_registers.get("PCYCLE_CYLBLEED_FF", 0))
        ui.PCYCLE_ACCHARGE_FF_box.setValue(plc_registers.get("PCYCLE_ACCHARGE_FF", 0))

        # SQL
        sql_config = self.config["sql"]
        ui.sql_enabled_box.setChecked(sql_config.get("enabled", False))
        ui.sql_hostname_edit.setText(sql_config.get("hostname", ""))
        ui.sql_port_box.setValue(sql_config.get("port", 0))
        ui.sql_user_edit.setText(sql_config.get("user", ""))
        ui.sql_database_edit.setText(sql_config.get("database", ""))
        ui.sql_run_table_edit.setText(sql_config.get("run_table", ""))
        ui.sql_event_table_edit.setText(sql_config.get("event_table", ""))

        # SiPM amplifiers
        for amp in ["amp1", "amp2", "amp3"]:
            sipm_amp_config = self.config["scint"][amp]
            widgets[f"sipm_{amp}_enabled_box"].setChecked(sipm_amp_config.get("enabled", False))
            widgets[f"sipm_{amp}_ip_addr_edit"].setText(sipm_amp_config.get("ip_addr", ""))
            widgets[f"sipm_{amp}_user_edit"].setText(sipm_amp_config.get("user", ""))
            widgets[f"sipm_{amp}_bias_box"].setValue(sipm_amp_config.get("bias", 0))
            widgets[f"sipm_{amp}_qp_box"].setValue(sipm_amp_config.get("qp", 0))
            widgets[f"sipm_{amp}_iv_enabled_box"].setChecked(sipm_amp_config.get("iv_enabled", False))
            widgets[f"sipm_{amp}_iv_data_dir_edit"].setText(sipm_amp_config.get("iv_data_dir", ""))
            widgets[f"sipm_{amp}_iv_rc_data_dir_edit"].setText(sipm_amp_config.get("iv_rc_dir", ""))
            widgets[f"sipm_{amp}_iv_interval_box"].setValue(sipm_amp_config.get("iv_interval", 0))
            widgets[f"sipm_{amp}_iv_start_box"].setValue(sipm_amp_config.get("iv_start", 0))
            widgets[f"sipm_{amp}_iv_stop_box"].setValue(sipm_amp_config.get("iv_stop", 0))
            widgets[f"sipm_{amp}_iv_step_box"].setValue(sipm_amp_config.get("iv_step", 0))
            for ch in range(1, 17):
                widgets[f"sipm_{amp}_ch{ch}_offset"].setValue(sipm_amp_config["ch_offset"][ch-1])
                widgets[f"sipm_{amp}_name_ch{ch}"].setCurrentText(sipm_amp_config["name"][ch-1])

        # CAEN
        caen_config = self.config["caen"]["global"]
        ui.caen_enabled_box.setChecked(caen_config.get("enabled", False))
        ui.caen_data_path_box.setText(caen_config.get("data_path", ""))
        ui.caen_model_box.setCurrentText(caen_config.get("model", ""))
        ui.caen_link_box.setValue(caen_config.get("link", 0))
        ui.caen_conn_box.setCurrentText(caen_config.get("connection", ""))
        ui.caen_evs_box.setValue(caen_config.get("evs_per_read", 0))
        ui.caen_length_box.setValue(caen_config.get("rec_length", 0))
        ui.caen_post_trig_box.setValue(caen_config.get("post_trig", 0))
        ui.caen_trigin_gate_box.setChecked(caen_config.get("trig_in_as_gate", False))
        ui.caen_decimation_box.setValue(caen_config.get("decimation", 0))
        ui.caen_overlap_box.setChecked(caen_config.get("overlap_en", False))
        ui.caen_mem_full_box.setCurrentText(caen_config.get("memory_full", ""))
        ui.caen_counting_box.setCurrentText(caen_config.get("counting_mode", ""))
        ui.caen_polarity_box.setCurrentText(caen_config.get("polarity", ""))
        ui.caen_majority_box.setValue(caen_config.get("majority_level", 0))
        ui.caen_majority_window_box.setValue(caen_config.get("majority_window", 0))
        ui.caen_clock_box.setCurrentText(caen_config.get("clock_source", ""))
        ui.caen_acq_box.setCurrentText(caen_config.get("acq_mode", ""))
        ui.caen_io_box.setCurrentText(caen_config.get("io_level", ""))
        ui.caen_ext_trig_box.setCurrentText(caen_config.get("ext_trig", ""))
        ui.caen_sw_trig_box.setCurrentText(caen_config.get("sw_trig", ""))
        ui.caen_ch_trig_box.setCurrentText(caen_config.get("ch_trig", ""))

        for g in range(4):
            gp = f"g{g}"
            gp_config = self.config["caen"][f"group{g}"]
            widgets[f"caen_{gp}_enable_box"].setChecked(gp_config.get("enabled", False))
            widgets[f"caen_{gp}_thres_box"].setValue(gp_config.get("threshold", 0))
            widgets[f"caen_{gp}_offset_box"].setValue(gp_config.get("offset", 0))
            widgets[f"caen_{gp}_range_box"].setCurrentText(gp_config.get("range", ""))
            for ch in range(8):
                widgets[f"caen_{gp}_name_{ch}"].setCurrentText(gp_config["name"][ch])
                widgets[f"caen_{gp}_trig_mask_{ch}"].setChecked(gp_config["trig_mask"][ch])
                widgets[f"caen_{gp}_acq_mask_{ch}"].setChecked(gp_config["acq_mask"][ch])
                widgets[f"caen_{gp}_plot_mask_{ch}"].setChecked(gp_config["plot_mask"][ch])
                widgets[f"caen_{gp}_offset_{ch}"].setValue(gp_config["ch_offset"][ch])

        # acoustics
        acous_config = self.config["acous"]
        # Acquisition settings
        ui.acous_enabled_box.setChecked(acous_config.get("enabled", False))
        ui.acous_data_dir_edit.setText(acous_config.get("data_dir", ""))
        ui.acous_driver_path_edit.setText(acous_config.get("driver_path", ""))
        ui.acous_mode_box.setCurrentText(acous_config.get("mode", ""))
        ui.acous_sample_rate_box.setCurrentText(acous_config.get("sample_rate", ""))
        ui.acous_timestamp_mode_box.setCurrentText(acous_config.get("timestamp_mode", ""))
        ui.acous_timestamp_clock_box.setCurrentText(acous_config.get("timestamp_clock", ""))
        ui.acous_pre_trig_box.setValue(acous_config.get("pre_trig_len", 0))
        ui.acous_post_trig_box.setValue(acous_config.get("post_trig_len", 0))
        ui.acous_acq_seg_count_box.setValue(acous_config.get("acq_seg_count", 0))
        ui.acous_trig_timeout_box.setValue(acous_config.get("trig_timeout", 0))
        ui.acous_trig_delay_box.setValue(acous_config.get("trig_delay", 0))
        ui.acous_trig_holdoff_box.setValue(acous_config.get("trig_holdoff", 0))

        # Application settings
        ui.acous_start_pos_box.setValue(acous_config.get("start_pos", 0))
        ui.acous_transfer_len_box.setValue(acous_config.get("transfer_len", 0))
        ui.acous_seg_start_box.setValue(acous_config.get("seg_start", 0))
        ui.acous_seg_count_box.setValue(acous_config.get("seg_count", 0))
        ui.acous_page_size_box.setValue(acous_config.get("page_size", 0))
        ui.acous_file_format_box.setCurrentText(acous_config.get("file_format", ""))
        ui.acous_file_name_edit.setText(acous_config.get("file_name", ""))

        # Channel settings
        for i in range(1,9):
            ch = f"ch{i}"
            ch_config = acous_config[ch]
            widgets[f"acous_name_{ch}"].setText(ch_config.get("name", ""))
            widgets[f"acous_range_{ch}"].setCurrentText(ch_config.get("range", ""))
            widgets[f"acous_offset_{ch}"].setValue(ch_config.get("offset", 0))
            widgets[f"acous_impedance_{ch}"].setCurrentText(ch_config.get("impedance", ""))
            widgets[f"acous_coupling_{ch}"].setCurrentText(ch_config.get("coupling", ""))
            widgets[f"acous_trig_{ch}"].setChecked(ch_config.get("trig", False))
            widgets[f"acous_polarity_{ch}"].setCurrentText(ch_config.get("polarity", ""))
            widgets[f"acous_threshold_{ch}"].setValue(ch_config.get("threshold", 0))
            widgets[f"acous_plot_{ch}"].setChecked(ch_config.get("plot", False))

        # external trigger settings
        acous_ext_config = acous_config["ext"]
        widgets[f"acous_range_ext"].setCurrentText(acous_ext_config.get("range", ""))
        widgets[f"acous_trig_ext"].setChecked(acous_ext_config.get("trig", False))
        widgets[f"acous_polarity_ext"].setCurrentText(acous_ext_config.get("polarity", ""))
        widgets[f"acous_threshold_ext"].setValue(acous_ext_config.get("threshold", 0))

        # cameras
        cam_config = self.config["cams"]
        for cam in ["cam1", "cam2", "cam3"]:
            config = cam_config[cam]
            widgets[f"{cam}_enabled_box"].setChecked(config.get("enabled", False))
            widgets[f"{cam}_rc_config_path"].setText(config.get("rc_config_path", ""))
            widgets[f"{cam}_config_path"].setText(config.get("config_path", ""))
            widgets[f"{cam}_data_path"].setText(config.get("data_path", ""))
            widgets[f"{cam}_ip_addr"].setText(config.get("ip_addr", ""))
            widgets[f"{cam}_mode"].setValue(config.get("mode", 0))
            widgets[f"{cam}_trig_wait"].setValue(config.get("trig_wait", 0))
            widgets[f"{cam}_exposure"].setValue(config.get("exposure", 0))
            widgets[f"{cam}_buffer_len"].setValue(config.get("buffer_len", 0))
            widgets[f"{cam}_post_trig_len"].setValue(config.get("post_trig", 0))
            widgets[f"{cam}_adc_threshold"].setValue(config.get("adc_threshold", 0))
            widgets[f"{cam}_pix_threshold"].setValue(config.get("pix_threshold", 0))
            widgets[f"{cam}_image_format"].setCurrentText(config.get("image_format", ""))
            widgets[f"{cam}_date_format"].setText(config.get("date_format", ""))
            widgets[f"{cam}_state_comm_pin"].setValue(config.get("state_comm_pin", 0))
            widgets[f"{cam}_trig_enbl_pin"].setValue(config.get("trig_en_pin", 0))
            widgets[f"{cam}_trig_latch_pin"].setValue(config.get("trig_latch_pin", 0))
            widgets[f"{cam}_state_pin"].setValue(config.get("state_pin", 0))
            widgets[f"{cam}_trig_pin"].setValue(config.get("trig_pin", 0))

        dio_config = self.config["dio"]
        trigger_config = dio_config["trigger"]
        ui.trigger_port_edit.setText(trigger_config.get("port", ""))
        ui.trigger_sketch_edit.setText(trigger_config.get("sketch", ""))
        ui.trig_loop_box.setValue(trigger_config.get("loop", 0))
        ui.trig_reset_pin_box.setValue(trigger_config.get("reset", 0))
        ui.trig_or_pin_box.setValue(trigger_config.get("or", 0))
        ui.trig_on_time_pin_box.setValue(trigger_config.get("on_time", 0))
        ui.trig_heartbeat_pin_box.setValue(trigger_config.get("heartbeat", 0))
        ui.trig_led_gate_pin_box.setValue(trigger_config.get("led_gate_pin", 0))
        ui.trig_led_gate_cycles_box.setValue(trigger_config.get("led_gate", 0))

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
        ui.clock_port_edit.setText(clock_config.get("port", ""))
        ui.clock_sketch_edit.setText(clock_config.get("sketch", ""))
        ui.clock_loop_box.setValue(clock_config.get("loop", 0))
        for i in range(1, 17):
            w = f"wave{i}"
            clock_port_name = clock_ports[(i - 1) // 8] + str((i - 1) % 8)
            clock_pin = self.main.arduino_clock_worker.reverse_port_map[clock_port_name]
            config = clock_config[w]
            widgets[f"{w}_enabled"].setChecked(config.get("enabled", False))
            widgets[f"clock_name_{w}"].setText(config.get("name", ""))
            widgets[f"clock_pin_{w}"].setValue(clock_pin)
            widgets[f"clock_gate_{w}"].setChecked(config.get("gated", False))
            widgets[f"clock_period_{w}"].setValue(config.get("period", 0))
            widgets[f"clock_phase_{w}"].setValue(config.get("phase", 0))
            widgets[f"clock_duty_{w}"].setValue(config.get("duty", 0))
            widgets[f"clock_polarity_{w}"].setCurrentText("Normal" if config.get("polarity", False) else "Reverse")

        position_config = dio_config["position"]
        ui.position_port_edit.setText(position_config.get("port", ""))
        ui.position_sketch_edit.setText(position_config.get("sketch", ""))
        ui.position_mac_edit.setText(position_config.get("mac_addr", ""))
        ui.position_ip_edit.setText(position_config.get("ip_addr", ""))
        ui.position_gateway_edit.setText(position_config.get("gateway", ""))
        ui.position_subnet_edit.setText(position_config.get("subnet", ""))

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
        # main window
        main_ui = self.main.ui

        # settings window
        widgets = ui.__dict__

        general_config = {
            "autorun": main_ui.autorun_box.isChecked(),
            "source": main_ui.source_box.currentText(),
            "source_location": main_ui.source_location_box.currentText(),
            "config_path": ui.config_path_edit.text(),
            "data_dir": ui.data_dir_edit.text(),
            "log_dir": ui.log_dir_edit.text(),
            "writer_enabled": ui.writer_enabled_box.isChecked(),
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
            "led1_control": ui.led1_control_box.value(),
            "led2_control": ui.led2_control_box.value(),
            "led3_control": ui.led3_control_box.value(),
            "led_control_max": ui.led_control_max_box.value(),
        }

        pressure_config = {
            "mode": ui.p_mode_box.currentText(),
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
            "LED1_OUT": ui.LED1_OUT_box.value(),
            "LED2_OUT": ui.LED2_OUT_box.value(),
            "LED3_OUT": ui.LED3_OUT_box.value(),
            "LED_MAX": ui.LED_MAX_box.value(),
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
            "user": ui.sipm_amp1_user_edit.text(),
            "bias": ui.sipm_amp1_bias_box.value(),
            "qp": ui.sipm_amp1_qp_box.value(),
            "iv_enabled": ui.sipm_amp1_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp1_iv_data_dir_edit.text(),
            "iv_rc_dir": ui.sipm_amp1_iv_rc_data_dir_edit.text(),
            "iv_interval": ui.sipm_amp1_iv_interval_box.value(),
            "iv_start": ui.sipm_amp1_iv_start_box.value(),
            "iv_stop": ui.sipm_amp1_iv_stop_box.value(),
            "iv_step": ui.sipm_amp1_iv_step_box.value(),
            "ch_offset": [widgets[f"sipm_amp1_ch{ch}_offset"].value() for ch in range(1,17)],
            "name": [widgets[f"sipm_amp1_name_ch{ch}"].currentText() for ch in range(1,17)],
        }

        sipm_amp2_config = {
            "enabled": ui.sipm_amp2_enabled_box.isChecked(),
            "ip_addr": ui.sipm_amp2_ip_addr_edit.text(),
            "user": ui.sipm_amp2_user_edit.text(),
            "bias": ui.sipm_amp2_bias_box.value(),
            "qp": ui.sipm_amp2_qp_box.value(),
            "iv_enabled": ui.sipm_amp2_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp2_iv_data_dir_edit.text(),
            "iv_rc_dir": ui.sipm_amp2_iv_rc_data_dir_edit.text(),
            "iv_interval": ui.sipm_amp2_iv_interval_box.value(),
            "iv_start": ui.sipm_amp2_iv_start_box.value(),
            "iv_stop": ui.sipm_amp2_iv_stop_box.value(),
            "iv_step": ui.sipm_amp2_iv_step_box.value(),
            "ch_offset": [widgets[f"sipm_amp2_ch{ch}_offset"].value() for ch in range(1,17)],
            "name": [widgets[f"sipm_amp2_name_ch{ch}"].currentText() for ch in range(1,17)],
        }

        sipm_amp3_config = {
            "enabled": ui.sipm_amp3_enabled_box.isChecked(),
            "ip_addr": ui.sipm_amp3_ip_addr_edit.text(),
            "user": ui.sipm_amp3_user_edit.text(),
            "bias": ui.sipm_amp3_bias_box.value(),
            "qp": ui.sipm_amp3_qp_box.value(),
            "iv_enabled": ui.sipm_amp3_iv_enabled_box.isChecked(),
            "iv_data_dir": ui.sipm_amp3_iv_data_dir_edit.text(),
            "iv_rc_dir": ui.sipm_amp3_iv_rc_data_dir_edit.text(),
            "iv_interval": ui.sipm_amp3_iv_interval_box.value(),
            "iv_start": ui.sipm_amp3_iv_start_box.value(),
            "iv_stop": ui.sipm_amp3_iv_stop_box.value(),
            "iv_step": ui.sipm_amp3_iv_step_box.value(),
            "ch_offset": [widgets[f"sipm_amp3_ch{ch}_offset"].value() for ch in range(1,17)],
            "name": [widgets[f"sipm_amp3_name_ch{ch}"].currentText() for ch in range(1,17)],
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
            ch_config["plot"] = widgets[f"acous_plot_{ch}"].isChecked()
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
    def save_config_from_ui(self, ui):
        self.apply_config(ui)
        self.save_config()

    @Slot()
    def save_config(self):
        with open(self.path, "w") as file:
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
        if self.run_config["plc"]["enabled"]:
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
            json_file = os.path.join(os.path.dirname(__file__), "..",
                                     ino_config["sketch"], f"{ino}_config.json")

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
        elif self.run_pressure_mode == "Random":
            self.event_pressure = random.choice(self.run_pressure_profiles)
        elif self.run_pressure_mode == "Cycle":
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
