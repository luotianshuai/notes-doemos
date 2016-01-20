#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

from services import linux

class BaseTemplat(object):
    def __init__(self):
        self.name = 'your templat name'
        self.host = [] #主机组里放机器
        self.services = [] #这里是你要包含那几个服务

class LinxGenricTemplate(BaseTemplat):
    def __init__(self):
        super(LinxGenricTemplate, self).__init__()
        self.name = "LinuxCommonServices"
        self.services = [
            linux.CPU(),
            linux.Memory()
        ]

class LinuxGenricTemplatesimple(BaseTemplat):
    def __init__(self):
        super(LinuxGenricTemplatesimple, self).__init__()
        self.name = "LinuxCommonServices"
        self.services = [
            linux.CPU(),
        ]