#!/usr/bin/env python
#-*- coding:utf-8 -*-

import person

def play(action):
    return getattr(person,action)
#两行代码解决问题


#下面是用户控制的东西！
action = play('run')
action()
action = play('eat')
action()