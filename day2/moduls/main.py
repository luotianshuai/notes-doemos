#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import os
import sys
import pickle
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class Buy(object): #定义类
    user_db = "%s\config\user_info" % BASE_DIR  #定义静态字段，使用打开用户信息
    product_db = "%s\config\product.list" % BASE_DIR #定义静态字段，使用打开商品清单
    def __init__(self): #构造方法
        self.run()

    def run(self): #run方法程序的主要方法
        name = self.login() #调用登陆方法
        if name:#如果，login方法返回为真执行
            print "\033[34;1mwelcome %s login.....\033[0m" % name #打印欢迎信息
            self.buy(name) #调用buy方法并传入登录用户名，登录用户名是为了消费使用
    def login(self): #登录方法
        with open(self.user_db,'rb') as f: #打开用户文件
            user_info = pickle.load(f) #转化数据类型
        while True:
            user_name = raw_input("\033[32;1mPlease input your name:\033[0m")#获取用户的输入
            user_pass = raw_input("\033[32;1mPlease input your pass:\033[0m")#获取用户的输入
            md5 = hashlib.md5() #调用md5加密
            md5.update(user_pass)#更新MD5加密
            user_pass = md5.hexdigest() #获取MD5加密信息
            if user_name in user_info.keys(): #判断用户名是否存在
                if user_info[user_name]['login_num'] >= 3:#判断用户是否被锁定
                    print "\033[31;1mYour account is lock,please ask admin to unlock\033[0m" #锁定就打印信息退出
                    with open(self.user_db,'wb') as f: #打开文件保存当前用户信息
                        pickle.dump(user_info,f)
                    return False #并返回False
                if user_pass == user_info[user_name]['password']: #如果密码正确
                    user_info[user_name]['login_num'] = 0 #重置用户登录的错误次数
                    with open(self.user_db,'wb') as f: #打开用户信息文件并保存当前用户信息
                        pickle.dump(user_info,f)
                        #print user_name
                    return user_name #并返回用户名

                else:
                    print "\033[31;1mInvalid password,please check if your Continuous mis\
typed 3 password will lock user" #如果密码不正确提示用户
                    user_info[user_name]['login_num'] += 1 #登录错误次数+1
                    if user_info[user_name]['login_num'] >= 3: #判断当前登录的用户登录次数是否大于等于3，如果大于
                        print "\033[31;1mYou in nput error three times in a row ,The %s will lock !\033[0m" % user_name
                        with open(self.user_db,'wb') as w: #打开用户文件信息，并保存
                            pickle.dump(user_info,w)
                        return False
            else:
                print "\033[31;1mSorry,username is invalid please check!\033[0m" #如果用户名不存在提示用户

    def buy(self,name): #商场购买方法
        shoping_list = [] #定义一个空列表存储购买后的商品
        with open(self.product_db,'rb') as f: #打开商品列表
            product_list = pickle.load(f)
        with open(self.user_db,'rb') as g: #打开用户信息
            user_inofss = pickle.load(g)
            salary = user_inofss[name]['money']
        while True:
            index = 1  #定义索引值从1开始
            for item in product_list: #打印商品列表
                print "\033[32;1m%s:Product name:\033[31;1m%s\033[0m    \
\033[32;1mPrice:\033[0m\033[31;1m%s\033[0m" %(index,item[0],item[1])
                index += 1 #定义商品编号加1
            print "\033[34;1mYou have %s$ now\033[0m " % salary #打印当前用户剩余金额
            try:#异常处理模块
                user_choice = int(raw_input("\033[34;1mPlease input what you want\
choice,or input 0 out of the shopping mail!\033[0m"))#获取用户输入商品编号或指令
            except KeyboardInterrupt as e:
                print "\033[31;1mPlease input the product number this is integes!\033[0m"#用户按错了处理
                continue
            except Exception as e:#其他异常处理
                print "\033[31;1mPlease input the product number this is integes!\033[0m"
                continue
            if user_choice == 0:#如果用户选择退出
                ask_exit = raw_input("\033[31;1mPlease input yes will exit ,any else will back shopping mail!")
                if ask_exit != 'yes':continue #判断确认
                print "\033[34:1mThis is you buy list:\033[0m"
                for buylist in shoping_list:  #打印商品列表
                    print "\033[34;1m%s\033[0m" % buylist[0]
                sum_money = 0#定义一个空值，来获取用户此次消费总金额
                for buy_money in shoping_list:
                    sum_money += buy_money[1] #获取用户消费总金额
                print "\033[32;1mYou this time cost :%s" % sum_money #打印总金额
                print "\033[32;1mYou have %s now" % salary #打印剩余金额
                user_inofss[name]['money'] = salary #更新用户信息打开文件保存
                with open(self.user_db,'wb') as b:
                    pickle.dump(user_inofss,b)
                print "\033[34;1mWelcome next shopping \033[0m"
                return

            user_choice -= 1 #用户选择商品编号存在减1为商品编号
            if user_choice > index: #判断如果用户输入的编号不存在提示用户
                print "\033[31;1mPlease input the right product number!\033[0m"
            item_price = product_list[user_choice][1] #如果商品编号存在
            if salary >= item_price:   #判断现有的金额是否大于物品价格
                salary -= item_price  #如果大于购买减去物品价格
                shoping_list.append(product_list[user_choice]) #加入商品列表
                print "\033[34;1mProduct:%s will add to shopping cart.\033[0m" % product_list[user_choice][0]#打印购物列表
                print "\033[33;1mYou have money now:%s\033[0m" %salary #打打印，剩余余额
            else:
                print "\033[31;1mSorry you can't buy %s ,you just have %s now,please buy other product!\033[0m "\
% (product_list[user_choice][0],salary) #剩余钱不足提示！

