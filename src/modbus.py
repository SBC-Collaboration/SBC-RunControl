import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread, QMutex, QWaitCondition
import signal
from configparser import ConfigParser
from multiprocessing import Process
import ctypes
from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import struct
import numpy as np
import time
from functools import wraps

class Modbus(QObject):
    pressure_cycle =  False
    run_started = Signal(str)
    run_stopped = Signal(str)
    event_started = Signal(str)
    event_stopped = Signal(str)
    success_msg = Signal(str)
    error_msg = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.config = self.main.config_class.config["plc"]

        self.timer = QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.periodic_task)



    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Modbus module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        if (self.main.run_state == self.main.run_states["active"] and self.pressure_cycle ==  False): 
            pressure_state  = read_procedure(self.Client_BO, self.config["registers"]["PRESSURE_CYCLE"]) 
            if(pressure_state[0] == False):
                start_pressure = start_procedure(self.Client_BO, self.config["registers"]["PRESSURE_CYCLE"])
                if((start_pressure)==True):
                    self.pressure_cycle  = True
                    self.logger.debug(f" Pressure cycle started successfully.")
                else:
                    self.logger.error(f" Pressure cycle start is unsuccessful.")


 
    @Slot()
    def start_run(self):
        IP_BO = self.config["hostname"]
        PORT_BO = self.config["port"]
        self.Client_BO = ModbusTcpClient(IP_BO, port=PORT_BO)
        try:
            self.Connected_BO = self.Client_BO.connect()
            self.logger.debug(f" Beckoff connected: {str(self.Connected_BO)}.")
        except Exception as e:
            self.logger.debug(f"BO connection exceptions.")
        self.run_started.emit("modbus")


    @Slot()                                                                      
    def start_event(self):
        if (start_procedure(self.Client_BO,self.config["registers"]["WRITE_SLOWDAQ"])) == True:
            self.logger.debug(f"SLOW DAQ process started.")
        else:
            self.logger.error(f"SLOW DAQ process start is unsuccessful.")

        if ((write_float(self.Client_BO,self.config["registers"]["PCYCLE_PSET"],self.config["pressure"]["profile1"]["setpoint"]))==True):
            self.logger.debug(f"write of PSET is successful.")
        else:
            self.logger.error(f"write of PSET is unsuccessful.")
            self.error_msg.emit("pset")
        self.event_started.emit("modbus")


    @Slot()
    def stop_event(self):
        pressure_counter = 0
        slowdaq_counter = 0
        end_state = read_procedure(self.Client_BO,self.config["registers"]["PRESSURE_CYCLE"])
        while(end_state[0] == True and pressure_counter < 20):
            end_state = read_procedure(self.Client_BO,self.config["registers"]["PRESSURE_CYCLE"])
            pressure_counter += 1
            time.sleep(0.1)
        if end_state[0] == True:
            stop_state = stop_procedure(self.Client_BO,self.config["registers"]["PRESSURE_CYCLE"])
            if stop_state != True:
                abort_state = abort_procedure(self.Client_BO,self.config["registers"]["PRESSURE_CYCLE"])
                if abort_state != True:
                    self.error_msg.emit("PRESSURE_CYCLE still running")
                else:
                    self.logger.debug("Pressure cycle aborted.")
            else:
                self.logger.debug("Pressure cycle stopped.")
        else:
            self.logger.debug("Pressure cycle ended.")
        fault_bits = read_FF(self.Client_BO,self.config["registers"]["PCYCLE_ABORT_FF"])
        self.logger.debug("fault_bits.")
        self.logger.debug(fault_bits)
        # write the fault bits in a file
        slowdaq_stop = stop_procedure(self.Client_BO,self.config["registers"]["WRITE_SLOWDAQ"])
        self.pressure_cycle = False
        if (slowdaq_stop == True):
            self.logger.debug(f"SLOW DAQ process ended successfully.")
        else:
            self.logger.error(f"SLOW DAQ process didn't end successfully.")
        # slowdaq_state = read_procedure(self.Client_BO,self.config["registers"]["WRITE_SLOWDAQ"])
        # while(slowdaq_state[0] != 0 and slowdaq_counter < 10):
        #     slowdaq_state = read_procedure(self.Client_BO,self.config["registers"]["WRITE_SLOWDAQ"])
        #     slowdaq_counter = slowdaq_counter + 1
        #     time.sleep(10)
       
       #### write log file from plc to RC ####
        self.event_stopped.emit("modbus")

    @Slot()
    def stop_run(self):
        self.Client_BO.close()
        self.run_stopped.emit("modbus")


################## Modbus helper function ##############################




def safe_modbus(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Try to get `pos` from kwargs or args
            pos = kwargs.get('pos') if 'pos' in kwargs else args[0] if args else '?'
            print(f"ERROR in {func.__name__} at register {pos}: {e}")
            return None
    return wrapper

@safe_modbus
def read_float(Client_BO,pos, endian='<'):
    # PARAM_F
    length = 2
    response = Client_BO.read_holding_registers(pos, count=length)
    packed_registers = struct.pack(f"{endian}HH", *response.registers)
    value_float = struct.unpack(f"{endian}f", packed_registers)[0]
    return value_float

@safe_modbus
def write_float(Client_BO, pos, value, endian='<'):
    """Write a 32-bit float value to two words at a Modbus register.

    Args:
        pos (int): The register position to write to.
        value (float): The 32-bit float value to write.
        endian (str, optional): The byte order to use. Defaults to '<'.

    Returns:
        bool: True if the write was successful, None otherwise.
    """
    # PARAM_F
    fl = float(value)
    bytes = struct.pack(f'{endian}f', fl)
    words = struct.unpack(f'{endian}HH', bytes)
    response = Client_BO.write_registers(pos, words)
    return True

@safe_modbus
def read_int(Client_BO,pos, endian='<'):
    # PARAM_I
    length = 1
    response = Client_BO.read_holding_registers(pos, count=length)
    value_int = struct.unpack(f"{endian}i", response.registers[0])[0]
    return value_int

@safe_modbus
def read_time(Client_BO, pos, endian='<'):
    # PARAM_T, TIME
    length = 2
    response = Client_BO.read_holding_registers(pos, count=length)
    words = response.registers
    packed = struct.pack(f"{endian}HH", *words)
    value_time = struct.unpack(f"{endian}i", packed)[0]
    return value_time  # ms

@safe_modbus
def write_time(Client_BO, pos, value, endian='<'):
    # PARAM_T
    t = int(value)
    bytes = struct.pack(f'{endian}i', t)
    words = struct.unpack(f'{endian}HH', bytes)
    response = Client_BO.write_registers(pos, words)
    return True

@safe_modbus
def read_flag(Client_BO, pos):
    # FLAG
    length = 1
    response = Client_BO.read_holding_registers(pos, count=length)
    word = response.registers[0]
    # Get running state at bit 0 and interlocked at bit 1
    running = (word >> 0) & 1 == 1
    interlocked = (word >> 1) & 1 == 1
    # TODO: make return into a named tuple
    return running, interlocked

@safe_modbus
def write_flag(Client_BO, pos, value):
    # FLAG
    # If true, set flag, set 1 to bit 1
    # If false, reset flag, set 1 to bit 2
    Client_BO.write_register(pos, 1<<(1 if value else 2))
    return True

@safe_modbus
def read_FF(Client_BO, pos):
    # FF
    length = 1
    response = Client_BO.read_holding_registers(pos, count=length)
    word = response.registers[0]
    # Check if each bit is true or false
    fault_bits = [(word >> i) & 1 == 1  for i in range(15)]
    return fault_bits

@safe_modbus
def reset_FF(Client_BO, pos):
    # FF
    # Reset all fault bits
    Client_BO.write_register(pos, 1<<15)
    return True

@safe_modbus
def read_procedure(Client_BO, pos):
    # PROCEDURE
    length = 2
    response = Client_BO.read_holding_registers(pos, count=length)
    word = response.registers[0]
    # make sure bit 2,3,4 are all 0, otherwise return error
    if (word >> 2) & 1 == 1:
        raise ValueError("Procedure is still being started. Value is not valid.")
    elif (word >> 3) & 1 == 1:
        raise ValueError("Procedure is still being stopped. Value is not valid.")
    elif (word >> 4) & 1 == 1:
        raise ValueError("Procedure is still being aborted. Value is not valid.")
    # Get state at bit 0 and interlocked at bit 1
    state = (word >> 0) & 1 == 1
    interlocked = (word >> 1) & 1 == 1
    exit = response.registers[1]
    # TODO: make return into a named tuple
    return state, interlocked, exit

@safe_modbus
def start_procedure(Client_BO, pos):
    # PROCEDURE
    # Write 1 to bit 2 to start procedure
    Client_BO.write_registers(pos, [1<<2, 0])
    return True

@safe_modbus
def stop_procedure(Client_BO, pos):
    # PROCEDURE
    # Write 1 to bit 3 to stop procedure
    Client_BO.write_registers(pos, [1<<3, 0])
    return True

@safe_modbus
def abort_procedure(Client_BO, pos):
    # PROCEDURE
    # Write 1 to bit 4 to abort procedure
    Client_BO.write_registers(pos, [1<<4, 0])
    return True