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
    def login(self):
        with open(self.user_db,'rb') as f:
            user_info = pickle.load(f)
        while True:
            user_name = raw_input("\033[32;1mPlease input your name:\033[0m")
            user_pass = raw_input("\033[32;1mPlease input your pass:\033[0m")
            md5 = hashlib.md5()
            md5.update(user_pass)
            user_pass = md5.hexdigest()
            if user_name in user_info.keys():
                if user_info[user_name]['login_num'] >= 3:
                    print "\033[31;1mYour account is lock,please ask admin to unlock\033[0m"
                    with open(self.user_db,'wb') as f:
                        pickle.dump(user_info,f)
                    return False
                if user_pass == user_info[user_name]['password']:
                    #print "\033[34;1mLogin success\033[0m"
                    user_info[user_name]['login_num'] = 0
                    with open(self.user_db,'wb') as f:
                        pickle.dump(user_info,f)
                        #print user_name
                    return user_name

                else:
                    print "\033[31;1mInvalid password,please check if your Continuous mis\
typed 3 password will lock user"
                    user_info[user_name]['login_num'] += 1
                    if user_info[user_name]['login_num'] >= 3:
                        print "\033[31;1mYou in nput error three times in a row ,The %s will lock !\033[0m" % user_name
                        with open(self.user_db,'wb') as w:
                            pickle.dump(user_info,w)
                        return False
            else:
                print "\033[31;1mSorry,username is invalid please check!\033[0m"

    def buy(self,name):
        shoping_list = []
        with open(self.product_db,'rb') as f:
            product_list = pickle.load(f)
        with open(self.user_db,'rb') as g:
            user_inofss = pickle.load(g)
            salary = user_inofss[name]['money']
        while True:
            index = 1  #定义索引值从1开始
            for item in product_list:
                print "\033[32;1m%s:Product name:\033[31;1m%s\033[0m    \
\033[32;1mPrice:\033[0m\033[31;1m%s\033[0m" %(index,item[0],item[1])
                index += 1
            print "\033[34;1mYou have %s$ now\033[0m " % salary
            try:
                user_choice = int(raw_input("\033[34;1mPlease input what you want choice,or input 0 out of the shopping mail!\033[0m"))
            except KeyboardInterrupt as e:
                print "\033[31;1mPlease input the product number this is integes!\033[0m"
                continue
            except Exception as e:
                print "\033[31;1mPlease input the product number this is integes!\033[0m"
                continue
            if user_choice == 0:
                ask_exit = raw_input("\033[31;1mPlease input yes will exit ,any else will back shopping mail!")
                if ask_exit != 'yes':continue
                print "\033[34:1mThis is you buy list:\033[0m"
                for buylist in shoping_list:
                    print "\033[34;1m%s\033[0m" % buylist[0]
                sum_money = 0
                for buy_money in shoping_list:
                    sum_money += buy_money[1]
                print "\033[32;1mYou this time cost :%s" % sum_money
                print "\033[32;1mYou have %s now" % salary
                user_inofss[name]['money'] = salary
                with open(self.user_db,'wb') as b:
                    pickle.dump(user_inofss,b)
                print "\033[34;1mWelcome next shopping \033[0m"
                return

            user_choice -= 1
            if user_choice > index:
                print "\033[31;1mPlease input the right product number!\033[0m"
            item_price = product_list[user_choice][1]
            if salary >= item_price:   #判断现有的金额是否大于物品价格
                salary -= item_price  #如果大于购买减去物品价格
                shoping_list.append(product_list[user_choice])
                print "\033[34;1mProduct:%s will add to shopping cart.\033[0m" % product_list[user_choice][0]#打印购物列表
                print "\033[33;1mYou have money now:%s\033[0m" %salary #打打印，剩余余额
            else:
                print "\033[31;1mSorry you can't buy %s ,you just have %s now,please buy other product!\033[0m "\
% (product_list[user_choice][0],salary) #剩余钱不足提示！

