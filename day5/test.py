#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ConfigParser
config = ConfigParser.ConfigParser()
config.read('productlist')

secs = config.sections()
print secs

options =