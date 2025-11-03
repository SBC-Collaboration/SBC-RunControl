from PySide6.QtCore import Signal, Slot
import datetime
import pymysql
import os
import logging
import numpy as np
import json
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import red_caen, ni_usb_6501, sbcbinaryformat

"""
Modified from SBC-SlowControl Database_SBC.py
PASSWORD IN THIS DOCUMENT are saved as enviroment variable at slowcontrol machine
You can also get it from SBC mysql document configuration
https://docs.google.com/document/d/1o2LEL3cKEVQ6zuR_jJgt-p3UgnVysMm6LkXXOvfMZeE/edit
"""

class SQL(QObject):
    run_started = Signal(str)
    run_stopped = Signal(str)
    event_started = Signal(str)
    event_stopped = Signal(str)
    error = Signal(int)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.db = None

        self.config = mainwindow.config_class.config["sql"]
        # save the password in ENV at sbcslowcontrol machine
        # self.home = os.path.expanduser('~')
        self.hostname = self.config["hostname"]
        self.user = self.config["user"]
        self.database = self.config["database"]
        self.run_table = self.config["run_table"]
        self.event_table = self.config["event_table"]
        self.port = self.config["port"]
        with open(os.path.expanduser("~/.config/runcontrol/sql_token"), "r") as f:
            self.password = f.read().strip()

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"SQL module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    def setup_connection(self):
        self.db = pymysql.connect(
            host=self.hostname, 
            user=self.user, 
            passwd=self.password,
            database=self.database, 
            port=self.port,
            connect_timeout=10)
        self.cursor = self.db.cursor()

    @Slot()
    def close_connection(self):
        if self.db and self.db.ping():
            self.db.commit()
            self.cursor.close()
            self.db.close()

    def deleteLater(self):
        # overwrite delete method to close connections
        self.close_connection()
        self.main.trigff_mutex.lock()
        self.main.trigff_wait.wakeOne() # wake in case it's hanging
        self.main.trigff_mutex.unlock() 
        super().deleteLater()

    def connect_and_execute(self, query):
        self.setup_connection()
        self.cursor.execute(query)
        self.close_connection

    @Slot()
    def retrieve_run_id(self, date=""):
        self.enabled = self.config["enabled"]
        if not self.enabled:
            return set()
        
        self.setup_connection()
        run_query = f"SELECT run_id FROM {self.run_table} WHERE run_ID LIKE '{date}%'" if date \
            else f"SELECT run_id FROM {self.run_table}"
        self.cursor.execute(run_query)
        dates = np.array(self.cursor.fetchall())
        if dates.ndim == 1:
            runs = set(dates)
        elif dates.ndim == 2:
            runs = set(dates[:,0])
        else:
            self.logger.warning("Unexpected dimensions for run IDs.")

        # now do the event table
        event_query = f"SELECT run_id FROM {self.event_table} WHERE run_ID LIKE '{date}%'" if date \
            else f"SELECT run_id FROM {self.event_table}"
        self.cursor.execute(event_query)
        dates = np.array(self.cursor.fetchall())
        if dates.ndim == 1:
            more_runs = set(dates)
        elif dates.ndim == 2:
            more_runs = set(dates[:,0])
        else:
            self.logger.warning("Unexpected dimensions for run IDs.")
        all_runs = runs.union(more_runs)
        self.close_connection()

        # get only the run number without date
        return {int(run.split("_")[-1]) for run in all_runs}

    @Slot()
    def start_run(self):
        self.config = self.main.config_class.run_config["sql"]
        self.enabled = self.config["enabled"]
        if not self.enabled:
            self.run_started.emit("sql-disabled")
            return
        
        self.setup_connection()

        self.db.ping()  # ping mysql server to make sure it's alive
        # TODO: data validation steps ...

        # get active modules
        self.active_modules = []
        for cam in ["cam1", "cam2", "cam3"]:
            if self.main.config_class.run_config["cams"][cam]["enabled"]:
                self.active_modules.append(cam)
        for amp in ["amp1", "amp2", "amp3"]:
            if self.main.config_class.run_config["scint"][amp]["enabled"]:
                self.active_modules.append(amp)
        for m in ["acous", "sql", "plc"]:
            if self.main.config_class.run_config[m]["enabled"]:
                self.active_modules.append(m)
        if self.main.config_class.run_config["caen"]["global"]["enabled"]:
            self.active_modules.append("caen")

        query = f"""
            INSERT INTO {self.run_table} (
                ID, run_ID, run_exit_code, num_events, run_livetime, comment,
                active_modules, pset_mode, pset,
                start_time, end_time,
                source1_ID, source1_location,
                source2_ID, source2_location,
                source3_ID, source3_location,
                rc_ver, red_caen_ver, niusb_ver, sbc_binary_ver,
                config
            )
            VALUES (
                NULL, %s, %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s,
                %s, %s,
                %s, %s,
                %s, %s,
                %s, %s, %s, %s,
                %s
            )
        """
        values = (
            self.main.run_id,                      # run_ID
            None,                                  # run_exit_code
            0,                                     # num_events
            "00:00:00.000",                        # run_livetime
            self.main.ui.comment_edit.toPlainText() or None,  # comment
            ",".join(self.active_modules) or None,                   # active_modules
            self.main.config_class.run_pressure_mode,                   # pset_mode
            self.main.config_class.run_pressure_profiles[0]["setpoint"]     # pset
                if len(self.main.config_class.run_pressure_profiles)==1 else None,                                   
            self.main.run_start_time.isoformat(sep=" ", timespec="milliseconds"),              # start_time
            None,                                  # end_time
            self.main.ui.source_box.currentText() or None,              # source1_ID
            self.main.ui.source_location_box.currentText() or None,     # source1_location
            None, None,                            # source2_ID, source2_location
            None, None,                            # source3_ID, source3_location
            self.main.writer_worker.rc_version,    # rc_ver
            red_caen.__version__,                  # red_caen_ver
            ni_usb_6501.__version__,               # niusb_ver
            sbcbinaryformat.__version__,           # sbc_binary_ver
            json.dumps(self.main.config_class.run_config),              # config (as JSON string)
        )
        self.cursor.execute(query, values)
        self.db.commit()

        self.run_started.emit("sql")

    @Slot()
    def stop_run(self):
        if not self.enabled:
            self.run_stopped.emit("sql-disabled")
            return
        self.db.ping()
        query = (f"UPDATE {self.run_table} "
                 f"SET run_exit_code = {self.main.run_exit_code}, "
                 f"end_time = '{self.main.run_end_time.isoformat(sep=" ", timespec="milliseconds")}' "
                 f"WHERE run_ID = '{self.main.run_id}';")
        self.cursor.execute(query)
        self.db.commit()
        self.run_stopped.emit("sql")
    
    @Slot()
    def start_event(self):
        if not self.enabled:
            self.event_started.emit("sql-disabled")
            return
        self.db.ping()
        query = f"""
            INSERT INTO {self.event_table} (
                ID, run_ID, event_ID, event_exit_code, event_livetime, cum_livetime,
                pset, pset_hi, pset_slope, pset_period,
                start_time, stop_time, trigger_source
            )
            VALUES (
                NULL, %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s
            )
        """
        values = (
            self.main.run_id,
            self.main.event_id,
            None,
            0,  # event livetime
            str(datetime.timedelta(milliseconds=self.main.run_livetime)),
            self.main.config_class.event_pressure["setpoint_lo"],
            self.main.config_class.event_pressure["setpoint_hi"],
            self.main.config_class.event_pressure["ramp1"],
            self.main.config_class.event_pressure["ramp_down"],
            self.main.event_start_time.isoformat(sep=" ", timespec="milliseconds"),
            None,  # end time
            None   # trigger source
        )
        self.cursor.execute(query, values)
        self.db.commit()
        self.event_started.emit("sql")

    @Slot()
    def stop_event(self):
        if not self.enabled:
            self.event_stopped.emit("sql-disabled")
            return
        self.db.ping()  # ping mysql server to make sure it's alive
        # TODO: data validation steps ...
        query = (f"UPDATE {self.run_table} "
                 f"SET num_events = {self.main.event_id + 1}, "  # event ID not updated yet
                     f"run_livetime = '{str(datetime.timedelta(milliseconds=self.main.run_livetime))}', "
                     f"comment = '{self.main.ui.comment_edit.toPlainText()}', "
                     f"end_time = '{self.main.event_end_time.isoformat(sep=" ", timespec="milliseconds")}', "
                     f"source1_ID = '{self.main.ui.source_box.currentText()}', "
                     f"source1_location = '{self.main.ui.source_location_box.currentText()}' "
                 f"WHERE run_ID = '{self.main.run_id}';")
        self.cursor.execute(query)

        self.main.trigff_mutex.lock()
        while not self.main.trigff_ready:
            self.main.trigff_wait.wait(self.main.trigff_mutex)
        self.main.trigff_mutex.unlock()

        query = f"""
            UPDATE {self.event_table} SET
                event_exit_code = %s,
                event_livetime = %s,
                cum_livetime = %s,
                stop_time = %s,
                trigger_source = %s
            WHERE run_ID = %s AND event_ID = %s
        """
        values = (
            self.main.event_exit_code,
            str(datetime.timedelta(milliseconds=self.main.event_livetime)),
            str(datetime.timedelta(milliseconds=self.main.run_livetime)),
            self.main.event_end_time.isoformat(sep=" ", timespec="milliseconds"),
            self.main.ui.trigger_edit.text(),
            self.main.run_id,
            self.main.event_id
        )

        self.cursor.execute(query, values)
        self.db.commit()
        self.event_stopped.emit("sql")
