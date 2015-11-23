#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pickle
import hashlib

'''
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()


user_info = {'tianshuai':{'username':'tianshuai',
             'password':'21232f297a57a5a743894a0e4a801fc3',
             'login_num':0,
             'credit_card':666666,
             'credit_card_password':'21232f297a57a5a743894a0e4a801fc3',
             'credit_money':15000,},
             'shuaige':{'username':'shuaige',
             'password':'21232f297a57a5a743894a0e4a801fc3',
             'login_num':0,
             'credit_card':88888888,
             'credit_card_password':'21232f297a57a5a743894a0e4a801fc3',
             'credit_money':15000,}
             }

'''



#print user_info['tianshuai']['username']

def login_api(username,password):
    with open('user_info','rb') as f:
        user_info = pickle.load(f)
    user_get = user_info.get(username)
    if user_get and user_info[username]['password'] == password:
        return True
    else:
        return False

print login_api('lskdjf','21232f297a57a5a743894a0e4a801fc3')
