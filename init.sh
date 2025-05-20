#!/usr/bin/sh
echo "Starting initialization script for run control."

# =================================================
# Populate dependencies folder
# =================================================
# copies config from .gitmodules to .git/config
git submodule sync --recursive
# clones submodules if not already cloned
git submodule update --init --recursive
# updates submodules to latest commit
git submodule update --remote --recursive

# =================================================
# Set up conda environment
# =================================================
echo "Setting up conda environment..."
# update conda to latest version
conda update -y -n base conda
if conda info --envs | grep -q runcontrol; then
  # if runcontrol environment already exists, update it
  echo "Conda environment \"runcontrol\" already exists. Updating...";
  conda env update --file ./dependencies/conda_rc.yml --prune;
else
  # if runcontrol environment doesn't exist, create it
  echo "Conda environment \"runcontrol\" doesn't exist. Creating environment...";
  conda env create -y -n runcontrol --file ./dependencies/conda_rc.yml;
fi
conda activate runcontrol;

# =================================================
# Generate all ui and resources files
# =================================================
echo "Generating Qt UI and resources files."
# generate all .py files from .ui files
for f in ./ui/*.ui; do
  name="${f%%.ui}";
  pyside6-uic $f -o "$name.py";
done
# generate all .py files from .qrc files
pyside6-rcc ./resources/resources.qrc -o ./resources_rc.py

# =================================================
# Add dependencies folder to PATH
# =================================================
export PATH=$PATH:$PWD/dependencies

# =================================================
# Install arduino packages
# =================================================
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
SCRIPT_UPDATED=false
SUDOER_SET=false

# Check if root script already installed
if [ -f "$ROOT_SCRIPT_DEST" ]; then
    echo "Root components already installed."
    SOURCE_HASH=$(sha256sum "$ROOT_SCRIPT_SOURCE")
    DESTINATION_HASH=$(sha256sum "$ROOT_SCRIPT_DEST")
    # Check if the script is up to date
    if [ "$SOURCE_HASH" = "$DESTINATION_HASH" ]; then
        echo "Root script is up to date."
        SCRIPT_UPDATED=true
    else
        echo "Root script is not up to date. Updating..."
        SCRIPT_UPDATED=false
    fi
else
    echo "Root script not installed yet."
    SCRIPT_UPDATED=false
fi

if [ "$SCRIPT_UPDATED" = "false" ]; then
    echo "Installing root script."
    sudo install -o root -g root -m 755 "$ROOT_SCRIPT_SOURCE" "$ROOT_SCRIPT_DEST" || {
        echo "Failed to install root script"
        exit 1
    }
    echo "Root script successfully installed."
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

# =================================================
# Handle group permissions for current user
# =================================================
if ! groups "$CURRENT_USER" | grep -q '\busbusers\b'; then
    sudo usermod -aG usbusers "$CURRENT_USER"
    echo "Added $CURRENT_USER to usbusers group."
fi
if ! groups "$CURRENT_USER" | grep -q '\bdialout\b'; then
    sudo usermod -aG dialout "$CURRENT_USER"
    echo "Added $CURRENT_USER to dialout group."
fi
echo "Group permissions set for $CURRENT_USER. Please log out and log back in for the changes to take effect."

# =================================================
# Execute root init script
# =================================================
echo "Executing root script"
sudo "$ROOT_SCRIPT_DEST"

echo "Run Control environment successfully initialized."
