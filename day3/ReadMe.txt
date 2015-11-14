#!/usr/bin/env python
#-*- coding:utf-8 -*-
#���͵�ַ��http://www.cnblogs.com/luotianshuai/p/4949497.html
#Github��ַ��https://github.com/Tim-luo/homework/tree/master/day3

#����֮ǰ���Ⱥ˲�ha�����ļ���������

���г���
����1��ȡha��¼
����2����ha��¼
����3ɾ��ha��¼
����0���˳�����
���������кţ�

����1���в���ha��¼��
���������кţ�1
��������Ҫ���ҵ�backend��aaa.oldboy.org
backend aaa.oldboy.org
        server 100.1.7.80 weight 20 maxconn 3000





����2��������ha��¼��
ԭ�м�¼Ϊ��������ȡ�˲������ݣ���ϸ�뿴�����ļ���
-------------------------------------------------
backend aaa.oldboy.org
        server 100.1.7.80 weight 20 maxconn 3000

backend bbb.oldboy.org
        server 100.1.7.90 weight 20 maxconn 3000

backend ccc.oldboy.org
        server 100.1.7.100 weight 20 maxconn 3000
-------------------------------------------------
�������û��backend��ô�������������£�
���������кţ�2
��������Ҫ���ӵ�backend��{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
soory you add backend we not have ��will create new backend

#�����Ľ�����£�����ȡ�˲������ݣ���ϸ�뿴�����ļ���
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
��������backend������ô׷�ӣ�
���������кţ�2
��������Ҫ���ӵ�backend��{"backend": "bbb.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
you add backend has bin��will add server info

==================================================
backend aaa.oldboy.org
        server 100.1.7.80 weight 20 maxconn 3000

backend bbb.oldboy.org
		server 100.1.7.9 weight 20 maxconn 30
        server 100.1.7.90 weight 20 maxconn 3000

backend ccc.oldboy.org
        server 100.1.7.100 weight 20 maxconn 3000
=================================================





����3����ɾ��ha��¼��
���ȵ�����ǰд�Ĳ鿴������~ ~�����ж��û������backend�Ƿ���ڲ������˳�����ʾ��
���������кţ�3
��������Ҫɾ����backend�� {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
sorry we cant find test.oldboy.org backend info

������ڣ�ɾ��
���������кţ�3
��������Ҫɾ����backend��{"backend": "ccc.oldboy.org","record":{"server": "100.1.7.100","weight": 20,"maxconn": 3000}}
you server info is del and is last line
work done please check !

