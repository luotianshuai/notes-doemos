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
mysql_clust.host = ['192.168.17.15',
                    '3.2.2.2',
                    '4.4.4.4',
                    ]

monitored_groups = [mysql_clust,web_cluster] #把主机组对象加入到监控组里





