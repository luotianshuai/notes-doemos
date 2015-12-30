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
            print "\033[34;1mwelcome %s login.....\033[0m" % name
            self.buy(name)



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
                    "\033[31;1mYour account is lock,please ask admin to unlock\033[0m"
                    with open(self.user_db,'wb') as f:
                        pickle.dump(user_info,f)
                    return False
                if user_pass == user_info[user_name]['password']:
                    #print "\033[34;1mLogin success\033[0m"
                    user_info[user_name]['login_num'] == 0
                    with open(self.user_db,'wb') as f:
                        pickle.dump(user_info,f)
                        #print user_name
                    return user_name

                else:
                    print "\033[31;1mInvalid password,please check if your Continuous mis\
typed 3 password will lock user"
                    user_info[user_name]['login_num'] += 1
            else:
                print "\033[31;1mSorry,username is invalid please check!\033[0m"

    def buy(self,name):
        with open(self.product_db,'rb') as f:
            product_list = pickle.dump(f)
        while True:
            index = 1  #定义索引值从1开始
            for item in product_list:
                print "\033[32;1m%s: %s\t%s\033[0m" %(index,item[0],item[1])
                index += 1
            try:
                user_choice = int(raw_input("Please input what you want choice,or input 0 out of the shoping mail!"))
            except Exception as e:
                print "\033[31;1mPlease input the product number this is integes!\033[0m"