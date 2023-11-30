
# SBC-RunControl
Run control software for SBC

# Installing Dependencies
1. Install [Miniconda3](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) or [Anaconda3](https://docs.anaconda.com/free/anaconda/install/index.html).
2. Open conda prompt inside this directory.
3. Update conda package list by running `conda update conda; conda update --all`.
4. Create `runcontrol` conda environment from file by running `conda env create --name runcontrol --file=conda_rc.yml`. This should install all required packages in the new environment, including `PySide6`, `pip`, `numpy`, `matplotlib`, etc.
5. Activate environment by running `conda activate runcontrol`.
6. Now it's good to go! Start the program by running `python rc.py`.

# Program Components
- Main Controls
- Trigger
- Bubble Chamber
- Slow Data
    - Pressures
    - Temperatures
    - Valve status
    - Bellow positions
- Scintillation
- Acoustics
- Cameras
- Settings
