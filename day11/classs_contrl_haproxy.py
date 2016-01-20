#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import paramiko
import uuid
class Haproxy(object):
    def __init__(self):
        self.hostname = '192.168.7.100'
        self.port = 22
        self.username = 'root'
        self.password = 'nihao123!'
    def create_file(self):
        file_name = str(uuid.uuid4())  #这个uuid.uuid4()会生成一个文件UUID然后当作文件名
        with open(file_name,'wb') as f:
            f.write('This is test file will send to services')
            return file_name

    def run(self):
        self.connect()
        self.upload()
        self.rename()
        self.close()

    def connect(self): #设置连接方法
        transport = paramiko.Transport(('192.168.7.100',22)) #创建一个连接对象
        transport.connect(username='root',password='nihao123!')#调用transport对象中的连接方法
        self.__transport = transport #把transport赋值给__transport

    def close(self): #关闭连接
        self.__transport.close()

    def upload(self): #上传文件方法
        file_name = self.create_file() #创建文件
        sftp = paramiko.SFTPClient.from_transport(self.__transport) #创建SFTPClient并基于transport连接，把他俩做个绑定
        sftp.put(file_name,'/tmp/luotianshuai.txt') #上传文件

    def rename(self): #执行命令方法
        ssh = paramiko.SSHClient() #建立ssh对象
        ssh._transport = self.__transport #替换ssh_transport字段为self.__transport
        stdin,stdout,stderr = ssh.exec_command('mv /tmp/luotianshuai /tmp/shuaige') #执行命令
        print stdout.read() #读取执行命令

if __name__ == '__main__':
    ha = Haproxy()
    ha.run()

'''
上面的例子中我们就连接了一次，然后用这一次连接进行命令和上传文件的管理!
不用来回的创建和关闭SSH连接
'''