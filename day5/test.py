#!/usr/bin/env python
#-*- coding:utf-8 -*-
#用于对特定的配置进行操作，当前模块的名称在 python 3.x 版本中变更为 configparser。
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('userinfo')

secs = config.sections()
print secs

#显示list-appliance下面的keys
options = config.options('list-appliance')
print options

#显示list-appliance里面的信息并以元组列表的形式列出来（key,values）
itme_list = config.items('list-appliance')
print itme_list

va1 = config.get('list-appliance','washer')
print va1