#!/usr/bin/env python
#-*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='nihao123!',db='jumpserver')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
cur.execute('SELECT user_name,user_pass FROM user_info')

command_mysql = cur.fetchall()
print command_mysqld

#print reCount
#print nret

