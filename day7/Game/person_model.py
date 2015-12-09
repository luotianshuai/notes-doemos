#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
定义：游戏角色模板和基础功能
'''



class game_pmodel(object):
    equipment = {"head":0,"bosom":0,"shoe":0,"weapon":0}
    def __init__(self,name,profession):
        self.name = name
        self.profession = profession
