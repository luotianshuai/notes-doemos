#!/usr/bin/env python
#-*- coding:utf-8 -*-

import paramiko
import threading
import sys
import os
import time

class Cmd(object):
    lock = threading.RLock() #启用线程锁
    def __init__(self,args): #定义构造函数，接收参数
        self.args = args
        self.works_start() #执行程序

    def works_start(self):
        if len(self.args) == 1: #如果程序后没有跟参数，调用help()方法并退出
            self.help()
        else:
            try: #启用异常处理
                if '-c' == self.args[1]: #如果第二个参数为-c
                    self.user_input = ' '.join(self.args[2:]) #把-c 后面的参数拼接成一串自字符串！
                    self.send_command() #执行命令方法
                elif '-f' == self.args[1] and len(self.args) == 4: #如果第二个参数为-f并且总共为4个参数
                    self.source_filepath = self.args[2] #获取源文件
                    if not os.path.exists(self.source_filepath): #判断如果源文件不存在退出并提示
                        print "\033[31;1mfile :%s is not exists please check file \033[0m" % self.source_filepath
                        return
                    self.destination_filepath = self.args[3] #获取目的路径和文件名
                    self.send_file() #执行发送文件
                else:
                    self.help()
            except KeyboardInterrupt as e:
                print "\033[34;1m the server will exit\033[0m"
            except Exception as e:
                print e
    def c_c(self,arg): #command执行方法
        self.lock.acquire() #线程锁
        host_ip = arg[0]
        host_port = int(arg[1])
        host_username = arg[2]
        host_userpass = arg[3]
        ssh = paramiko.SSHClient() #调用paramikoSSH连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #密码认证策略
        ssh.connect(host_ip,host_port,host_username,host_userpass) #传入server信息进行认证
        stdin, stdout, stderr = ssh.exec_command(self.user_input) #传入用户输入的命令
        print stdout.read() #打印结果
        ssh.close(); #关闭ssh连接
        self.lock.release() #释放线程锁

    def send_command(self): #定义命令方法
        master_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #定义顶级目录
        config_file = '%s\conf\ip.txt' % master_dir #找到server服务信息文件
        with open(config_file,'rb') as f: #循环
            for i in f:
                i = i.strip()
                i = i.split('|')
                print i
                t = threading.Thread(target=self.c_c,args=(i,)) #启用多线程
                t.start() #开始执行
    def c_f(self,arg):
        self.lock.acquire()#线程锁
        host_ip = arg[0]
        host_port = int(arg[1])
        host_username = arg[2]
        host_userpass = arg[3]
        t = paramiko.Transport((host_ip,host_port)) #调用paramiko传输连接端口和服务器
        t.connect(username=host_username,password=host_userpass) #传入用户认证信息
        sftp = paramiko.SFTPClient.from_transport(t) #调用paramiko传输，实例化对象
        print "\033[34;1mFile is put done Source:%s Destination:%s\033[0m" % (self.source_filepath,self.destination_filepath)
        sftp.put(self.source_filepath,self.destination_filepath) #传输源文件、目的文件
        t.close()#关闭连接
        self.lock.release() #释放线程锁
    def send_file(self):#定义发送文件方法
        master_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #定义顶级目录
        config_file = '%s\conf\ip.txt' % master_dir #获取server服务器信息文件
        with open(config_file,'rb') as f: #打开文件并循环
            for i in f:
                i = i.strip()
                i = i.split('|')
                print i
                t = threading.Thread(target=self.c_f,args=(i,))#启用多线程
                t.start() #开始执行
    def help(self):
        msg = '''\033[31;1m
python action.py -c command   :will send command to all server
python action.py -f source_filepath destination_filepath :will send file to all server user home dir
        \033[0m
        '''
        sys.exit(msg)