import json
import os
import logging
from PySide6.QtCore import QTimer, QObject, Slot, Signal, QThread
from collections import namedtuple
import copy
import json
from ctypes import *
import src.global_variable  as gv #BM
import subprocess
import signal
import time


class Acoustics(QObject):
    acous_started = Signal(str)
    acous_stopped = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.logger = logging.getLogger("rc")
        self.acous_config = self.main.config_class.config["acous"]

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.periodic_task)

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"Acoustics module initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):
        pass

    @Slot(str)                                                                      
    def start_event(self,module):

        self.config = self.main.config_class.run_config[module]
        
        self.logger.info(f"Acoustic data acquisition starting.")                    
        process = subprocess.Popen(['python', '/home/sbc/packages/gati-linux-driver/Sdk/SBC-Piezo-Base-Code/sbc_reader_dll_wrapper.py'])             
        while True:
            if(gv.TRIG_LATCH==1):
                process.send_signal(signal.SIGINT)
                break                                                         
            if process.poll() != None:                                            
                process = subprocess.Popen(['python', '/home/sbc/packages/gati-linux-driver/Sdk/SBC-Piezo-Base-Code/sbc_reader_dll_wrapper.py']) 
            time.sleep(0.001) #time.sleep(0.0005)  # Sleep for 0.5 milliseconds
                                        
        self.logger.info(f"Acoustic data acquisition ended.")

    @Slot()
    def stop_event(self):
        self.client.close()
