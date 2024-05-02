import os.path
from sshtunnel import SSHTunnelForwarder
from PySide6.QtCore import Signal, Slot
import mysql.connector
import datetime
import time as tm
import paramiko, pymysql
import random
import pandas as pd
import logging
import json
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
from sqlalchemy import create_engine

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

        self.config = mainwindow.config_class.config["general"]["sql"]
        # save the password in ENV at sbcslowcontrol machine
        # self.home = os.path.expanduser('~')
        self.hostname = self.config["hostname"]
        self.user = self.config["user"]
        self.token = os.environ.get(self.config["token"])
        self.database = self.config["database"]
        self.run_table = self.config["run_table"]
        self.event_table = self.config["event_table"]
        self.port = self.config["port"]

        self.setup_connection()

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
        self.db = pymysql.connect(host=self.hostname, user=self.user, passwd=self.token,
                                  database=self.database, port=self.port)
        self.cursor = self.db.cursor()

    def close_connection(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def connect_and_execute(self, query):
        self.setup_connection()
        self.cursor.execute(query)
        self.close_connection

    def generate_run_data(self):
        data = {}
        data["ID"] = "NULL" # placeholder for auto generated id number
        data["run_ID"] = f"'{self.main.run_id}'"
        data["num_events"] = self.main.event_id
        data["run_livetime"] = self.main.run_livetime/1000  # total livetime of the run
        data["comments"] = f"'{self.main.ui.comment_edit.toPlainText()}'"
        data["active_datastreams"] = "''"
        data["pset_mode"] = f"'random'"
        data["pset"] = f"'{self.main.ui.pressure_setpoint_box.value()}'"
        data["pset_hi"] = "NULL"
        data["pset_slope"] = "NULL"
        data["pset_period"] = "NULL"
        data["start_time"] = f"'{self.start_time}'"
        data["stop_time"] = f"'{self.stop_time}'"
        data["source1_ID"] = f"'{self.main.ui.source_box.currentText()}'"
        data["source1_location"] = f"'{self.main.ui.source_location_box.currentText()}'"
        data["source2_ID"] = "NULL"
        data["source2_location"] = "NULL"
        data["source3_ID"] = "NULL"
        data["source3_location"] = "NULL"
        data["config"] = f"'{json.dumps(self.config)}'"

        return data

    @Slot()
    def insert_run_data(self):
        self.db.ping() # ping mysql server to make sure it's alive
        # TODO: data validation steps ...
        data = self.generate_run_data()
        query = (f"INSERT INTO {self.run_table} "
                 f"VALUES({data['ID']},"
                        f"{data['run_ID']},"
                        f"{data['num_events']},"
                        f"{data['run_livetime']},"
                        f"{data['comments']},"
                        f"{data['active_datastreams']},"
                        f"{data['pset_mode']},"
                        f"{data['pset']},"
                        f"{data['pset_hi']},"
                        f"{data['pset_slope']},"
                        f"{data['pset_period']},"
                        f"{data['start_time']},"
                        f"{data['stop_time']},"
                        f"{data['source1_ID']},"
                        f"{data['source1_location']},"
                        f"{data['source2_ID']},"
                        f"{data['source2_location']},"
                        f"{data['source3_ID']},"
                        f"{data['source3_location']},"
                        f"{data['config']}"
                        f")")
        try:
            self.cursor.execute(query)
        except:
            self.logger.error(f"SQL data insertion for run {self.main.run_id} failed.")
        self.db.commit()

    @Slot()
    def start_run(self):
        self.start_time = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
        self.config = self.main.config_class.run_config
        self.run_started.emit("SQL")

    @Slot()
    def stop_run(self):
        self.stop_time = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
        self.insert_run_data()
        self.run_stopped.emit("SQL")

    @Slot()
    def stop_event(self):
        self.event_stopped.emit("SQL")
