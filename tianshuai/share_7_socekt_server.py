#!/usr/bin/env python
# -*- coding:utf-8 -*-
import SocketServer

class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.services
        conn = self.request
        conn.sendall('欢迎致电 10086，请输入1xxx,0转人工服务.')
        Flag = True
        while Flag:
            data = conn.recv(1024)
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall('通过可能会被录音.balabala一大推')
            else:
                conn.sendall('请重新输入.')


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()