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
    event_stopped = Signal(str)

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
        self.token = os.environ.get(self.config["token"])
        self.database = self.config["database"]
        self.run_table = self.config["run_table"]
        self.event_table = self.config["event_table"]
        self.port = self.config["port"]

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
            passwd=self.token,
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
        run_query = f"SELECT run_id FROM {self.run_table} WHERE run_ID LIKE '{date}%'" if date \
            else f"SELECT run_id FROM {self.run_table}"
        self.cursor.execute(run_query)
        runs = set(np.array(self.cursor.fetchall())[:,0])

        # now do the event table
        event_query = f"SELECT run_id FROM {self.event_table} WHERE run_ID LIKE '{date}%'" if date \
            else f"SELECT run_id FROM {self.event_table}"
        self.cursor.execute(event_query)
        more_runs = set(np.array(self.cursor.fetchall())[:,0])
        return runs.union(more_runs)

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

        query = f"""
            INSERT INTO {self.run_table} (
                ID, run_ID, run_exit_code, num_events, run_livetime, comment,
                active_datastreams, pset_mode, pset,
                start_time, end_time,
                source1_ID, source1_location,
                source2_ID, source2_location,
                source3_ID, source3_location,
                red_caen_ver, niusb_ver, sbc_binary_ver,
                config
            )
            VALUES (
                NULL, %s, %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s,
                %s, %s,
                %s, %s,
                %s, %s,
                %s, %s, %s,
                %s
            )
        """
        values = (
            self.main.run_id,                      # run_ID
            None,                                  # run_exit_code
            0,                                     # num_events
            "00:00:00.000",                        # run_livetime
            self.main.ui.comment_edit.toPlainText() or None,  # comment
            "",                                    # active_datastreams
            self.main.config_class.run_pressure_mode,                   # pset_mode
            self.main.config_class.run_pressure_profiles[0]["setpoint"]     # pset
                if len(self.main.config_class.run_pressure_profiles)==1 else None,                                   
            self.main.run_start_time,              # start_time
            self.main.run_start_time,              # end_time
            self.main.ui.source_box.currentText() or None,              # source1_ID
            self.main.ui.source_location_box.currentText() or None,     # source1_location
            None, None,                            # source2_ID, source2_location
            None, None,                            # source3_ID, source3_location
            red_caen.__version__,                # red_caen_ver
            ni_usb_6501.__version__,             # niusb_ver
            sbcbinaryformat.__version__,         # sbc_binary_ver
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
                 f"SET run_exit_code = {self.main.run_exit_code} "
                 f"WHERE run_ID = '{self.main.run_id}';")
        self.cursor.execute(query)
        self.db.commit()
        self.run_stopped.emit("sql")

    @Slot()
    def stop_event(self):
        if not self.enabled:
            self.event_stopped.emit("sql-disabled")
            return
        self.db.ping()  # ping mysql server to make sure it's alive
        # TODO: data validation steps ...
        query = (f"UPDATE {self.run_table} "
                 f"SET num_events = {self.main.event_id}, "
                     f"run_livetime = '{str(datetime.timedelta(milliseconds=self.main.run_livetime))}', "
                     f"comment = '{self.main.ui.comment_edit.toPlainText()}', "
                     f"end_time = '{self.main.event_end_time}', "
                     f"source1_ID = '{self.main.ui.source_box.currentText()}', "
                     f"source1_location = '{self.main.ui.source_location_box.currentText()}' "
                 f"WHERE run_ID = '{self.main.run_id}';")
        self.cursor.execute(query)

        self.main.trigff_mutex.lock()
        while not self.main.trigff_ready:
            self.main.trigff_wait.wait(self.main.trigff_mutex)
        self.main.trigff_ready = False
        self.main.trigff_mutex.unlock()

        query = f"""
            INSERT INTO {self.event_table} (
                ID, run_ID, event_ID, event_livetime, cum_livetime,
                pset, pset_hi, pset_slope, pset_period,
                start_time, stop_time, trigger_source
            )
            VALUES (
                NULL, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s
            )
        """
        values = (
            self.main.run_id,
            self.main.event_id,
            str(datetime.timedelta(milliseconds=self.main.event_livetime)),
            str(datetime.timedelta(milliseconds=self.main.run_livetime)),
            self.main.config_class.event_pressure["setpoint"],
            self.main.config_class.event_pressure["setpoint_high"],
            self.main.config_class.event_pressure["slope"],
            self.main.config_class.event_pressure["period"],
            self.main.event_start_time,
            self.main.event_end_time,
            self.main.ui.trigger_edit.text()
        )
        self.cursor.execute(query, values)
        self.db.commit()
        self.event_stopped.emit("sql")
