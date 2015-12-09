#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
定义：游戏角色模板和基础功能
'''



class Game_pmodel(object):
    equipment = {"head":0,"bosom":0,"shoe":0,"weapon":0}  #定义静态字段包含角色的装备
    def __init__(self,name,profession,gold=0,): #初始化函数，名字和职业
        self.name = name   #定义普通字段
        self.profession = profession #定义普通字段
        self.gold = gold

    def startkillmob(self):
        pass


class Warrior(Game_pmodel):
    pass



p1 = Warrior("shuaige","zhanshi")