#-*- coding:utf-8 -*-

#Standar Imports
import os
#Third-Party Imports
#Custom Imports
from .log import LOGGER

class Application():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.additional_commands = kwargs['additional_commands']

    def install(self):
        os.system('apt install -y %s'%(self.name))
        LOGGER.info('%s installed successfully'%(self.name))
        pass

    def execute_additional_commands(self):
        for command in self.additional_commands:
            LOGGER.info('Executing \'%s\''%(command))
            os.system(command)
