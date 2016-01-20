#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

from generic import BaseService

class CPU(BaseService):
    def __init__(self):
        super(CPU,self).__init__() #调用父类的构造方法并重构构造字段
        self.interval = 30 #监控间隔
        self.name = 'linux_cpu' #定义监控的服务名称
        self.plugin_name = 'get_cpu_status' #定义Client使用的插件名称

        self.triggers = {
            'idle':{
                'func':'arg',
                'last':10*60,
                'operator':'lt',
                'count':1,
                'warning':20,
                'critical':5,
                'data_type':float

            },
            'iowait':{
                'func':'hit',
                'last':15*60,
                'operator':'gt',
                'count':5,
                'warning':40,
                'critical':50,
                'data_type':float
            }
                    }
class Memory(BaseService):
    def __init__(self):
        super(Memory,self).__init__() #调用父类的构造方法并重构构造字段
        self.interval = 20 #监控间隔
        self.name = 'linux_cpu' #定义监控的服务名称
        self.plugin_name = 'get_cpu_status' #定义Client使用的插件名称

        self.triggers = {
            'usage':{
                'func':'arg',
                'last':5*60,
                'operator':'lt',
                'count':1,
                'warning':80,
                'critical':90,
                'data_type':float
            }

        }

class Network(BaseService):
    pass
