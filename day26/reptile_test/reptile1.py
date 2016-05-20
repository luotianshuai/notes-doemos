#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import requests
import json



login_dic = {
    'email':'shuaige@qq.com',
    'password':'shuaige!',
    '_ref':'frame',
}

login_ret = requests.post(url='https://huaban.com/auth/',
                          data=login_dic,
                          )
print login_ret.text

print '*' * 50

check_my_info = requests.get(url='http://huaban.com/ugb8cx9ky3/following/')
print check_my_info.text