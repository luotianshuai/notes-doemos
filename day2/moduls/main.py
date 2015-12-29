#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import os
import sys
import pickle
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class Buy(object):
    user_db = "%s\config\user_info" % BASE_DIR
    product_db = "%s\config\product.list" % BASE_DIR
    def __init__(self):
        self.run()

    def run(self):

        if self.login():
            print "hello"
        else:
            print "Login fail"

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
                    print "\033[34;1mLogin success\033[0m"
                    user_info[user_name]['login_num'] == 0
                    with open(self.user_db,'wb') as f:
                        pickle.dump(user_info,f)
                    return True
                else:
                    print "\033[31;1mInvalid password,please check if your Continuous mis\
typed 3 password will lock user"
                    user_info[user_name]['login_num'] += 1
            else:
                print "\033[31;1mSorry,username is invalid please check!\033[0m"

