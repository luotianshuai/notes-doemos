#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR)

from  modules import socket_client

if __name__ == '__main__':
    entry_point = socket_client.Client_Handler(sys.argv)