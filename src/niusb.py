from dependencies.NI_USB6501.ni_usb_6501 import *
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal
import numpy as np
import os
import time


class NIUSB(QObject):
    pin_definition = {  # input / output from run control
        "trig": "output",  # trigger
        "latch": "input",  # trigger latch
        "reset": "output",  # trigger reset
        "state_cam1": "input",  # state confirmation from pi
        "comm_cam1": "output",  # state comm to pi
        "trigen_cam1": "output",  # trigger enable signal
        "state_cam2": "input",
        "comm_cam2": "output",
        "trigen_cam2": "output",
        "state_cam3": "input",
        "comm_cam3": "output",
        "trigen_cam3": "output",
        "trigff_rc": "input",  # trigger first fault, run control
        "trigff_p": "input",  # pressure
        "trigff_but": "input",  # external button
        "trigff_cam1": "input",  # camera video trigger
        "trigff_cam2": "input",
        "trigff_cam3": "input",
        "trigff_piezo": "input",  # piezo acoustic trigger
        "trigff_ar": "input",  # Kulite trigger for Ar
        "trigff_cf4": "input",  # kulite trigger for CF
        "": "input",
        # and more ...
    }

    ff_dict = {  # dictionary for display name of first faults
        "trigff_rc": "Run Control",  # trigger first fault, run control
        "trigff_p": "Pressure",  # pressure
        "trigff_but": "Ext Button",  # external button
        "trigff_cam1": "Cam1",  # camera video trigger
        "trigff_cam2": "Cam2",
        "trigff_cam3": "Cam3",
        "trigff_piezo": "Piezo",  # piezo acoustic trigger
        "trigff_ar": "Kulite Ar",  # Kulite trigger for Ar
        "trigff_cf4": "Kulite CF4",  # kulite trigger for CF
    }

    run_started = Signal(str)
    event_started = Signal(str)
    trigger_detected = Signal()
    event_stopped = Signal(str)
    run_stopped = Signal(str)
    trigger_ff = Signal(str)

    def __init__(self, mainwindow):
        super().__init__()
        self.main = mainwindow
        self.config = mainwindow.config_class.config["dio"]["niusb"]
        self.logger = logging.getLogger("rc")

        self.timer = QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.periodic_task)
        self.ff_pin = ""

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"NI_USB class initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):

        # when state is active and a trigger latch is detected, send out signal
        if (self.main.run_state == self.main.run_states["active"] and
                self.dev and
                self.dev.read_pin(*self.reverse_config["latch"])):
            self.trigger_detected.emit()

    @Slot()
    def check_niusb(self):
        try:
            os.stat("/dev/niusb")
        except:
            self.logger.error(f"NIUSB not connected.")
        self.logger.debug(f"NIUSB connected")

    @Slot(str)
    def send_trigger(self, source):
        self.ff_pin = source
        self.dev.write_pin(*self.reverse_config["trig"], 1)

    @Slot()
    def start_run(self):
        # check serial connection and initialize object
        self.check_niusb()
        self.dev = get_adapter()
        if not self.dev:
            self.logger.error("NI USB device not found!")

        # get config
        self.config = self.main.config_class.run_config["dio"]["niusb"]
        self.reverse_config = {}

        # use output/input table to get io mask
        # if undefined, set as input
        for k in self.config.keys():
            port, pin = [int(s) for s in k.split(".")]
            try:
                self.reverse_config[self.config[k]] = (port, pin)
                # set io of pin to 1 if output, else 0
                self.dev.change_pin_io(port, pin, self.pin_definition[self.config[k]] == "output")
            except IndexError:
                self.logger.error(f"Pin {k} {self.config[k]} invalid.")
                continue

        self.run_started.emit("niusb")

    @Slot()
    def start_event(self):
        # unset first faults
        self.ff_pin = ""
        # lower trigger pin
        self.dev.write_pin(*self.reverse_config["trig"], 0)
        # send out trigger reset signal
        self.dev.write_pin(*self.reverse_config["reset"], 1)
        # wait until trigger latch is low
        while self.dev.read_pin(*self.reverse_config["latch"]):
            self.dev.write_pin(*self.reverse_config["trig"], 0)
            self.dev.write_pin(*self.reverse_config["reset"], 1)
        self.dev.write_pin(*self.reverse_config["reset"], 0)
        self.event_started.emit("niusb")

        # check cameras ready
        cam_ready = {"cam1": "idle", "cam2": "idle", "cam3": "idle"}
        while "idle" in cam_ready.values() or "starting" in cam_ready.values():
            for cam in cam_ready.keys():
                if cam_ready[cam] == "disabled" or cam_ready[cam] == "ready":
                    continue
                if not self.main.config_class.run_config["cam"][cam]["enabled"]:
                    cam_ready[cam] = "disabled"
                    self.logger.debug(f"{cam} is disabled.")
                elif cam_ready[cam] == "idle":
                    # starting up send trigen to false and comm to true
                    self.dev.write_pin(*self.reverse_config[f"trigen_{cam}"], False)
                    self.dev.write_pin(*self.reverse_config[f"comm_{cam}"], True)
                    cam_ready[cam] = "starting"
                elif cam_ready[cam] == "starting":
                    if self.dev.read_pin(*self.reverse_config[f"state_{cam}"]):
                        cam_ready[cam] = "ready"
                        self.logger.info(f"{cam} is ready.")
                        self.event_started.emit(cam)

        # wait for certain time before sending trig enable pin
        cam_trig = {"cam1": False, "cam2": False, "cam3": False}
        while False in cam_trig.values():
            for cam in cam_trig.keys():
                wait_time = self.main.config_class.run_config["cam"][cam]["trig_wait"]
                if cam_trig[cam]:
                    continue
                elif cam_ready[cam] == "disabled":
                    cam_trig[cam] = True
                elif self.main.event_timer.elapsed() > wait_time * 1000:
                    self.dev.write_pin(*self.reverse_config[f"trigen_{cam}"], True)
                    self.logger.info(f"{cam} trigger is enabled.")
                    cam_trig[cam] = True

    @Slot()
    def stop_event(self):
        # lower trigger pin
        self.dev.write_pin(*self.reverse_config["trig"], 0)
        # read FF pins
        for k in [k for k in self.reverse_config.keys() if "trigff" in k]:
            if self.dev.read_pin(*self.reverse_config[k]):
                self.logger.debug(k)
                # if no previous ff pin, set ff_pin to the pin name
                if self.ff_pin == "":
                    self.ff_pin = self.ff_dict[k]
                # if already set by RC signal, then pass
                elif self.ff_dict[k] == "Run Control" and self.ff_pin in ["Timeout", "Software"]:
                    continue
                # if more than one pin, report error
                else:
                    self.logger.warning(f"More than one first fault detected: {self.ff_pin} and {self.ff_dict[k]}")
        if self.ff_pin == "":
            self.logger.warning(f"No first fault pin detected.")
        else:
            self.logger.debug(f"First fault pin for the event is {self.ff_pin}")
        self.trigger_ff.emit(self.ff_pin)
        time.sleep(1)
        self.event_stopped.emit("niusb")

        cam_ready = {}
        for cam in ["cam1", "cam2", "cam3"]:
            if self.main.config_class.run_config["cam"][cam]["enabled"]:
                self.dev.write_pin(*self.reverse_config[f"comm_{cam}"], False)
                self.dev.write_pin(*self.reverse_config[f"trigen_{cam}"], False)
                # camera using reverse logic
                while not self.dev.read_pin(*self.reverse_config[f"state_{cam}"]):
                    time.sleep(0.01)
                    # print("cam not ready")
                self.logger.debug(f"{cam} is complete.")
                self.event_stopped.emit(cam)

    @Slot()
    def stop_run(self):
        self.dev.release_interface()
        self.logger.debug("NIUSB device released")
        self.run_stopped.emit("niusb")
