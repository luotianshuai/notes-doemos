# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'

from config import shopping_config


def login(func_arg):
    def inner(*args, **kwargs):
        print("""Welcome login Mr Tim shopping mail""".count("="*50))
        user_info = shopping_config.user_db
        for i in range(2):
            user_name_input = input("Please Input your user name:")
            if user_name_input in user_info.keys():
                user_pass_input = input("Please Input your password:")
                if user_pass_input == user_info[user_name_input]["password"]:
                    func_arg(user_name_input, *args, **kwargs)
                    break
                else:
                    print("Your password is invalid, Please check!")
            else:
                print("Your user name is invalid,Please check!")
    return inner
