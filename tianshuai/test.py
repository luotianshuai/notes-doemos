#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import hashlib

'''
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()

#例子：
user_info = {'tianshuai':{'username':'tianshuai',
             'password':'21232f297a57a5a743894a0e4a801fc3',
             'login_num':0},
             'shuaige':{'username':'shuaige',
             'password':'21232f297a57a5a743894a0e4a801fc3',
             'login_num':0},
             }
card_info = {'666666':{'password':'21232f297a57a5a743894a0e4a801fc3',
             'username':'tianshuai',
             'credit_money':15000,'mail':'451161316@qq.com', 'login_num':0},
             '88888888':{'password':'21232f297a57a5a743894a0e4a801fc3',
             'username':'shuaige',
             'credit_money':15000,'mail':'451161316@qq.com', 'login_num':0}
}
'''
'''
with open('user_info','w') as f:
    json.dump(user_info,f)
'''
'''
#with open('user_info','wb') as f:
#    json.dump(user_info,f)
with open('card_info','rb') as f:
    a = json.load(f)
print a['666666']['username']
'''
'''
with open('201511tianshuai','rb') as f:
    new = json.load(f)
print new
'''
li = [1,2,3,4,5]
new_li = [6,7,8,9,10]
li.extend(new_li)
print li