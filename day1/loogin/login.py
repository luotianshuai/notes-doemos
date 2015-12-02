#!/usr/bin/env python
#-*- coding:utf-8 -*-

with open('db','rb') as user_info: #打开文件
    user_infos = user_info.readlines() #读取用户信息按行存储到列表中

user_dic = {} #定义一个空字典把列表中的用户循环加入到字典中

for list_to_dic in user_infos: #循环列表
    #list_to_dic = list_to_dic.strip() #取消每行后面的换行符
    list_info = list_to_dic.split(';') #按照‘；’分割每行
    user_dic[list_info[0]] = {'password':list_info[1],'login_num':int(list_info[2].strip())}
    #按照用户名为key，其他信息为vlaue的样式追加至字典并取消后面的换行符

while True:
    username = raw_input("\033[32;1m您好请输入您的用户名：\033[0m")
    password = raw_input("\033[32;1m您好请输入您的密码：")
    if username in user_dic.keys():   #循环判断用户输入的用户名是否存在
    #user_dic.keys()是获取user_dic中的所有key，然后user_dic.keys()或生成包含所有keys的列表
        if user_dic[username]['login_num'] >= 3: #首先判断用户名是否被锁
            print "\033[31;1m%s用户账户已被锁定请联系管理员解锁\033[0m" % username
            user_listnew = []  #定义一个空列表存储新的的用户信息
            for k,v in user_dic.items():  #循环内存中的User_dic信息，然后拼接为字符串
                userinfo = "%s;%s;%d" % (k,v['password'],v['login_num'])  #拼接字符串并加入到列表中
                user_listnew.append(userinfo)  #追加到列表
            usernewinfo = "\n".join(user_listnew)  #用\n来把列表分割并转换为字符串
            with open('db','wb') as f:  #以写的方式打开文件
                f.write(usernewinfo) #写入至文件中
                f.flush() #立刻刷新至硬盘
            break
        if password == user_dic[username]['password']: #如果密码匹配退出程序
            print "\033[32;1m欢迎\033[31;1m%s\033[0m\033[32;1m登录系统\033[0m" % username
            user_dic[username]['login_num'] = 0 #登录成功后重置登录错误次数
            user_listnew = []  #定义一个空列表存储新的的用户信息
            for k,v in user_dic.items():  #循环内存中的User_dic信息，然后拼接为字符串
                userinfo = "%s;%s;%d" % (k,v['password'],v['login_num'])  #拼接字符串并加入到列表中
                user_listnew.append(userinfo)  #追加到列表
            usernewinfo = '\n'.join(user_listnew)  #用\n来把列表分割并转换为字符串
            with open('db','wb') as f:  #以写的方式打开文件
                f.write(usernewinfo) #写入至文件中
                f.flush() #立刻刷新至硬盘
            break  #登录成功后退出程序
        else:
            print "\033[31;1m%s的密码错误\033[0m" % username
            user_dic[username]['login_num'] += 1
    else:
        print "\033[31;1m您输入的用户名：\033[34;1m%s\033[0m\033[31;1m不存在\033[0m" % username