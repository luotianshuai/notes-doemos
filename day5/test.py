#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pickle
import time
mothe_now = time.strftime("%Y%m")
shoping_list = [1,2,3,4,5]
shuai = [100,101,102]

print shuai.extend(shoping_list)
print shoping_list

'''
with open(mothe_now,'r') as d: #存在追加
    cost_list = pickle.load(d)
print cost_list
new_cost_list = shoping_list.extend(cost_list)
for i in new_cost_list:
    print i
'''
'''
    new_cost_list = cost_list.extend(shoping_list) #把两个列表进行扩展
print new_cost_list
'''