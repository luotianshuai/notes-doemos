#!/usr/bin/env python
#-*- coding:utf-8 -*-

import person_model
import login_model
import os

@login_model.wrapper
def run_game(arg):
    if os.path.exists(arg):
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
        user_input = raw_input("\033[32;1m请输入您选择的职业\033[0m")
        if user_input == '1':
            game_name = raw_input(("\033[32;1m请输入您的角色名字：\033[0m"))
            obj1 = person_model.Warrior(game_name,'战士')
            while True:
                print '''副本
                '''
