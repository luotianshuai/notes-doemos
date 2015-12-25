#!/usr/bin/env python
-*- coding:utf-8 -*-

实现功能：
1、上传
2、下载
3、MD5值认证
4、查看文件列表
5、server端日志记录
6、进度条
7、断点续传

一、server端启动服务
C:\Github\homework\day9\FTP\FTPserver\bin>python server.py start
Start FTPserver on IP:127.0.0.1 PORT:9999

二、客户端连接并输入用户名密码3次后退出
C:\Github\homework\day9\FTP\FTPclient\bin>python client.py -s 127.0.0.1 -p 9999
127.0.0.1 9999
Please input user name:shuaige
Please input  password:admin
response|200|pass user authentication
['response', '200', 'pass user authentication']
200
pass user authentication
get filename    :will to download file from server
push filename   :filename    will to update file to server
show    :will list server file and Directory list

[shuaige]:[/]:

三、上传、下载MD5值确认

下载：
[shuaige]:[/]:get nihao.rar
Download: 100% ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
----file download finished-----
MD5 is same!
get filename    :will to download file from server
push filename   :filename    will to update file to server
show    :will list server file and Directory list

[shuaige]:[/]:


上传：
[shuaige]:[/]:push nihao.rar
will to send file to server
Download: 100% ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
----file transfer time:--- 0.223000049591
----successfully sent file to server----
get filename    :will to download file from server
push filename   :filename    will to update file to server
show    :will list server file and Directory list

[shuaige]:[/]:

四、查看
[shuaige]:[/]:show
nihao.rar
test.iso
get filename    :will to download file from server
push filename   :filename    will to update file to server
show    :will list server file and Directory list

[shuaige]:[/]:


五、日志记录
日志文件里记录用户操作

