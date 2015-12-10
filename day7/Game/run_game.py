#!/usr/bin/env python
#-*- coding:utf-8 -*-

import person_model
import login_model
import os
import random
import pickle
@login_model.wrapper
def run_game(arg):
    if os.path.exists(arg):  #判断角色是否有存档
        print "角色已存在，如果要新建立角色请删除旧的角色"
        with open(arg,'rb') as f:
            obj1 = pickle.load(f)
        print "\033[32;1m[1]进入副本任意键退出程序"
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
                                obj1.blood = obj1.blood + cishu*obj2.attack + 10
                                status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")
                                if status == 'yes':
                                    with open(arg,'wb') as f:
                                        pickle.dump(obj1,f)
                                        obj1.detail()
                                        print "\033[32;1m您好账户信息已保存"
                                        return
                                break
                            print "\033[34;1m------------回合结束--------------\033[0m"
                            if obj2.attack > obj1.blood:
                                print "\033[31;1m您现在的血量不足，下回合必死小心，呼叫帅哥吧！！！\033[0m"
                            obj1.detail()
                            obj2.detail()
                            skill = raw_input('''\033[32;1m请问是否使用技能
[1]加血(100点)
[2]加攻击力（100点）
[3]大吼帅哥无敌，(攻击力+1000，血量+1000)
[8]逃跑\033[0m
▄︻┻═┳一 :::::::::''')
                            if skill == '1':
                                obj1.aspirine()
                            elif skill == '2':
                                obj1.add_attack()
                            elif skill == '3':
                                print "\033[32;1m呼唤帅哥\033[0m"
                                obj1.supershuai()
                            elif skill == '8':
                                obj1.blood = obj1.blood + cishu*obj2.attack
                                break
                            else:
                                continue
                    elif action == 'save':
                        with open(arg,'wb') as f:
                            pickle.dump(obj1,f)
                            print "\033[32;1m您好账户信息已保存"
                            return
                else:
                    b = random.randrange(3000,5000)
                    a = random.randrange(2000,10000)
                    obj2 = person_model.Game_pmodel('怪物','精英怪',a,b)
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
                                obj1.blood = obj1.blood + cishu*obj2.attack + 10
                                status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")
                                if status == 'yes':
                                    with open(arg,'wb') as f:
                                        pickle.dump(obj1,f)
                                        obj1.detail()
                                        print "\033[32;1m您好账户信息已保存"
                                        return
                                break
                            print "\033[34;1m------------回合结束--------------\033[0m"
                            if obj2.attack > obj1.blood:
                                print "\033[31;1m您现在的血量不足，下回合必死小心，呼叫帅哥吧！！！\033[0m"
                            obj1.detail()
                            obj2.detail()
                            skill = raw_input('''\033[32;1m请问是否使用技能
[1]加血(100点)
[2]加攻击力（100点）
[3]大吼帅哥无敌，(攻击力+1000，血量+1000)
[8]逃跑\033[0m
▄︻┻═┳一 :::::::::''')
                            if skill == '1':
                                obj1.aspirine()
                            elif skill == '2':
                                obj1.add_attack()
                            elif skill == '3':
                                print "\033[32;1m呼唤帅哥\033[0m"
                                obj1.supershuai()
                            elif skill == '8':
                                obj1.blood = obj1.blood + cishu*obj2.attack
                                break
                            else:
                                continue
                    elif action == 'save':
                        with open(arg,'wb') as f:
                            pickle.dump(obj1,f)
                            print "\033[32;1m您好账户信息已保存"
                            return


        else:
            print "\033[32;1m欢迎下次继续游戏\033[0m"
            return

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
攻击力：1500

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
                                    obj1.blood = obj1.blood + cishu*obj2.attack + 10
                                    status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")
                                    if status == 'yes':
                                        with open(arg,'wb') as f:
                                            pickle.dump(obj1,f)
                                            obj1.detail()
                                            print "\033[32;1m您好账户信息已保存"
                                            return
                                    break
                                print "\033[34;1m------------回合结束--------------\033[0m"
                                if obj2.attack > obj1.blood:
                                    print "\033[31;1m您现在的血量不足，下回合必死小心，呼叫帅哥吧！！！\033[0m"
                                obj1.detail()
                                obj2.detail()
                                skill = raw_input('''\033[32;1m请问是否使用技能
[1]加血(100点)
[2]加攻击力（100点）
[3]大吼帅哥无敌，(攻击力+1000，血量+1000)
[8]逃跑\033[0m
▄︻┻═┳一 :::::::::''')
                                if skill == '1':
                                    obj1.aspirine()
                                elif skill == '2':
                                    obj1.add_attack()
                                elif skill == '3':
                                    print "\033[32;1m呼唤帅哥\033[0m"
                                    obj1.supershuai()
                                elif skill == '8':
                                    obj1.blood = obj1.blood + cishu*obj2.attack
                                    break
                                else:
                                    continue
                        elif action == 'save':
                            with open(arg,'wb') as f:
                                pickle.dump(obj1,f)
                                print "\033[32;1m您好账户信息已保存"
                                return
                    else:
                        b = random.randrange(3000,5000)
                        a = random.randrange(2000,10000)
                        obj2 = person_model.Game_pmodel('怪物','精英怪',a,b)
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
                                    obj1.blood = obj1.blood + cishu*obj2.attack + 10
                                    status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")
                                    if status == 'yes':
                                        with open(arg,'wb') as f:
                                            pickle.dump(obj1,f)
                                            obj1.detail()
                                            print "\033[32;1m您好账户信息已保存"
                                            return
                                    break
                                print "\033[34;1m------------回合结束--------------\033[0m"
                                if obj2.attack > obj1.blood:
                                    print "\033[31;1m您现在的血量不足，下回合必死小心，呼叫帅哥吧！！！\033[0m"
                                obj1.detail()
                                obj2.detail()
                                skill = raw_input('''\033[32;1m请问是否使用技能
    [1]加血(100点)
    [2]加攻击力（100点）
    [3]大吼帅哥无敌，(攻击力+1000，血量+1000)
    [8]逃跑\033[0m
    ▄︻┻═┳一 :::::::::''')
                                if skill == '1':
                                    obj1.aspirine()
                                elif skill == '2':
                                    obj1.add_attack()
                                elif skill == '3':
                                    print "\033[32;1m呼唤帅哥\033[0m"
                                    obj1.supershuai()
                                elif skill == '8':
                                    obj1.blood = obj1.blood + cishu*obj2.attack
                                    break
                                else:
                                    continue
                        elif action == 'save':
                            with open(arg,'wb') as f:
                                pickle.dump(obj1,f)
                                print "\033[32;1m您好账户信息已保存"
                                return
            else:
                print "\033[32;1m欢迎下次继续游戏\033[0m"
                return
        if user_input == '2':
            game_name = raw_input(("\033[32;1m请输入您的角色名字：\033[0m"))
            obj1 = person_model.Game_pmodel(game_name,'猎人',1500,700)
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
                                    obj1.blood = obj1.blood + cishu*obj2.attack + 10
                                    status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")
                                    if status == 'yes':
                                        with open(arg,'wb') as f:
                                            pickle.dump(obj1,f)
                                            obj1.detail()
                                            print "\033[32;1m您好账户信息已保存"
                                            return
                                    break
                                print "\033[34;1m------------回合结束--------------\033[0m"
                                if obj2.attack > obj1.blood:
                                    print "\033[31;1m您现在的血量不足，下回合必死小心，呼叫帅哥吧！！！\033[0m"
                                obj1.detail()
                                obj2.detail()
                                skill = raw_input('''\033[32;1m请问是否使用技能
[1]加血(100点)
[2]加攻击力（100点）
[3]大吼帅哥无敌，(攻击力+1000，血量+1000)
[8]逃跑\033[0m
▄︻┻═┳一 :::::::::''')
                                if skill == '1':
                                    obj1.aspirine()
                                elif skill == '2':
                                    obj1.add_attack()
                                elif skill == '3':
                                    print "\033[32;1m呼唤帅哥\033[0m"
                                    obj1.supershuai()
                                elif skill == '8':
                                    obj1.blood = obj1.blood + cishu*obj2.attack
                                    break
                                else:
                                    continue
                        elif action == 'save':
                            with open(arg,'wb') as f:
                                pickle.dump(obj1,f)
                                print "\033[32;1m您好账户信息已保存"
                                return
                    else:
                        b = random.randrange(3000,5000)
                        a = random.randrange(2000,10000)
                        obj2 = person_model.Game_pmodel('怪物','精英怪',a,b)
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
                                    obj1.blood = obj1.blood + cishu*obj2.attack + 10
                                    status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")
                                    if status == 'yes':
                                        with open(arg,'wb') as f:
                                            pickle.dump(obj1,f)
                                            obj1.detail()
                                            print "\033[32;1m您好账户信息已保存"
                                            return
                                    break
                                print "\033[34;1m------------回合结束--------------\033[0m"
                                if obj2.attack > obj1.blood:
                                    print "\033[31;1m您现在的血量不足，下回合必死小心，呼叫帅哥吧！！！\033[0m"
                                obj1.detail()
                                obj2.detail()
                                skill = raw_input('''\033[32;1m请问是否使用技能
    [1]加血(100点)
    [2]加攻击力（100点）
    [3]大吼帅哥无敌，(攻击力+1000，血量+1000)
    [8]逃跑\033[0m
    ▄︻┻═┳一 :::::::::''')
                                if skill == '1':
                                    obj1.aspirine()
                                elif skill == '2':
                                    obj1.add_attack()
                                elif skill == '3':
                                    print "\033[32;1m呼唤帅哥\033[0m"
                                    obj1.supershuai()
                                elif skill == '8':
                                    obj1.blood = obj1.blood + cishu*obj2.attack
                                    break
                                else:
                                    continue
                        elif action == 'save':
                            with open(arg,'wb') as f:
                                pickle.dump(obj1,f)
                                print "\033[32;1m您好账户信息已保存"
                                return
            else:
                print "\033[32;1m欢迎下次继续游戏\033[0m"
                return