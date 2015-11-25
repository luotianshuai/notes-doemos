#!/usr/bin/env python
#-*- coding:utf-8 -*-
import portal
import bank





if __name__ == '__main__':
    while True:
        print '''\033[34;1m请输入您需要的功能：
1、商城系统
2、银行系统
3、管理系统\033[0m
'''
        num = raw_input("\033[32;1m请输入您功能项：")
        if num == '1':
            portal.buy()
        elif num == '2':
            bank.bank()
        else:
            continue
