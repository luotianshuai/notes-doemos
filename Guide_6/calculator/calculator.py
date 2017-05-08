# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
该计算器思路：
    1、递归寻找表达式中只含有 数字和运算符的表达式，并计算结果
    2、由于整数计算会忽略小数，所有的数字都认为是浮点型操作，以此来保留小数
使用技术：
    1、正则表达式
    2、递归
"""
import re


def compute_mul_div(arg):
    """ 操作乘除
    :param arg:方程式
    :return:计算结果
    """
    val = arg[0]  # 获取整个方程式
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)  # 获取乘除方程式
    '''
    \d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*  这个方程式匹配的是
    例子：10.0 */ -+ 22.100  小数点后面的可以是0个或者没有  ，并且后面的数字可以是正或者负
    '''
    if not mch:  # 判断是否知道乘除的方程式，如果没有直接return
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val).group()  # 获取乘除的算式
 
    if len(content.split('*')) > 1:  # 判断用*分割后的列表元素个数是否大于1，如果大于1说明获取的是乘法算式
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)  # 用浮点进行计算
    else:
        n1, n2 = content.split('/')  # 除法算是
        value = float(n1) / float(n2)   # 用浮点进行计算
 
    before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val, 1)  # 获取第一个乘除的算式，并用这个算式分割
    new_str = "%s%s%s" % (before, value, after)  # 把计算结果进行拼接，获得新的方程式
    arg[0] = new_str  # 写入至列表中
    compute_mul_div(arg)   # 递归计算
 
 
def compute_add_sub(arg):  # 现在处理加减的时候他现在是个列表，并且仅包含加减
    """ 操作加减
    :param arg:表达式
    :return:计算结果
    """
    while True:
        if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__("--"):
            '''
            __contains__ 如果找到我们们定义的item就会返回True
            这里在处理完乘除之后很可能出现 +-  ++ -+ -- 的的算术符
            '''
            arg[0] = arg[0].replace('+-', '-')  # 替换运算符
            arg[0] = arg[0].replace('++', '+')  # 替换运算符
            arg[0] = arg[0].replace('-+', '-')  # 替换运算符
            arg[0] = arg[0].replace('--', '+')  # 替换运算符
        else:
            break

    if arg[0].startswith('-'):  # 把算式最前面的-号提出来，并把表达式内+，-进行互换
        arg[1] += 1  # 把提取出来的-号的次数，累加到列表中的第二个素值中
        arg[0] = arg[0].replace('-', '&')  # 把-替换为&
        arg[0] = arg[0].replace('+', '-')  # 把+替换为-
        arg[0] = arg[0].replace('&', '+')  # 在把&替换为+
        arg[0] = arg[0][1:]  # 取出算式
    val = arg[0]
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val)
    if not mch:  # 判断是否有+-运算
        return
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val).group()
    if len(content.split('+')) > 1:  # 获取第一个算式，如果分割后的元素数量大于1说明是+法运算
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)  # 进行加法运算
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)  # 进行减法运算

    before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val, 1)  # 把算式进行分割
    new_str = "%s%s%s" % (before, value, after)  # 把计算后的结果进行拼接
    arg[0] = new_str  # 替换原来的算式
    compute_add_sub(arg)  # 递归算式
 
 
def compute(expression):
    """ 操作加减乘除
    :param expression:表达式
    :return:计算结果
    """
    inp = [expression, 0]   # 把算式加入到列表中，用列表的方式操作，可以在函数中操作时不需要return
 
    # 处理表达式中的乘除
    compute_mul_div(inp)
    '''
    上面计算完乘除之后列表里的元算就只剩下
    inp[0] 个元素就等于  不包含*/的表达式字符串了，下面就进行加减了
    '''
    # 处理加减运算
    compute_add_sub(inp)
    if divmod(inp[1], 2)[1] == 1:  # 如果有余数数名值是负的
        result = float(inp[0])
        result = result * -1
    else:
        result = float(inp[0])  # 为正，直接返回值
    return result
 
 
def exec_bracket(expression):
    """ 递归处理括号，并计算
    :param expression: 表达式
    :return:最终计算结果
    """
    # 如果表达式中已经没有括号，则直接调用负责计算的函数，将表达式结果返回
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression):
        final = compute(expression)
        return final
    # 获取 第一个 只含有 数字/小数 和 操作符 的括号
    # 如：
    #    ['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    #    找出：(-40.0/5)
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression).group()
 
    # 分割表达式，即：
    # 将['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    # 分割更三部分：['1-2*((60-30+(    (-40.0/5)      *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    # 至分割第一个找到符合规范的算式
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression, 1)
    '''
    ('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression, 1)
    ([\+\-\*\/]*\d+\.*\d*)这个匹配的是一个（一个数字，前面可以有+ - * / 并且后面可以有小数点）
    {2,} 是表示至少有两个或者多个
    '''
    print('before：', expression)
    # 用分片的方式去掉括号 1：-1 就不包含0和-1了，这样字符串在分片的时候就取消了两边的括号
    content = content[1:len(content)-1]
 
    # 计算，提取的表示 (-40.0/5)，并活的结果，即：-40.0/5=-8.0
    ret = compute(content)
 
    print('%s=%s' % (content, ret))
 
    # 将执行结果拼接，['1-2*((60-30+(      -8.0     *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    expression = "%s%s%s" % (before, ret, after)
    print('after：', expression)
    print("="*10, '上一次计算结束', "="*10)
 
    # 循环继续下次括号处理操作，本次携带者的是已被处理后的表达式，即：
    # ['1-2*((60-30+   -8.0  *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
 
    # 如此周而复始的操作，直到表达式中不再含有括号
    return exec_bracket(expression)
 

# 使用 __name__ 的目的：
# 只有执行 python index.py 时，以下代码才执行
# 如果其他人导入该模块，以下代码不执行
if __name__ == "__main__":
    """print '*'*20,"请计算表达式：", "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ))
- (-4*3)/ (16-3*2) )" ,'*'*20"""
    inpp = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) '
    # inpp = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
    # inpp = "1-5*980.0"
    inpp = re.sub('\s*', '', inpp)  # 取出算式中的空格
    result = exec_bracket(inpp)
    print(result)
