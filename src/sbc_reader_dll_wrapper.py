import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ctypes import *
import os
import signal
import time
import subprocess
import signal
import os
import ctypes

lib = cdll.LoadLibrary('./SBCAbort.so')
x = lib.main()
