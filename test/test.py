#!/usr/bin/env python
#-*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host='192.168.0.110',user='root',passwd='nihao123!',db='jumpserver')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
reCount = cur.execute('SELECT * FROM user_info')
nret = cur.fetchall()

cur.close()
conn.close()

print reCount
print nret

for i in nret:
    print i[0],i[1]