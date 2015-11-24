#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pickle
import login
def card_login(card_id,card_password):
    lock_user = 0
    for i in range(3):
        user_name = raw_input("\033[32;1m请输入您的用户名\033[0m")
        user_password = raw_input("\033[32:1m请输入你的密码\033[0m")
