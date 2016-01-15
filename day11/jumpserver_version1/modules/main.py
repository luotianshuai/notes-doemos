#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getpass
import MySQLdb



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

    def func__p(self):
        self.mysql_command.execute('SELECT address FROM host_info a,host_group_relation b,host_group c,user_info d where a.host_id = b.host_id and b.group_id = c.group_id and b.group_id = d.user_group_id = %s' % self.login_name)
        #ip_infos = self.mysql_command.fetchall()
        #
        print 'shuaige'


    def func_list(self):
        print '''
            ###########################################################################
            #                                                                         #
            #                           Shuai JumpServer                              #
            #                                                                         #
            ###########################################################################
            1)Input p will show all server (only you can see,and you can chose ip login)
            2)Input g will show all server group
            3)Input e send command to all server
            4)Input d download file from all server
            5)Input u put file to all server
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