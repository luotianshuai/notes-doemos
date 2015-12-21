#!/usr/bin/env python
# -*- coding:utf-8 -*-
import SocketServer
import os
import pickle
import hashlib

class MyServer(SocketServer.BaseRequestHandler):
    def hashfile(self,filename):  #定义md5认证函数
        md5 = hashlib.md5()
        with open(filename,'rb') as f: #打开文件
            while True:
                data = f.read(1024) #循环读取文件内容
                if not data:
                    break
                md5.update(data) #更新md5值
            return md5.hexdigest() #返回md5值

    def authon(self,username,password):  #认证函数
        with open('user_info','rb') as f: #打开文件
            user_infos = pickle.load(f)  #通过pickle把文件内容字符串转换成数据类型
        if user_infos.get(username): #如果用户名存在
            if user_infos[username]['password'] == password: #如果用户名存在密码相同返回True反之返回False
                return True #登录成功返回True
        else:
            return False #登录失败返回False

    def sendfile(self):  #定义发送文件函数
        while True:
            file_list = os.listdir("./") #获取文件列表
            print file_list
            send_pk = pickle.dumps(os.listdir("./")) #发送文件列表，通过字符串的方式，socket必须发送字符串
            self.request.sendall(send_pk)  #发送给用户
            client_choice = self.request.recv(1024) #接收用户返回的
            if client_choice == 'exit': #如果用户返回exit退出
                return
            if client_choice in file_list:  #如果用户返回的信息是文件名
                f = open(client_choice,'rb')
                file_len = str(len(f.read())) #读取文件的长度并转换成字符串
                '''
                TypeError: must be string or buffer, not int  这里发送的时候必须是字符串不能是数字或者其他类型
                '''
                server_md5file = self.hashfile(client_choice) #获取文件的MD5值
                self.request.sendall(server_md5file) #发送给用户md5值
                self.request.recv(1024) #接收用户返回给server的接收状态信息

                self.request.sendall(file_len)  #发送字符串的长度
                client_ask = self.request.recv(1024) #接收用户返回给server的接收状态信息
                print client_ask  #打印
                f = open(client_choice,'rb') #打开文件
                self.request.sendall(f.read()) #发送文件给用户
                client_check = self.request.recv(1024) #接收用户返回给server的文件接收状态
                if client_check == 'done': #如果接收完成退出
                    return
            else:
                continue
    def receivefile(self):
        self.request.sendall("\033[32;1m服务端准备就绪，可以发送文件\033[0m") #发送个用户状态信息告诉用户可以发送文件
        file_name = self.request.recv(1024) #获取用户发送的文件名
        if file_name == 'exit':
            return
        self.request.sendall("\033[32;1m文件名已接收\033[0m")
        client_md5 = self.request.recv(1024) #获取用户发送的md5值
        self.request.sendall("\033[32;1mMd5值已收到，请继续发文件长度\033[0m") #发送给用户收到MD5值的确认
        client_siz = self.request.recv(1024) #接收用户发送过来的字符串的长度
        print "\033[32;1m文件长度为：%s" % client_siz
        self.request.sendall("\33[32;1m文件长度已收到，请继续发送文件\033[0m")
        total_size = int(client_siz) #把客户端发过来的字符串长度转换成数字类型
        if total_size <= 1024:  #判断如果字符串的长度小于等与1024直接接收
            data = self.request.recv(1024) #接收文件
            f = file(file_name,'wb')#打开文件
            f.write(data)#写入文件
            f.close()#关闭文件
            #发送md5
            if client_md5 == self.hashfile(file_name):  #判断调用md5认证函数
                self.request.sendall('same') #如果相同返回same
                self.request.recv(1024) #接收用户发送的的MD5值确认
                self.request.sendall('done') #接收完成发回done
                return
            else:
                self.request.sendall("different") #如果不同返回different
                self.request.recv(1024) #接收用户发送的的MD5值确认
                self.request.sendall('done') #接收完成返回done
                return
        else:
            received_size = 0  #定义接收长度起始值
            content_tag = False #定义标志位
            f = open(file_name,'wb') #打开文件
            while True: #循环写入文件
                data = self.request.recv(1024) #接收文件
                received_size += len(data) #累加接收长度
                if total_size == received_size: #如果就接收长度和发送长度相同定义标志位True
                    content_tag = True #更改标志位True
                f.write(data)
                if content_tag: #当标志位为True的时候执行！
                    f.close() #关闭文件
                    update_md5 = self.hashfile(file_name) #调用md5函数
                    if update_md5 == client_md5: #判断md5值是否相等
                        self.request.sendall('same')#如果相等发送same
                        self.request.recv(1024) #接收用户发送的的MD5值确认
                        self.request.sendall('done') #发送接收完成确认
                        return
                    else:
                        self.request.sendall("different") #如果不同发送different
                        self.request.recv(1024) #接收用户发送的的MD5值确认
                        self.request.sendall('done') #发送接收完成确认
                        return
    def command(self):
        while True:
            self.request.sendall("\033[34;1m请输入命令\033[0m")
            client_cmd = self.request.recv(1024) #接收client命令行
            if client_cmd == 'shuai':
                return
            cmd_result = os.popen(client_cmd).read() #获取命令结果
            print cmd_result
            cmd_len = str(len(cmd_result))
            self.request.sendall(cmd_len) #发送字符串长度
            self.request.recv(1024) #接收用户发送的确认信息
            self.request.sendall(cmd_result)


    def handle(self):
        connect = self.request #等待用户连接
        connect.sendall('\033[34;1m欢迎登录FTP请输入您的用户名密码！\033[0m') #发送用户接入信息
        user_inputname,user_inputpass = connect.recv(1024).split('|')  #拆分用户返回过来的用户密码信息
        if not self.authon(user_inputname,user_inputpass): #调用认证函数
            connect.sendall("login failed")
            return
        else:
            connect.sendall("succeed")
        clien_logincheck = connect.recv(1024)
        if clien_logincheck == "login succeed":
            while True:
                print '1'
                client_choice = connect.recv(1024)
                print client_choice
                if client_choice == '1':
                    self.sendfile()
                elif client_choice == '2':
                    self.receivefile()
                elif client_choice == '0':
                    self.command()
                else:
                    return



if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',6666),MyServer)
    server.serve_forever()