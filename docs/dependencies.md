# Dependencies

## Installation
1. Install [Miniconda3](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) or [Anaconda3](https://docs.anaconda.com/free/anaconda/install/index.html).
2. Open the main repository directory in a shell terminal. Run `source ./init.sh` to initialize the environment for 
   run control. The script will do the following things:
   - Update conda.
   - If there is no conda environment called `runcontrol`, then create a new environment using 
     `dependencies/conra_rc.yml`. If it already exists, then update the packages to satisfy the file.
   - Activate `runcontrol` environment and generate all ui and resources files.
   - Download `arduino-cli` program, initialize, and download necessary libraries including `incbin` and `ArduinoJson`.
3. Now it's good to go! Start the program by running `python3 rc.py`.

## Software Dependencies
- [**PySide6**](https://pypi.org/project/PySide6/): Python library for Qt6 GUI framework.
- [**Arduino-Cli**](https://arduino.github.io/arduino-cli/0.35/): Command line utility for compiling and uploading Arduino sketches to the boards.
- [**SBC-ArduinoSketches**](https://github.com/SBC-Collaboration/SBC-ArduinoSketches): This repository includes Arduino sketches for clock, trigger fan-in/fan-out, and position sensing Arduinos.
- [**SBCBinaryFormat**](https://github.com/SBC-Collaboration/SBCBinaryFormat): This repository provides the python library for writing to and reading from sbc binary data format.
- [**RedDigitizerplusplus**](https://github.com/shengzhiheng/RedDigitizerplusplus): This is a PyBind11 wrapper around a C++ wrapper for CAEN's C API. It can be used to control the CAEN digitizer directly from python.
- [**CAENDigitizer**](https://www.caen.it/products/caendigitizer-library/): Library of functions for CAEN Digitizers high level management.
- [**CAENComm**](https://www.caen.it/products/caencomm-library/): Interface library for CAEN Data Acquistion Modules/
- [**CAENVMELib**](https://www.caen.it/products/caenvmelib-library/): Interface library for CAEN VME Bridges.
- [**SBC-Piezo-Base-Code**](https://github.com/SBC-Collaboration/SBC-Piezo-Base-Code): This is a C++ driver for the GaGe digitizer. It is modified to work around the pre-trigger length limit imposed by the GaGe driver.
- [**NI_USB-6501**](https://github.com/shengzhiheng/NI_USB-6501): A third party driver for NI USB device, modified to work with Python3.
- [**Icons8**](https://icons8.com/icon/set/file/ios): Icons used in the program is by Icons8, specifically the IOS17 Outlined icon set.
- Other standard python libraries including `logging`, `json`, `time`, `datetime`, `os`, `sys`, `enum`, `re`, etc.

## Managing and Updating Dependencies
The dependencies of this project is managed in a few different ways. `PySide6` is a public python library installed from pip into the conda environment. `SBCBinaryFormat` is a custom python library that is compiled and installed locally using pip into the conda environment. `SBC-ArduinoSketches` and `NI_USB-6501` are custom/modified code that is included in this repository in the `dependencies` folder. They are managed using `git subtree` comand. `Arduino-Cli` is a public command line program, and the binary executable is downloaded to the DAQ PC, and the path to it is specified in config file.

### Using `git subtree`
`git subtree` can be used to handle dependencies on external code. Unlike `git submodule` which contains a link to the original git repository, `git subtree` contains a hard copy of the repository. Here's a brief tutorial for using `git subtree`, using the example of `SBC-ArduinoSketches` which is saved to `dependencies/ArduinoSketches`.
- First add the `SBC-ArduinoSketches` as a remote in the `RunControl` repository: 
```
git remote add arduino-repo https://github.com/SBC-Collaboration/SBC-ArduinoSketches.git
```
- Check that the remote has been added. Run `git remote -v`. The output should be:
```
arduino-repo	https://github.com/SBC-Collaboration/SBC-ArduinoSketches.git (fetch)
arduino-repo	https://github.com/SBC-Collaboration/SBC-ArduinoSketches.git (push)
origin	https://github.com/SBC-Collaboration/SBC-RunControl.git (fetch)
origin	https://github.com/SBC-Collaboration/SBC-RunControl.git (push)
```
- Add the repository into git subtree: 
```
git subtree add --prefix {local directory being pulled into} {remote repo} {remote branch} --squash
``` 
In this example, it would be:
```
git subtree add --prefix dependencies/ArduinoSketches arduino-repo main --squash
```
This should copy the external repository in the the local directory. The `--squash` parameter consolidates all commit history of the external repository into one commit, simplifying the local repository history.
- After changes have been made locally in the `dependencies/ArduinoSketches` folder, committhe changes using `git add` and `git commit`.
- Upload the changes to external repository by running the following command in the main directory of `RunControl`:
```
git subtree push --prefix=dependencies/ArduinoSketches arduino-repo main
```
- Upload changes to `RunControl` repository by running `git push origin main`.
- If there has been some changes in the external repository, run `git subtree pull --prefix=dependencies/ArduinoSketches arduino-repo main` to pull the changes. Commit merges in `RunControl` repository and upload.

## Using Qt designer and resource manager
Qt designer can be used to edit all the UI components, then a python script can load the UI and add functionalities to the widgets (buttons, labels, etc). To use the designer program, run `pyside6-designer` within the conda envrionment. After saving the `.ui` file, run 
```
pyside6-uic filename.ui -o filename.py
``` 
to generate the python file. This step needs to be repeated for every `.ui` file.

The resource manager in Qt can be used as a convinient way to keep track of all resources. This can include icons, images, config files, data, etc. The list is saved as a `.qrc` file, and can be edited in the designer. To update the resources, run 
```
pyside6-rcc filename.qrc -o resources_rc.py
``` 
to generate python script. The `resources_rc` filename seems to be the default expected by the uic program. After placing the `resources_rc.py` file in the working directory, the program should load all data correctly.
