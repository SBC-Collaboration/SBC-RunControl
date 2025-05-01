#!/bin/bash
set -euo pipefail  # fail hard on errors

# install CAEN drivers
echo "Installing CAENDigitizer"
cd /home/sbc/RunControl/dependencies/CAENDrivers/CAENDigitizer*/lib/ && bash ./install_x64
echo "Installing CAENComm"
cd /home/sbc/RunControl/dependencies/CAENDrivers/CAENComm*/lib/ && bash ./install_x64
echo "Installing CAENVME"
cd /home/sbc/RunControl/dependencies/CAENDrivers/CAENVME*/lib/ && bash ./install_x64
echo "Installing CAENUSB"
make -j10 -C /home/sbc/RunControl/dependencies/CAENDrivers/CAENUSB* && make -j10 -C /home/sbc/packages/CAENUSB* install

# install GaGe driver
echo "Installing GaGe driver"
cd /home/sbc/RunControl/dependencies/gati-linux-driver/ && ./gagesc.sh install -c spider -ad
