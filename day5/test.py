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
'''
import datetime

d = datetime.datetime.now()
year = d.year
month = d.month
if month == 1 :
    month = 12
    year -= 1
else :
    month -= 1
last_month = str(year)+ str(month)
print last_month
'''
'''
商城已经写完了：！！nice
需要优化：还款那里！
如果到1号，上个月的款项，还没有还完，那么计息（在管理接口那里设置，并发邮件）

'''