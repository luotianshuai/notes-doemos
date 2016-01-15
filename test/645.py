#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1234',db='mydb')
#cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
cur = conn.cursor()

reCount = cur.execute('select Name,Address from UserInfo')

nRet = cur.fetchall()

cur.close()
conn.close()

print reCount
print nRet
for i in nRet:
    print i[0],i[1]