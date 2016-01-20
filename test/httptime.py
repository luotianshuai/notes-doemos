#!/usr/bin/python
# coding: UTF-8
import pycurl
import sys
import os
import json

class Test:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + buf
def web_performance(input_url,mykey):
    t = Test()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()
    if mykey == "NAMELOOKUP_TIME":
        #DNS解析时间ms
        NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)
        print "%.2f"%(NAMELOOKUP_TIME*1000)
        #return mykey
    elif mykey == "CONNECT_TIME":
        #建立连接时间ms
        CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)
        print "%.2f" %(CONNECT_TIME*1000)
        #return mykey  
    elif mykey == "PRETRANSFER_TIME":
        #准备传输时间ms
        PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)
        print "%.2f" %(PRETRANSFER_TIME*1000)
        #return mykey
    elif mykey == "STARTTRANSFER_TIME":
        #传输开始时间ms
        STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
        print "%.2f" %(STARTTRANSFER_TIME*1000)
        #return mykey
    elif mykey == "TOTAL_TIME":
        #传输结束总时间ms
        TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
        print "%.2f" %(TOTAL_TIME*1000)
        #return mykey
    elif mykey == "SIZE_DOWNLOAD":
        #下载数据包大小bytes/s
        SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)
        print "%d" %(SIZE_DOWNLOAD)
        #return mykey
    elif mykey == "HEADER_SIZE":
        #HTTP头部大小bytes
        HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
        print "%d" %(HEADER_SIZE)
        #return mykey
    elif mykey == "SPEED_DOWNLOAD":
        #平均下载速度bytes/s
        SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)
        print "%d" %(SPEED_DOWNLOAD)
        #return mykey

def web_discovery():
  website = open('/usr/local/zabbix/bin/web.txt','r').read().split()
  devices = []
  for devpath in  website:
     #device = os.path.basename(devpath)
     devices.append({'{#SITENAME}':devpath})
  print json.dumps({'data':devices},sort_keys=True,indent=7,separators=(',',':'))

if __name__ == '__main__':
  if sys.argv[1] == "web_discovery":
        web_discovery()
  if sys.argv[1] == "web_performance":
        input_url = sys.argv[2]
        mykey = sys.argv[3]
        web_performance(input_url,mykey)
