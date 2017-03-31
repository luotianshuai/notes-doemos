# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'

from moduls.login_func import login


@login
def core(*args, **kwargs):
    """
    商城主函数
    :param args:参数组 
    :param kwargs: 字典组
    :return: None
    """


def shopping_run():
    core()


