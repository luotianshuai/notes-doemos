#!/usr/bin/env python
#-*- coding:utf-8 -*-

import SocketServer
import json
import hashlib
from conf import settings
class FtpServer(SocketServer.BaseRequestHandler):
    response_code = {
            '200': "pass user authentication",
            '401': "wrong username or password",
            '404': "invalid username or password",
            '301': "Ready to get file from server",
            '302': "Ready to send to  server",
            '403': "File doesn't exist on ftp server",
    }
    print ('\033[34;1mStart FTPserver on IP:%s PORT:%s' % (settings.BIND_HOST,settings.BIND_PORT))
    def handel(self):
        while  True:
            data = self.request.recv(1024) #接收1024字节数据,收到的数据不一定是1024,根据客户端实际发过来的大小来定
            print("client send data::",data)
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
            func()
        else:
            print ("\033[31;1mReceived invalid instruction [%s] from client!\033[0m" %(instructions))
    def user_auth(self,data):#认证函数
        auth_info = json.loads(data[1])
        if auth_info['username'] in settings.USER_ACCOUNT:
            if auth_info['password'] == settings.USER_ACCOUNT[auth_info['username']]:
                response_code = '200'
                self.loging_user = auth_info['user_name'] #定义全局变量，方便获取
            else:
                response_code = '401'
        else:
            response_code = '404'
        response_str = "response|%s|%s" %(response_code,self.response_code_list[response_code])
        #这里self.response_code_list 是为了以后扩展使用
        self.request.send(response_str)

