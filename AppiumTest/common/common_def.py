#coding: utf-8
#filename: common.py
#
#   coding by: shaw
#
import os
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

def cmd_exc_list(command):
    '''
    执行cmd命令，按行返回结果序列
    :param command:
    :return:return_value
    '''
    return_value = os.popen(command).readlines()
    return return_value

def cmd_exc_str(command):
    '''
    执行cmd命令，以string方式返回序列
    :param command:
    :return:return_value
    '''
    return_value = os.popen(command).read()
    return return_value

