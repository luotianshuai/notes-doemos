#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import paramiko

transport = paramiko.Transport(('192.168.7.100',22))
transport.connect(username='root',password='nihao123!') #调用transport进行连接

sftp = paramiko.SFTPClient.from_transport(transport)#然后创建SFTPClient并基于transport连接，把他俩做个绑定

sftp.put('testsftpfile.zip','/tmp/sftpfile-luotianshuai.zip') #将sftpfile.zip上传到目标机器的/tmp/sftpfile-luotianshuai.zip
sftp.get('/tmp/messages.log','shuaige.log') #下载目标服务器/tmp/messages.log 到本地的shuaige.log文件（程序执行目录中）

transport.close()