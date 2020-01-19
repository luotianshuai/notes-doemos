# !/usr/bin/env python
# -*- coding:utf-8 -*-
city_map = {"河北省": {"石家庄市": {'平山县': {}, '无极县': {}, '灵寿县': {}}, "衡水市": {'饶阳县': {}, '安平县': {}, '武强县': {}}, },
            "山东省": {"济南市": {'济阳县': {}, '商河县': {}, '平阴县': {}}, "青岛市": {'市南区': {}, '市北区': {}, '市东区': {}}, },
            "河南省": {"洛阳市": {'新安县': {}, '洛宁县': {}, '宜阳县': {}}, "郑州市": {'金水区': {}, '惠济区': {}, '上街区': {}}, }}


last_layers = []  # 上一层
current_layers = city_map  # 当前层
while True:
    if not current_layers:  # 如果当前层为空，输出提示
        print("Empty layer. please input b back last layers!")

    for i in current_layers:  # 打印当前层的key
        print(i)
    choice = input("Input your choice: ").strip()  # 输入想进入的地点
    if choice in current_layers:  # 如果输入存在
        last_layers.append(current_layers)  # 将当前层加入上一层列表
        current_layers = current_layers[choice]  # 进入下一层
    if choice == "q":  # 输入 q 退出程序
        print("Exit.")
        break
    if choice == "b" and len(last_layers):  # 输入 b 并且上一级列表不为空，则取最后一条记录为当前层
        current_layers = last_layers.pop()  # 取出上一次记录在列表中的最后一个元素
        print("Super layer.")
