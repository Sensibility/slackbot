#!/bin/sh

#check for proper permissions
if [ $(id -u) -ne 0 ]
then
	if [ $DISPLAY && $(which gksudo) ]
	then
		gksudo "$0"
		exit 0
	fi
	if [ $(which sudo) ]
	then
		sudo "$0"
		exit 0
	fi
	echo "This script must be run with root permissions, and you don't appear to have sudo or gksudo installed, so we can't do it ourselves"
fi

#List of dependancies we need to install
PYTHON = true
PYTHONVERSION = true
SYSTEMD = true
PIP = true



#check for python version 3
if [ ! $(which python) ]
then
	PYTHON = false
fi

if [ $(python --version | sed 's/.*\s//' | sed 's/\..*//') != 3 ]
then
	echo "Python appears to not be version 3+, either it is not installed or `$PATH/python` is not a symlink to it."
	exit 1
fi
