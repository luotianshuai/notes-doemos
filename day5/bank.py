#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import portal
import datetime
import os
import time

def bank():
    with open('card_info','rb') as f:  #打开文件并用json把字符串转换数据类型
        card_infocard = json.load(f)
    cardid = portal.card_api()  #调用信用卡登录函数
    if cardid:
        card_user = card_infocard[cardid]['username']  #取出卡的用户(为了欢迎信息和取出上个月份的消费列表)
        print "\033[32;1mwelecom %s\033[0m" % card_user  #打印欢迎信息
        while True:
            print '''\033[34;1m请选择您需要的服务：
1、还款
2、取现
3、转账\033[0m
'''
            num = raw_input("\033[32;1m请输入服务项目：\033[0m")
            if num == '1':
                '''使用datetime取出上个月的时间,并取出上个月消费列表'''
                d = datetime.datetime.now()  #取出当前时间
                year = d.year  #取出当前年份
                month = d.month  #取出当前月份
                if month == 1 :  #判断是否为第一个月，如果是那么年份-1 并且，月份为12月
                    month = 12
                    year -= 1
                else :
                    month -= 1 #如果不是第一个月，年份为当年，月份-1即可
                last_month = str(year)+ str(month)  #取出上个月的时间
                #print last_month
                filename = last_month + card_user  #取出上个月的消费信息文件
                if os.path.exists(filename):      #判断上个是否有消费记录
                    with open(filename,'rb') as b: #如果有打开文件，并计算上个月消费总额
                        last_monthcost = json.load(b)
                        cost_all = 0
                    for i in last_monthcost:
                        cost_all += i[1]
                    print "\033[31;1m您好您上个月的消费总额为：%d 请还款" % cost_all
                else:
                    print "\033[31;1m您上个月没有消费\033[0m"

                back_money = raw_input("\033[32;1m请输入您要还款的金额：\033[0m")  #输入还款金额
                back_money = int(back_money)   #转换为数字类型
                card_moneyold = card_infocard[cardid]['credit_money']  #取出现有余额
                card_moneynew = back_money + card_moneyold  #把还款金额和原有金额进行相加
                card_infocard[cardid]['credit_money'] = card_moneynew  #修改card_info里原有的金额并打印
                print "\033[32;1m您现在新的可用余额为：%s\33[0m" % card_infocard[cardid]['credit_money']
                with open('card_info','wb') as f:  #打开文件并把现在的金额写入文件
                    json.dump(card_infocard,f)
                continue
            if num ==  '2':
                card_moneyold = card_infocard[cardid]['credit_money']  #取出现有余额
                print "\033[32;1m您现在卡里剩余的金额为：%s" % card_moneyold
                get_money = raw_input("\033[32;1m请您输入您要取的金额\033[0m")
                get_money = int(get_money)
                get_moneyfc = get_money * 0.005
                get_money += get_moneyfc
                card_moneyold = int(card_moneyold)
                if get_money <= card_moneyold:
                    moneynow = card_moneyold - get_money
                    card_infocard[cardid]['credit_money'] = moneynow
                    card_getnow = card_infocard[cardid]['credit_money']
                    print "\033[32;1m支取完成，您现在的金额为：%s感谢您使用帅哥银行，嘿嘿...\033[0m" % card_getnow
                    get_cache = [('getcache',get_money)]  #定义消费记录把取现的记录加入到消费记录中
                    mothe_now = time.strftime("%Y%m")  #获取本月日期
                    file_cost = mothe_now + card_user #获取消费记录
                    if os.path.exists(file_cost):
                        with open(file_cost,'rb') as d:
                            cach_list = json.load(d)
                        cach_list.extend(get_cache)
                        with open(file_cost,'wb') as e:
                            json.dump(cach_list,e)
                    else:
                        with open(file_cost,'wb') as f:
                            json.dump(get_cache,f)
                else:
                    print "\033[31;1m您好您剩余的金额不足，现在的金额为：%s\033[0m" % card_moneyold

            if num == '3':
                card_moneyold = card_infocard[cardid]['credit_money']  #取出现有余额
                print "\033[32;1m您现在卡里剩余的金额为：%s" % card_moneyold
                other_user = raw_input("\033[32;1m请输入您要至的账号：\033[0m")
                if card_infocard.get(other_user):
                    not_money = raw_input("\033[34;1m请输入您要转账的金额：\033[0m")
                    card_moneyold = int(card_moneyold) #转换为数字类型,把目前现有的金额
                    not_money = int(not_money)   #转换为数字类型（用户转出的金额）
                    if card_moneyold >= not_money:  #判断剩余金额是否大于要转出的金额
                        give_moeny = card_moneyold - not_money   #减去转存的金额
                        card_infocard[cardid]['credit_money'] = give_moeny  #修改转出去的剩余金额
                        other_moeny = card_infocard[other_user]['credit_money']
                        other_moeny = int(other_moeny)
                        other_moeny = other_moeny + not_money
                        card_infocard[other_user]['credit_money'] = other_moeny
                        with open('card_info','wb') as o:
                            json.dump(card_infocard,o)
                        print "\033[32;1m转账成功\033[0m"
                    else:
                        print "\033[31;1m您好您剩余的金额不足，请仔细确认后重新输入\033[0m"

                else:
                    print "\033[31;1m用户不存在，请仔细确认后重新输入\033[0m"



    else:
        return #登录失败退出函数

