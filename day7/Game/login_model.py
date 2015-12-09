#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
游戏账号登录接口，用户密码登录游戏、密码输入3次后锁定
'''
import pickle
import hashlib
import getpass
'''
userlist = {"shuaige":{'password':'37d2b9990df5a6843caf19352fee42a6','login_num':0},
            "tianshuai":{'password':'37d2b9990df5a6843caf19352fee42a6','login_num':0}

}
with open('user_info','wb') as f:
    pickle.dump(userlist,f)
'''

def login_api():
    with open('user_info','rb') as f:
        user_infos = pickle.load(f)  #通过pickle把文件内容字符串转换成数据类型
    lock_user = 0  #定义循环起始值，用来判断用户输入错误密码的次数！
    for i in range(3):
        username = raw_input("\033[32;1m请输入您的用户名：\033[0m")
        password = raw_input("\033[32;1m请输入您的密码：\033[0m")
        hash = hashlib.md5()  #md5加密
        hash.update(password) #md5加密
        password = hash.hexdigest()#md5加密
        if user_infos.get(username): #判断用户输入的用户是否存在，通过字典的get方法判断key是否存在
            if user_infos[username]['login_num'] >= 3:
                print "\033[31;1m您好你输入的账户已被锁定\033[0m"
            print "用户存在"
        else:
            print "\033[31;1m您好您输入的用户信息不存在\033[0m"


login_api()
