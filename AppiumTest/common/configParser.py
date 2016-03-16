#coding: utf-8
#filename: configParser.py
#
#   coding by: shaw
#
import configparser
import codecs
import os
from common_def import *
#

class ConfigParser():
    def __init__(self):
        configfile_path = PATH("../config/config.ini")
        #
        # 尝试打开文件，最后判断文件是否被打开，打开则关闭
        # 去除配置文件内BOM
        #
        try:
            fd = open(configfile_path)
            data = fd.read()
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                file = codecs.open(configfile_path,'w')
                file.write(data)
                file.close()
        except:
            pass
        finally:
            if 'fd' in locals():
                fd.close()

        self.config = configparser.ConfigParser()
        self.config.read(configfile_path)

    def getConfigValue(self,name):
        value = self.config.get("config",name)
        return value

    def getCmdValue(self,name):
        value = self.config.get("cmd",name)
        return value

if __name__ == "__main__":
    confi = ConfigParser()
    print confi.getCmdValue("startServer")