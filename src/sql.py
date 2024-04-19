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


class SQL:
    def __init__(self, mainwindow):
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
        self.ssh_host = self.config["ssh_host"]
        self.ssh_pkey = self.config["ssh_pkey"]
        self.ssh_user = self.config["ssh_user"]
        self.ssh_port = self.config["ssh_port"]
        self.ssh_keep_alive = 30.0 # time interval after which a dummy packet is sent to keep connection alive

    def deleteLater(self):
        pass

    def setup_connection(self):
        self.tunnel = SSHTunnelForwarder(
            (self.ssh_host, self.ssh_port),
            ssh_username=self.ssh_user,
            ssh_pkey=self.ssh_pkey,
            remote_bind_address=(self.hostname, self.port),
            set_keepalive=self.ssh_keep_alive)

        self.db = pymysql.connect(host=self.hostname, user=self.user, passwd=self.token,
                                  database=self.database, port=self.tunnel.local_bind_port)
        self.cursor = self.db.cursor()

    def close_connection(self):
        self.cursor.close()
        self.db.close()

    def connect_and_execute(self, query):
        self.setup_connection()
        self.cursor.execute(query)
        self.close_connection

    def generate_run_query(self):
        data = {}
        data["ID"] = "NULL" # placeholder for auto generated id number
        data["run_ID"] = self.main.run_id
        data["num_events"] = self.main.run_livetime # total livetime of the run
        data["comments"] = self.main.ui.comment_edit.text()
        data["active_datastreams"] = ""
        data["pset_mode"] = "random"
        data["pset"] = self.main.ui.pressure_setpoint_box.value()
        data["pset_hi"] = "NULL"
        data["source1_ID"] = self.main.ui.source_box.currentText()
        return data

    def insert_run_data(self, data):
        self.db.ping() # ping mysql server to make sure it's alive
        # TODO: data validation steps ...
        query = (f"INSERT INTO {self.run_table}"
                 f"VALUES ({data["ID"]},"
                 f"        '{data["run_ID"]}',"
                 f"        {data["num_events"]},"
                 f"        '{data["comments"]}',"
                 f"        '{data["active_datastreams"]}',"
                 f"        '{data["pset_mode"]}',"
                 f"        {data["pset"]},"
                 f"        {data["pset_hi"]}")
        print(query)
        try:
            self.cursor.execute(query)
        except:
            self.logger.error(f"SQL data insertion for run {self.main.run_id} failed.")
        self.db.commit()
