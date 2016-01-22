#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import os
import sys
import time
import json
from redishelper import RedisHelper
import serialize
import action_process

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR) #加载环境变量

from config import hosts

class MonitorServer(object): #创建主的类，调用连接Redis&调用serialize序列化，把监控模板上传至Redis
    def __init__(self):
        self.r = RedisHelper()
        self.save_configs()
        self.sub = self.r.subscribe()

    def start(self):
        while True:
            client_data = json.loads(self.sub.parse_response()[2])
            client_data['last_update'] = time.time()
            #print client_data
            business_type = client_data.keys()[0]
            action_process.action_process(self,business_type,client_data)
            '''
            self.r.set('ServiceData::%s:%s' % (client_data['report_monitor_data']['ip_address'],
                                               client_data['report_monitor_data']['service_name']),
                                               client_data)
                                               '''
            #数据存入到Redis中并且存储的相同数据只保留一条，数据不断刷新
    def save_configs(self):
        serialize.push_config_toredis(self,hosts.monitored_groups)#这里把self传过去，在push_config_toredis中即可调用实例
