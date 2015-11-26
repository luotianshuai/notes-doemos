#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import mail
def manage_api():
    while True:
        print '''\033[34;1m管理接口提供的功能有：
1、解锁商城用户或信用卡用户
2、添加商城用户或信用卡用户
3、信用卡账单邮件\033[0m
'''
        num = raw_input("\033[32;1m请输入您需要的功能：\033[0m")
        if num == '1':
            ulocak_user = raw_input("\033[34;1m请输入您要解锁的类型：1、为解锁商城用户   2、解锁信用卡用户：\033[0m")
            if ulocak_user == '1':
                user_lockli = [] #定义一个空列表存储被锁用户的信息
                with open('user_info','rb') as d:  #打开文件并用json把字符串转换为数据类型
                    user_info = json.load(d)
                for k,v in user_info.items(): #循环查找字典中的用户状态
                    if v['login_num'] == '3':  #如果用户处于被锁状态的话加入到列表中
                        lock_user = v['username']
                        print u'\033[31;1m%s用户已被锁定' % lock_user  #打印被锁用户信息
                        user_lockli.append(lock_user)  #把被锁用户追加到列表中
                if user_lockli: #判断如果列表不为空，如果有内容说明有被锁用户
                    user_unlock = raw_input("\033[32;1m请输入您要解锁的用户名：\033[0m") #获取用户要解锁的用户
                    if user_unlock in user_lockli: #判断，如果用户存在
                        user_info[user_unlock]['login_num'] = int(0)  #把user_info转换为数字类型
                        neirong = "%s用户已解锁" % user_unlock
                        yonghu = ulocak_user
                        youxiang = user_info[user_unlock]['mail']
                        zhuti = '账户解锁通知'
                        mail.email(neirong,yonghu,youxiang,zhuti)
                        with open('user_info','wb') as f:  #把新的用户状态写入user信息中
                            json.dump(user_info,f)
                        print "\033[32;1m\033[32;1m%s\033[0m\033[31;1m用户已被解锁\033[0m" % user_unlock

                    else:
                        print "\033[31;1m\033[32;1m%s\033[0m\033[31;1m用户不存在\033[0m" % user_unlock  #不能存在提示用户不存在！

                else:
                    print "\033[31;1m没有账户被锁定\033[0m"
            if ulocak_user == '2':
                card_lockli = [] #定义一个空列表存储被锁用户的信息
                with open('card_info','rb') as d:  #打开文件并用json把字符串转换为数据类型
                    card_info = json.load(d)
                for k,v in card_info.items(): #循环查找字典中的用户状态
                    if v['login_num'] == '3': #如果用户处于被锁状态的话加入到列表中
                        lock_card = k
                        print u'\033[31;1m%s用户已被锁定' % lock_card  #打印被锁用户信息
                        card_lockli.append(lock_card)
                if card_lockli: #判断如果列表不为空，如果有内容说明有被锁用户
                    card_id = raw_input("\033[32;1m请输入您要解锁的卡号：\033[0m")
                    if card_id in card_lockli:
                        card_info[card_id]['login_num'] = int(0)
                        neirong = "%s卡号已解锁" % card_id
                        yonghu = card_id
                        youxiang = card_info[card_id]['mail']
                        zhuti = '卡号解锁通知'
                        mail.email(neirong,yonghu,youxiang,zhuti)
                        with open('card_info','wb') as f:
                            json.dump(card_info,f)
                        print  "\033[32;1m\033[32;1m%s\033[0m\033[31;1m卡号已被解锁\033[0m" % card_id
                    else:
                        print "\033[31;1m\033[32;1m%s\033[0m\033[31;1m卡号不存在\033[0m" % card_id #不能存在提示卡号不存在！
                else:
                    print "\033[31;1m没有卡号被锁定\033[0m"
        elif num == '2':
            user_add = raw_input('\033[34;1m请选择您要添加的账户类型1、添加商城用户 2、信用卡用户：\033[0m')
            if user_add == '1':
                with open('user_info','rb') as d:
                    user_infos = json.load(f)
                add_name = raw_input('\033[32;1m请输入你要添加的用户：\033[0m')
                if not user_infos.get(add_name):
                    add_pass = raw_input("\033[32;1m请输入您添加用户的密码：\033[0m")
                    add_mail = raw_input("\033[32;1m请输入您添加用户的邮箱：\033[0m")

                else:
                    print "\033[31;1m用户已存在\033[0m"
        else:
            print "\033[31;1m请输入正确的功能项目\033[0m"