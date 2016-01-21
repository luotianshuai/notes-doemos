#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

list_b = []

a = {"backend": "add.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}

list_b.append("server %s" % a.get("record")["server"])
list_b.append("weight %s" % a.get('record')['weight'])
list_b.append("maxconn %s" % a.get('record')['maxconn'])
print list_b


