#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import subprocess

def monitor_cpu(frist_invoke=1):
    shell_command = 'sar 1 3|grep "^Average:"'
    status,result = subprocess.Popen(shell_command,shell=True)
