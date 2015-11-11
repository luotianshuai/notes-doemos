#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import json

def get_info(info):
    with open('haproxy.conf','r') as f:
        for i in f.readlines():
            i = i.strip('\n')
            if info in i and i[0:6] == 'backen':


        else:
            return "\033[31;1m对不起，无法找到您输入的backen\033[0m"

if __name__ == '__main__':
    print '''\033[34;1m\
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录\033[0m'''
    num = raw_input('\033[32;1m请输入序列号：\033[0m')
    if num == '1':
        read = raw_input('\033[033;1m请输入backend：\033[0m')
        print get_info(read)
#www.oldboy.org