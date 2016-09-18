#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
#coding:utf-8

from mysql_server import MysqlServer


def group_list():
    db = MysqlServer(dict(DB='shipman',USERNAME='root',PASSWORD='oldboy@123',HOST='localhost',PORT=3306))
    sql = "select distinct `node_group` from node"
    ret = db.run_sql(sql)
    db.close()
    return ret

if __name__ == "__main__":
    print(group_list())