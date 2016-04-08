#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
mobile = [18688965746,18620109616,18666214117,18025311442,15013806055]
CONTENT = "this is test message"
def sendmessage():
    for i in mobile:
        url='http://219.133.59.101/GsmsHttp'
        parms = {
                'username':'65243:admin',
                'password':'24671115',
                'from':'3399',
                'to':i,
                'content':CONTENT,
                'presendTime':'',
                'expandPrefix':'113'
        }
        querystring = urllib.urlencode(parms)    #定义POST地址
        print (querystring)
        u = urllib2.urlopen(url+'?'+querystring)    #提交完整POST地址，包括url和接口相关信息。
        print (u)
        resp = u.read()    #返回结果，成功还是失败。
        print (resp)

if __name__ == '__main__':
    sendmessage()
