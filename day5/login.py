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
             'login_num':0},
             '666666':{'credit_card_password':'21232f297a57a5a743894a0e4a801fc3',
             'credit_money':15000,'mail':'451161316@qq.com', 'login_num':0},
             'shuaige':{'username':'shuaige',
             'password':'21232f297a57a5a743894a0e4a801fc3',
             'login_num':0},
             '88888888':{'credit_card_password':'21232f297a57a5a743894a0e4a801fc3',
             'credit_money':15000,'mail':'451161316@qq.com', 'login_num':0}
             }
with open('user_info','wb') as f:
    pickle.dump(user_info,f)

'''
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pickle

def login_api():
    with open('user_info','rb') as f:
        usernew_info = pickle.load(f)
    lock_user = 0
    for i in range(3):
        username = raw_input("\033[32;1m请输入您的用户名：")
        password = raw_input("\033[32;1m请输入您的密码：")
        if usernew_info.get(username):
            if usernew_info[username]['login_num'] == '3':
                return "\033[31;1m您好您的账号已被锁定\033[0m"
            if usernew_info[username]['password'] == password:
                return "登录成功"
            else:
                print "\033[31;1m您好您输入的密码错误请重新输入\033[0m"
                lock_user += 1
                if lock_user == 3:
                    usernew_info[username]['login_num'] = '3'
                    with open('user_info','wb') as f:
                        pickle.dump(usernew_info,f)
                    return "\033[31;1m您的账户输入错误了3次密码账号已被锁定\033[0m"
        else:
            print "\033[31;1m您输入的用户名不存在\033[0m"

