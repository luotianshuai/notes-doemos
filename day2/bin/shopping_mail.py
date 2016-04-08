#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'

import os
import sys


#os.path.abspath(__file__) #获取文件的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from moduls import main

if __name__ == '__main__':
    runbuy = main.Buy()


