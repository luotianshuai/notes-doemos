#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='nihao123!',db='jumpserver')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
tim = '\'luotianshuai\''
cur.execute('select  and d.user_name = %s' % tim)

command_mysql = cur.fetchall()
print command_mysql
#print reCount
#print nret

'''
import threading
import paramiko

ssh = paramiko.SSHClient() #创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许连接不在know_hosts文件中的主机
ssh.connect(hostname='192.168.0.111',port=22,username='root',password='nihao123!')
stdin,stdout,stderror = ssh.exec_command('df -h') #执行命令

print stdout.read() #获取命令结果
print stderror.read() #如果执行错误返回错误结果
#ssh.close() #关闭连接
