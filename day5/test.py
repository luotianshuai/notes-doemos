#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
import time
import ConfigParser
import os
mothe_now = time.strftime("%Y%m") #获取当前月份
day_now = time.strftime("%d") #获取当天日期
day_second = time.strftime("%H%M%S")
print day_second
'''
'''
if os.path.exists(mothe_now):  #判断当前月份的文件是否存在
    config = ConfigParser.ConfigParser()  #打开消费列表
    config.read(mothe_now) #读取消费列表
    sec = config.has_section(day_now)  #判断当天是否有过消费
    if sec:
        print "日期存在"
    else:
        print "日期不存在"
else:
    with open(mothe_now,'wb') as f:
        pass
    config = ConfigParser.ConfigParser()  #打开消费列表
    config.read(mothe_now) #读取消费列表
    config.add_section(day_now) #创建section

    config.write(open(mothe_now,'w')) #修改后的数据写入配置文件
'''
li = [1,2,3,4,5]
li1 = [2,3,4,5]
li.extend(li1)
print li