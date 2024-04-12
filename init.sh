#!/usr/bin/sh
echo "Starting initialization script for run control."

# Set up conda environment
echo "Setting up conda environment..."
conda update -y -n base conda
if conda info --envs | grep -q runcontrol; then
  echo "Conda environment \"runcontrol\" already exists. Updating...";
  conda env update --file ./dependencies/conda_rc.yml --prune;
else
  echo "Conda environment \"runcontrol\" doesn't exist. Creating environment...";
  conda env create -y -n runcontrol --file ./dependencies/conda_rc.yml;
fi
conda activate runcontrol;

# install arduino packages
echo "Setting up Arduino cli and libraries..."
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=./dependencies sh
./dependencies/arduino-cli config init
./dependencies/arduino-cli lib update-index
./dependencies/arduino-cli lib upgrade
./dependencies/arduino-cli lib install incbin ArduinoJson
