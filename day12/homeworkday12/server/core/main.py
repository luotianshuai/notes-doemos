#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import redishelper
import serialize
from config import hosts

class MonitorServer(object):
    def __init__(self):
        self.r = redishelper.RedisHelper()
        self.save_configs()
    def start(self):
        pass
    def save_configs(self):
        serialize.push_config_toredis(hosts.monitored_groups)
