#!/usr/bin/env python
#-*- coding:utf-8 -*-
name_info =['alex;1234;1', 'eric;1234;2', 'tony;1234;3']
count  =  3
newInfo = []
for info in name_info:
    tempLst = info.split(';')
    tempLst[2] = str(count)
    newInfo.append(tempLst)
print newInfo