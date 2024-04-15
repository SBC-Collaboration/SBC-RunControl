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

# add dependencies folder to PATH
export PATH=$PATH:$PWD/dependencies

# install arduino packages
echo "Setting up Arduino cli and libraries..."
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=./dependencies sh
arduino-cli config init
arduino-cli core install arduino:avr
arduino-cli lib update-index
arduino-cli lib upgrade
arduino-cli lib install incbin ArduinoJson Ethernet
