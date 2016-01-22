#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR) #加载环境变量

from config import services

def push_config_toredis(main_ins,host_groups):
    host_config_dic = {} #定义一个空字典
    for group in host_groups: #循环monitored_groups列表
        for h in group.host: #循环对象中的主机IP列表
            if h not in host_config_dic:#如果主机IP不在字典中
                host_config_dic[h] = {} #给每台主机生成一个空字典
            for s in group.services:#循环group.services里面的服务，把服务添加到主机配置字典中
                host_config_dic[h][s.name] = [s.plugin_name,s.interval]
    for h,v in host_config_dic.items():
        host_config_key = "HostConfig::%s" % h  #他的KEY就是IP地址
        main_ins.r.set(host_config_key,json.dumps(v))

def report_monitor_data(main_server_instance,client_data):
    main_server_instance.r.set('ServiceData::%s:%s' % (client_data['report_monitor_data']['ip_address'],
                                               client_data['report_monitor_data']['service_name']),
                                               client_data)
    #print "------------------------>>",main_server_instance.r.get('ServiceData::%s:%s' % (client_data['report_monitor_data']['ip_address'],
                                               #client_data['report_monitor_data']['service_name']))

def linux_mem(main_instance,keys_name):
    data = main_instance.r.get(keys_name)
    mem = services.linux.Memory()
    mem_parameter = mem.triggers.keys()[1]
    print mem_parameter


def linux_cpu(main_instance,keys_name):
    data = main_instance.r.get(keys_name)
    print data