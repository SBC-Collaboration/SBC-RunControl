# Project Structure
This documentation provides a short explanation of the different folders and files in this repository. Below is the 
structure of this repository:
```
├── README.md
├── conda_rc.yml
├── config.json
├── docs
│   ├── data_format.md
│   └── project_structure.md
│   └── rc.log
├── rc.py
├── resources
├── resources_rc.py
├── src
│   ├── arduinos.py
│   ├── cameras.py
│   ├── config.py
│   ├── sipm_amp.py
│   ├── ui_loader.py
│   └── workers.py
├── ui
│   ├── logwindow.py
│       ├── logwindow.ui
│       ├── mainwindow.py
│       ├── mainwindow.ui
│       ├── settingswindow.py
│       └── settingswindow.ui
└── dependencies
    ├── ArduinoSketches
    │   ├── README.md
    │   ├── clock
    │   │   ├── README.md
    │   │   ├── clock.ino
    │   │   └── clock_config.json
    │   ├── position
    │   │   ├── MgsModbus.cpp
    │   │   ├── MgsModbus.h
    │   │   └── position.ino
    │   ├── trigger
    │   │   ├── README.md
    │   │   └── TRIG.ino
    │   └── uti-docs
    │       └── level_meter_read.py
    └── SBCBinaryFormat
        ├── README.md
        ├── cpp
        └── python
        ├── README.md
        ├── examples
        │   ├── test.sbc.bin
        │   └── writer_example.py
        ├── sbcbinaryformat
        │   ├── __init__.py
        │   └── files.py
        └── setup.py
```