#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import pickle
import hashlib


def login_api(username,password):
    with open('user_info','rb') as f:
        user_info = pickle.load(f)
    usernew_info = pickle.loads(user_info)
    u_name = usernew_info[username['username']]
    u_password = usernew_info[username['password']]
    if u_name == username and password == u_password:
        return True
    else:
        return False
def auth(func):
    def inner(*args,**kwargs):
        if login_api()
@auth
def buy(username,password):
    with open('buy_list','rb') as f:
        for k,v in enumerate(pickle.load(f),1):
            print k,v[0],v[1]
#buy()

if __name__ == '__main__':
    print "\033[32;1m欢迎来到帅哥商城\033[0m"
    user_name = raw_input("\033[32;1m请输入您的用户名：")
    user_pass = raw_input("\033[32;1m请输入您的密码：")
    hash = hashlib.md5()
    user_pass = hash.update(user_pass)
    buy(user_name,user_pass)
