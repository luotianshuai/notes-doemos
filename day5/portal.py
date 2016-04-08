#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import hashlib
import time
import os

def login_api():
    with open('user_info','rb') as f:  #打开文件
        usernew_info = json.load(f)  #通过json将字符串转换成数据类型
    lock_user = 0  #定义循环起始值，用来判断用户输入错误密码的次数！
    for i in range(3):
        username = raw_input("\033[32;1m请输入您的用户名：")
        password = raw_input("\033[32;1m请输入您的密码：")
        hash = hashlib.md5()  #md5加密
        hash.update(password) #md5加密
        password = hash.hexdigest()#md5加密
        if usernew_info.get(username):  #判断用户输入的信息是否存在
            if usernew_info[username]['login_num'] == '3':  #判断用户是否被锁
                print "\033[31;1m您好您的账号已被锁定\033[0m"
                return
            if usernew_info[username]['password'] == password:  #判断用户密码是否匹配
                return "登录成功"

            else:
                print "\033[31;1m您好您输入的密码错误请重新输入\033[0m"
                lock_user += 1  #累加错误密码的次数
                if lock_user == 3:
                    usernew_info[username]['login_num'] = '3'  #错误3次后修改配置文件
                    with open('user_info','wb') as f:  #写入文件下次加载时使用
                        json.dump(usernew_info,f)
                    print "\033[31;1m您的账户输入错误了3次密码账号已被锁定\033[0m"
                    return
        else:
            print "\033[31;1m您输入的用户名不存在\033[0m"

def card_api():
    with open('card_info','rb') as f:  #打开文件
        cards_info = json.load(f)# 通过json将字符串转换成数据类型
    lock_user = 0 #定义循环起始值，用来判断用户输入错误密码的次数！
    for i in range(3):
        card_id = raw_input("\033[32;1m请输入您的卡号：\033[0m")
        card_pd = raw_input("\033[32;1m请输入您的密码：\033[0m")
        hash = hashlib.md5() #md5加密
        hash.update(card_pd)#md5加密
        card_pd = hash.hexdigest() #md5加密
        if cards_info.get(card_id):  #判断用户输入的信息是否存在
            if cards_info[card_id]['login_num'] == '3':  #判断用户是否被锁
                print "\033[31;1m您好您的账号已被锁定\033[0m"
                return False
            if cards_info[card_id]['password'] == card_pd: #用户匹配后判断密码是否匹配
                return card_id #用户匹配后返回用户账号
            else:
                print "\033[31;1m您好您输入的密码错误请重新输入\033[0m"
                lock_user += 1  #累加用户输入错误密码次数
                if lock_user == 3:
                    cards_info[card_id]['login_num'] = '3' #修改用户错误次数信息
                    with open('card_info','wb') as f:
                        json.dump(cards_info,f)  #写入至文件
                    print "\033[31;1m您的账户输入错误了3次密码账号已被锁定\033[0m"
                    return False
        else:
            print "\033[31;1m您输入的用户名不存在\033[0m"



def wrapper(func):
    def inner(): #封装调用装饰器的函数
        check_user = login_api()  #在装饰器内新增的功能
        if check_user == "登录成功": #判断，登录函数的登录是否成功
            func()
        else:
            return check_user #如果登录失败返回登录函数所提示的信息
    return inner #返回调用装饰器的函数

@wrapper
def buy():
    print "\033[32;1m欢迎光临本商场，下面是本商场所包含的商品，请输入左侧的商品号购买:\033[0m"
    product_list = [
        ('Iphon',5800),
        ('Bike',800),
        ('Book',45),
        ('Coffee',35),
        ('iphon touch',1590),
        ('MX4',1999)
    ]
    shoping_list = []  #定义一个空列表，把用户选择的商品加入到空列表中（类似购物车）
    while True:
        index = 1  #定义索引值从1开始
        for item in product_list:  #循环商品列表
            print "\033[32;1m%s: %s\t%s\033[0m" %(index,item[0],item[1])  #打印商品列表
            index += 1

        user_choice = int(raw_input("\033[33;1m温馨提示:输入0推出购物\033[0m|\033[34;1m输入数列号购买物品，请问您需要购买什么物品：\033[0m ").strip()) #.strip()把空格取消
        if user_choice == 0:  #定义推出接口
            ask_exit = raw_input("\033[33;1m为了防止您的误操作如果退出请输入yes/YES,输入其他任意键返回购物列表:\033[0m")
            if ask_exit == "yes" or ask_exit == "YES":
                print "\033[34;1m下面是您本次的购物清单：\033[0m"
                for buy_list in shoping_list: #打印出此次购买列表
                    print "\033[34;1m%s \033[0m" % buy_list[0]  #打印shoping_list 用户购买列表
                sum_money = 0
                for buy_money in shoping_list:
                    sum_money += buy_money[1]  #计算消费总额
                print "\033[32;1m本次您需要支付的金额为：%d \033[0m" % sum_money #打印总共消费了多少钱
                cardid = card_api() #调用card登录程序
                if cardid:
                    with open('card_info','rb') as f:
                        card_infos = json.load(f)
                    card_money = int(card_infos[cardid]['credit_money']) #获取卡里的金额
                    if card_money >= sum_money: #判断金额是否足够
                        card_moneynow = card_money - sum_money  #减去消费的金额
                        card_infos[cardid]['credit_money'] = card_moneynow
                        mothe_now = time.strftime("%Y%m")  #获取本月日期
                        card_name = card_infos[cardid]['username']  #获取卡片的用户名
                        filename = mothe_now+card_name  #消费记录的名字
                        if os.path.exists(filename):  #判断文件是否存在
                            with open(filename,'rb') as f:  #如果文件存在已只读的方式打开文件
                                cost_list = json.load(f)  #通过json把字符串转换为数据类型
                                cost_list.extend(shoping_list)  #把购物车中的信息加入到消费列表中
                            with open(filename,'wb') as f:  #已写的方式打开文件，并把修改后的消费列表加入到消费列表文件中
                                json.dump(cost_list,f)
                            with open('card_info','wb') as f:#已写的方式打开文件，修改改后的card_info写回原card_info文件中，（消费扣款）
                                json.dump(card_infos,f)
                            print "\033[32;1m购买完成，欢迎下次光临\033[0m"
                            return
                        else:
                            with open(filename,'wb') as f:  #如果文件不存在，直接打开文件把，购物列表写入到消费列表中
                                json.dump(shoping_list,f)
                            with open('card_info','wb') as f: #已写的方式打开文件，修改改后的card_info写回原card_info文件中，（消费扣款）
                                json.dump(card_infos,f)
                            print "\033[32;1m购买完成，欢迎下次光临\033[0m"
                            return
                    else:
                        print "\033[31;1m您好，您的银行卡金额不足，请充值！"  #金额不足退出提示用户充值
                        print card_infos[cardid]['credit_money']
                        return
                else:
                    return  #登录失败退出函数
            else:
                continue

        user_choice -= 1 #这里因为是从1开始的了所以需要-1 要不然下面输入索引的时候会有问题！
        if user_choice >= index:  #判断用户输入是否超出下标范围
            print "\033[33;1m您输入的序列号超出了范围,请重新输入\033[0m "
            continue
        user_add = product_list[user_choice]  #匹配用户选择商品
        shoping_list.append(product_list[user_choice]) #把用户输入的的商品加入到购物车
        print "\033[34;1m物品 %s 已购买并加入购物车\033[0m" % product_list[user_choice][0]  #打印添加值购物列表

