#!/usr/bin/env python
#-*- coding:utf-8 -*-

import SocketServer

class FtpServer(SocketServer.BaseRequestHandler):
    def handel(self):
        print self.client_address
