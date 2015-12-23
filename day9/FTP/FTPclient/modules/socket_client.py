#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import socket
import json
import hashlib

class Client_Handler(object):
    response_code = {
            '200': "pass user authentication",
            '401': "wrong username or password",
            '404': "invalid username or password",
            '300': "Ready to send file",
            '301': "Ready to get file from server",
            '302': "Ready to send to  server",
            '403': "File doesn't exist on ftp server",
    }
    def __init__(self,args):
        self.args = args
        self.argv_parser() #调用判断参数的方法
        self.client_handel()
    def argv_parser(self):
        if len(self.args) == 1: #判断是否程序后跟了参数如果没有跟参数提示帮助信息
            self.help_msg()
        else:
            try:
                self.ftp_host = self.args[self.args.index('-s') +1] #获取程序后面-s 后的参数
                self.ftp_port = int(self.args[self.args.index('-p') +1]) #获取程序后面-p 后的参数
            except (IndexError,ValueError):
                self.help_msg()
                sys.exit()

    def help_msg(self):
        msg = '''
        example    :python client.py -s ip_address -p port_number
        -s         :which ip address you will connection
        -p         :which port you will connection
        help       :print help information
        '''
        sys.exit(msg)

    def connection(self,host,port): #定义连接函数
        try:
            print host,port
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #实例化socket
            self.sock.connect((host,port)) #连接socket服务器
        except socket.error as e:
            sys.exit("\033[31;1m%s\033[0m"%e)


    def auth(self): #定义认证函数
        try:
            retry_count = 0
            while retry_count < 3:
                username = raw_input("\033[32;1mPlease input user name:\033[0m")
                if len(username) == 0: continue #如果用户没有输入重新输入
                userpass = raw_input("\033[32;1mPlease input  password:\033[0m")
                if len(userpass) == 0: continue #如果用户密码没有输入重新输入
                hash = hashlib.md5()  #md5加密
                hash.update(userpass) #md5加密
                userpass = hash.hexdigest()#md5加密
                acount_info = json.dumps({
                    'username':username,
                    'password':userpass}) #把用户的输入转换成josn模式
                auth_string = "user_auth|%s" % (acount_info) #把动作和信息一起发送过去！
                self.sock.send(auth_string) #发送登录信息
                server_response = self.sock.recv(1024) #接收server端返回的状态信息
                print server_response
                response_codeid = self.get_response_code(server_response)
                print response_codeid
                print (self.response_code[response_codeid]) #获取上面定义的code状态
                if response_codeid == '200':
                    self.username = username
                    self.cwd = '/'
                    return True
                else:
                    retry_count += 1
            else:
                sys.exit('\033[31;1mToo many attempt\033[0m')
        except Exception as e:
            print e
    def get_response_code(self,code): #获取状态码函数
        response_info = code.split("|") #分割server端返回的状态信息
        print response_info
        codenow = response_info[1] #获取状态码所在字段
        return codenow #返回状态码
    def parse_instruction(self,user_input): #拼接函数
        user_input_to_list = user_input.split()  #把用户的输入用空格分割
        func_str = user_input_to_list[0] #获取元素
        if hasattr(self,'instruction__'+ func_str): #判断拼接后的方法是否存在
            return True,user_input_to_list #返回True并返用户输入
        else:
            return False,user_input_to_list #如果没有返回False，并返回输入
    def interactive(self):
        self.logout_flag = False
        while  self.logout_flag is not True:
            print """get filename    :will to download file from server
            push filename    will to update file to server
            show    will list server file and Directory list
            change    will change Directory and list Directory
            """
            user_input = raw_input("[%s]:%s" %(self.login_user,self.cwd)).strip() #获取用户输入
            if len(user_input) == 0:continue
            status,user_input_instructions = self.parse_instruction(user_input) #parse_instruction 防止和python自定义命令冲突，把命令进行自定义拼接
            if status is True:
                func = getattr(self,"instruction__" + user_input_instructions[0])
                func(user_input_instructions)
            else:
                print("\033[31;1mInvalid instruction!\033[0m")
    def instruction__get(self,instructions): #下载函数
        if len(instructions) == 1: #如果后面没有跟文件名退出
            print("Input the remote filename which you want to be downloaded!")
            return
        else:
            file_name = instructions[1]
            raw_str = "file_get|%s"% (json.dumps(file_name))
            self.sock.send(raw_str)

    def client_handel(self): #
        self.connection(self.ftp_host,self.ftp_port) #调用连接方法
        if self.auth():#调用认证方法
            self.interactive()

