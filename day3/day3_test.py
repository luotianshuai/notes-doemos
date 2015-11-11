#!/usr/bin/env python
#-*- coding:utf-8 -*-

with open('haproxy.conf','r') as f:
    for i in f.readlines():
        i = i.strip('\n')
        if info in i and i[0:6] == 'backen':