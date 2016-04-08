#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Tim Luo  LuoTianShuai

def CallMyself(n):
    print('level:',n)
    CallMyself(n+1)
    print('\033[32;1m测试输出\033[0m')
    return 0

CallMyself(1)