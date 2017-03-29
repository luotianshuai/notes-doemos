# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'

import os
import sys
import platform

# 添加BASE_DIR,添加顶级目录到路径中,方便调用其他目录模块
"""
print(__file__)  # 这个函数是获取文件名的函数
# 如果在pycharm输出这个结果就是这个文件的绝对路径
C:/Users/luotianshuai/Documents/Notes/day2/bin/run_shopping_mail.py
# 如果在cmd里调用仅输出文件的文件名
run_shopping_mail.py
# 默认Python会把当前运行的.py文件所在目录加入到环境变量里，但是不会把他的上级目录加到变量里就需要我们使用其他内置函数

print(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1]) 
# 分割完的结果，列表顾头不顾尾。这样我们取出文件所在目录的父亲目录然后在做处理
['C:', 'Users', 'luotianshuai', 'Documents', 'Notes', 'day2']
# 拼接
BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
# 加载环境变量
sys.path.append(BASE_DIR)
"""

if platform.system() == 'windows':
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])

# 加载环境变量
sys.path.append(BASE_DIR)

