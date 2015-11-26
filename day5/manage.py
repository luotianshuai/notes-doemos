#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json

def manage_api():
    while True:
        print '''\033[34;1m管理接口提供的功能有：
1、解锁商城用户或信用卡用户
2、添加商城用户或信用卡用户
3、信用卡账单邮件\033[0m
'''
        num = raw_input("\033[32;1m请输入您需要的功能：\033[0m")
        if num == '1':
            ulocak_user = raw_input("\033[34;1m请输入您要解锁的类型：1、为解锁商城用户   2、解锁信用卡用户\033[0m")
            if ulocak_user == '1':
                user_lockli = [] #定义一个空列表存储被锁用户的信息
                with open('user_info','rb') as d:  #打开文件并用json把字符串转换为数据类型
                    user_info = json.load(d)
                for k,v in user_info.items(): #循环查找字典中的用户状态
                    if v['login_num'] == 3:  #如果用户处于被锁状态的话加入到列表中
                        lock_user = v['username']
                        print u'\033[31;1m%s用户已被锁定' % lock_user
                        user_lockli.append(lock_user)
                if user_lockli:
                    user_unlock = raw_input("\033[32;1m请输入您要解锁的用户名：\033[0m")
                    if user_unlock in user_lockli:
                        user_info[user_unlock]['login_num'] = int(0)
                        with open('user_info','wb') as f:
                            json.dump(user_info,f)
                        print "\033[32;1m%s用户已被解锁" % user_unlock

                else:
                    print "\033[31;1m没有账户被锁定\033[0m"

        else:
            print "\033[31;1m请输入正确的功能项目\033[0m"