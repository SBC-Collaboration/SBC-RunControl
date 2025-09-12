import os
import logging
from PySide6.QtCore import QTimer, QElapsedTimer, QObject, Slot, Signal, QThread
from pymodbus.client import ModbusTcpClient
import struct
import time
from functools import wraps
from enum import Enum
from sbcbinaryformat import Writer as SBCWriter
from src.guardian import ErrorCodes

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
    error = Signal(int)

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

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Modbus module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        if (self.main.run_state == self.main.run_states["active"] and 
            self.enabled and self.pressure_cycle ==  False): 
            pressure_state  = self._read_procedure(self.registers["PRESSURE_CYCLE"]) 
            if(pressure_state is None or pressure_state[0] == False):
                start_pressure = self._start_procedure(self.registers["PRESSURE_CYCLE"])
                if((start_pressure)==True):
                    self.pressure_cycle  = True
                    self.logger.debug(f"Pressure cycle started successfully.")
                else:
                    self.logger.error(f"Pressure cycle start failed.")
                    self.error.emit(ErrorCodes.PLC_PRESSURE_CYCLE_START_FAILED)
    
    @Slot()
    def turn_off_leds(self):
        # Turn off LEDs
        ret = True
        ret = ret and self._write_float(self.registers["LED1_OUT"], 0)
        ret = ret and self._write_float(self.registers["LED2_OUT"], 0)
        ret = ret and self._write_float(self.registers["LED3_OUT"], 0)
        if ret:
            self.logger.debug(f"LED control voltages successfully changed to 0.")
        else:
            self.logger.error(f"Writing of LED control voltages failed.")
            self.error.emit(ErrorCodes.PLC_LED_OFF_FAILED)

    @Slot()
    def start_run(self):
        self.config = self.main.config_class.run_config["plc"]
        self.enabled = self.config["enabled"]
        if not self.enabled:
            self.run_started.emit("modbus-disabled")
            return

        self.client = ModbusTcpClient(self.config["hostname"], port=self.config["port"])
        try:
            self.connected = self.client.connect()
            self.logger.debug(f"Beckoff PLC connected: {str(self.connected)}.")
        except Exception as e:
            self.logger.error(f"Beckoff PLC connection failed: {e}.")
            self.error.emit(ErrorCodes.PLC_CONNECTION_FAILED)
        self.run_started.emit("modbus")


    @Slot()                                                                      
    def start_event(self):
        if not self.enabled:
            self.event_started.emit("modbus-disabled")
            return
        
        if (self._start_procedure(self.registers["WRITE_SLOWDAQ"])) == True:
            self.logger.debug(f"SLOW DAQ process started.")
        else:
            self.logger.error(f"SLOW DAQ process start failed.")
            self.error.emit(ErrorCodes.PLC_SLOWDAQ_START_FAILED)

        if (self._write_float(self.registers["PCYCLE_PSET"],
                               self.config["pressure"]["profile1"]["setpoint"]) == True):
            self.logger.debug(f"write of PSET is successful.")
        else:
            self.logger.error(f"write of PSET failed.")
            self.error.emit(ErrorCodes.PLC_PSET_FAILED)
            self.event_started.emit("modbus-error")
            return
        
        # turn on LEDs
        ret = True
        ret = ret and self._write_float(self.registers["LED_MAX"], self.config["led_control_max"])
        ret = ret and self._write_float(self.registers["LED1_OUT"],
            min(self.config["led1_control"], self.config["led_control_max"]) 
            if self.config["led1_enabled"] else 0)
        ret = ret and self._write_float(self.registers["LED2_OUT"],
            min(self.config["led2_control"], self.config["led_control_max"])
            if self.config["led2_enabled"] else 0)
        ret = ret and self._write_float(self.registers["LED3_OUT"],
            min(self.config["led3_control"], self.config["led_control_max"])
            if self.config["led3_enabled"] else 0)
        if ret:
            self.logger.debug(f"Writing of LED control voltages successful.")
        else:
            self.logger.error(f"Writing of LED control voltages failed.")
            self.error.emit(ErrorCodes.PLC_LED_ON_FAILED)
            self.event_started.emit("modbus-error")
            return
        
        self.event_started.emit("modbus")

    @Slot()
    def stop_event(self):
        if not self.enabled:
            self.event_stopped.emit("modbus-disabled")
            return

        # Stop the pressure cycle if it's running
        self._stop_pressure_cycle()

        # Read the first fault bits, PSET value, and exit code of the pressure cycle procedure
        plc_data = {
            "SLOWDAQ_FF": self._read_FF(self.registers["SLOWDAQ_FF"]),
            "PCYCLE_ABORT_FF": self._read_FF(self.registers["PCYCLE_ABORT_FF"]),
            "PCYCLE_FASTCOMP_FF": self._read_FF(self.registers["PCYCLE_FASTCOMP_FF"]),
            "PCYCLE_SLOWCOMP_FF": self._read_FF(self.registers["PCYCLE_SLOWCOMP_FF"]),
            "PCYCLE_PSET": self._read_float(self.registers["PCYCLE_PSET"]),
            "PCYCLE_EXIT_CODE": self._read_procedure(self.registers["PRESSURE_CYCLE"])[2],
            "LED1_OUT": self._read_float(self.registers["LED1_OUT"]),
            "LED2_OUT": self._read_float(self.registers["LED2_OUT"]),
            "LED3_OUT": self._read_float(self.registers["LED3_OUT"]),
            "LED_MAX": self._read_float(self.registers["LED_MAX"]),
        }

        # write the plc_data in a file
        headers = ["SLOWDAQ_FF","PCYCLE_ABORT_FF","PCYCLE_FASTCOMP_FF","PCYCLE_SLOWCOMP_FF", "PCYCLE_PSET", 
                   "PCYCLE_EXIT_CODE", "LED1_OUT", "LED2_OUT", "LED3_OUT", "LED_MAX"]
        dtypes = [ "i1", "i1", "i1", "i1", "f", "u2", "f", "f", "f", "f"]
        shapes = [[15], [15], [15], [15], [1], [1], [1], [1], [1], [1]]
        with SBCWriter(
                os.path.join(
                    self.main.event_dir, "plc.sbc"
                ),
                headers, dtypes, shapes
        ) as plc_writer:
            plc_writer.write(plc_data)
                    
        slowdaq_stop = self._stop_procedure(self.registers["WRITE_SLOWDAQ"])
        self.pressure_cycle = False
        time.sleep(1)
        if (self._read_procedure(self.registers["WRITE_SLOWDAQ"])[0]):
            self.logger.error("SLOW_DAQ process didn't end successfully.")
            self.error.emit(ErrorCodes.PLC_SLOWDAQ_STOP_FAILED)
            self.event_stopped.emit("modbus-error")
        else:
            self.logger.debug("SLOW_DAQ process ended successfully.")
            
        # copy data file from plc to RC
        hostname = self.config["hostname"]
        share = self.config["smb_share"]
        perm_file = os.path.expanduser("~/.config/runcontrol/smb_token")
        remote_file = self.config["smb_filename"]
        local_path = os.path.join(self.main.event_dir, "slow_daq.sbc")
        if not os.path.exists(perm_file):
            self.logger.error(f"PLC SMB Permission file {perm_file} does not exist.")
            self.error.emit(ErrorCodes.PLC_SMB_PERMISSION_FILE_MISSING)
            self.event_stopped.emit("modbus-error")
            return
        command = f"smbclient //{hostname}/{share} -A {perm_file} -c 'get {remote_file} {local_path}'"
        ret_os = os.system(command)
        if (ret_os > 0):
            self.logger.error("PLC log File copy is unsuccessful.")
            self.event_stopped.emit("modbus-error")
            return
        else:
            self.logger.debug("PLC log File copied successfully.")

        self.event_stopped.emit("modbus")

    @Slot()
    def stop_run(self):
        if not self.enabled:
            self.run_stopped.emit("modbus-disabled")
            return
        
        self.client.close()
        self.run_stopped.emit("modbus")
    
    def _stop_pressure_cycle(self):
        """
        Helper function to stop the pressure cycle procedure.
        First it waits some time for the procedure to finish.
        If it is still running after the wait, it tries to stop it.
        If stopping fails, or after some time it's still running, it tries to abort.
        If aborting fails, or after some time it's still running, it raises an error.
        """
        trigger_proc_wait_ms = self.config["trig_timeout"] * 1000
        stop_proc_wait_ms = self.config["stop_timeout"] * 1000
        abort_proc_wait_ms = self.config["abort_timeout"] * 1000
        pc_register = self.registers["PRESSURE_CYCLE"]
        self.stop_event_timer = QElapsedTimer()
        self.stop_event_timer.start()

        # Check status every 100ms until the procedure is not running anymore, or timeout occurs
        while (self._get_procedure_state(pc_register) and
            self.stop_event_timer.elapsed() < trigger_proc_wait_ms):
            time.sleep(0.1)

        if not self._get_procedure_state(pc_register):
            self.logger.debug("PRESSURE_CYCLE ended.")
            return
        
        # If timed out, try to stop procedure
        ret = self._stop_procedure(pc_register)
        while (ret and self._get_procedure_state(pc_register) and
                self.stop_event_timer.elapsed() < stop_proc_wait_ms):
            time.sleep(0.1)
        
        if not self._get_procedure_state(pc_register):
            self.logger.warning("PRESSURE_CYCLE stopped.")
            return
        
        # If still running, or stop failed, try to abort procedure
        ret = self._abort_procedure(pc_register)
        while (ret and self._get_procedure_state(pc_register) and
                self.stop_event_timer.elapsed() < abort_proc_wait_ms):
            time.sleep(0.1)
        
        # If abort failed, or timeout, raise an error
        if not self._get_procedure_state(pc_register):
            self.logger.warning("PRESSURE_CYCLE aborted.")
        else:
            self.logger.error("PRESSURE_CYCLE failed to abort.")
            self.error.emit("PRESSURE_CYCLE still running")
    
    #############################################################
    # Private helper functions to read / write Modbus registers
    #############################################################

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

    class _FlagBits(Enum):
        """Enum for bits in FLAG."""
        RUNNING = 0
        SET = 1
        RESET = 2
        INTERLOCKED = 3

    @safe_modbus
    def _read_flag(self, pos):
        # FLAG
        length = 1
        response = self.client.read_holding_registers(pos, count=length)
        word = response.registers[0]
        # Get running state at bit 0 and interlocked at bit 1
        running = (word >> self._FlagBits.RUNNING.value) & 1 == 1
        interlocked = (word >> self._FlagBits.INTERLOCKED.value) & 1 == 1
        # TODO: make return into a named tuple
        return running, interlocked

    @safe_modbus
    def _write_flag(self, pos, value):
        # FLAG
        # If true, set flag, set 1 to bit 1
        # If false, reset flag, set 1 to bit 2
        return self.client.write_register(pos, 1<<(self._FlagBits.SET.value if value else self._FlagBits.RESET.value))

    @safe_modbus
    def _read_FF(self, pos):
        # FF
        length = 1
        response = self.client.read_holding_registers(pos, count=length)
        word = response.registers[0]
        fault_bits = [(word >> i) & 1   for i in range(15)]
        return fault_bits

    @safe_modbus
    def _reset_FF(self, pos):
        # FF
        # Reset all fault bits
        return self.client.write_register(pos, 1<<15)

    class _ProcedureBits(Enum):
        """Enum for bits in procedure."""
        RUNNING = 0
        INTERLOCKED = 1
        START = 2
        STOP = 3
        ABORT = 4

    @safe_modbus
    def _read_procedure(self, pos):
        # PROCEDURE
        length = 2
        response = self.client.read_holding_registers(pos, count=length)
        word = response.registers[0]
        # make sure bit 2,3,4 are all 0, otherwise return error
        if (word >> self._ProcedureBits.START.value) & 1 == 1:
            raise ValueError("Procedure is still being started. Value is not valid.")
        elif (word >> self._ProcedureBits.STOP.value) & 1 == 1:
            raise ValueError("Procedure is still being stopped. Value is not valid.")
        elif (word >> self._ProcedureBits.ABORT.value) & 1 == 1:
            raise ValueError("Procedure is still being aborted. Value is not valid.")
        # Get state at bit 0 and interlocked at bit 1
        state = (word >> self._ProcedureBits.RUNNING.value) & 1 == 1
        interlocked = (word >> self._ProcedureBits.INTERLOCKED.value) & 1 == 1
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
        self.client.write_register(pos, 1<<self._ProcedureBits.START.value)
        return True

    @safe_modbus
    def _stop_procedure(self, pos):
        # PROCEDURE
        # Write 1 to bit 3 to stop procedure
        self.client.write_register(pos, 1<<self._ProcedureBits.STOP.value)
        return True

    @safe_modbus
    def _abort_procedure(self, pos):
        # PROCEDURE
        # Write 1 to bit 4 to abort procedure
        self.client.write_register(pos, 1<<self._ProcedureBits.ABORT.value)
        return True
