# !/usr/bin/env python
# -*- coding:utf-8 -*-

city_map = {"河北省":{"石家庄市":['平山县','无极县','灵寿县'],"衡水市":['饶阳县','安平县','武强县'],},
            "山东省":{"济南市":['济阳县','商河县','平阴县'],"青岛市":['市南区','市北区','市东区'],},
            "河南省":{"洛阳市":['新安县','洛宁县','宜阳县'],"郑州市":['金水区','惠济区','上街区'],}}

# 设置一个标志位用来控制整个循环
map_flag = False


while not map_flag:
    # 打印省份名称
    for index,province in enumerate(list(city_map.keys())):
        print(index,province)
    # 选择省份
    user_input_province = input("请输入您要选择的省份,或输入q退出程序:").strip()
    if user_input_province.isdigit():
        province_key = list(city_map.keys())[int(user_input_province)]
        # 打印选择的省份的城市名称
        while not map_flag:
            for index,city in enumerate(list(city_map[province_key].keys())):
                print(index,city)
            # 选择城市
            user_input_city = input("请输入你要选择的城市,输入b返回上级菜单或者输入q退出程序:").strip()
            if user_input_city.isdigit():
                while not map_flag:
                    city_key = list(city_map[province_key].keys())[int(user_input_city)]
                    for index, town in enumerate(city_map[province_key][city_key]):
                        print(town)
                    user_input_end = input("到达三层菜单结尾,请输入b返回上一层或者q退出程序:")
                    if user_input_end == 'q':
                        "再见如果想继续访问三级菜单请重新运行程序"
                        break
                    else:
                        print("\033[31;1m请输入正确的序列号,或者输入q退出程序!\033[0m")
            else:
                if user_input_city == 'q':
                    "再见如果想继续访问三级菜单请重新运行程序"
                    break
                else:
                    print("\033[31;1m请输入正确的序列号,或者输入q退出程序!\033[0m")
    else:
        if user_input_province == 'q':
            "再见如果想继续访问三级菜单请重新运行程序"
            map_flag = True
        else:
            print("\033[31;1m请输入正确的序列号,或者输入q退出程序!\033[0m")



