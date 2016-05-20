#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
 # 请计算表达式： 1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# def bracket(s):
#     ret=re.search('\([^()]+\)',s).group()
#     return ret
#
# def mul(s):
#     ret=re.search('\d+\.?\d*([*/]|\*\*)\d+\.?\d*',s).group()
#     if len(ret.split('*'))>1:
#         a,b=ret.split('*')
#         c=int(a)*int(b)
#     else:
#         a,b=ret.split('/')
#         c=int(a)/int(b)
#     return str(c)
#
# def ad(s):
#     ret=re.search('[\-]?\d+\.?\d*[+-][\-]?\d+\.?\d*',s).group()
#     if len(ret.split('+'))>1:
#         a,b=ret.split('+')
#         c=int(a)+int(b)
#     else:
#         a,b=ret.split('-')
#         c=int(a)-int(b)
#     return str(c)




# s='1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
s='1 - 2 * (60-30)'
# s='1+2*5'

# while re.search('\([^()]+\)',s):
#     print('12111111111')
#     a=bracket(s).strip('(').strip(')')
#     print(a)
#     while re.search('\d+\.?\d*([*/]|\*\*)\d+\.?\d*',a):
#         b=mul(a)
#         a=re.sub(re.search('\d+\.?\d*([*/]|\*\*)\d+\.?\d*',a).group(),b,a)
#     while re.search('[\-]?\d+\.?\d*[+-][\-]?\d+\.?\d*',a):
#         b=ad(a)
#         a=re.sub(re.search('[\-]?\d+\.?\d*[+-][\-]?\d+\.?\d*',a).group(),b,a)
#     s=re.sub(re.search('\([^()]+\)',s).group().replace('(','\(').replace(')','\)'),a,s)
# print(s)
while re.search('\d+\.?\d*([*/]|\*\*)\d+\.?\d*','1-2*30'):
    print('1')
#     b=mul(s)
#     a=re.sub(re.search('\d+\.?\d*([*/]|\*\*)\d+\.?\d*',s).group(),b,s)
# while re.search('[\-]?\d+\.?\d*[+-][\-]?\d+\.?\d*',s):
#     b=ad(s)
#     a=re.sub(re.search('[\-]?\d+\.?\d*[+-][\-]?\d+\.?\d*',s).group(),b,s)
#
#
# print(s)