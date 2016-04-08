#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'


flag = True

while flag:
    '''
    yes will continue
    no will stop
    '''
    user_iniput = raw_input("do you want continue yes/no：")
    if user_iniput == 'no':
        flag = False
    else:
        continue