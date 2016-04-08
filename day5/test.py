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
             'mail':'451161316@qq.com',
             'login_num':0},
             'shuaige':{'username':'shuaige',
             'password':'21232f297a57a5a743894a0e4a801fc3',
             'mail':'451161316@qq.com',
             'login_num':0},
             }
card_info = {'666666':{'password':'21232f297a57a5a743894a0e4a801fc3',
             'username':'tianshuai',
             'mail':'451161316@qq.com',
             'credit_money':15000,'mail':'451161316@qq.com', 'login_num':0},
             '88888888':{'password':'21232f297a57a5a743894a0e4a801fc3',
             'username':'shuaige',
             'mail':'451161316@qq.com',
             'credit_money':15000,'mail':'451161316@qq.com', 'login_num':0}
}

with open('user_info','wb') as f:
    json.dump(user_info,f)
with open('card_info','wb') as f:
    json.dump(card_info,f)
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
'''
with open('card_info','rb') as d:  #打开文件并用json把字符串转换为数据类型
    card_info = json.load(d)
for k,v in card_info.items(): #循环查找字典中的用户状态
    if v['login_num'] == 3: #如果用户处于被锁状态的话加入到列表中
        print k
        #print u'\033[31;1m%s用户已被锁定' % lock_user  #打印被锁用户信
'''
'''
def test(*arg):
    print arg
    print arg[1]

test(1,2,3,4,5)
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
print d.day