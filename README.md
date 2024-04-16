
# SBC-RunControl
Data acquisition software for SBC.

## Installing Dependencies
1. Install [Miniconda3](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) or [Anaconda3](https://docs.anaconda.com/free/anaconda/install/index.html).
2. Open the main repository directory in a shell terminal. Run `source ./init.sh` to initialize the environment for 
   run control. The script will do the following things:
   - Update conda.
   - If there is no conda environment called `runcontrol`, then create a new environment using 
     `dependencies/conra_rc.yml`. If it already exists, then update the packages to satisfy the file.
   - Activate `runcontrol` environment and generate all ui and resources files.
   - Download `arduino-cli` program, initialize, and download necessary libraries including `incbin` and `ArduinoJson`.
3. Now it's good to go! Start the program by running `python3 rc.py`.

## Documentations
- [**Program behavior**](docs/program_behavior.md): The states of operation of the run control program, and the 
  bahavior of its submodules.
- [**Dependencies**](docs/dependencies.md): A list of all dependencies and some tips on Qt usage.
- [**Project structure**](docs/project_structure.md): Folders and files in this repository, and what do they do.
- [**Data structure**](docs/data_format.md): Definition of data files saved by run control and related modules.
  - [**Configuration**](docs/data_format.md#configuration-file): Master configuration json file used by run control 
    software. Configuration files are generated from this file for each module.
  - [**Run Data**](docs/data_format.md#run-data): The run data is saved in the `RunData` tables in the slow control 
    SQL 
    database. There is one line per run.
  - [**Event Data**](docs/data_format.md#event-data): This data is saved in the SBC binary format using SBCBinaryFormat 
    library at the end of each event.
