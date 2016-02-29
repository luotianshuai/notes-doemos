#!/usr/bin/env python
#-*- coding:utf-8 -*-

city_maps = {1:{'河北':{11:{'石家庄':['平山县','无极县','灵寿县']},12:{'衡水':['饶阳县','安平县','武强县']}}},
             2:{'山东':{21:{"济南市":['济阳县','商河县','平阴县']},22:{"青岛市":['市南区','市北区','市东区']}}},
             3:{'河南':{31:{"洛阳市":['新安县','洛宁县','宜阳县']},33:{"郑州市":['金水区','惠济区','上街区']}}},
            }
class Three_level_menu(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            for k,v in city_maps.items():
                print k,v.keys()
            try:
                user_input = raw_input("\033[32;1m请输入您要选择的省份序列号或输入省份名字:\033[0m")
            except Exception, e:
                print "\033[33;1m错误如下：\033[0m"
                print e
if __name__ == '__main__':
    menu = Three_level_menu()
    menu.run()



