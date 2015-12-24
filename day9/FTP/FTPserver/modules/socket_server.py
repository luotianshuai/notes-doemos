#!/usr/bin/env python
#-*- coding:utf-8 -*-

import SocketServer
import json
import os
import hashlib
import subprocess
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
            '303': "Ready to recv file from client",
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
        if hasattr(self,function_str): #判断是否能找到相应的方法处理通过反射
            func = getattr(self,function_str)
            func(instructions)
        else:
            print ("\033[31;1mReceived invalid instruction [%s] from client!\033[0m" %(instructions))
    def user_auth(self,data):#认证函数
        auth_info = json.loads(data[1])
        if auth_info['username'] in settings.USER_ACCOUNT: #判断是否是有效用户
            if auth_info['password'] == settings.USER_ACCOUNT[auth_info['username']]['password']: #判断密码是否相同
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
                file_md5 = self.hashfile(file_abs_path)
                print file_md5
                file_size = os.path.getsize(file_abs_path) #获取文件大小
                response_msg = "response|300|%s|%s" %(file_size,file_md5)
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
                        #print ("send:",file_size,sent_size)
                    else:
                        t_cost = time.time() - t_start
                        print "----file transfer time:---",t_cost
                        print("\033[32;1m----successfully sent file to client----\033[0m")
            else:
                response_msg = "response|403|n/a|n/a"
                self.request.send(response_msg)
    def file_push(self,user_data):#上传方法
        print("\033[32;1m---client will push  file----\033[0m")
        if self.login_user:#判断用户是否登录
            file_name = json.loads(user_data[1])#获取文件名
            print file_name
            file_abs_path = "%s/%s/%s" %(settings.USER_HOME,self.login_user, file_name) #获取文件的路径
            self.request.send('303')
            file_size = self.request.recv(1024)
            print file_size
            total_file_size = int(file_size) #取出文件大小
            self.request.send('do it')
            received_size = 0
            local_file_obj = open(file_abs_path,"wb") #打开文件
            while total_file_size != received_size: #循环接收文件
                data = self.request.recv(4096)
                received_size += len(data)
                local_file_obj.write(data)
                print("recv size:", total_file_size,received_size)

            else:
                print("\033[32;1m----file update finished-----\033[0m")
                local_file_obj.close()
    def file_show(self,show):
        print ("\033[32;1m---client will show file list---\033[32;1m")
        if self.login_user:
            file_abs_path = "%s/%s" %(settings.USER_HOME,self.login_user)
            file_list = json.dumps(os.listdir(file_abs_path))
            self.request.send(file_list)
    def hashfile(self,filename):  #定义md5认证函数
        md5 = hashlib.md5()
        with open(filename,'rb') as f: #打开文件
            while True:
                data = f.read(1024) #循环读取文件内容
                if not data:
                    break
                md5.update(data) #更新md5值
            return md5.hexdigest() #返回md5值

