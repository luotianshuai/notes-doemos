#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import portal

def bank():
    with open('card_info','rb') as f:
        card_infocard = json.load(f)
    cardid = portal.card_api()
    if cardid:
        card_user = card_infocard[cardid]['username']
        print "\033[32;1mwelecom %s\033[0m" % card_user
        while True:
            print '''\033[34;1m请选择您需要的服务：
1、还款
2、取现
3、转账\033[0m
'''
            num = raw_input("\033[32;1m请输入服务项目：\033[0m")
            if num == 1:
                back_money = int(raw_input("\033[32;1m请输入您要还款的金额：\033[0m"))
                card_moneyold = card_infocard[cardid]['credit_money']

    else:
        return #登录失败退出函数

