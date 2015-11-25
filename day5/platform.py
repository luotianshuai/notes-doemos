#!/usr/bin/env python
#-*- coding:utf-8 -*-
import login
import portal
import pickle





if __name__ == '__main__':
    print '''\033[34;1m输入1进入商城系统
输入2进入银行系统\033[0m
        '''
    print"************************************"
    user_chus = raw_input("请输入您需要的功能：")
    if user_chus == '1':
        portal.buy()
    elif user_chus == '2':
        print "欢迎登录银行系统"