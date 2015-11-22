#!/usr/bin/env python
#-*- coding:utf-8 -*-

#博客地址：http://www.cnblogs.com/luotianshuai/p/4949497.html
#Github地址：https://github.com/Tim-luo/homework/tree/master/day4

修改配置文件程序功能有：
1、查询
2、添加
3、删除
4、退出

#注：已增加装饰器使用！OH，YES  A A A A A A A A A A A A +


1、查询函数

用户输入backend，如果backend存在输出backend下的record信息

输入1获取ha记录
输入2增加ha记录
输入3删除ha记录
输入0将退出程序
请输入您需要的功能：1
查询功能测试：
存在：www.oldboy.org buy.oldboy.org nb.oldboy.org  不存在：none.oldboy.org
请输入您要查看的backend名称：buy.oldboy.org
server 100.1.7.10 100.1.7.10 weight 20 maxconn 3000
server 100.1.7.16 100.1.7.16 weight 20 maxconn 3000

2、添加函授

调用查询函数，如果查询函数不为空，说明backend存在
并判断record信息是否存在如果存在不添加如果不存在添加并写入。

原理把文件分为上、中、下3部分。上为backend上面的信息、下为backend下面的信息，匹配到的backend为中
对中进行操作，
如果backend不存在直接在文件后面追加
================================================================================================================
请输入您需要的功能：2
输入添加测试：backend不存在：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入添加测试：backend存在record存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
输入添加测试：backend存在record不存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.101","weight": 20,"maxconn": 3000}}
请输入您要添加的信息：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
您添加的backend是新的已为您新增backend和记录！
================================================================================================================
如果backend存在并且record信息存在提示用户信息已存在
================================================================================================================
请输入您需要的功能：2
输入添加测试：backend不存在：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入添加测试：backend存在record存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
输入添加测试：backend存在record不存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.101","weight": 20,"maxconn": 3000}}
请输入您要添加的信息：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
您添加的backend和record信息已存在！
================================================================================================================
如果backned存在record信息不存在在backend下面追加
================================================================================================================
请输入您需要的功能：2
输入添加测试：backend不存在：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入添加测试：backend存在record存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
输入添加测试：backend存在record不存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.101","weight": 20,"maxconn": 3000}}
请输入您要添加的信息：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.101","weight": 20,"maxconn": 3000}}
backend存在并且record信息不存在，已添加record信息！
================================================================================================================

3、删除函数
同样调用查询函数、如果查询函数为空说明backned不存在
直接提示用户backend不存在
================================================================================================================
请输入您需要的功能：3
输入删除测试：backend不存在：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且仅有一条record记录：{"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且有其他record记录：：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record不存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.99","weight": 20,"maxconn": 3000}}
请输入您要删除的信息：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
您输入的backend不存在
================================================================================================================
如果不为空说明backend存在
判断recordrecord是否存在如果record不存在提示用户record不存在
================================================================================================================
请输入您需要的功能：3
输入删除测试：backend不存在：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且仅有一条record记录：{"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且有其他record记录：：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record不存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.99","weight": 20,"maxconn": 3000}}
请输入您要删除的信息：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.99","weight": 20,"maxconn": 3000}}
您好backend下无法找到record信息！
================================================================================================================
如果backned存在record存在并且仅有一条记录，删除record后删除backend
================================================================================================================
请输入您需要的功能：3
输入删除测试：backend不存在：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且仅有一条record记录：{"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且有其他record记录：：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record不存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.99","weight": 20,"maxconn": 3000}}
请输入您要删除的信息：{"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
您好backend下的record已经删除并且backend下没有记录，将要删除backend！
================================================================================================================
backned存在并且record存在并且有多条其他记录仅删除匹配的record记录
================================================================================================================
请输入您需要的功能：3
输入删除测试：backend不存在：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且仅有一条record记录：{"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record存在,且有其他record记录：：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
输入删除测试：backend存在record不存在：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.99","weight": 20,"maxconn": 3000}}
请输入您要删除的信息：{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}
您好backend下的record已经删除，并且backend还有记录！
================================================================================================================