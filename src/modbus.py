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

# Wrapper to handle exceptions in Modbus functions
def safe_modbus(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            pos = kwargs.get('pos') if 'pos' in kwargs else args[1] if len(args) > 1 else '?'
            print(f"ERROR in {func.__name__} at register {pos}: {e}")
            return None
    return wrapper

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
        self.registers = self.config["registers"]
        self.client = None

        self.timer = QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.periodic_task)
    
    # Private helper functions to read / write Modbus registers
    @safe_modbus
    def _read_float(self, pos, endian='<'):
        # PARAM_F
        length = 2
        response = self.client.read_holding_registers(pos, count=length)
        packed_registers = struct.pack(f"{endian}HH", *response.registers)
        value_float = struct.unpack(f"{endian}f", packed_registers)[0]
        return value_float

    @safe_modbus
    def _write_float(self, pos, value, endian='<'):
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
        response = self.client.write_registers(pos, words)
        return True

    @safe_modbus
    def _read_int(self, pos, endian='<'):
        # PARAM_I
        length = 1
        response = self.client.read_holding_registers(pos, count=length)
        value_int = struct.unpack(f"{endian}i", response.registers[0])[0]
        return value_int

    @safe_modbus
    def _read_time(self, pos, endian='<'):
        # PARAM_T, TIME
        length = 2
        response = self.client.read_holding_registers(pos, count=length)
        words = response.registers
        packed = struct.pack(f"{endian}HH", *words)
        value_time = struct.unpack(f"{endian}i", packed)[0]
        return value_time  # ms

    @safe_modbus
    def _write_time(self, pos, value, endian='<'):
        # PARAM_T
        t = int(value)
        bytes = struct.pack(f'{endian}i', t)
        words = struct.unpack(f'{endian}HH', bytes)
        response = self.client.write_registers(pos, words)
        return True

    @safe_modbus
    def _read_flag(self, pos):
        # FLAG
        length = 1
        response = self.client.read_holding_registers(pos, count=length)
        word = response.registers[0]
        # Get running state at bit 0 and interlocked at bit 1
        running = (word >> 0) & 1 == 1
        interlocked = (word >> 1) & 1 == 1
        # TODO: make return into a named tuple
        return running, interlocked

    @safe_modbus
    def _write_flag(self, pos, value):
        # FLAG
        # If true, set flag, set 1 to bit 1
        # If false, reset flag, set 1 to bit 2
        self.client.write_register(pos, 1<<(1 if value else 2))
        return True

    @safe_modbus
    def _read_FF(self, pos):
        # FF
        length = 1
        response = self.client.read_holding_registers(pos, count=length)
        word = response.registers[0]
        # Check if each bit is true or false
        fault_bits = [(word >> i) & 1 == 1  for i in range(15)]
        return fault_bits

    @safe_modbus
    def _reset_FF(self, pos):
        # FF
        # Reset all fault bits
        self.client.write_register(pos, 1<<15)
        return True

    @safe_modbus
    def _read_procedure(self, pos):
        # PROCEDURE
        length = 2
        response = self.client.read_holding_registers(pos, count=length)
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
    def _get_procedure_state(self, pos):
        return self._read_procedure(pos)[0]

    @safe_modbus
    def _start_procedure(self, pos):
        # PROCEDURE
        # Write 1 to bit 2 to start procedure
        self.client.write_register(pos, 1<<2)
        return True

    @safe_modbus
    def _stop_procedure(self, pos):
        # PROCEDURE
        # Write 1 to bit 3 to stop procedure
        self.client.write_register(pos, 1<<3)
        return True

    @safe_modbus
    def _abort_procedure(self, pos):
        # PROCEDURE
        # Write 1 to bit 4 to abort procedure
        self.client.write_register(pos, 1<<4)
        return True

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Modbus module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        if (self.main.run_state == self.main.run_states["active"] and self.pressure_cycle ==  False): 
            pressure_state  = _read_procedure(self.registers["PRESSURE_CYCLE"]) 
            if(pressure_state[0] == False):
                start_pressure = _start_procedure(self.registers["PRESSURE_CYCLE"])
                if((start_pressure)==True):
                    self.pressure_cycle  = True
                    self.logger.debug(f" Pressure cycle started successfully.")
                else:
                    self.logger.error(f" Pressure cycle start is unsuccessful.")
 
    @Slot()
    def start_run(self):
        self.client = ModbusTcpClient(self.config["hostname"], port=self.config["port"])
        try:
            self.connected = self.client.connect()
            self.logger.debug(f"Beckoff PLC connected: {str(self.connected)}.")
        except Exception as e:
            self.logger.error(f"Beckoff PLC connection failed: {e}.")
        self.run_started.emit("modbus")


    @Slot()                                                                      
    def start_event(self):
        if (self._start_procedure(self.registers["WRITE_SLOWDAQ"])) == True:
            self.logger.debug(f"SLOW DAQ process started.")
        else:
            self.logger.error(f"SLOW DAQ process start is unsuccessful.")

        if ((self._write_float(self.registers["PCYCLE_PSET"],self.config["pressure"]["profile1"]["setpoint"]))==True):
            self.logger.debug(f"write of PSET is successful.")
        else:
            self.logger.error(f"write of PSET is unsuccessful.")
            self.error_msg.emit("pset")
        self.event_started.emit("modbus")


    @Slot()
    def stop_event(self):
        slowdaq_counter = 0
        stop_procedure_wait = 30 * 1000  # ms
        abort_procedure_wait = 30 * 1000  # ms
        pc_register = self.registers["PRESSURE_CYCLE"]
        self.stop_event_timer = QElapsedTimer(self)
        self.stop_event_timer.start()

        while(self._get_procedure_state(pc_register) and \
            self.stop_event_timer.elapsed() < stop_procedure_wait):
            time.sleep(0.1)
        if self._get_procedure_state(pc_register):
            stop_state = self._stop_procedure(pc_register)
            if stop_state != True:
                abort_state = self._abort_procedure(pc_register)
                if abort_state != True:
                    self.error_msg.emit("PRESSURE_CYCLE still running")
                else:
                    self.logger.debug("PRESSURE_CYCLE aborted.")
            else:
                self.logger.debug("PRESSURE_CYCLE stopped.")
        else:
            self.logger.debug("PRESSURE_CYCLE ended.")
        
        # Read the first fault bits
        fault_bits = self._read_FF(self.registers["PCYCLE_ABORT_FF"])
        self.logger.debug("fault_bits.")
        self.logger.debug(fault_bits)
        # TODO: write the fault bits in a file
        slowdaq_stop = self._stop_procedure(self.registers["WRITE_SLOWDAQ"])
        self.pressure_cycle = False
        if (slowdaq_stop == True):
            self.logger.debug(f"SLOW_DAQ process ended successfully.")
        else:
            self.logger.error(f"SLOW_DAQ process didn't end successfully.")
       
        # TODO: write log file from plc to RC
        self.event_stopped.emit("modbus")

    @Slot()
    def stop_run(self):
        self.client.close()
        self.run_stopped.emit("modbus")
