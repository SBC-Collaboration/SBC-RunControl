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

# generate all ui and resources files
echo "Generating Qt UI and resources files."
for f in ./ui/*.ui; do
  name="${f%%.ui}";
  pyside6-uic $f -o "$name.py";
done
pyside6-rcc ./resources/resources.qrc -o ./resources_rc.py

# add dependencies folder to PATH
export PATH=$PATH:$PWD/dependencies

# install arduino packages
# user need to be in dialout group on linux
echo "Setting up Arduino cli and libraries..."
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=./dependencies sh
arduino-cli config init
arduino-cli update
arduino-cli upgrade
arduino-cli core install arduino:avr
arduino-cli lib install incbin ArduinoJson Ethernet

# =================================================
# Install root init script
# =================================================
ROOT_SCRIPT_DEST="/usr/local/bin/rc-init"
ROOT_SCRIPT_SOURCE="./dependencies/root-init.sh"
SUDOERS_FILE="/etc/sudoers.d/runcontrol"
CURRENT_USER=$(whoami)
SUDOER_SET=false

# Check if root script already installed
if [ -f "$ROOT_SCRIPT_DEST" ]; then
    echo "Root components already installed."
else
    echo "Installing root script."
    sudo install -o root -g root -m 755 "$ROOT_SCRIPT_SOURCE" "$ROOT_SCRIPT_DEST" || {
        echo "Failed to install root script"
        exit 1
    }
    echo "Root script installed."
fi

# Check if sudoer file has been set
if [ -f "$SUDOERS_FILE" ]; then
    echo "Sudoer file already exists."
    SUDOER_SET=true
fi

# Set up sudoer file if not set
if [ "$SUDOER_SET" = "false" ]; then
    echo "Setting sudoer file"
    sudo bash -c "echo '$CURRENT_USER ALL=(ALL) NOPASSWD: $ROOT_SCRIPT_DEST' > $SUDOERS_FILE" || {
        echo "Failed to create sudoers entry"
        sudo rm -f "$ROOT_SCRIPT_DEST"
        exit 1
    }

    # Set correct permission of sudoer
    sudo chmod 440 "$SUDOERS_FILE"

    # Check if sudoer file is valid
    if ! sudo visudo -cf "$SUDOERS_FILE"; then
        echo "Invalid sudo configuration. Rolling back..."
        sudo rm -f "$SUDOERS_FILE" "$ROOT_SCRIPT_DEST"
        exit 1
    fi
fi

# Execute root script
echo "Executing root script"
sudo "$ROOT_SCRIPT_DEST"

echo "Run Control environment successfully initialized."
