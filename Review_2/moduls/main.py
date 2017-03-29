# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'

import sys
print(sys.path)

from moduls.login_func import login


@login
def core():
    pass


def shopping_run():
    core()


