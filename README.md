
# SBC-RunControl
Data acquisition software for SBC.

# Installing Dependencies
1. Install [Miniconda3](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) or [Anaconda3](https://docs.anaconda.com/free/anaconda/install/index.html).
2. Open conda prompt inside this directory.
3. Update conda package list by running `conda update conda; conda update --all`.
4. Create `runcontrol` conda environment from file by running `conda env create --name runcontrol --file=conda_rc.yml`. This should install all required packages in the new environment, including `PySide6`, `pip`, `numpy`, `matplotlib`, `paramiko`, etc.
5. Install [Arduino IDE](https://arduino.github.io/arduino-cli/0.35/installation/) and add the installation 
   directory to `PATH`. This is used by run control to compile and upload sketches to Arduinos.
6. Activate environment by running `conda activate runcontrol`.
7. Now it's good to go! Start the program by running `python3 rc.py`.

# Using Qt designer and resource manager
Qt designer can be used to edit all the UI components, then a python script can load the UI and add functionalities to the widgets (buttons, labels, etc). To use the designer program, run `pyside6-designer` within the conda envrionment. After saving the `.ui` file, run `pyside6-uic filename.ui -o filename.py` to generate the python file. This step needs to be repeated for every `.ui` file.

The resource manager in Qt can be used as a convinient way to keep track of all resources. This can include icons, images, config files, data, etc. The list is saved as a `.qrc` file, and can be edited in the designer. To update the resources, run `pyside6-rcc filename.qrc -o resources_rc.py` to generate python script. The `resources_rc` filename seems to be the default expected by the uic program. After placing the `resources_rc.py` file in the working directory, the program should load all data correctly.

# Program Components
- Main Controls
- Trigger
- Bubble Chamber
- Slow Data/PLC
    - Pressures
    - Temperatures
    - Valve status
    - Bellow positions
- Scintillation
- Acoustics
- Cameras
- Settings

