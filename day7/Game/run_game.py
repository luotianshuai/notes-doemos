#!/usr/bin/env python
#-*- coding:utf-8 -*-

import person_model
import login_model
import os
import random

@login_model.wrapper
def run_game(arg):
    if os.path.exists(arg):  #判断角色是否有存档
        print "账号存在是否登录，如果要创建新的账号"
    else:
        print "\033[31;1m您好，您目前没有账号，请创建新的账号"
        print '''\033[34;1m欢迎来到创建角色页面
1、战士

o【$▅▆▇◤

基础血量：1000
防御力：2000
攻击力：500


2、猎人

    /
    )
 ##-------->
    )
    /

基础血量：700
防御力350
攻击力：2000

'''
        user_input = raw_input("\033[32;1m请输入您选择的职业:\033[0m") #获取用户的输入创建角色
        if user_input == '1':
            game_name = raw_input(("\033[32;1m请输入您的角色名字：\033[0m"))
            obj1 = person_model.Game_pmodel(game_name,'战士',500,1000)
            #print obj1.name,obj1.profession,obj1.blood,obj1.attack,obj1.defense
            print "\033[32;1m{1}进入副本任意键退出程序"
            zhandou = raw_input("\033[32;1m请问是否进入副本：\033[0m")
            if zhandou == '1':
                while True:
                    monster = random.randrange(1,3)
                    if monster == 1:
                        b = random.randrange(300,1000)
                        a = random.randrange(300,1000)
                        obj2 = person_model.Game_pmodel('怪物','普通怪',b,a)
                        obj1.detail()
                        obj2.detail()
                        action = raw_input("\033[31;1m请问是否攻击yes/no其他为no:\033[0m")
                        if action == 'yes':
                            cishu = 0
                            while True:
                                cishu += 1
                                print "\033[31;1m战斗开始\033[0m"
                                obj1.blood = obj1.blood - obj2.attack
                                obj2.blood = obj2.blood - obj1.attack
                                if obj1.blood <= 0:
                                    print "\33[31;1m您已经死亡，请重新来过！\033[0m"
                                    return
                                if obj2.blood <= 0:
                                    print "\033[32;1m怪物已死亡,角色升级\033[0m"
                                    obj1.attack = obj1.attack + 10
                                    obj1.blood = obj1.blood + cishu*
                                print "\033[34;1m------------回合结束--------------\033[0m"
                                obj1.detail()
                                obj2.detail()
                                skill = raw_input("\033[32;1m请问是否使用技能{1}加血｛2｝加攻击力｛3｝大吼帅哥无敌，怪物直接秒杀\033[0m")

                    else:
                        pass


            else:
                print "\033[32;1m欢迎下次继续游戏\033[0m"
                return
