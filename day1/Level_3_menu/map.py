#!/usr/bin/env python
#-*- coding:utf-8 -*-
#

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



for i in range(3):
    print "---------------------地图---------------------------"
    sheng_list = city_map.keys()
    for sheng_listname in sheng_list:
        print sheng_listname
    print "----------------------------------------------------"
    city_name = raw_input("请输如您要查看的省名: ")
    jump_up_flag = False
    if city_name in city_map:           #检查输入是否为正确的省名
        sheng_name = city_map[city_name]  #使用输入的信息作为下标,（省名）
        shi_nl = sheng_name.keys()

#        for i in range(3):
        while True:
            print"-----------------%s包含的市为--------------------" % city_name
            for  shi_list in shi_nl:
                print shi_list         #打印市列表
            print "----------------------------------------------------"
            shi_pl = raw_input("请输入你要查看的市名：")
            if shi_pl in shi_nl:
                print "-----------------%s包含的县为--------------------" % shi_pl
                xian_nl = city_map[city_name][shi_pl]  #总结上面的输入，设置县列表
                for xian_list in xian_nl:
                    print xian_list
                print "-----------------------------------------------------"
            if shi_pl not in shi_nl:
                print "你输入的信息无效，请重新输入！"
                continue
            jump_shi = raw_input("请问是否退出：1 退出、2 返回最上层,任意键返回上一层：")
            if jump_shi == "1":
                jump_up_flag = True
                break
            if jump_shi == "2":
                break
            print "您输入的信息有误请重新输入！"
    if jump_up_flag:
        break
else:
    print "信息无效请重新输入！3次错误之后程序将退出！"
