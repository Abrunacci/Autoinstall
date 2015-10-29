#! /usr/bin/env python
#-*- coding: utf-8 -*-

import os
from configparser import ConfigParser
import subprocess

# path from applications.ini file
path = './applications.ini'


def run():
    configFile = ConfigParser()
    configFile.read(path)
    start_customization(configFile)
    start_applications_installation(configFile)

def start_customization(configFile):
    if configFile.has_section('oh-my-zsh'):
        if configFile.getboolean('oh-my-zsh','install'):
            try:
                print '>> Installing zsh...'
                os.system('apt-get install -y zsh')
                print '>> Getting oh-my-zsh!...'
                cmd = 'sudo -u $USERNAME sh ./tools/zshFiles/zsh.sh'
                os.system(cmd)
                print '>> Getting "syntax-highligthing" plugin...'
                cmd = 'git clone git://github.com/zsh-users/zsh-syntax-highlighting.git'
                os.system(cmd)
                print '>> Moving to folder'
                cmd = 'mv zsh-syntax-highlighting /home/$USERNAME/.oh-my-zsh/plugins/'
                os.system(cmd)
                configFile.set('oh-my-zsh','install','False')
                print 'Changing bash for zsh as default shell'
                cmd = 'sudo $USERNAME chsh -s $(which zsh)'
                os.system(cmd)
                cmd = 'cp tools/zshFiles/.zshrc /home/$USERNAME/'
                os.system(cmd)
                print '>> success'
            except Exception,e:
                print 'An error has occurred: {0}'.format(e)
    if configFile.has_section('vim-as-a-python-ide'):
        if configFile.getboolean('vim-as-a-python-ide','install'):
            try:
                print '>> Creating configuration folders...'
                cmd = 'mkdir /home/$USERNAME/.vim \
                        /home/$USERNAME/.vim/colors \
                        /home/$USERNAME/.vim/autoload \
                        /home/$USERNAME/.vim/bundle'
                os.system(cmd)
                print '>> Getting plugins...'
                cmd = 'git clone git://github.com/Lokaltog/vim-powerline.git'
                os.system(cmd)
                cmd = 'git clone git://github.com/davidhalter/jedi-vim.git'
                os.system(cmd)
                cmd = 'mv vim-powerline jedi-vim /home/$USERNAME/.vim/bundle'
                os.system(cmd)
                cmd = 'wget -O /home/$USERNAME/.vim/colors/wombat256mod.vim \
                        "http://www.vim.org/scripts/download_script.php?src_id=13400"'
                os.system(cmd)
                print '>> Curl -so /home...'
                cmd = 'curl -so /home/$USERNAME/.vim/autoload/pathogen.vim \
                        "https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim"'
                os.system(cmd)
                print '>> Setting False to configFile'
                configFile.set('vim-as-a-python-ide','install','False')
                print 'Adding .vimrc file'
                cmd = 'mv ./tools/vim-as-a-python-ide/.vimrc /home/$USERNAME/'
                os.system(cmd)
                print '>> Changing folders permision'
                cmd = 'chown -R $USERNAME:$USERNAME /home/$USERNAME/.vim'
                os.system(cmd)
                print '>> Success'
            except Exception,e:
                print 'An error has occurred {0}'.format(e)
    if configFile.has_section('virtualenvwrapper'):
        if configFile.getboolean('virtualenvwrapper','install'):
            try:
                print 'Installing virtualenvwrapper...'
                cmd = 'pip install virtualenvwrapper'
                os.system(cmd)
                line1 = 'sed -i "1i export WORKON_HOME=$HOME/.virtualenvs"'
                line2 = 'sed -i "2i export MSYS_HOME=/c/msys/1.0"'
                zshrc = '/home/'+os.getlogin()+'/.zshrc'
                bashrc = '/home/'+os.getlogin()+'/.bashrc'
                if os.path.exists(zshrc):
                    os.system(line1+' '+zshrc)
                    os.system(line2+' '+zshrc)
                if os.path.exists(bashrc):
                    os.system(line1+' '+bashrc)
                    os.system(line2+' '+bashrc)
            except Exception,e:
                print 'An error has occurred {0}'.format(e)


def start_applications_installation(configFile):
    response = ''
    for section in configFile.sections():
        if configFile.get(section,'install') == 'True':
            if configFile.has_option(section, 'prerequisites'):
                for prerequisite in configFile.get(section,'prerequisites'):
                    print install(prerequisite)
            response = install(section)
            if response == 'success':
                print response
                if configFile.has_option(section,'related_packages'):
                    applications = configFile.get(section,'related_packages').split(',')
                    for application in applications:
                        print install(application) 
                if configFile.has_option(section,'others_commands'):
                    commands = configFile.get(section,'others_commands').split(',')
                    for command in commands:
                        os.system(command)
            else:
                print response


def install(application):
    try:
        print ">> Installing {0}...".format(application)
        cmd = "apt-get install -y {0}".format(application)
        os.system(cmd)
        return 'success'
    except Exception,e:
        return 'An error has occurred: {0}'.format(e)


def configurate(application, filepath):
    try:
        print ">> Configurating {0}".format(application)
        cmd = "vim "+filepath  
        os.system(cmd)
        return 'success'
    except Exception,e:
        return 'An error has occurred: {0}'.format(e)


if __name__ == '__main__':
    run()
