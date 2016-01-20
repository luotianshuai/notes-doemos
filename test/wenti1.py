#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import collections
A=collections.OrderedDict(name='chen',age='25',job='it')

for k,v in A.items():
    print k,v
