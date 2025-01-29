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
import numpy as np
import json
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
import time

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

    @Slot()
    def close_connection(self):
        if self.db.ping():
            self.db.commit()
            self.cursor.close()
            self.db.close()

    def deleteLater(self):
        # overwrite delete method to close connections
        self.close_connection()
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
        self.config = self.main.config_class.run_config
        runs = self.retrieve_run_id("20240508")

        self.db.ping()  # ping mysql server to make sure it's alive
        # TODO: data validation steps ...
        query = (f"INSERT INTO {self.run_table} "
                 f"VALUES(NULL, "
                        f"'{self.main.run_id}', "
                        f"0, "
                        f"'00:00:00.000', "
                        f"'{self.main.ui.comment_edit.toPlainText()}', "
                        f"'', "
                        f"'random', "
                        f"NULL, "
                        f"'{self.main.run_start_time}', "
                        f"'{self.main.run_start_time}', "
                        f"'{self.main.ui.source_box.currentText()}', "
                        f"'{self.main.ui.source_location_box.currentText()}', "
                        f"NULL, "
                        f"NULL, "
                        f"NULL, "
                        f"NULL, "
                        f"'{json.dumps(self.config)}'"
                        f");")
        self.cursor.execute(query)
        self.db.commit()

        self.run_started.emit("sql")

    @Slot()
    def stop_run(self):
        self.run_stopped.emit("sql")

    @Slot()
    def stop_event(self):
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
        self.main.trigff_wait.wait(self.main.trigff_mutex)
        self.main.trigff_mutex.unlock()

        query = (f"INSERT INTO {self.event_table} "
                 f"VALUES(NULL,"
                        f"'{self.main.run_id}',"
                        f"{self.main.event_id},"
                        f"'{str(datetime.timedelta(milliseconds=self.main.event_livetime))}',"
                        f"'{str(datetime.timedelta(milliseconds=self.main.run_livetime))}',"
                        f"{0},"
                        f"NULL,"
                        f"1,"
                        f"NULL,"
                        f"'{self.main.event_start_time}',"
                        f"'{self.main.event_end_time}',"
                        f"'{self.main.ui.trigger_edit.text()}'"
                        f");")
        self.cursor.execute(query)
        self.db.commit()
        self.event_stopped.emit("sql")
