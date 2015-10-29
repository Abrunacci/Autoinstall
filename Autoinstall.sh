#!/bin/bash

echo '>> Starting... '
echo '>> Changing sources file'
cp tools/sources.list /etc/apt/sources.list
echo '>> Update & Upgrade'
# update & upgrade system
apt-get update
apt-get -y upgrade

echo '>> Installing SUDO'
# install sudo and adding user to sudoers
 apt-get -y install sudo
echo '>> Adding '$USERNAME' to sudoers'
 adduser $USERNAME sudo

# Prerequisites
 apt-get install -y curl python-pip git vim-nox
 pip install configparser

echo '>> Starting applications instalation'
# Executing program
 python autoinstall.py

if [ -e /home/$USERNAME/.zshrc ]
then
    cp tools/zshFiles/.zshrc /home/$USERNAME/
fi

if [ -e /etc/postgresql/9.4/main/pg_hba.conf ]
then
    cp tools/postgres_files/* /etc/postgresql/9.4/main/
fi
exit
