#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
import os
import json

def web_discovery():
    website = open('web.txt','r').read().split('\n')
    devices = []
    for devpath in website:
        print devpath
        #device = os.path.basename(devpath)
        devices.append({'{#SITENAME}':devpath})
    print json.dumps({'data':devices},sort_keys=True,indent=7,separators=(',',':'))

web_discovery()