# Usage

## Installation
1. Install [miniforge](https://github.com/conda-forge/miniforge) or [conda-forge](https://conda-forge.org/download/). This is preferred over miniconda and anaconda because of licensing problems of anaconda at Fermilab. If you already have those installed, it should still work, since the `conda_rc.yml` file has specified the channel. If there's problem, follow [these instructions](https://conda-forge.org/docs/user/transitioning_from_defaults/) to transition to conda-forge.
2. Open the main repository directory in a shell terminal. Run `source ./init.sh` to initialize the environment for 
   run control. The script will do the following things:
   - Update conda.
   - If there is no conda environment called `runcontrol`, then create a new environment using 
     `dependencies/conra_rc.yml`. If it already exists, then update the packages to satisfy the file.
   - Activate `runcontrol` conda environment.
   - Using PySide6 tools to generate python files from ui and resources files.
   - Add dependencies folder to system path.
   - Download `arduino-cli` program, initialize, and download necessary libraries including `incbin` and `ArduinoJson`.
3. Now it's good to go! Start the program by running `python rc.py`.

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
The dependencies of this project is managed in a few different ways. `PySide6` is a public python library installed from pip into the conda environment. `SBCBinaryFormat` is a custom python library that is compiled and installed locally using pip into the conda environment. `SBC-ArduinoSketches` and `NI_USB-6501` are custom/modified code that is included in this repository in the `dependencies/` folder. They are managed using `git subtree` comand. The drivers for CAEN and GaGe digitizers are also copied into `dependencies/` folder, but using `git submodule` command for copyright reasons. `Arduino-Cli` is a public command line program, and the binary executable is downloaded to the DAQ PC, and the path to it is specified in config file.

### Using `git subtree`
`git subtree` can be used to handle dependencies on external code. Unlike `git submodule` which contains a link to the original git repository, `git subtree` contains a hard copy of the repository. Here's a brief tutorial for using `git subtree`, using the example of `SBC-ArduinoSketches` which is saved to `dependencies/ArduinoSketches`.
- First add the `SBC-ArduinoSketches` as a remote in the `RunControl` repository: 
```bash
git remote add arduino-repo https://github.com/SBC-Collaboration/SBC-ArduinoSketches.git
```
- Check that the remote has been added. Run `git remote -v`. The output should be:
```bash
arduino-repo	https://github.com/SBC-Collaboration/SBC-ArduinoSketches.git (fetch)
arduino-repo	https://github.com/SBC-Collaboration/SBC-ArduinoSketches.git (push)
origin	https://github.com/SBC-Collaboration/SBC-RunControl.git (fetch)
origin	https://github.com/SBC-Collaboration/SBC-RunControl.git (push)
```
- Add the repository into git subtree: 
```bash
git subtree add --prefix {local directory being pulled into} {remote repo} {remote branch} --squash
``` 
In this example, it would be:
```bash
git subtree add --prefix dependencies/ArduinoSketches arduino-repo main --squash
```
This should copy the external repository in the the local directory. The `--squash` parameter consolidates all commit history of the external repository into one commit, simplifying the local repository history.
- After changes have been made locally in the `dependencies/ArduinoSketches` folder, committhe changes using `git add` and `git commit`.
- Upload the changes to external repository by running the following command in the main directory of `RunControl`:
```bash
git subtree push --prefix=dependencies/ArduinoSketches arduino-repo main
```
- Upload changes to `RunControl` repository by running `git push origin main`.
- If there has been some changes in the external repository, run `git subtree pull --prefix=dependencies/ArduinoSketches arduino-repo main` to pull the changes. Commit merges in `RunControl` repository and upload.

### Using `git submodule`
Like `git subtree`, `git submodule` also handles including other git repositories as dependencies. Submodules act as pointers to external repositories, which are managed independently, including access control and pointers to specific commits. Using the example of `CAENDrivers`, which has a nested working tree as `dependencies/CAENDrivers`. The remote repository of `CAENDrivers` is private, requiring authentication.  
- To download submodule repositories while cloning the main repo. By default, only the submodule configuration file `.gitmodules` and an empty folder is created at cloning.
```bash
> git clone --recurse-submodules https://github.com/SBC-Collaboration/SBC-RunControl.git RunControl
```
Downloading the submodules can also be done as a separate step at later times.
```bash
> git clone https://github.com/SBC-Collaboration/SBC-RunControl.git RunControl
> cd RunControl
RunControl> git submodule update --init --recursive  # Populates submodules
```
- To add the repository as a `git submodule` dependency, add the submodule, commit the changes in `.gitmodules` and `dependencies/CAENDrivers`, and push the commit to main repo. Note that cloning the submodule and pushing to remote may require token or public key authentication.
```bash
RunControl> git submodule add <submodule_url> <path> 
RunControl> git commit -m <commit_message>
RunControl> git push
```
For the `CAENDrivers` example, it would be
```bash
RunControl> git submodule add https://github.com/SBC-Collaboration/CAENDrivers.git dependencies/CAENDrivers
RunControl> git commit -m "Add CAENDrivers submodule"
RunControl> git push
```
- To make changes in the submodule locally, and push to remote of both submodule and main repositories.
1. Update the submodule
```bash
RunControl> cd dependencies/CAENDrivers
CAENDrivers> git add . 
CAENDrivers> git commit -m <commit_message>
CAENDrivers> git push
CAENDrivers> cd ../..
```
2. Update parent repo
```bash
RunControl> git add dependencies/CAENDrivers
RunControl> git commit -m <commit_message>
RunControl> git push
```
- To pull updates in the remote submodule repository:
```bash
RunControl> git submodule update --remote --recursive  # Pull latest version of submodules
RunControl> git add dependencies/CAENDrivers
RunControl> git commit -m <commit_message>
RunControl> git push
```

## Using Qt designer and resource manager
Qt designer can be used to edit all the UI components, then a python script can load the UI and add functionalities to the widgets (buttons, labels, etc). To use the designer program, run `pyside6-designer` within the conda envrionment. After saving the `.ui` file, run 
```bash
pyside6-uic filename.ui -o filename.py
``` 
to generate the python file. This step needs to be repeated for every `.ui` file.

The resource manager in Qt can be used as a convinient way to keep track of all resources. This can include icons, images, config files, data, etc. The list is saved as a `.qrc` file, and can be edited in the designer. To update the resources, run 
```bash
pyside6-rcc filename.qrc -o resources_rc.py
``` 
to generate python script. The `resources_rc` filename seems to be the default expected by the uic program. After placing the `resources_rc.py` file in the working directory, the program should load all data correctly.
