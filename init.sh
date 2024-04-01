#!/usr/bin/sh

# Set up conda environment
if conda info --envs | grep -q runcontrol; then
  echo "runcontrol environment already exists";
else
  echo "runcontrol environment doesn't exist. Creating environment";
  conda env create -y -n runcontrol --file ./dependencies/conda_rc.yml;
fi

conda activate runcontrol;

# install arduino packages
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=./dependencies sh
./dependencies/arduino-cli config init
./dependencies/arduino-cli lib update-index
./dependencies/arduino-cli lib upgrade
./dependencies/arduino-cli lib install incbin ArduinoJson
