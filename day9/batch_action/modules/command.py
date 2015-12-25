#!/usr/bin/env python
#-*- coding:utf-8 -*-

import paramiko
import threading
import sys
import os
import time

class Cmd(object):
    lock = threading.RLock()
    def __init__(self,args):
        self.args = args
        self.works_start()

    def works_start(self):
        if len(self.args) == 1:
            self.help()
        else:
            try:
                if '-c' == self.args[1]:
                    self.user_input = ' '.join(self.args[2:])
                    print self.user_input
                    self.send_command()
                elif '-f' == self.args[1] and len(self.args) == 4:
                    self.source_filepath = self.args[2]
                    if not os.path.exists(self.source_filepath):
                        print "\033[31;1mfile :%s is not exists please check file \033[0m" % self.source_filepath
                        return
                    self.destination_filepath = self.args[3]
                    self.send_file()
                else:
                    self.help()
            except KeyboardInterrupt as e:
                print "\033[34;1m the server will exit\033[0m"
            except Exception as e:
                print e
    def c_c(self,arg):
        self.lock.acquire()
        host_ip = arg[0]
        host_port = int(arg[1])
        host_username = arg[2]
        host_userpass = arg[3]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host_ip,host_port,host_username,host_userpass)
        stdin, stdout, stderr = ssh.exec_command(self.user_input)
        print stdout.read()
        ssh.close();
        self.lock.release()

    def send_command(self):
        master_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file = '%s\conf\ip.txt' % master_dir
        with open(config_file,'rb') as f:
            for i in f:
                i = i.strip()
                i = i.split('|')
                print i
                t = threading.Thread(target=self.c_c,args=(i,))
                t.start()
    def c_f(self,arg):
        self.lock.acquire()
        host_ip = arg[0]
        host_port = int(arg[1])
        host_username = arg[2]
        host_userpass = arg[3]
        t = paramiko.Transport((host_ip,host_port))
        t.connect(username=host_username,password=host_userpass)
        sftp = paramiko.SFTPClient.from_transport(t)
        print "\033[34;1mFile is put done Source:%s Destination:%s\033[0m" % (self.source_filepath,self.destination_filepath)
        sftp.put(self.source_filepath,self.destination_filepath)
        t.close()
        self.lock.release()
    def send_file(self):
        master_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file = '%s\conf\ip.txt' % master_dir
        with open(config_file,'rb') as f:
            for i in f:
                i = i.strip()
                i = i.split('|')
                print i
                t = threading.Thread(target=self.c_f,args=(i,))
                t.start()
    def help(self):
        msg = '''\033[31;1m
python action.py -c command   :will send command to all server
python action.py -f source_filepath destination_filepath :will send file to all server user home dir
        \033[0m
        '''
        sys.exit(msg)




'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.108', 22, 'alex', '123')
    stdin, stdout, stderr = ssh.exec_command('df')
    print stdout.read()
    ssh.close();
    '''