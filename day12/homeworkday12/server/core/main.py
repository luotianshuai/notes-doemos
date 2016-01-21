#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import os
import sys
from redishelper import RedisHelper
import serialize


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR) #加载环境变量

from config import hosts

class MonitorServer(object): #创建主的类，调用连接Redis&调用serialize序列化，把监控模板上传至Redis
    def __init__(self):
        self.r = RedisHelper()
        self.save_configs()
    def start(self):
        pass
    def save_configs(self):
        serialize.push_config_toredis(self,hosts.monitored_groups)#这里把self传过去，在push_config_toredis中即可调用实例
