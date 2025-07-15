from ni_usb_6501 import *
import usb.core
import logging
from PySide6.QtCore import QTimer, QObject, QThread, Slot, Signal, QMutex, QWaitCondition
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

    drive_definition = {  # input / output from run control
        "trig": "open_collector",  # trigger
        "latch": "open_collector",  # trigger latch
        "reset": "open_collector",  # trigger reset
        "state_cam1": "open_collector",  # state confirmation from pi
        "comm_cam1": "active_drive",  # state comm to pi
        "trigen_cam1": "active_drive",  # trigger enable signal
        "state_cam2": "open_collector",
        "comm_cam2": "active_drive",
        "trigen_cam2": "active_drive",
        "state_cam3": "open_collector",
        "comm_cam3": "active_drive",
        "trigen_cam3": "active_drive",
        "trigff_rc": "open_collector",  # trigger first fault, run control
        "trigff_p": "open_collector",  # pressure
        "trigff_but": "open_collector",  # external button
        "trigff_cam1": "open_collector",  # camera video trigger
        "trigff_cam2": "open_collector",
        "trigff_cam3": "open_collector",
        "trigff_piezo": "open_collector",  # piezo acoustic trigger
        "trigff_ar": "open_collector",  # Kulite trigger for Ar
        "trigff_cf4": "open_collector",  # kulite trigger for CF
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
        self.cams_ready = []

        self.run_mutex = QMutex()
        self.run_wait = QWaitCondition()
        self.run_ready = False
        self.cam_config_mutex = QMutex()
        self.cam_config_wait = QWaitCondition()
        self.cam_config_ready = False

    @Slot()
    def run(self):
        self.timer.start()
        self.logger.debug(f"NI_USB class initialized in {QThread.currentThread().objectName()}.")

    @Slot()
    def periodic_task(self):

        # when state is active and a trigger latch is detected, send out signal
        # python evaluates conditions lazily, so it shouldn't have too much of an effect on performance
        if (self.main.run_state == self.main.run_states["active"] and
                self.dev and
                self.dev.read_pin(*self.reverse_config["latch"])):
            self.trigger_detected.emit()

        # camera trigger enable test
        if self.main.run_state == self.main.run_states["active"] and False in self.cam_trig.values():
            elapsed_time = self.main.event_timer.elapsed()
            for cam in self.cam_trig.keys():
                wait_time = self.main.config_class.run_config["cams"][cam]["trig_wait"]
                if self.cam_trig[cam]:
                    continue
                elif elapsed_time > wait_time * 1000:
                    self.dev.write_pin(*self.reverse_config[f"trigen_{cam}"], True)
                    self.logger.info(f"Camera {cam} trigger is enabled.")
                    self.cam_trig[cam] = True

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
        self.logger.info("Software trigger sent.")

    @Slot()
    def start_run(self):
        # check serial connection and initialize object
        self.check_niusb()
        try:
            self.dev = get_adapter()
        except usb.core.USBError as e:
            dev = usb.core.find(idVendor=ID_VENDOR, idProduct=ID_PRODUCT)
            if dev.is_kernel_driver_active(0):
                dev.detach_kernel_driver(0)
            self.dev = get_adapter()
        self.dev.reset()
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
                # set the drive type to active drive
                self.dev.change_pin_io(port, pin,
                                       self.pin_definition[self.config[k]] == "output",
                                       self.drive_definition[self.config[k]] == "active_drive")
            except IndexError:
                self.logger.error(f"Pin {k} {self.config[k]} invalid.")
                continue

        # initialize output pins
        for cam in ["cam1", "cam2", "cam3"]:
            self.dev.write_pin(*self.reverse_config[f"comm_{cam}"], False)
            self.dev.write_pin(*self.reverse_config[f"trigen_{cam}"], False)

        self.dev.write_pin(*self.reverse_config["trig"], False)
        self.dev.write_pin(*self.reverse_config["reset"], True)

        self.run_mutex.lock()
        self.run_ready = True
        self.run_wait.wakeAll()
        self.run_mutex.unlock()
        self.run_started.emit("niusb")

    @Slot()
    def start_event(self):
        # unset first faults
        self.ff_pin = ""
        # lower trigger pin
        self.dev.write_pin(*self.reverse_config["trig"], False)
        # send out trigger reset signal
        self.dev.write_pin(*self.reverse_config["reset"], True)
        # wait until trigger latch is low
        while self.dev.read_pin(*self.reverse_config["latch"]):
            self.dev.write_pin(*self.reverse_config["trig"], False)
            self.dev.write_pin(*self.reverse_config["reset"], True)
        self.dev.write_pin(*self.reverse_config["reset"], 0)
        # reset trigff ready flag
        self.main.trigff_mutex.lock()
        self.main.trigff_ready = False
        self.main.trigff_mutex.unlock()
        self.event_started.emit("niusb")

        # check if cameras config are saved
        self.cam_config_mutex.lock()
        while not self.cam_config_ready:
            self.cam_config_wait.wait(self.cam_config_mutex)
        self.cam_config_mutex.unlock()

        # check cameras ready
        cam_ready = {"cam1": "idle", "cam2": "idle", "cam3": "idle"}
        while "idle" in cam_ready.values() or "starting" in cam_ready.values():
            for cam in cam_ready.keys():
                if cam_ready[cam] == "disabled" or cam_ready[cam] == "ready":
                    continue
                if not self.main.config_class.run_config["cams"][cam]["enabled"]:
                    cam_ready[cam] = "disabled"
                    self.event_started.emit(f"{cam}-disabled")
                    self.logger.debug(f"{cam} is disabled.")
                elif cam_ready[cam] == "idle":
                    # starting up send trigen to false and comm to true
                    self.dev.write_pin(*self.reverse_config[f"trigen_{cam}"], False)
                    self.dev.write_pin(*self.reverse_config[f"comm_{cam}"], True)
                    cam_ready[cam] = "starting"
                elif cam_ready[cam] == "starting":
                    if self.dev.read_pin(*self.reverse_config[f"state_{cam}"]):
                        cam_ready[cam] = "ready"
                        self.dev.write_pin(*self.reverse_config[f"comm_{cam}"], False)
                        self.logger.info(f"Camera {cam} is ready.")
                        self.event_started.emit(cam)

        # wait for certain time before sending trig enable pin
        self.cam_trig = {"cam1": False, "cam2": False, "cam3": False}
        for cam in self.cam_trig.keys():
            if cam_ready[cam] == "disabled":
                self.cam_trig[cam] = True

    @Slot()
    def stop_event(self):
        # lower trigger pin
        self.dev.write_pin(*self.reverse_config["trig"], False)
        # self.dev.write_pin(*self.reverse_config["reset"], True)
        # read FF pins
        for k in [k for k in self.reverse_config.keys() if "trigff" in k]:
            if self.dev.read_pin(*self.reverse_config[k]):
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
        self.main.trigff_mutex.lock()
        self.main.trigff_ready = True
        self.main.trigff_wait.wakeAll()
        self.main.trigff_mutex.unlock()
        self.event_stopped.emit("niusb")

        cam_ready = {}
        for cam in ["cam1", "cam2", "cam3"]:
            if self.main.config_class.run_config["cams"][cam]["enabled"]:
                self.dev.write_pin(*self.reverse_config[f"comm_{cam}"], False)
                self.dev.write_pin(*self.reverse_config[f"trigen_{cam}"], False)
                while self.dev.read_pin(*self.reverse_config[f"state_{cam}"]):
                    time.sleep(0.01)
                self.logger.debug(f"{cam} is complete.")
                self.event_stopped.emit(cam)
            else:
                self.event_stopped.emit(f"{cam}-disabled")

    @Slot()
    def stop_run(self):
        self.dev.release_interface()
        self.logger.debug("NIUSB device released")
        self.run_stopped.emit("niusb")

        # reset run initialized flag
        self.run_mutex.lock()
        self.run_ready = False
        self.run_mutex.unlock()
