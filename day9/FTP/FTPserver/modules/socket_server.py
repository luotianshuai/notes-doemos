#!/usr/bin/env python
#-*- coding:utf-8 -*-

import SocketServer
import json
import os
import hashlib
import time
from conf import settings
class FtpServer(SocketServer.BaseRequestHandler):
    #继承BaseRequestHandler基类，然后必须重写handle方法，并且在handle方法里实现与客户端的所有交互
    response_code_list  = {
            '200': "pass user authentication",
            '401': "wrong username or password",
            '404': "invalid username or password",
            '300': "Ready to send file",
            '301': "Ready to get file from server",
            '302': "Ready to send to  server",
            '403': "File doesn't exist on ftp server",
    }

    print ('\033[34;1mStart FTPserver on IP:%s PORT:%s\033[0m' % (settings.BIND_HOST,settings.BIND_PORT))

    def handle(self):
        while  True:
            data = self.request.recv(1024) #接收1024字节数据,收到的数据不一定是1024,根据客户端实际发过来的大小来定
            print("client send data::%s" % data)
            if not data:
                print("\033[31;1mHas lost client\033[0m", self.client_address)
                break     #如果收不到客户端数据了（代表客户端断开了），就断开
            self.instruction_allowcation(data) #客户端发过来的数据统一交给功能分发器处理,他会判断需要做的动作
    def instruction_allowcation(self,instructions):
        '''功能分发器,负责按照客户端的指令分配给相应的方法处理'''
        instructions = instructions.split("|")
        function_str = instructions[0]# 客户端发过来的指令中,第一个参加都必须在服务器端有相应的方法处理
        if hasattr(self,function_str): #判断是否能找到相应的方法处理
            func = getattr(self,function_str)
            func(instructions)
        else:
            print ("\033[31;1mReceived invalid instruction [%s] from client!\033[0m" %(instructions))
    def user_auth(self,data):#认证函数
        auth_info = json.loads(data[1])
        if auth_info['username'] in settings.USER_ACCOUNT:
            if auth_info['password'] == settings.USER_ACCOUNT[auth_info['username']]['password']:
                response_code = '200'
                self.login_user = auth_info['username'] #定义全局变量，方便获取
            else:
                response_code = '401'
        else:
            response_code = '404'
        response_str = "response|%s|%s" % (response_code,self.response_code_list[response_code]) #拼接server发送信息
        self.request.send(response_str)
        return response_code
    def file_get(self,user_data):
        print("\033[32;1m---client will get  file----\033[0m")
        if self.login_user : #判断用户是否登录
            filename_with_path = json.loads(user_data[1])#获取文件名
            file_abs_path = "%s/%s/%s" %(settings.USER_HOME,self.login_user, filename_with_path) #获取文件的路径
            print file_abs_path
            if os.path.isfile(file_abs_path): #判断文件是否存在
                file_size = os.path.getsize(file_abs_path) #获取文件大小
                response_msg = "response|300|%s|n/a" %(file_size)
                print '111111111111111111111111111111111111111111111111111111111'
                print response_msg
                self.request.send(response_msg) #发送确认信息
                client_response = self.request.recv(1024).split("|")
                print "\033[34;1m%s\033[0m" % client_response
                if client_response[1] == "301": #客户端已经准备接收文件
                    sent_size = 0
                    f = open(file_abs_path,"rb")
                    t_start = time.time()
                    while file_size != sent_size:
                        data = f.read(4096)
                        self.request.send(data)
                        sent_size += len(data)
                        print ("send:",file_size,sent_size)
                    else:
                        t_cost = time.time() - t_start
                        print "----file transfer time:---",t_cost
                        print("\033[32;1m----successfully sent file to client----\033[0m")
            else:
                response_msg = "response|403|n/a|n/a"
                self.request.send(response_msg)