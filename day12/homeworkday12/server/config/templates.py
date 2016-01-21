#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

from services import linux


class BaseTemplat(object):#定义基础模版
    def __init__(self):
        self.name = 'your templat name'
        self.host = [] #主机组里放机器
        self.services = [] #这里是你要包含那几个服务

class LinxGenricTemplate(BaseTemplat):#继承基类的基础模版创建新的模版并为模版增加监控服务
    def __init__(self):
        super(LinxGenricTemplate, self).__init__()
        self.name = "Linux_cpu_mem"
        self.services = [
            linux.CPU(),
            linux.Memory()
        ]

class LinuxGenricTemplatesimple(BaseTemplat):#继承基类的基础模版创建新的模版并为模版增加监控服务
    def __init__(self):
        super(LinuxGenricTemplatesimple, self).__init__()
        self.name = "Linux_only_cpu"
        self.services = [
            linux.CPU(),
        ]