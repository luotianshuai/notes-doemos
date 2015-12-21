#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR) #加载环境变量

from modules import main

if __name__ == '__main__':
    entry_point = main.ArgvHandler(sys.argv) #Python内部提供一个 sys 的模块，其中的 sys.argv 用来捕获执行执行python脚本时传入的参数
