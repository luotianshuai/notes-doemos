#!/usr/bin/env python
#-*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(*arg):
    msg = MIMEText(arg[0], 'plain', 'utf-8')
    msg['From'] = formataddr(["帅哥",'luo_tianshuai@163.com'])
    msg['To'] = formataddr([arg[1],arg[2]])
    msg['Subject'] = arg[3]

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("luo_tianshuai@163.com", "SHUAIge^^^!")
    server.sendmail('luo_tianshuai@163.com', ['451161316@qq.com',], msg.as_string())
    server.quit()


''' #arg[0] = 内容
    #arg[1] = 用户名
    #arg[2] = 邮箱地址
    #arg[3] = 主题
'''