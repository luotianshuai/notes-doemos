#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import os
import sys
import json
import pickle
import send_mail

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

def linux_mem(main_instance,keys_name): #内存监控判断
    client_datas_info = main_instance.r.get(keys_name) #获取客户端返回的数据
    client_datas_info = json.dumps(client_datas_info)
    client_datas_info = json.loads(client_datas_info,encoding=unicode)
    print type(client_datas_info)
    print client_datas_info



    mem = services.linux.Memory()#实例化Memory，取出监控值
    mem_parameter = mem.triggers.values()[0] #取出监控阀值信息

    # neirong = "%sCPU已超过阀值请检查" %s host_ip
    # yonghu = 'luotianshuai'
    # youxiang = '451161316@qq.com'
    # zhuti = 'CPU已超过阀值请检查'
    # send_mail.email(neirong,yonghu,youxiang,zhuti)  #发送报警邮件邮件！


def linux_cpu(main_instance,keys_name):#CPU监控判断
    pass

    # client_datas = main_instance.r.get(keys_name) #获取客户端返回的数据
    # print type(client_datas)
    # print client_datas
    #
    # cpu = services.linux.CPU()#实例化Memory，取出监控值
    # cpu_parameter = cpu.triggers.values()[0] #取出监控阀值信息