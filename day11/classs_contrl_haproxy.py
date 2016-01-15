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
            f.write('This is test file will send to server')
            return file_name
    def run(self):
        self.connect()
        self.upload()
        self.rename()
        self.close()
    def connect(self):
        transport = paramiko.Transport(('192.168.7.100',22)) #创建一个连接对象
        transport.connect(username='root',password='nihao123!')#调用transport对象中的连接方法
        self.__transport = transport #把transport赋值给__transport
    def close(self):
        self.__transport.close()
    def upload(self):
        file_name = self.create_file()
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(file_name,'/tmp/luotianshuai.txt')
    def rename(self):
        ssh = paramiko.SSHClient
        ssh._transport = self.__transport
        stdin,stdout,stderr = ssh.exec_command('mv /tmp/luotianshuai.txt /tmp/shuaige')
        result = stdout.read()
        print result

if __name__ == '__main__':
    woker = Haproxy()
    woker.run()
