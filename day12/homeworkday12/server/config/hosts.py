#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import templates

#主机组1
web_cluster = templates.LinxGenricTemplate()
web_cluster.host = ['192.168.17.15',
                    '1.1.1.1',
                    '2.2.2.2',
                    ] #

#主机组2
mysql_clust = templates.LinuxGenricTemplatesimple()
mysql_clust.host = ['192.168.7.15',
                    '3.2.2.2',
                    '4.4.4.4',
                    ]

monitored_groups = [mysql_clust,web_cluster] #把主机组对象加入到监控组里

if __name__ == '__main__':
    host_config_dic = {} #定义一个空字典
    for group in monitored_groups: #循环monitored_groups列表
        for h in group.host: #循环对象中的主机IP列表
            if h not in host_config_dic:#如果主机IP不在字典中
                host_config_dic[h] = {} #定义一个空字典
            for s in group.services:#循环group.services
                #print s
                #print s.name
                host_config_dic[h][s.name] = [s.plugin_name,s.interval]
    for h,v in host_config_dic.items():
        print h,v




