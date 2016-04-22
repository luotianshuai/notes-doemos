#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Tim Luo  LuoTianShuai



data = [
    (None,'A'),
    ('A','A1'),
    ('A','A1-1'),
    ('A1','A2'),
    ('A1-1','A2-3'),
    ('A2-3','A3-4'),
    ('A1','A2-2'),
    ('A2','A3'),
    ('A2-2','A3-3'),
    ('A3','A4'),
    (None,'B'),
    ('B','B1'),
    ('B1','B2'),
    ('B1','B2-2'),
    ('B2','B3'),
    (None,'C'),
    ('C','C1'),

]

def tree_search(d_dic,parent,son):
    #一层一层找,先拨第一层,一层一层往下找
    for k,v in d_dic.items():
        #举例来说我先遇到A,我就把A来个深度查询,A没有了在找B
        if k == parent:#如果等于就找到了parent,就吧son加入到他下面
            d_dic[k][son] = {} #son下面可能还有儿子
            #这里找到就直接return了,你找到就直接退出就行了
            return
        else:
            #如果没有找到,有可能还有更深的地方,的需要剥掉一层
            tree_search(d_dic[k],parent,son)



data_dic = {}

for item in data:
    # 每一个item代表两个值一个父亲一个儿子
    parent,son = item
    #先判断parent是否为空,如果为空他就是顶级的,直接吧他加到data_dic
    if parent is None:
        data_dic[son] = {}  #这里如果为空,那么key就是他自己,他儿子就是一个空字典
    else:
        '''
        如果不为空他是谁的儿子呢?举例来说A3他是A2的儿子,但是你能直接判断A3的父亲是A2你能直接判断他是否在A里面吗?你只能到第一层.key
        所以咱们就得一层一层的找,我们知道A3他爹肯定在字典里了,所以就得一层一层的找,但是不能循环找,因为你不知道他有多少层,所以通过递归去找
        直到找到位置
        '''
        tree_search(data_dic,parent,son) #因为你要一层一层找,你的把data_dic传进去,还的把parent和son传进去


for k,v in data_dic.items():
    print(k,v)