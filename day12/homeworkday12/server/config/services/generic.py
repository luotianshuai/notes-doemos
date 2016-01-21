#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

class BaseService(object):#定义监控参数基类
    def __init__(self):
        self.name = 'BaseService'#定义服务的名称
        self.interval = 300 #监控间隔
        self.plugin_name = 'your_plugin_name'#插件名称
        self.triggers = {} #空的阀值列表