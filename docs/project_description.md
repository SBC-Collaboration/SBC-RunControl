# Project Description
This documentation describes the general way the run control program works, and what the main thread and the modules do at each state.

## Project Structure
This documentation provides a short explanation of the different folders and files in this repository. Below is the 
structure of this repository:
```
.
├── README.md
├── config.json
├── dependencies
│   ├── ArduinoSketches/
│   ├── CAENDrivers/
│   ├── gati-linux-driver/
│   ├── conda_rc.yml
│   └── root-init.sh
├── docs
│   ├── images/
│   ├── .readthedocs.yaml
│   ├── api.rst
│   ├── conf.py
│   ├── data_format.md
│   ├── index.md
│   ├── project_structure.md
│   └── usage.rst
├── init.sh
├── rc.py
├── resources/
├── src
│   ├── acoustics.py
│   ├── arduinos.py
│   ├── caen.py
│   ├── cameras.py
│   ├── config.py
│   ├── niusb.py
│   ├── plc.py
│   ├── sipm_amp.py
│   ├── sql.py
│   ├── ui_loader.py
│   └── writer.py
└── ui
    ├── custom_widgets.py
    ├── logwindow.ui
    ├── mainwindow.ui
    ├── quitdialog.ui
    └── settingswindow.ui
```

## Run States
The run control program uses multithreading to avoid freezing the GUI when things are happening in the background. Specifically, it has one main thread and a thread for each module. For the secondary threads, there is one worker per thread. The threads communicate with each other via `Signal` and `Slot`.  
At the Start of a run, the main thread will send out a `run_starting` signal. This signal is connected to the `start_run` method of each module worker. (TODO: then the main thread waits for all modules to return a signal that they are ready to go active.) A similar process happens at every state transition.
There are seven states, which are `preparing`, `idle`. `starting_run`, `stopping_run`, `starting_event`, `stopping_event`, `active`. 

### Preparing
When the run control program starts, it will first enter the `preparing` state. In this state it will instantiate all the secondary threads and workers, and load the GUI with initial information.
- Config: Load config from file to a dictionary in memory.

### Idle
After the `preparing` state ends, it will enter the `idle` state. The "Start Run" button will be available to start a new run, and any changes to the configuration can be applied immediately.

### Starting Run
After the "Start Run" button is pressed, the program will enter this state. When all modules are ready, it will enter into `starting_event` state.
- GUI: set run ID, event ID, event livetime, run livetime
- Writer: create run folder. Save current config file. Create log file and add to logger. Initialize run_data variable.
- SQL: Insert a new row for the current run into the Run Data table.
- SiPM amp: Bias SiPMs.
- CAEN: Establish connection. Apply configuration to CAEN. 
- Arduinos: Check if the code on the arduino is the same as the one in the repository. This includes any json configuration files. If they are different, compile the code in the repository and upload to the arduino.
- Camera: Send config file. Start `imdaq` script.
- Config: save current config to run folder.
- Modbus: Start connection to the PLC modbus server. 

### Stopping Run
This is the state then the run is stopping. If autorun is selected and this run is not stopped by manually pressing the button, a new run will automatically start after this one.
- SQL: Update the row for current event with end of run exit code and timestamp.
- SiPM amp: unbias SiPM
- Writer: Write run info binary file.
- Camera: close connection to camera.
- NIUSB: Release USB device.

### Starting Event
When the `starting_run` state ends, or then `stopping_event` state ends, and neither "Stop Run" button is pressed, or maximum number of events is reached, the program will start a new event. It will send out a `Signal` to all modules. When all modules are ready, it will enter `active` state.
- GUI: set event ID and event livetime display.
- Writer: Create folder for the event.
- NIUSB: Set input/output pins. Sends out `trig_reset` signal. Set outputs to camera.
- CAEN: Start data acquisition.
- Acoustics: Save config file. Start a data acquisition process.
- Modbus: Start SLOWDAQ procesure, and set pressure setpoint.
- NIUSB: Send out trigger reset signal until trigger latch is back to low.
- SQL: Insert row for the current event.

### Stopping Event
This is the state when the event is stopping. A `Signal` is sent to all modules to save data for the event. After the state is finished, it will enter into either `starting_event` to start a new event, or `stopping_run` to end the run. That decision will depend on if the "Stop Run" button is pressed, or maximum number of events is reached.
- Writer: save event binary data.
- SQL: Update row for current event inth the Event Data with information like exit code and livetime. Update the row for current run in the Run Data table with up to date information.
- Modbus: wait for PLC pressure cycle procedure to stop, and stop/abort if times out. Stops SLOWDAQ procedure and copies file into event folder at `slow_daq.sbc`. Saves PLC first fault bits into `plc.sbc`.
- Cameras: Take remaining images. Save images, info table and log into event folder.
- CAEN: Stop data acquisition. Retrieve any data from CAEN buffer to PC. Save data to event folder.
- Acoustics: Terminate the data taking process. Transfer all data to PC's memory. Save data around trigger to event folder.
- NIUSB: Retrieve first fault information. Monitor that all cameras successfully goes back into idle state.

### Active
All modules in this state will be actively taking data in buffer, and waiting for a trigger. When a trigger is received by run control, it will enter into `stopping_event` state.
- GUI: Start event timer. Update event livetime and run livetime. Check for max event time to send out trigger.
- Acoustics: Check if the GaGe process is still running. If it has quitted after the buffer is full, start another process.
- CAEN: Retrieve data from CAEN buffer to PC memory on a loop. 
- Camera: (In NIUSB module) send out start event digital signal. Send out trigger enable signal after certain wait time.
- Modbus: Start PRESSURE_CYCLE procedure.

## Modules
The run control program is organized in modules. The main module is responsible for the graphical interface. All other modules are launched in their own threads. Each module is defined by a python script in the `src/` folder, and one or more instances of a module may be created. For example, there are three camera threads, each controlling a camera RPi. A thread is created at the start of the program for each module, and the module class is instantiated into a worker inside that thread. The communication between modules and the main thread is handled by PySide6 signals and threads, and there is also limited number of communication between modules directly. The threads live across events and runs, and are only killed when run control is closed.

### UI Loader
This modules contains the classes for settings window and log window, as well as helper classes. The settings window is the central place where the user can set configuration for both run control and all modules. Every field in `config.json` can be edited from here. The log window display all logs generated by run control. Note that logs produced by child processes run from run control will not be included here, even they may appear in the terminal. These include camera RPi logs and SiPM amp outputs.

### Config
The main job of the config module is to translate between the fields in the settings window, the config dictionary in python, and the `config.json` file. When run control starts, it reads configuration from `config.json` and stores it in a dictionary. When settings window is opened, it fills all of the fields in the GUI from the dictionary. When "Apply" button is clicked in settings window, the dictioanry is updated using the fields in the GUI. When "Save" button is clicked, the dictionary is updated using the GUI, and then the `config.json` is also overwritten using the new dictionary.  
When a run starts, it saves a copy of the config dictionary for the run, so any subsequent changes in the settings window when the run is active won't affect the current run. It then saves the run config into a `config.json` in the run data folder, and then updates the config files for cameras and arduinos.

### NI USB
Using the third party custom driver, this modules handles all digitital input/output requests from run control to the NI USB6501 device. It defines a name and direction for each of the pins, and handles reading from and writing to the pins. Specifically, it handles communication to and from the trigger arduino and the camera RPis. 

### Arduinos
At the start of each run, the Arduinos module checks that the build on the Arduino is up to date. It generates a zip file containing the `.ino` C++ file as well as wll supporting files, including the `.json` configuration file. Then it compares the zip file to the existing zip file in the build folder. If that zip file doesn't exist, or if they are different, the module will compile the code and upload to the corresponding Arduino, while overwriting the zip file with the newer version. If the two zip files are the same, then nothing will happen to prevent unnecessary writes to the EEPROM.

### Writer
The writer module is responsible for writing the event info into a binary file in the event data folder. This file includes event ID, livetime, and trigger source. This is roughly the same as the data saved in **EventData** SQL table. TODO: Write a `run_info` file including data about each run, similar to the **RunData** table.

### SQL
The SQL module sets up a connection when run control starts, and closes connection when run control quits. At the start of each run, it inserts a line into the **RunData** table with information including run ID, livetime, sources, user provided comments, active datastreams, pressure setpoint (if same for all events), and driver versions. At the end of each event, it updates number of events, livetime, comments, etc. This ensures a software crash will not cause all data to be lost. At the end of each event, a new line is also inserted into **EventData** table, including event livetime, event pressure setpoint, and trigger source.

### Cameras
Before this module starts for a run, the **Config** module saves a `.json` file for each camera in the shared data folder. At the start of each run, this module establishes SSH connections to the camera Raspberry Pis. Then it waits for the NIUSB module to finish setting up the digital input / output lines. Afterwards, it starts up the camera server script. The start and end of each event is handled by the NIUSB module only via the digital IO signals. At end of run, this module closes the SSH connection.

### CAEN
This module uses the `red_caen` C++ driver to communicate with the CAEN digitizer via USB. When a run starts, the CAEN module reads configuration from the master Run Control configuration and populates fields in the `GlobalConfiguration` and `GroupConfiguration` structs. Then it establishes a serial connection, sets configuration, reads them back from the digitizer, and clears the buffer. At the start of an event, it sets up the `SBCBinaryFormat` writer, and enables acquisition through the driver. When an event is active, the module runs a loop retrieving raw data from digitizer back to memory handled by the driver, and decodes into structured waveform formats. Retrievals needs to happen frequently before the on-board buffer fills up, and number of triggers retrieved each time is also limited in configuration. The retrieved data is saved in a buffer managed by the module. At the end of the event, the module disables CAEN acquisition using software, and retrieves all data left on the on-board buffer into the module's buffer. Then it saves all data to file in the SBC binary format. At the end of a run, the module releases all buffer and handle to the digitizer.

### SiPM Amp
At the start of a run this modules checks the time of last IV curve taken. If it is longer than the duration in setting, it will start taking an IV curve, adn save data to the data folder. Then at the start and end of an event, it will bias and unbias the SiPMs. 

### Acoustics
The acoustics module controls the GaGe digitizer using the provided `gati-linux-driver`, as well as the custom `SBC-Piezo-Base-Code`. We need ~100 ms of data at 1 MHz for 8 channels around the bubble trigger. This is much lower than the on-board buffer size of the GaGe digitizer, but more than the length limit imposed on the pre-trigger length. The work around is to start an acquisition and immediately sends a software trigger, wait for the buffer to fill up, which takes about 4 minutes. If no bubble trigger happens during this time, this modules kills the acquisition instance and starts again. If there is a bubble trigger, it immediately stops acquisition, retrieves all data from the digitizer to the PC, and save the period of interest to SBC binary file. When a run starts, run control saves a `.ini` file to the main repository directory, which the GaGe driver then loads.

### PLC
Run control communicates with the PLC using Modbus in this module. It opens and closes the Modbus-TCP connection at the start and end of a run, respectively. When a event starts, it starts the `WRITE_SLOWDAQ` procedure on the PLC, starts data taking. Also it sets all relavent variables for the event, like pressure setpoint. When the event becomes active, it start the `PRESSURE_CYCLE` procedure, telling the PLC to start a pressure cycle. When a trigger happens at the end of an event, the module waits until the `PRESSURE_CYCLE` procedure ends, reads the `PCYCLE_*_FF` for any first fault information, stops the `WRITE_SLOWDAQ` procedure, and copies the data via SMB to the data folder. 

### Digiscope
This module uses NI CompactRIO device to serve as a global clock sync at 1 us resolution for up to 64 digital lines.
