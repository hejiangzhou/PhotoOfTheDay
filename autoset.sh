#!/bin/bash

# run the script daily
crontab -l | { cat; echo "@daily /dir/to/main.py > /dev/null"; } | crontab -

# You would like to add this script to the startup application list of Gnome
# Do it by hand.
