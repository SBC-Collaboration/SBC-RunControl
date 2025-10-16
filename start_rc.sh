#!/bin/bash

if [ -f "$HOME/.bashrc" ]; then
  source "$HOME/.bashrc"
fi
conda activate runcontrol

SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd "$SCRIPT_DIR"
python rc.py
