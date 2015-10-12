#!/bin/bash

echo '>> Starting... '
echo '>> Update & Upgrade'
# update & upgrade system
 atp-get update
 apt-get upgrade

echo '>> Installing SUDO'
# install sudo and adding user to sudoers
 apt-get -y install sudo
echo '>> Adding '$USERNAME' to sudoers'
 adduser $USERNAME sudo

# Prerequisites
 apt-get install -y curl python-pip git vim-nox
 pip install configparser

# Executing program
python autoinstall.py

