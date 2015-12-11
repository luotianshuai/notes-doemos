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
        print "\033[31;1m角色已存在，如果要新建立角色请删除旧的角色\033[0m"
        with open(arg,'rb') as f: #打开存储游戏角色的文件
            obj1 = pickle.load(f) #加载文件
        zhandou = raw_input("\033[32;1m请问是否进入副本，[1]进入、任意键退出程序！：\033[0m") #获取用户输入是否进入副本
        if zhandou == '1':  #如果为1进入副本
            while True:
                monster = random.randrange(1,3)  #定义随机生成怪物的属性和利害程度使用random模块
                if monster == 1:
                    b = random.randrange(300,1000)  #血量
                    a = random.randrange(300,1000)  #攻击力
                    s = random.randrange(300,1500)  #速度
                    obj2 = person_model.Game_pmodel('怪物','普通怪',b,a,s)
                    obj1.detail()
                    obj2.detail()
                else:
                    b = random.randrange(1000,5000)#血量
                    a = random.randrange(2000,3000)#攻击力
                    s = random.randrange(1000,2000)#速度
                    obj2 = person_model.Game_pmodel('怪物','精英怪',b,a,s)
                    obj1.detail() #打印现在人物角色的属性
                    obj2.detail() #打印现在怪物的属性
                action = raw_input("\033[31;1m请问是否攻击yes/save为保存，no和其继续o:\033[0m")  #询问玩家是否攻击
                if action == 'yes':  #攻击
                    cishu = 0
                    while True:
                        cishu += 1  #定义一个循环次数，带怪物被杀死后，恢复角色的血量
                        print "\033[31;1m战斗开始\033[0m"
                        if obj1.speed > obj2.speed:  #判断如果人物的速度，高于怪物的属性，那么人物先攻击
                            obj2.blood = obj2.blood - obj1.attack  #怪物的血量等物，怪物的血量减去人物的攻击力
                            if obj2.blood <= 0: #判断如果怪物的血量小于或等于0说明怪物死亡，角色获取相应的属性奖励
                                print "\033[32;1m怪物已死亡,角色升级\033[0m"
                                obj1.attack = obj1.attack + 100  #获取攻击力的属性奖励
                                obj1.blood = obj1.blood + cishu*obj2.attack + 100  #还原原有血量，并获得属性奖励
                                obj1.speed = obj1.speed + 50  #获取属性奖励
                                status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m") #提示用户是否退出
                                if status == 'yes':
                                    with open(arg,'wb') as f:  #打开文件，存储的文件名称是用户的用户名
                                        pickle.dump(obj1,f)
                                        obj1.detail()
                                        print "\033[32;1m您好账户信息已保存\033[0m"
                                        return
                                break #这里的break是，如果用户不退出怪物死亡了，需要跳出这个循环！！
                            else: #如果怪物没死，攻击人物
                                obj1.blood = obj1.blood-obj2.attack   #人物的血量等于，人物的血量减去怪物的攻击力
                                if obj1.blood <= 0: #如果人物死亡，死亡惩罚，本次游戏的奖励没有！
                                    print "\033[31;1m您已死亡请重新来过！\033[0m"
                                    return
                        else:
                            obj1.blood = obj1.blood - obj2.attack  #怪物的速度快，人物的血量等于，血量减去-怪物的攻击力
                            if obj1.blood <= 0: #如果人物的血量小于0，惩罚，取消本次游戏的奖励
                                print "\033[31;1m您已死亡请重新来过！\033[0m"
                                return
                            else:
                                obj2.blood = obj2.blood - obj1.attack #如果人物没死攻击怪物
                                if obj2.blood <= 0: #判断怪物的血量，如果小于零，说明怪物死亡获取相应的胜利属性
                                    print "\033[32;1m怪物已死亡,角色升级\033[0m"
                                    obj1.attack = obj1.attack + 100
                                    obj1.blood = obj1.blood + cishu*obj2.attack + 100
                                    obj1.speed = obj1.speed + 50
                                    status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m") #提示用户是否退出
                                    if status == 'yes':
                                        with open(arg,'wb') as f: #打开文件保存
                                            pickle.dump(obj1,f)
                                            obj1.detail()  #输出用户的详细信息
                                            print "\033[32;1m您好账户信息已保存\033[0m"
                                            return
                                    break
                        print "\033[34;1m------------回合结束--------------\033[0m" #如果人物和怪物都没有死亡，那次回合结束提示人物技能！
                        if obj2.attack > obj1.blood:
                            print "\033[31;1m您现在的血量不足，下回合可能会死小心，呼叫帅哥吧！！！\033[0m"
                        obj1.detail() #打印当前角色信息
                        obj2.detail() #打印当前怪物信息
                        skill = raw_input('''\033[32;1m请问是否使用技能
[1]加血(100点)
[2]加攻击力（100点）
[3]大吼帅哥无敌，(攻击力+1000，血量+1000)
[8]逃跑\033[0m
▄︻┻═┳一 :::::::::''')
                        if skill == '1':
                            obj1.aspirine()  #调用加血方法
                        elif skill == '2':
                            obj1.add_attack() #调用加攻击力方法
                        elif skill == '3':
                            print "\033[32;1m呼唤帅哥\033[0m"
                            obj1.supershuai() #呼叫帅哥方法基本上不会死，死了也不管 0 0！
                        elif skill == '8':
                            obj1.blood = obj1.blood + cishu*obj2.attack  #逃跑，回复进入战斗前的血量
                            break
                        else:
                            continue
                elif action == 'save':  #用户执行退出程序
                    with open(arg,'wb') as f:
                        pickle.dump(obj1,f)
                        print "\033[32;1m您好账户信息已保存，再见！\033[0m"
                        return
        else:
            print "\033[32;1m魔兽世界随时恭候,再见！\033[0m"
            return
    else:
        print "\033[31;1m您好，您目前没有账号，请创建新的账号"  #如果用户登录后没有角色会提示用户注册角色！
        print '''\033[34;1m欢迎来到创建角色页面
1、战士

o【$▅▆▇◤

基础血量：3000
攻击力：500
速度：800


2、猎人

    /
    )
 ##-------->
    )
    /

基础血量：700
攻击力：1500
速度：1000

\033[0m'''
        user_input = raw_input("\033[32;1m请输入您选择的职业默认（猎人）:\033[0m") #获取用户的输入创建角色
        if user_input == '1':  #根据用户的输入生成不通的职业和属性
            zhiye = '战士'
            gongji = 500
            xeiliang = 3000
            sudu = 800
        else:#根据用户的输入生成不通的职业和属性
            zhiye = '猎人'
            gongji = 1500
            xeiliang = 700
            sudu = 1000
        game_name = raw_input(("\033[32;1m请输入您的角色名字：\033[0m")) #获取用户输入的角色名称
        obj1 = person_model.Game_pmodel(game_name,zhiye,gongji,xeiliang,sudu)  #生成角色信息
        zhandou = raw_input("\033[32;1m请问是否进入副本，[1]进入、任意键退出程序！：\033[0m") #询问是否进入副本
        if zhandou == '1':
            while True:
                monster = random.randrange(1,3)   #定义一个随机的数字，然后用他来生成不通种类的怪物
                if monster == 1:
                    b = random.randrange(300,1000)
                    a = random.randrange(300,1000)
                    s = random.randrange(300,1500)
                    obj2 = person_model.Game_pmodel('怪物','普通怪',b,a,s) #根据随机的属性生成怪物
                    obj1.detail()
                    obj2.detail()
                else:
                    b = random.randrange(1000,5000)
                    a = random.randrange(2000,3000)
                    s = random.randrange(1000,2000)
                    obj2 = person_model.Game_pmodel('怪物','精英怪',b,a,s)#根据随机的属性生成怪物
                    obj1.detail()
                    obj2.detail()
                action = raw_input("\033[31;1m请问是否攻击yes/save保存退出，其他继续:\033[0m") #询问用户攻击与否，是否退出？
                if action == 'yes':
                    cishu = 0
                    while True:
                        cishu += 1  #定义一个循环次数，带怪物被杀死后，恢复角色的血量
                        print "\033[31;1m战斗开始\033[0m"
                        if obj1.speed > obj2.speed:  #判断人物的速度是否大于怪物
                            obj2.blood = obj2.blood - obj1.attack  #如果大于怪物的速度，怪物的血量减去人物的攻击力！
                            if obj2.blood <= 0: #判断怪物是否被杀死
                                print "\033[32;1m怪物已死亡,角色升级\033[0m" #如果被杀死会获取相应的属性
                                obj1.attack = obj1.attack + 100
                                obj1.blood = obj1.blood + cishu*obj2.attack + 100
                                obj1.speed = obj1.speed + 50
                                status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")  #询问用户
                                if status == 'yes': #退出
                                    with open(arg,'wb') as f: #保存文件
                                        pickle.dump(obj1,f)
                                        obj1.detail()  #打印当前用户角色信息
                                        print "\033[32;1m您好账户信息已保存\033[0m"
                                        return
                                break
                            else:
                                obj1.blood = obj1.blood-obj2.attack  #怪物攻击人物
                                if obj1.blood <= 0:  #如果人物死亡，惩罚，取消本次游戏的奖励
                                    print "\033[31;1m您已死亡请重新来过！\033[0m"
                                    return
                        else:
                            obj1.blood = obj1.blood - obj2.attack  #如果怪物先攻击
                            if obj1.blood <= 0:  #如果人物的血量小于0说明人物死亡，惩罚！
                                print "\033[31;1m您已死亡请重新来过！\033[0m"
                                return
                            else:
                                obj2.blood = obj2.blood - obj1.attack  #人物没死，攻击怪物
                                if obj2.blood <= 0: #判断怪物是否死亡，如果死亡获取相应的奖励
                                    print "\033[32;1m怪物已死亡,角色升级\033[0m"
                                    obj1.attack = obj1.attack + 100
                                    obj1.blood = obj1.blood + cishu*obj2.attack + 100
                                    obj1.speed = obj1.speed + 50
                                    status = raw_input("\033[32;1m是否退出游戏？yes退出，其他继续\033[0m")#询问用户
                                    if status == 'yes': #退出
                                        with open(arg,'wb') as f: #打开文件
                                            pickle.dump(obj1,f)  #序列化对象
                                            obj1.detail() #打印当前角色的属性
                                            print "\033[32;1m您好账户信息已保存\033[0m"
                                            return
                                    break
                        print "\033[34;1m------------回合结束--------------\033[0m"
                        if obj2.attack > obj1.blood:  #判断当前血量，并回执给用户信息！
                            print "\033[31;1m您现在的血量不足，下回合可能会死小心，呼叫帅哥吧！！！\033[0m"
                        obj1.detail() #打印角色信息
                        obj2.detail() #打印怪物信息
                        skill = raw_input('''\033[32;1m请问是否使用技能
[1]加血(100点)
[2]加攻击力（100点）
[3]大吼帅哥无敌，(攻击力+1000，血量+1000)
[8]逃跑\033[0m
▄︻┻═┳一 :::::::::''')
                        if skill == '1':
                            obj1.aspirine()  #调用加血方法
                        elif skill == '2':
                            obj1.add_attack() #调用加攻击力方法
                        elif skill == '3':
                            print "\033[32;1m呼唤帅哥\033[0m"
                            obj1.supershuai() #调用帅哥方法
                        elif skill == '8':
                            obj1.blood = obj1.blood + cishu*obj2.attack  #逃跑，恢复血量前提是没死！
                            break
                        else:
                            continue
                elif action == 'save': #保存用户信息！
                    with open(arg,'wb') as f:
                        pickle.dump(obj1,f)
                        print "\033[32;1m您好账户信息已保存\033[0m"
                        return
        else:
            print "\033[32;1m魔兽世界随时恭候,再见！\033[0m"
            return