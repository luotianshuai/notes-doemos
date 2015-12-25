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
                if '-c' in self.args and len(self.args) == 3:
                    self.user_input = self.args[self.args.index('-c') +1]
                    self.send_command()
                elif '-f' in self.args and len(self.args) == 3:
                    self.user_inputf = self.args[self.args.index('-f') +1]
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
    def send_file(self):
        pass

    def help(self):
        msg = '''\033[31;1m
python action.py -c command   :will send command to all server
python action.py -f file path :will send file to all server user home dir
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