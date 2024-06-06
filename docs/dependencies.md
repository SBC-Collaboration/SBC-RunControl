# Dependencies

## Software Dependencies
- [**PySide6**](https://pypi.org/project/PySide6/): Python library for Qt6 GUI framework.
- [**Arduino-Cli**](https://arduino.github.io/arduino-cli/0.35/): Command line utility for compiling and uploading Arduino sketches to the boards.
- [**SBC-ArduinoSketches**](https://github.com/SBC-Collaboration/SBC-ArduinoSketches): This repository includes Arduino sketches for clock, trigger fan-in/fan-out, and position sensing Arduinos.
- [**SBCBinaryFormat**](https://github.com/SBC-Collaboration/SBCBinaryFormat.git): This repository provides the python library for writing to and reading from sbc binary data format.
- [**NI_USB-6501**](https://github.com/shengzhiheng/NI_USB-6501): A third party driver for NI USB device, modified to work with Python3.
- [**Icons8**](https://icons8.com/icon/set/file/ios): Icons used in the program is by Icons8, specifically the IOS17 Outlined icon set.
- Other standard python libraries including `logging`, `json`, `time`, `datetime`, `os`, `sys`, `enum`, `re`, etc.

## Using Qt designer and resource manager
Qt designer can be used to edit all the UI components, then a python script can load the UI and add functionalities to the widgets (buttons, labels, etc). To use the designer program, run `pyside6-designer` within the conda envrionment. After saving the `.ui` file, run `pyside6-uic filename.ui -o filename.py` to generate the python file. This step needs to be repeated for every `.ui` file.

The resource manager in Qt can be used as a convinient way to keep track of all resources. This can include icons, images, config files, data, etc. The list is saved as a `.qrc` file, and can be edited in the designer. To update the resources, run `pyside6-rcc filename.qrc -o resources_rc.py` to generate python script. The `resources_rc` filename seems to be the default expected by the uic program. After placing the `resources_rc.py` file in the working directory, the program should load all data correctly.