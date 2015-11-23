#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pickle

def login_api(username,password):
    with open('user_info','rb') as f:
        user_info = pickle.load(f)
    user_get = user_info.get(username)
    if user_get and user_info[username]['password'] == password:
        return True
    else:
        return False


import login
import shopingmail

login()