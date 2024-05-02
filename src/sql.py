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

class mydatabase():
    def __init__(self):
        # db=mysql.connector.connect()
        self.db = mysql.connector.connect(host="localhost", user="slowcontrol", passwd=os.environ.get("SLOWCONTROL_LOCAL_TOKEN"), database="SBCslowcontrol")

        self.mycursor = self.db.cursor()
        self.stack= pd.DataFrame(columns=['Instrument', 'Time', 'Value'])

    def query(self, statement):
        try:
            self.mycursor.execute(statement)
        except:
            print("Statement formal is wrong, please check it")
    # user slowcontrol doesn't have permission to create tables. Besides, table columVn name should be different
    # def create_table(self, table_name):
    #     self.mycursor.execute(
    #         "CREATE TABLE {}(Time DATETIME, Value DECIMAL(7,3), PRIMARY KEY(Time));".format(table_name))
    #     self.db.commit()

    def show_tables(self, key=None):
        if key is None:
            self.mycursor.execute(
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'SBCslowcontrol'"
            )
        else:
            self.mycursor.execute(
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'sbc' AND TABLE_NAME LIKE '%{}%'".format(key)
            )
        result = self.mycursor.fetchall()
        print(result)

    def insert_data_into_datastorage(self,instrument, time,value):
        # time must be like '2021-02-17 20:36:26' or datetime.datetime(yy,mm,dd,hh,mm,ss)
        # value is a decimal from -9999.999 to 9999.999
        # name must be consistent with P&ID
        data=(instrument, time,value)
        self.mycursor.execute(
            "INSERT INTO DataStorage (Instrument, Time, Value) VALUES(%s, %s, %s);", data)
        self.db.commit()

    def insert_data_into_datastorage_wocommit(self,instrument, time,value):
        # time must be like '2021-02-17 20:36:26' or datetime.datetime(yy,mm,dd,hh,mm,ss)
        # value is a decimal from -9999.999 to 9999.999
        # name must be consistent with P&ID
        data=(instrument, time,value)
        self.mycursor.execute(
            "INSERT INTO DataStorage (Instrument, Time, Value) VALUES(%s, %s, %s);", data)
    def insert_data_into_stack(self,instrument, time,value):
        # time must be like '2021-02-17 20:36:26' or datetime.datetime(yy,mm,dd,hh,mm,ss)
        # value is a decimal from -9999.999 to 9999.999
        # name must be consistent with P&ID
        data=(instrument, time,value)
        new_df=pd.DataFrame({'Instrument':instrument,"Time":time,"Value": value},index=[len(self.stack)])
        self.stack = pd.concat((self.stack,new_df), axis=0,ignore_index= True)

    def sort_stack(self):
        self.stack = self.stack.sort_values(by=['Time'])
        self.stack = self.stack.reset_index(drop=True)
        # print("first", self.stack.iloc[:5])
        # print("last",self.stack.iloc[-5:])

    def convert_stack_into_queries(self):
        for idx in self.stack.index:
            newdata = (self.stack['Instrument'][idx], self.stack['Time'][idx], self.stack['Value'][idx])
            # print(newdata)

            self.mycursor.execute(
                "INSERT INTO DataStorage (Instrument, Time, Value) VALUES(%s, %s, %s);", newdata)

    def drop_stack(self):
        self.stack = self.stack.iloc[0:0]
        # print(self.stack)

    def insert_data_into_metadata(self,instrument, Description,Unit):
        # time must be like '2021-02-17 20:36:26' or datetime.datetime(yy,mm,dd,hh,mm,ss)
        # value is a decimal from -9999.999 to 9999.999
        # name must be consistent with P&ID
        data=(instrument, Description,Unit)
        self.mycursor.execute(
            "INSERT INTO MetaDataStorage VALUES(%s, %s, %s);", data)
        self.db.commit()

    def show_data_datastorage(self,start_time=None, end_time=None):
        # if start_time==None or end_time==None:
        print(start_time,end_time)
        query = "SELECT * FROM DataStorage"
        self.mycursor.execute(query)
        for (ID,Instrument,Time, Value) in self.mycursor:
            print(str("DataStorage"+"| {} | {} | {}".format(Instrument,Time, Value)))

    def show_data_metadatastorage(self):
        query = "SELECT * FROM MetaDataStorage"
        self.mycursor.execute(query)
        for (Instrument, Description, unit) in self.mycursor:
            print(str("MetaDataStorage" + "| {} | {} | {}".format(Instrument, Description, unit)))

    def close_database(self):
        self.mycursor.close()
        self.db.close()


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