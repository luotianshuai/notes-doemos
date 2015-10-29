#!/usr/bin/env python 
#-*- coding:utf-8 -*_-

import getpass

count = 0

for i in range(3):
    input_user = raw_input("请输入用户名: ")
    input_pwd = getpass.getpass("请输入密码: ")
    check_lock = file('lockuser','r') #打开被锁用户文件，查看用户是否被锁
    lock_user = check_lock.readlines() #每行读取
    user_login_flag = False
    
    for line in lock_user:
        line = line.strip('\n')  #取消回车符
        if input_user == line:       #检查用户是否被锁
            print "%s 用户是被锁定的，请联系管理员解锁！"  % input_user
            user_login_flag = True
            break        
    if user_login_flag:
        user_login_flag = True
        break
    
    user_list = file('userlist','r')
    user_line = user_list.readlines()   #每行读取
    
    for userline in user_line:
        value_name = userline.strip()
        user_list = value_name.split(';')
        user_name = user_list[0]    #获取用户名
        user_pwd = user_list[1]     #获取密码
        
        if input_user == "guest":
            print "欢迎%s"  % input_user
            user_login_flag = True
            break
        elif input_user == user_name and input_pwd == user_pwd:  #判断是可用用户并且密码正确，登录
            print "欢迎%s 登录系统" % input_user
            user_login_flag = True
            break
        elif input_user == user_name and input_pwd != user_pwd:  #判断是可用用户，如果密码错误！尝试3次，锁定
            print "您输入的密码有误，请重新输入："
            while True:
                count += 1
                input_pwd = getpass.getpass("请输入密码: ")
                user_login_flag = False
                
                if  input_pwd == user_pwd:
                    print "欢迎%s 登录系统" % input_user
                    user_login_flag = True
                    break
                else:
                    print "您输入的密码有误请重新输入："
                if count == 2:  #连续输入错误3次密码后锁定
                    tolock = open('lockuser','a')
                    tolock.write(input_user)   #写入只锁定文件，程序启动时讲读取
                    tolock.write("\n")                          
                    tolock.close
                    print "%s 用户联系输入错误3次密码已被锁定，请联系管理员解锁" % input_user
                    user_login_flag = True
                    break
            if user_login_flag:
                user_login_flag = True
                break

    if user_login_flag:
        break
    else:
        print "您输入的%s用户名无效，请重新输入" % input_user
else:
    print "你输入错误了3次用户名或密码系统讲退出！"