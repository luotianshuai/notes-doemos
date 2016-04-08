#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import socket
import pickle
import os
import getpass

ip_port = ('127.0.0.1',6666)
client = socket.socket()
client.settimeout(20)

class Ftp(Exception):  #纯粹为了装B用，回顾下自定义异常
    def __init__(self,msg=None):
        self.msg = msg
    def __str__(self):
        if self.msg:
            return self.msg
        else:
            return "\033[32:1m登录失败\033[0m"

def hashfile(filename): #定义加密函数
    md5 = hashlib.md5()
    with open(filename,'rb') as f: #打开文件
        while True:
            data = f.read(1024)  #循环读取文件内容
            if not data:
                break
            md5.update(data) #更新md5值
        return md5.hexdigest() #返回md5值

def authon(): #认证函数
    server_answer = client.recv(1024) #接收server返回的信息
    print server_answer #打印server返回的信息
    user_inputu = raw_input("\033[34:1m请输入用户名：\033[0m：") #获取用户输入的用户名
    user_inputp = getpass.getpass("\033[34:1m请输入密码：\033[0m") #获取用户输入的密码
    hash = hashlib.md5()  #md5加密
    hash.update(user_inputp) #md5加密
    user_inputp = hash.hexdigest()#md5加密
    user_input = '%s|%s' % (user_inputu,user_inputp) #拼接用户的输入返回个server
    client.sendall(user_input) #返回给server
    server_answer = client.recv(1024) #接收server返回的状态信息
    if server_answer == 'login failed': #如果返回login failed 捕获并输出
        return 'failed'
    else:
        return "succeed" #如果返回succeed，捕获并输出

def receivefile(): #接收文件函数
    while True:
        server_sendlist = client.recv(1024)  #接收文件列表
        server_sendlist = pickle.loads(server_sendlist) #把文件列表字符串转换成数据类型
        for i in server_sendlist: #打印文件列表
            print i
        choice_file = raw_input("\033[32;1m请输入您想要下载的文件或者输入exit退出：\033[0m")
        if choice_file in server_sendlist: #如果文件存在
            client.sendall(choice_file) #把用户选择的文件名发送给server
            print choice_file #打印用户选择的文件（打印有的是为了测试用的可以不用打印）
            server_filemd5 = client.recv(1024) #接收MD5值
            client.sendall('\033[32;1mMD5值已接收\033[0m')
            res_size = client.recv(1024) #接收长度
            print res_size #打印文件长度
            print "\033[32;1m准备接收的数据大小为：%s类型为：%s\033[0m:" % (res_size,type(res_size))
            total_size = int(res_size)#把文件长度转换为数字类型
            if total_size != 0:
                client.sendall("\033[34;1m数据大小已查收，请发送数据\033[0m")
            else:
                print "\033[31;1m您输入的文件有问题!\033[0m"
                return
            if total_size < 1024: #如果内容小于1024直接保存
                f = open(choice_file,'wb') #打开文件
                data = client.recv(1024) #接收文件内容
                f.write(data) #把内容写入文件
                client.sendall('done') #发送接收状态信息
                f.close()#关闭文件
                downloadmd5 = hashfile(choice_file) #调用md5值函数
                print downloadmd5,server_filemd5 #打印MD5值信息
                if downloadmd5 == server_filemd5:  #判断md5值是否相等并打印结果
                    print "\033[32;1m文件内容MD5值相同\033[0m"
                else:
                    print "\033[31;1m文件内容MD5值不同\033[0m"
                return
            else: #如果文件大于1024循环接收文件内容
                received_size = 0
                content_tag = False #定义标志位，文件接收完毕后使用
                f = open(choice_file,'wb') #打开文件
                while True:
                    data = client.recv(1024) #循环接收
                    received_size += len(data) #递增接收文件的大小
                    if total_size == received_size: #判断如果文件接收完毕修改标志位值
                        client.sendall('done')
                        content_tag = True
                    print data
                    f.write(data)#写入文件
                    if content_tag: #如果标志位为True执行
                        f.close()
                        downloadmd5 = hashfile(choice_file) #调用MD5函数
                        print downloadmd5
                        if downloadmd5 == server_filemd5: #判断如果MD5值并打印结果
                            print "\033[32;1m文件内容MD5值相同\033[0m"
                        else:
                            print "\033[31;1m文件内容MD5值不同\033[0m"
                        return

        elif choice_file == 'exit':
            client.sendall('exit')
            return
        else:
            print "请输入正确的文件"
            client.sendall("用户输入错误")

def sendfile():
    server_ask = client.recv(1024) #接收server返回的信息并打印
    print server_ask
    file_list = os.listdir("./") #显示当前目录的文件信息
    for i in file_list: #打印文件列表
        print i
    while True:
        user_sendfile = raw_input("\033[32;1m请输入文件名，或者exit退出：\033[0m")
        if user_sendfile in file_list: #判断用户输入的文件名是否正确
            client.sendall(user_sendfile) #发送文件名给server
            client.recv(1024) #接收server接收文件名的状态
            clinet_filemd5 = hashfile(user_sendfile)  #获取文件的md5值
            client.sendall(clinet_filemd5) #发送md5值给server端
            client.recv(1024) #接收server发过来的md5值接收确认信息
            print "要发送的文件为：",user_sendfile
            f = open(user_sendfile,'rb') #打开文件发送文件长度
            file_len = str(len(f.read())) #获取文件长度
            print "文件长度为",file_len
            f.close() #关闭文件
            client.sendall(file_len) #发送文件长度给server
            client.recv(1024)#接收server端发送给用户的字符串接收状
            y = open(user_sendfile,'rb')
            client.sendall(y.read()) #发送文件给用户
            server_md5 = client.recv(1024) #接收server发过来的md5值的状态信息
            print "MD5的值是：",server_md5
            if server_md5 == 'same':
                print "\033[32;1mMD5值相同\033[0m"
            else:
                print "\033[31;1mMD5值不同\033[0m"
            client.sendall("\033[32;1mMD5值判断完成，请发送文件接收状态")
            server_check = client.recv(1024) #接收文件状态
            if server_check == 'done':
                return
        elif user_sendfile == 'exit':
            client.sendall('exit')
            return
        else:
            print "\033[31;1m您好您输入的文件名不存在"
def command():
    while True:
        client.recv(1024) #接收server端返回的确认信息
        user_cmd = raw_input("\033[34;1m请输入命令或输入shuai退出：\033[0m")
        if user_cmd == 'shuai':
            client.sendall('shuai')
            return
        client.sendall(user_cmd)
        cmd_len = client.recv(1024) #接收字符串的长度
        client.sendall("字符串长度已接收请发送数据")
        total_size = int(cmd_len)
        if total_size <= 1024:
            data = client.recv(1024)
            print data
        else:
            received_size = 0
            content_tag = False
            while True:
                data = client.recv(1024)
                received_size += len(data)
                if total_size == received_size:
                    content_tag = True
                print data
                if content_tag:
                    break
try:
    client.connect(ip_port) #连接服务器端口与IP
    ret = authon() #调用认证函数
    if ret == "succeed": #如果server端返回succeed
        print "\033[32;1m登录成功\033[0m" #提示用户登录成功
        client.send("login succeed") #返回给用户登录状态
        while True:
            print "\033[32;1m请输入您需要的功能[0]命令 [1]下载  [2]上传 [3]退出\033[0m"
            user_choice = raw_input('\033[32;1m请输入您的选择：\033[0m') #获取用户输入的功能
            send_userchoice = client.sendall(user_choice) #把用户的选择功能发送给server
            if user_choice == '1': #如果用户输入的1调用接收函数
                receivefile()
            elif user_choice == '2': #如果用户输入的2调用发送函数
                sendfile()
            elif user_choice == '0':#如果用户输入0调用命令函数
                command()
            else:
                client.sendall('3')
                break
    else:
        raise Ftp("\033[31;1m登录失败\033[0m")
except Exception,e:
    print e
finally:
    client.close()