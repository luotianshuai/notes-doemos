#!/usr/bin/env python
#-*- coding:utf-8 -*-

#博客地址：http://www.cnblogs.com/luotianshuai/p/4949497.html
#Github地址：https://github.com/Tim-luo/homework/tree/master/day3

#操作之前请先核查ha配置文件！

运行程序
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录
输入0将退出程序
请输入序列号：

输入1进行查找ha记录：
请输入序列号：1
请输入您要查找的backend：aaa.oldboy.org
backend aaa.oldboy.org
        server 100.1.7.80 weight 20 maxconn 3000





输入2进行增加ha记录：
原有记录为：（仅截取了部分内容，详细请看配置文件）
-------------------------------------------------
backend aaa.oldboy.org
        server 100.1.7.80 weight 20 maxconn 3000

backend bbb.oldboy.org
        server 100.1.7.90 weight 20 maxconn 3000

backend ccc.oldboy.org
        server 100.1.7.100 weight 20 maxconn 3000
-------------------------------------------------
如果输入没有backend那么将会新增：如下：
请输入序列号：2
请输入您要增加的backend：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
soory you add backend we not have ，will create new backend

#变更后的结果如下（仅截取了部分内容，详细请看配置文件）
==================================================
backend aaa.oldboy.org
        server 100.1.7.80 weight 20 maxconn 3000

backend bbb.oldboy.org
        server 100.1.7.90 weight 20 maxconn 3000

backend ccc.oldboy.org
        server 100.1.7.100 weight 20 maxconn 3000

backend test.oldboy.org
		server 100.1.7.9 weight 20 maxconn 30
=====================================================
如果输入的backend存在那么追加：
请输入序列号：2
请输入您要增加的backend：{"backend": "bbb.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
you add backend has bin，will add server info

==================================================
backend aaa.oldboy.org
        server 100.1.7.80 weight 20 maxconn 3000

backend bbb.oldboy.org
		server 100.1.7.9 weight 20 maxconn 30
        server 100.1.7.90 weight 20 maxconn 3000

backend ccc.oldboy.org
        server 100.1.7.100 weight 20 maxconn 3000
=================================================





输入3进行删除ha记录：
首先调用以前写的查看参数（~ ~），判断用户输入的backend是否存在不存在退出并提示：
请输入序列号：3
请输入你要删除的backend： {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
sorry we cant find test.oldboy.org backend info

如果存在：删除
请输入序列号：3
请输入你要删除的backend：{"backend": "ccc.oldboy.org","record":{"server": "100.1.7.100","weight": 20,"maxconn": 3000}}
you server info is del and is last line
work done please check !
