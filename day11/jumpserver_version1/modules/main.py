#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getpass
import MySQLdb
import paramiko
from multiprocessing import Process
from login_terminal import login_terminal

class Jumpserver(object):
    def __init__(self):
        self.mysql_conn()

    def login(self):
        print '''\033[32;1m**********welcom login jumpserver**********\033[0m
        '''
        while True:
            user_name = raw_input('\033[34;1mPlease input your contrl name: ').strip()
            user_pass = getpass.getpass('\033[34;1mPlease input your pasword: ')
            if self.auth(user_name,user_pass):
                self.login_name = user_name
                self.login_pass = user_pass
                return

    def auth(self,username,password):
        self.mysql_command.execute('select user_name,user_pass from user_info')
        userinfo = self.mysql_command.fetchall()
        for i in userinfo:
            if username in i.values() and password in i.values():
                print "\033[32;1mWelcom login %s jumpserver" % username
                return True
        else:
            print "\033[31;1mSorry your input user name or password is worng ,please check It."
            return False


    def mysql_conn(self):
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='nihao123!',db='jumpserver')
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        self.mysql_command = cur
    def func_command(self,ip,username,pwd,usercommand):
        print "%s start======>" % ip
        ssh = paramiko.SSHClient() #创建SSH对象
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许连接不在know_hosts文件中的主机
        ssh.connect(hostname=ip,port=22,username=username,password=pwd)
        stdin,stdout,stderror = ssh.exec_command(usercommand) #执行命令

        print stdout.read() #获取命令结果
        print stderror.read() #如果执行错误返回错误结果
        #ssh.close() #关闭连接
        print "%s command =====> \n %s\n" % (ip,stdout.read()) #读取执行命令

    def func__e(self):
        user_intpu = raw_input("\033[32;1mPlease input you command:\033[0m")

        login_user = '\'%s\'' % self.login_name
        self.mysql_command.execute('select address from host_info a,host_group_relation b,host_group c,user_info d where a.host_id = b.host_id and b.group_id = c.group_id and b.group_id = d.user_group_id and d.user_name= %s' % login_user)
        ip_infos = self.mysql_command.fetchall()
        server_list = []
        for i in ip_infos:
            print i.values()
            server_list.append(i.values()[0])
        for r in server_list:
            t = Process(target=self.func_command,args=(r,self.login_name,self.login_pass,user_intpu,))
            print r
            t.start()

    def func__d(self):
        pass
        #方法和执行命令类似
    def func__u(self):
        pass
        #方法和执行命令类似
    def func__p(self):
        login_user = '\'%s\'' % self.login_name
        #print login_user
        self.mysql_command.execute('select address from host_info a,host_group_relation b,host_group c,user_info d where a.host_id = b.host_id and b.group_id = c.group_id and b.group_id = d.user_group_id and d.user_name= %s' % login_user)
        ip_infos = self.mysql_command.fetchall()
        server_list = []
        for i in ip_infos:
            print i.values()
            server_list.append(i.values()[0])
        ask_userlogin = raw_input('\033[34;1mIf you want to login server please input the IP address any else back func list: ')
        print server_list
        if ask_userlogin in server_list:
            print "fuck"
            login_terminal(ask_userlogin,self.login_name,self.login_pass)
            del server_list
        else:
            del server_list




    def func_list(self):
        print '''
            ###########################################################################
            #                                                                         #
            #                           Shuai JumpServer                              #
            #                                                                         #
            ###########################################################################
            1)Input p will show all server (only you can see,and you can chose ip login)
            2)Input e send command to all server
            3)Input d download file from all server
            4)Input u put file to all server
        '''
        while True:
            func_input = raw_input('\033[34;1mPlease input what you want:::\033[0m')
            if hasattr(self,'func__' + func_input):
                func = getattr(self,'func__' + func_input)
                func()
            else:
                print "\033[31;1mYou input invalid please check!"

    def run(self):
        self.login()
        self.func_list()
