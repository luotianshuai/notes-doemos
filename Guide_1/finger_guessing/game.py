# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'
"""
需求:
写一个程序和电脑进行猜拳总共有：石头、剪刀、布三种情况
采用5回合3胜制度
最后输出结果谁胜利，当电脑胜利达到3次或者你胜利达到3次的时候直接结束
"""
import random
choice_list = ["石头", "剪刀", "布"]
code_check = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
user_win = 0
computer_win = 0
draw = 0
for i in range(5):
    computer_choice = random.randrange(3)
    user_input = int(input("五局三胜制度,您输入错误也将计入失败,请输入:0:石头  1:剪刀 2:布："))
    if user_input in range(3):
        print("\033[34;1m您出的是%s\033[0m" % choice_list[user_input], "\033[34;1m电脑出的是%s\033[0m" % choice_list[computer_choice])
        if user_input == computer_choice:
            draw += 1
            print("\033[34;1m出的一样啊~~\033[0m")
            continue
        elif code_check[user_input].index(computer_choice) == 1:
            # 如果用户输入石头的时候
            computer_win += 1
            print("\033[31;1m电脑胜利了一局\033[0m")
        else:
            user_win += 1
            if user_win >= 3:
                exit("您已经胜利了3次了，您胜利")
            print("\033[32;1m您胜利了一局\033[0m")
    else:
        print("输入错误您失败了1次,电脑出的是%s" % computer_choice)
        computer_win += 1
        # 判断如果已经输了3次了直接退出
        if computer_win >= 3:
            exit("您已经失败了3次，电脑胜利")
else:
    print("电脑胜利次数为：%s" % computer_win, "您的胜利次数为%s您胜利了" % user_win)
    if computer_win == user_win:
        print("平局")
    elif computer_win > user_win:
        print("电脑胜利")
    else:
        print("您获得胜利")