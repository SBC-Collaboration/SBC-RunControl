import os.path
from sshtunnel import SSHTunnelForwarder
import mysql.connector
import datetime
import time as tm
import paramiko, pymysql
import random
import pandas as pd
# import matplotlib as plot

"""
Modified from SBC-SlowControl Database_SBC.py
PASSWORD IN THIS DOCUMENT are saved as enviroment variable at slowcontrol machine
You can also get it from SBC mysql document configuration
https://docs.google.com/document/d/1o2LEL3cKEVQ6zuR_jJgt-p3UgnVysMm6LkXXOvfMZeE/edit
"""


def datetime_in_s():
    d=datetime.datetime.now()
    timeR = int(d.microsecond%1e6)
    delta=datetime.timedelta(microseconds=timeR)
    x=d-delta
    return x

def datetime_in_1e5micro():
    d=datetime.datetime.now()
    timeR = int(d.microsecond%1e5)
    delta=datetime.timedelta(microseconds=timeR)
    x=d-delta
    return x

def early_datetime():
    d = datetime.datetime.now()
    timeR = int(d.microsecond % 1e5)
    delta = datetime.timedelta(microseconds=timeR)
    x = d - delta - datetime.timedelta(microseconds=1e5)
    return x

def later_datetime():
    d = datetime.datetime.now()
    timeR = int(d.microsecond % 1e5)
    delta = datetime.timedelta(microseconds=timeR)
    x = d - delta + datetime.timedelta(microseconds=1e5)
    return x

def UNIX_time(self):
    return int(tm.time())



class mydatabase():
    def __init__(self):
        # db=mysql.connector.connect()
        self.db = mysql.connector.connect(host="localhost", user="slowcontrol", passwd=os.environ.get("SLOWCONTROL_LOCAL_TOKEN"), database="SBCslowcontrol")

        self.mycursor = self.db.cursor()
        self.stack= pd.DataFrame(columns=['Instrument', 'Time', 'Value'])

    def query(self,statement):
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


class DataBase():
    def __init__(self):
        # save the password in ENV at sbcslowcontrol machine
        self.home = os.path.expanduser('~')
        self.sql_hostname = 'localhost'
        self.sql_username = 'slowcontrol'
        self.sql_password = os.environ.get("SLOWCONTROL_SQL_TOKEN")
        self.sql_main_database = 'run_data'
        self.sql_port = 3306
        self.ssh_host = 'sbcslowcontrol.fnal.gov'
        self.ssh_password = os.environ.get("SLOWCONTROL_SSH_TOKEN")
        self.ssh_user = 'hep'
        self.ssh_port = 22

    def ssh_write(self):
        with SSHTunnelForwarder(
                (self.ssh_host, self.ssh_port),
                ssh_username=self.ssh_user,
                ssh_password= self.ssh_password,
                remote_bind_address=(self.sql_hostname, self.sql_port)) as tunnel:

            self.db = pymysql.connect(host="localhost", user=self.sql_username, passwd=self.sql_password, database=self.sql_main_database, port=tunnel.local_bind_port)
            self.mycursor = self.db.cursor()
            self.update_alarm()
            self.close_database()

            # conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            #                        passwd=sql_password, db=sql_main_database,
            #                        port=tunnel.local_bind_port)
            # query = '''SELECT VERSION();'''
            # data = pd.read_sql_query(query, conn)
            # conn.close()

    def ssh_select(self):
        with SSHTunnelForwarder(
                (self.ssh_host, self.ssh_port),
                ssh_username=self.ssh_user,
                ssh_password= self.ssh_password,
                remote_bind_address=(self.sql_hostname, self.sql_port)) as tunnel:
            print("pointer 0")
            print(tunnel.local_bind_port)
            self.db = pymysql.connect(host="127.0.0.1", user=self.sql_username, passwd=self.sql_password, database=self.sql_main_database, port=tunnel.local_bind_port)
            # self.db = mysql.connector.connect(host="127.0.0.1", user=self.sql_username, passwd=self.sql_password, database=self.sql_main_database, port=tunnel.local_bind_port)
            print(1)
            self.mycursor = self.db.cursor()
            self.show_data()
            self.close_database()

            # conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            #                        passwd=sql_password, db=sql_main_database,
            #                        port=tunnel.local_bind_port)
            # query = '''SELECT VERSION();'''
            # data = pd.read_sql_query(query, conn)
            # conn.close()
    def show_data(self,start_time=None, end_time=None):
        # if start_time==None or end_time==None:
        print(start_time,end_time)
        query = "SELECT * FROM sbc_FNAL_alarms"
        self.mycursor.execute(query)
        for (id,datime,alarm_state, alarm_message) in self.mycursor:
            print(str("Alarm_info"+"| {} | {} | {}".format(datime,alarm_state, alarm_message)))


    def close_database(self):
        self.mycursor.close()
        self.db.close()


