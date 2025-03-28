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
│   ├── ArduinoSketches
│   │   ├── README.md
│   │   ├── clock/
│   │   ├── ln2autofill_rtd/
│   │   ├── ln2autofill_scale/
│   │   ├── position/
│   │   ├── trigger/
│   │   └── uti-docs/
│   ├── NI_USB6501/
│   └── conda_rc.yml
├── docs
│   ├── api.rst
│   ├── conf.py
│   ├── data_format.md
│   ├── dependencies.md
│   ├── images/
│   ├── index.md
│   ├── program_behavior.md
│   ├── project_structure.md
│   ├── requirements.txt
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
### `preparing`
When the run control program starts, it will first enter the `preparing` state. In this state it will instantiate all the secondary threads and workers, and load the GUI with initial information.
- Arduinos: Flash sketch to board?
- SiPM amp: run IV curve if no data for today?
### `idle`
After the `preparing` state ends, it will enter the `idle` state. The "Start Run" button will be available to start a new run, and any changes to the configuration can be applied immediately.
### `starting_run`
After the "Start Run" button is pressed, the program will enter this state. When all modules are ready, it will enter into `starting_event` state.
- GUI: set run ID, event ID, event livetime, run livetime
- Writer: create run folder. Save current config file. Create log file and add to logger. Initialize run_data variable.
- SiPM amp: bias SiPMs
- Config: save current config to run folder.
### `stopping_run`
This is the state then the run is stopping.
- SiPM amp: unbias SiPM
- Write run data into SQL RunData table.
### `starting_event`
When the `starting_run` state ends, or then `stopping_event` state ends, and neither "Stop Run" button is pressed, or maximum number of events is reached, the program will start a new event. It will send out a `Signal` to all modules. When all modules are ready, it will enter `active` state.
- GUI: set event ID and event livetime display.
- Writer: Create folder for the event.
- Camera: Send config file. Start `imdaq` script.
- NIUSB: set input/output pins. Sends out `trig_reset` signal. Set outputs to camera.
- CAEN: save config file. Start data acquisition.
- Acoustics: save config file. Start data acquisition.
### `stopping_event`
This is the state when the event is stopping. A `Signal` is sent to all modules to save data for the event. After the state is finished, it will enter into either `starting_event` to start a new event, or `stopping_run` to end the run. That decision will depend on if the "Stop Run" button is pressed, or maximum number of events is reached.
- Writer: save event binary data.
- Cameras: Take remaining images. Save images, info table and log into event folder.
- CAEN: stop data acquisition, save data to event folder.
- Acoustics: save data to event folder.
### `active`
All modules in this state will be actively taking data in buffer, and waiting for a trigger. When a trigger is received by run control, it will enter into `stopping_event` state.
GUI: Start event timer. Update event livetime and run livetime. Check for max event time to send out trigger.

## Modules
The run control program is organized in modules. The main module is responsible for the graphical interface. All other modules are launched in their own threads. Each module is defined by a python script in the `src/` folder, and one or more instances of a module may be created. For example, there are three camera threads, each controlling a camera RPi. A thread is created at the start of the program for each module, and the module class is instantiated into a worker inside that thread. The communication between modules and the main thread is handled by PySide6 signals and threads, and there is also limited number of communication between modules directly. The threads live across events and runs, and are only killed when run control is closed.

### UI Loader
This modules contains the classes for settings window and log window, as well as helper classes. The settings window is the central place where the user can set configuration for both run control and all modules. Every field in `config.json` can be edited from here. The log window display all logs generated by run control. Note that logs produced by child processes run from run control will not be included here, even they may appear in the terminal. These include camera RPi logs and SiPM amp outputs.

### Config
The main job of the config module is to translate between the fields in the settings window, the config dictionary in python, and the `config.json` file. When run control starts, it reads configuration from `config.json` and stores it in a dictionary. When settings window is opened, it fills all of the fields in the GUI from the dictionary. When "Apply" button is clicked in settings window, the dictioanry is updated using the fields in the GUI. When "Save" button is clicked, the dictionary is updated using the GUI, and then the `config.json` is also overwritten using the new dictionary.  
When a run starts, it saves a copy of the config dictionary for the run, so any subsequent changes in the settings window when the run is active won't affect the current run. It then saves the run config into a `config.json` in the run data folder, and then updates the config files for cameras and arduinos.

### NI USB

### Arduinos

### Writer

### SQL

### Cameras

### CAEN

### SiPM Amp

### Acoustics
