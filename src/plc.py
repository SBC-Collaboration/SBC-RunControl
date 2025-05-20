from pymodbus.client import ModbusTcpClient
import struct
import numpy as np
from functools import wraps

# PLC register map: https://github.com/SBC-Collaboration/SBC-PLC/blob/main/SBC_FNAL/SBC_FNAL/SBC_FNAL_MAIN/GVLs/MB.TcGVL
# slow control map: https://github.com/SBC-Collaboration/SBC-SlowControl/blob/main/slowcontrol_reconstruct/SBC_env.py
