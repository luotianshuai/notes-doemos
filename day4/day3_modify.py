#!/usr/bin/env python
#-*- coding:utf-8 -*-

def fetch(backend):
    with open('haproxy.conf') as obj:
        backend_list = []
        flag = False
        for line in obj:
            if line.strip() == 'backend %s' % backend
                flag = True
                continue
            if flag and line.strip() == line.strip().startswith('backend'):
                break
            if flag and line.strip():
                backend_list.append(line)

fetch('aaa.oldboy.org')