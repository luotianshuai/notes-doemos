#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR) #把路径加入到环境变量


from  modules import command  #导入模块

if __name__ == '__main__':
    works = command.Cmd(sys.argv) #实例化对象


