#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

client = socket.socket()
client.connect(('127.0.0.1',6666))
client.settimeout(5)

while True:
    client_input = raw_input('please input message:').strip()
    client.sendall(client_input)
    server_data = client.recv(1024)
    print server_data