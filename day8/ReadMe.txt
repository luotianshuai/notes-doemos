#!/usr/bin/env python
#-*- coding:utf-8 -*-

博客地址：
http://www.cnblogs.com/luotianshuai/p/5044380.html
http://www.cnblogs.com/luotianshuai/p/5058562.html

GitHub地址：
https://github.com/Tim-luo/homework/tree/master/day8


程序功能：
1、远程执行命令显示结果，必须有返回结果的，比如ifconfig ,ls cat 等命令
2、上传文件
3、下载文件
4、多线程


开启服务端：
python server.py

开启服务端（可以有多个）：
python client.py



一、登录认证

可用用户：
shuaige admin
tianshuai admin

欢迎登录FTP请输入您的用户名密码！
请输入用户名：：shuaige
请输入密码：
登录成功
请输入您需要的功能[0]命令 [1]下载  [2]上传 [3]退出
请输入您的选择：


二、执行命令
root@tim:/tim/clientdir# python client.py 
欢迎登录FTP请输入您的用户名密码！
请输入用户名：：shuaige
请输入密码：
登录成功
请输入您需要的功能[0]命令 [1]下载  [2]上传 [3]退出
请输入您的选择：0
请输入命令或输入shuai退出：ls    
server.py
testfile_2
testfile_2big1024
testfile_3big2048
user_info

请输入命令或输入shuai退出：shuai
请输入您需要的功能[0]命令 [1]下载  [2]上传 [3]退出
请输入您的选择：


三、下载文件
请输入命令或输入shuai退出：shuai
请输入您需要的功能[0]命令 [1]下载  [2]上传 [3]退出
请输入您的选择：1
testfile_2
user_info
server.py
testfile_2big1024
testfile_3big2048
请输入您想要下载的文件或者输入exit退出：testfile_2
testfile_2
1147
准备接收的数据大小为：1147类型为：<type 'str'>:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
landscape:x:103:109::
/var/lib/landscape:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
tim:x:1000:1000:tim,,,:/home/tim:/bin/bash

374e4118ff56fdcd844f6ca8f9da2a69
文件内容MD5值相同
请输入您需要的功能[0]命令 [1]下载  [2]上传 [3]退出
请输入您的选择：

文件已下载目录中：
root@tim:/tim/clientdir# ls
client.py  testfile_2


四、上传文件

请输入文件名，或者exit退出：testfile_2
要发送的文件为： testfile_2
文件长度为 1147
MD5的值是： same
MD5值相同
请输入您需要的功能[0]命令 [1]下载  [2]上传 [3]退出
请输入您的选择：



