#!/bin/bash
set -euo pipefail  # fail hard on errors

# install CAEN drivers
echo "Installing CAENDigitizer"
cd $HOME/RunControl/dependencies/CAENDrivers/CAENDigitizer*/lib/ && \
  bash ./install_x64
echo "Installing CAENComm"
cd $HOME/RunControl/dependencies/CAENDrivers/CAENComm*/lib/ && \
  bash ./install_x64
echo "Installing CAENVME"
cd $HOME/RunControl/dependencies/CAENDrivers/CAENVME*/lib/ && \
  bash ./install_x64
echo "Installing CAENUSB"
make -j10 -C $HOME/RunControl/dependencies/CAENDrivers/CAENUSB* && \
  make -j10 -C $HOME/RunControl/dependencies/CAENDrivers/CAENUSB* install

# install GaGe driver
echo "Installing GaGe driver"
cd $HOME/RunControl/dependencies/gati-linux-driver/ && \
  ./gagesc.sh install -c spider -ad && \
  ./gagesc.sh sdkdev -t install
