#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getpass
import MySQLdb



class Jumpserver(object):
    def __init__(self):
        pass

    def login(self):
        print '''\033[32;1m**********welcom login jumpserver**********\033[0m
        '''
        while True:
            user_name = raw_input('\033[34;1mPlease input your contrl name: ').strip()
            user_pass = getpass.getpass('\033[34;1mPlease input your pasword: ')


    def mysql_conn(self,command):
        conn = MySQLdb.connect(host='192.168.0.110',user='root',password='nihao123!',db='jumpserver')
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)



    def run(self):
        self.login()