#!/usr/bin/env python
#-*- coding:utf-8 -*-


city_map = {"河北省":{"石家庄市":['平山县','无极县','灵寿县'],
                    "衡水市":['饶阳县','安平县','武强县']
                    },
            "山东省":{"济南市":['济阳县','商河县','平阴县'],
                    "青岛市":['市南区','市北区','市东区'],
                   },
            "河南省":{"洛阳市":['新安县','洛宁县','宜阳县'],
                    "郑州市":['金水区','惠济区','上街区']
                   }
}



for i in range(3):  #循环3次防止无限调用
    print "\033[31;1m---------------------地图---------------------------\033[0m"
    sheng_list = city_map.keys()  #获取省的列表
    for sheng_listname in sheng_list: #循环省的列表
        print "\033[31;1m%s\033[0m" % sheng_listname #打印省的列表
    print "\033[34;1m----------------------------------------------------\033[0m"
    province_name = raw_input("\033[34;1m请输如您要查看的省名:\033[0m ")  #获取市的名称
    jump_up_flag = False  #定义标志位用来跳出整个循环
    if province_name in city_map:           #检查输入是否为正确的省名
        sheng_name = city_map[province_name]  #如果用户输入的信息存在，使用用户输入的信息作为字典的key,（省名）
        shi_nl = sheng_name.keys() #获取省名下的value
        while True:
            print"\033[34;1m-----------------%s包含的市为--------------------\033[0m" % province_name
            for shi_list in shi_nl:
                print "\033[34;1m%s\033[0m" % shi_list         #打印市列表
            print "----------------------------------------------------"
            shi_pl = raw_input("\033[33;1m请输入你要查看的市名：\033[0m")
            if shi_pl in shi_nl:
                print "\033[33;1m-----------------%s包含的县为--------------------\033[0m" % shi_pl
                xian_nl = city_map[province_name][shi_pl]  #
                for xian_list in xian_nl:
                    print "\033[33;1m%s\033[0m" % xian_list
                print "\033[31;1m-----------------------------------------------------\033[0m"
            else:
                print "\033[31;1m你输入的市名\033[34;1m%s\033[0m\033[31;1m不存在请重新输入！\033[0m" % shi_pl
                continue
            jump_shi = raw_input("\033[32;1m请问是否退出：1 退出、2 返回最上层,任意输入返回上一层：\033[0m")
            if jump_shi == "1":
                jump_up_flag = True
                break
            if jump_shi == "2":
                break
    if jump_up_flag:
        break
    else:
        print "\033[31;1m您输入的省名\033[34;1m%s\033[0m\033[31;1m不存在请重新输入\033[0m" % province_name
else:
    print "\033[31;1m信息无效请重新输入！3次错误之后程序将退出！\033[0m"
