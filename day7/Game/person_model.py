#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
定义：游戏角色模板和基础功能
'''
import random


class Game_pmodel(object):
    equipment = {"head":0,"bosom":0,"shoe":0,"weapon":0}  #定义静态字段包含角色的装备

    def __init__(self,name,profession,gold=0,attack=0,blood=0,defense=0): #初始化函数，名字和职业
        self.name = name   #定义普通字段
        self.profession = profession #定义普通字段
        self.gold = gold
        self.attack = attack
        self.blood = blood
        self.defense = defense

    def simpleness(self):
        pass


class Warrior(Game_pmodel):
    def __init__(self,name,profession,gold=0,attack=500,blood=1000,defense=2000):
        self.name = name   #定义普通字段
        self.profession = profession #定义普通字段
        self.gold = gold
        self.attack = attack
        self.blood = blood
        self.defense = defense

class Hunter(Game_pmodel):
    def __init__(self,attack=2000,blood=700,defense=950):
        self.attack = attack
        self.blood = blood
        self.defense = defense
