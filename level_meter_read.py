from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import struct
import time

history = []

# IP address of arduino ethernet shield
# should be the same as the one specified in arduino code
client = ModbusTcpClient("192.168.3.3", port=502)
client.connect()
# length of registers to read, 2 words
length = 2
# starting position of register
start = 2

while(True):
    # read the registers on arduino
    response = client.read_holding_registers(start,length)
    # convert from 32bit binary to a float, with big endian
    val = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big).decode_32bit_float()
    if (1+val != 0):
        percentage = val/(1.+val)
    else: percentage = 0.
    print(f"C1/C2: {val:.5},\tC1/(C1+C2): {percentage:.5}")

client.close()