#!/bin/bash

thisdir=$(dirname "$0")
cd $thisdir
python3 simplemenu.py &
cd $HOME
