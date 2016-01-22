#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import os
import sys
import json
import time
import threading
import redishelper

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR) #加载环境变量

from config import settings
from plugins import plugin_api

class MonitorClients(object):
    def __init__(self):
        self.r = redishelper.RedisHelper() #连接Redis
        self.ip = settings.ClientIP #设置客户端IP
        self.host_config = self.get_host_config() #执行get_host_config方法并把值赋予给host_config

    def start(self):
        print "what's the fuck "
        self.handle()

    def get_host_config(self): #定义get_host_config方法
        config_key = "HostConfig::%s" % self.ip
        config_info = self.r.get(config_key) #获取监控参数
        if config_info: #判断是否可以获取到
            config_info = json.loads(config_info)
        return config_info

    def handle(self):#主运行方法
        print 'fuck'
        if self.host_config: #判断host_config是否有值
            while True: #循环
                for servers,val in self.host_config.items():
                    if len(val) < 3:#确保第一次客户端启动时会运行所有插件
                        self.host_config[servers].append(0)
                    plugin_name,interval,last_run_time = val
                    if time.time() - last_run_time < interval:#判断当前时间是否小于监控间隔
                        next_run_time = interval - (time.time() - last_run_time )
                        print "Service [%s] next run time is in [%s] secs" % (servers,next_run_time)
                    else:
                        print "\033[34;1m------will to run the [%s] again------\033[0m" % servers
                        self.host_config[servers][2] = time.time() #重置计数时间
                        t = threading.Thread(target=self.run_plugin,args=(servers,plugin_name))#调用插件去获取参数，多线程
                        t.start()
                time.sleep(1)
        else:
            print "\033[31;1mYour config is None,please check Server config!!\033[0m"

    def run_plugin(self,service_name,plugin_name): #调用插件方法
        func = getattr(plugin_api,plugin_name) #通过反射获取方法
        result = json.dumps(func())  #执行方法并获取数据
        msg = self.format_msg('report_service_data',
                              {'ip_address':self.ip,
                               'service_name':service_name,
                               'data':result})
        self.r.public(msg) #发送消息
    def format_msg(self,key,value):
        msg = {key:value}
        return json.dumps(msg)