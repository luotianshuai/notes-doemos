#!/usr/bin/env python 
#-*- coding:utf-8 -*-
#I have Readme ,if you have any question you can check it !
#
import getpass
import os

print """欢迎登录，登录流程控制台
输入1：解锁用户
输入2：添加用户
输入3：删除用户
"""

function_name = raw_input("请输入功能（1-3）：")
if function_name == "1":
    print '''目前已锁账户为'''
    print "-------------------------------------------"
    f = file('lockuser','r')
    list_f = f.readlines()
    for line_list in list_f:   #打印已锁列表start
        line_list = line_list.strip()
        print line_list        #打印已锁列表end
    f.close
    print "-------------------------------------------"


    
    for i in range(3):
        name_1 = raw_input("请输入用户名：")
        f = file('lockuser','r')   #
        new_f = file('new_lockuser','a') 
        list_file = f.readlines()
        for line in list_file:
            if name_1 in line:
                line = line.replace(line,'\n')  #替换输入的用户为空白行！
                
                print "用户%s已解锁，请重新登录！" % name_1
                continue   #执行成功后跳出当次循环，后则后面的内容不保！
            new_f.write(line)    #写入文件
            
        f.close()
        new_f.close()
        os.rename('new_lockuser','lockuser')  #替换旧文件
        break
    else:
        print "用户无效请重新输入"

elif function_name == "2":
    print '''目前已有用户为：
请注意用户不能重名'''
    print "-------------------------------------------"
    f = file('userlist','r')   #
    new_f = file('new_userlist','a') 
    list_file = f.readlines() #以行输出
    for line_list in list_file:   
        line_list = line_list.strip()
        print line_list        #打印用户列表
    print "--------------------------------------------"
    add_username = raw_input("请输入如您要添加的用户名：")
    add_pwd = raw_input("请输入要添加用户的密码：") 
    name_none = []
    name_none.append(add_username)
    name_none.append(add_pwd)
    name_list = ";".join(name_none)
    print name_list
    if add_username.strip != '' and add_pwd != '':
        open_userlist = file('userlist','a')
        open_userlist.write(name_list)
        open_userlist.write(';')
        open_userlist.write('\n')
        open_userlist.close
        print "�û�%s�����"  % add_username             
elif function_name == "3":
    print '''目前有效用户为：'''
    print "-------------------------------------------"
    f = file('userlist','r')   #
    new_f = file('new_userlist','a') 
    list_file = f.readlines() #以行输出
    for line_list in list_file:   
        line_list = line_list.strip()
        print line_list        #打印用户列表
    f.close
    print "-------------------------------------------"
    for i in range(3):
        name_userlist = raw_input("请输入要删除的用户名：")
        f = file('userlist','r')   #
        new_f = file('new_userlist','w') 
        list_file = f.readlines()
        for line in list_file:
            if name_userlist in line:
                line = line.replace(line,'\n')  #替换输入的用户为空白行！
                
                print "�û�%s��ɾ����" % name_userlist
                continue   #执行成功后跳出当次循环，后则后面的内容不保！
            new_f.write(line)    #写入文件
            
        f.close()
        new_f.close()
        os.rename('new_userlist','userlist')  #替换旧文件
        break
    else:
        print "用户无效请重新输入"
else:
    print "无效的功能码请输入1-3！"