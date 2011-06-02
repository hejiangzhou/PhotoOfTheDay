#!/bin/bash

# run the script daily
crontab -l | { cat; echo "@daily $(readlink -f $(dirname $0))/main.py > /dev/null 2>&1"; } | crontab -

# You would like to add this script to the startup application list of Gnome
# Do it by hand.
