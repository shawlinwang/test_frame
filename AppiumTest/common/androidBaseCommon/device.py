#coding: utf-8
#filename: device.py
#
#   coding by: shaw
#
import os
from common.configParser import ConfigParser
from time import sleep
from common.common_def import *
#
config = ConfigParser()
class Device():
    def __init__(self):
        global viewPhone

    def check_connect(self):
        pass

    def get_deviceName(self):
        pass

    def get_androidVersion(self):
        pass

    def start_server(self):
        '''
        stop the adb server
        :return:
        '''
        pass

    def stop_server(self):
        pass

    def re_startServer(self):
        pass
