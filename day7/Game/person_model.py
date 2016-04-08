#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
定义：游戏角色模板和基础功能
'''
import random


class Game_pmodel(object):
    def __init__(self,name,profession,attack=0,blood=0,speed=0): #构造函数，名字和职业等信息
        self.name = name   #定义普通字段
        self.profession = profession #定义普通字段
        self.attack = attack
        self.blood = blood
        self.speed = speed

    def supershuai(self):
        self.blood = self.blood + 1000
        self.attack = self.attack + 1000
        self.speed = self.speed + 1000
        print "\033[32;1m呼叫及时当前血量：%s 当前攻击为：%s，当前速度为：%s" % (self.blood,self.attack,self.speed)
    def add_attack(self):
        self.attack = self.attack +300
        print "\033[32;1m您当前的攻击力为%s\033[0m" % self.attack
    def aspirine(self):
        self.blood = self.blood + 300
        print "\033[32;1m您当前的血量为%s\033[0m" % self.blood
    def detail(self):
        """注释：当前对象的详细情况"""
        temp = "角色:%s ; 职业:%s ; 战斗力:%s ; 血量:%s ; 速度:%s"  % (self.name, self.profession, self.attack, self.blood,self.speed)
        print temp

