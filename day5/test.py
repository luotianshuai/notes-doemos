#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pickle
import time
mothe_now = time.strftime("%Y%m")
li = [1,2,3,4,5]

with open(mothe_now,'r') as d: #存在追加
    cost_list = pickle.load(d)

print cost_list