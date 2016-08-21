
# -*- coding: utf-8 -*-
# Standard lib imports
import os
import sys
import time

# Third Party imports

# CUSTOM imports
from .messages import MESSAGES
from .log import LOGGER
from .application import Application
from config import APPLICATIONS, ADDITIONAL_COMMANDS

__version__ = '0.1.0'


class Main:
    def __init__(self):
        self.username = os.getlogin()

    def run(self):
        print(MESSAGES['welcome'])
        LOGGER.debug('Starting application...')
        self.wait_and_clear()
        self.check_sudo()
        self.install_applications()
        self.wait_and_clear()
        LOGGER.debug('Closing application...')

    def wait_and_clear(self):
        # FIXME: I don't know if this is correct but...
        cmd = """bash -c 'read -s -n 1 -p "Press any key to continue..."'"""
        os.system(cmd)
        os.system('clear')

    def check_sudo(self):
        LOGGER.debug('Checking if user is sudo')
        if not os.geteuid() == 0:
            LOGGER.error('USER: "%s" is not sudo.'%(self.username))
            print(MESSAGES['root_error'])
            LOGGER.debug('Closing application...')
            quit()
        LOGGER.debug('User is sudo.')

    def install_applications(self):
        for application in APPLICATIONS:
            LOGGER.info('Installing %s...'%(application))
            ac = ADDITIONAL_COMMANDS.get(application) or []
            # app = Application(name=application,
            #                   additional_commands=ac)
            # app.install()
            # if ac:
            #     app.execute_additional_commands()
