#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
import socket_server
from conf import settings

class ArgvHandler(object):
    def __init__(self,args):
        self.args = args #定义普通字段
        self.argv_parser()  #调用判断参数的方法

    def argv_parser(self): #判断参数方法！
        if len(self.args) == 1: #sys.argv程序本身就是一个参数
            self.help_msg() #如后后面没有跟参数执行help方法
        else:
            if hasattr(self,self.args[1]): #通过反射判断当前的类中是否存在用户输入的方法
                func = getattr(self,self.args[1]) #如果存在获取方法
                func() #执行方法
            else:
                self.help_msg()


    def help_msg(self):
        msg = '''\033[31;1m
        start       :will to start ftp services
        ctrl+c      :will to stop  ftp services
        help        :will to show  ftp helpmsg\033[0m
        '''
        sys.exit(msg) #打印并退出

    def start(self):
        try: #调用异常处理模块捕捉错误！
            server = socket_server.SocketServer.ThreadingTCPServer((settings.BIND_HOST,settings.BIND_PORT),socket_server.FtpServer)
            server.serve_forever()
        except KeyboardInterrupt as e: #捕捉退出错误
            print ("\033[32;1mThe Server will be shutdown!\033[0m")
            server.shutdown()
        except Exception as e: #使用万能错误捕捉
            print (e)
    def help(self):
        self.help_msg()
        sys.exit()
