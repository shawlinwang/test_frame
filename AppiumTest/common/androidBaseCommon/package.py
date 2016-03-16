#coding: utf-8
#filename: package.py
#
#   coding by: shaw
#
import os
from common.configParser import ConfigParser
from device import  Device
from time import sleep
from common.common_def import *
#
config = ConfigParser()
device = Device()
class Device():
    def __init__(self):
        global viewPhone

    def cmd_exc(self):
        pass

    def install(self):
        pass

    def uninstall(self):
        pass

    def find_app(self):
        pass

    def find_apps(self):
        pass

    def find_path(self):
        pass

if __name__ == "__main__":
    print PATH("configParser.py")
