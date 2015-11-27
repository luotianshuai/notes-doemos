#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import mail
import hashlib
import datetime
import time
import os
def manage_api():
    while True:
        print '''\033[34;1m管理接口提供的功能有：
1 解锁商城用户或信用卡用户
2 添加商城用户或信用卡用户
3 信用卡账单邮件
0 输入0返回上级菜单\033[0m
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
                    card_id = raw_input("\033[32;1m请输入您要解锁的卡号：\033[0m")  #获取用户解锁账号
                    if card_id in card_lockli:  #判断用户输入的账号是否在被锁账号中
                        card_info[card_id]['login_num'] = int(0)  #存在替换账号信息并发送邮件
                        neirong = "%s卡号已解锁" % card_id
                        yonghu = card_id
                        youxiang = card_info[card_id]['mail']
                        zhuti = '卡号解锁通知'
                        mail.email(neirong,yonghu,youxiang,zhuti)  #用户解锁完成后调用发送邮件函数，发送邮件！
                        with open('card_info','wb') as f:
                            json.dump(card_info,f)
                        print  "\033[32;1m\033[32;1m%s\033[0m\033[31;1m卡号已被解锁\033[0m" % card_id
                    else:
                        print "\033[31;1m\033[32;1m%s\033[0m\033[31;1m卡号不存在\033[0m" % card_id #不存在提示卡号不存在！
                else:
                    print "\033[31;1m没有卡号被锁定\033[0m"
        elif num == '2':
            user_add = raw_input('\033[34;1m请选择您要添加的账户类型1、添加商城用户 2、信用卡用户：\033[0m')
            if user_add == '1':
                with open('user_info','rb') as d: #读取原有的用户信息
                    user_infos = json.load(d) #把原有的用户信息由字符串转换为数据类型
                add_name = raw_input('\033[32;1m请输入你要添加的用户：\033[0m') #获取用户输入的用户名
                if not user_infos.get(add_name): #判断原文件中是否有相同的用户名，如果有提示用户已存在，如果没有添加！
                    add_pass = raw_input("\033[32;1m请输入您添加用户的密码：\033[0m")  #获取用户的密码并加密
                    add_mail = raw_input("\033[32;1m请输入您添加用户的邮箱：\033[0m") #获取用户的邮箱
                    hash = hashlib.md5()
                    hash.update(add_pass)
                    add_pass = hash.hexdigest()

                    user_infos[add_name] = {'username':add_name,'mail':add_mail,'login_num': 0,'password':add_pass,'credit_money':15000}  #添加用户信息
                    with open('user_info','wb') as e:
                        json.dump(user_infos,e)
                    print "\033[32;1m%s用户添加完成\033[0m" % add_name

                    neirong = "%s用户注册成功" % add_name
                    yonghu = add_name
                    youxiang = user_infos[add_name]['mail']
                    zhuti = '用户注册成功'
                    mail.email(neirong,yonghu,youxiang,zhuti)  #调用发送邮件函数发送邮件
                else:
                    print "\033[31;1m用户已存在\033[0m"
            if user_add == '2':
                with open('card_info','rb') as d:  #读取用户原有信息
                    card_info = json.load(d)
                add_name = raw_input('\033[32;1m请输入你要添加的卡号：\033[0m')
                if not card_info.get(add_name): #判断原文件中是否有相同的用户名，如果有提示用户已存在，如果没有添加！
                    add_pass = raw_input("\033[32;1m请输入您添加卡号的密码：\033[0m") #获取用户的密码并加密
                    add_mail = raw_input("\033[32;1m请输入您添加卡号的邮箱：\033[0m") #获取用户的邮箱
                    hash = hashlib.md5()
                    hash.update(add_pass)
                    add_pass = hash.hexdigest()
                    card_info[add_name] = {'username':add_name,'mail':add_mail,'login_num': 0,'password':add_pass}
                    with open('card_info','wb') as e:  #把新增的内容写入文件
                        json.dump(card_info,e)
                    print "\033[32;1m%s卡号添加完成\033[0m" % add_name

                    neirong = "%s卡号注册成功" % add_name
                    yonghu = add_name
                    youxiang = card_info[add_name]['mail']
                    zhuti = '卡号注册成功'
                    mail.email(neirong,yonghu,youxiang,zhuti)  #调用邮件函数发送邮件
                else:
                    print "\033[31;1m用户已存在\033[0m"
        elif num == '3':
            print '''\033[32;1m30号为账单日发送本月的消费记录通过邮件发送，月底为最后还款日期，10号为计息日如有为还款按未还款的万分之五计算。
输入1发送消费记录、输入2计算利息\033[0m'''
            func = raw_input("\033[32;1m请输入选择的功能：\033[0m")
            '''d = datetime.datetime.now()
               d.day = daynow  获取天的日期
               if daynow = 30: 如果为20号就发送邮件  (为了方便测试就没有使用自动的操作，请手动执行输入，1发送消费记录)
            '''
            if func == '1':
                print "\033[32;1m请确保用户这个月有消费记录\033[0m"
                #循环查找用户，然后匹配用户的信息判断用户消费记录是否存在
                user_list = [] #添加空列表把用户信息加入到列表中然后获取列表使用发送邮件！
                mothe_now = time.strftime("%Y%m")  #获取本月日期
                with open('user_info','rb') as f:  #加载用户信息
                    user_get = json.load(f)
                for k,v in user_get.items():
                    user_list.append(k)  #获取用户列表
                for i in user_list:
                    file_name = mothe_now+i  #取出消费记录的文件名称
                    print file_name
                    if os.path.exists(file_name): #如果消费列表文件存在打开，然后发送账单！
                        with open(file_name,'rb') as f: #打开消费列表
                            cost_list = json.load(f)
                        cost_all = 0
                        cost_info = []
                        for m in cost_list:
                            cost_liebiao = m[0]
                            cost_all += m[1]   #计算消费额度
                            cost_info.append(cost_liebiao) #把消费列表中的商品加入到列表中

                        neirong = "您本月的消费列表为：%s您本月的消费总额为：%d，请在下个月10号前还款" % (cost_info,cost_all)
                        yonghu = i
                        youxiang = user_get[i]['mail']
                        zhuti = '消费记录'
                        mail.email(neirong,yonghu,youxiang,zhuti)  #调用邮件函数发送邮件

            if func == '2':
                print "\033[32;1m请把系统时调为每个月的10号即可\033[0m"
                d = datetime.datetime.now()
                if d.day == 1:



            else:
                print "\033[32;1m请把系统时调为每个月的1号即可\033[0m"
        elif num == '0':
            break
        else:
            print "\033[31;1m请输入正确的功能项目\033[0m"