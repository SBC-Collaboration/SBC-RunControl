import numpy
import ctypes
import time

# import the shared library
caen_path = "/home/sbc/packages/RedDigitizerplusplus/libcaen_runcontrol.so"
lib = ctypes.CDLL(caen_path)

# declare C structure to allocate memory
# for documentation, see run control or RedDigitizer++ code
num_groups = 4
num_ch_per_group = 8

class CAENGlobalConfig(ctypes.Structure):
    _fields_ = [
        ("MaxEventsPerRead", ctypes.c_uint32),
        ("RecordLength", ctypes.c_uint32),
        ("PostTriggerPorcentage", ctypes.c_uint32),
        ("EXTAsGate", ctypes.c_bool),
        ("EXTTriggerMode", ctypes.c_uint8),
        ("SWTriggerMode", ctypes.c_uint8),
        ("CHTriggerMode", ctypes.c_uint8),
        ("AcqMode", ctypes.c_uint8),
        ("IOLevel", ctypes.c_uint8),
        ("TriggerOverlappingEn", ctypes.c_bool),
        ("MemoryFullModeSelection", ctypes.c_bool),
        ("TriggerPolarity", ctypes.c_uint8),
        ("DecimationFactor", ctypes.c_uint16),
        ("MajorityLevel", ctypes.c_uint32),
        ("MajorityCoincidenceWindow", ctypes.c_uint32)
    ]

class ChannelsMask(ctypes.Structure):
    _fields_ = [
        ('CH', ctypes.c_bool * num_ch_per_group)
    ]

class CAENGroupConfig(ctypes.Structure):
    _fields_ = [
        ('Enabled', ctypes.c_bool),
        ('TriggerMask', ChannelsMask),
        ('AcquisitionMask', ChannelsMask),
        ('DCOffset', ctypes.c_uint32),
        ('DCCorrections', ctypes.c_uint8 * num_ch_per_group),
        ('DCRange', ctypes.c_uint8),
        ('TriggerThreshold', ctypes.c_uint32)
    ]

# declare argument and return types for used functions
lib.caen_init.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint32]
lib.caen_init.restype = ctypes.c_void_p  # Returns a void* (generic pointer)
lib.caen_destroy.argtypes = [ctypes.c_void_p]
lib.caen_destroy.restype = None
lib.caen_is_connected.argtypes = [ctypes.c_void_p]
lib.caen_is_connected.restype = ctypes.c_int
lib.caen_get_board_info.argtypes = [ctypes.c_void_p]
lib.caen_get_board_info.restype = ctypes.c_void_p
lib.caen_get_global_configs.argtypes = [ctypes.c_void_p]
lib.caen_get_global_configs.restype = ctypes.c_void_p
lib.caen_get_group_configs.argtypes = [ctypes.c_void_p]
lib.caen_get_group_configs.restype = ctypes.c_void_p
lib.caen_get_number_of_events.argtypes = [ctypes.c_void_p]
lib.caen_get_number_of_events.restype = ctypes.c_uint
lib.caen_get_current_max_buffer.argtypes = [ctypes.c_void_p]
lib.caen_get_current_max_buffer.restype = ctypes.c_uint
lib.caen_setup.argtypes = [ctypes.c_void_p, ctypes.POINTER(CAENGlobalConfig), CAENGroupConfig * num_groups]
lib.caen_setup.restype = None
lib.caen_reset.argtypes = [ctypes.c_void_p]
lib.caen_reset.restype = None
lib.caen_enable_acquisition.argtypes = [ctypes.c_void_p]
lib.caen_enable_acquisition.restype = None
lib.caen_disable_acquisition.argtypes = [ctypes.c_void_p]
lib.caen_disable_acquisition.restype = None
lib.caen_write_register.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32]
lib.caen_write_register.restype = None
lib.caen_read_register.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
lib.caen_read_register.restype = None
lib.caen_write_bits.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8]
lib.caen_write_bits.restype = None
lib.caen_software_trigger.argtypes = [ctypes.c_void_p]
lib.caen_software_trigger.restype = None
lib.caen_get_events_in_buffer.argtypes = [ctypes.c_void_p]
lib.caen_get_events_in_buffer.restype = ctypes.c_uint
lib.caen_retrieve_data_until_n_events.argtypes = [ctypes.c_void_p, ctypes.c_uint]
lib.caen_retrieve_data_until_n_events.restype = ctypes.c_int
lib.caen_decode_event.argtypes = [ctypes.c_void_p, ctypes.c_uint]
lib.caen_decode_event.restype = ctypes.c_void_p
lib.caen_decode_events.argtypes = [ctypes.c_void_p]
lib.caen_decode_events.restype = None
lib.caen_clear_data.argtypes = [ctypes.c_void_p]
lib.caen_clear_data.restype = None
lib.caen_get_waveform.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
lib.caen_get_waveform.restype = ctypes.c_void_p

# fill in configuration values
global_config = CAENGlobalConfig(
    MaxEventsPerRead=512,
    RecordLength=100,
    PostTriggerPorcentage=50,
    EXTAsGate=False,
    EXTTriggerMode=0,
    SWTriggerMode=0,
    CHTriggerMode=0,
    AcqMode=0,
    IOLevel=0,
    TriggerOverlappingEn=False,
    MemoryFullModeSelection=True,
    TriggerPolarity=0,
    DecimationFactor=1,
    MajorityLevel=0,
    MajorityCoincidenceWindow=0
)
# initialize structure
group_configs = (CAENGroupConfig * num_groups)()
for i in range(num_groups):
    group_configs[i].Enabled = True
    group_configs[i].TriggerMask = ChannelsMask()
    group_configs[i].AcquisitionMask = ChannelsMask()
    group_configs[i].DCOffset = 0x8000
    group_configs[i].DCRange = 1
    group_configs[i].TriggerThreshold = 1000

    for ch in range(num_ch_per_group):
        group_configs[i].TriggerMask.CH[ch] = True
        group_configs[i].AcquisitionMask.CH[ch] = True

    group_configs[i].DCCorrections = (ctypes.c_uint8 * num_ch_per_group)(0, 0, 0, 0, 0, 0, 0, 0)

# connect to digitizer
handle = lib.caen_init(2,0,0,0,0)

# check connection status
print(f"Connection status: {lib.caen_is_connected(handle)}")

# set up configuration
lib.caen_setup(handle, ctypes.byref(global_config), group_configs)

# read back configuration


# start acquisition
lib.caen_enable_acquisition(handle)
print("starting acquisition")
time.sleep(5)

# stop acquisition
lib.caen_disable_acquisition(handle)

# retrieve data

# decode event

# disconnect
lib.caen_destroy(handle)
print("CAEN object destroyed!")
