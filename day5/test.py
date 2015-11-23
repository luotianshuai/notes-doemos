#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pickle

with open('user_info','rb') as f:
    user_info = pickle.load(f)
print user_info
print type(user_info)
a = 'tianshuai'
print user_info[a]