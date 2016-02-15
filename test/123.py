#!/usr/bin/env python
#-*-  coding:utf-8 -*-
import re


a = '10/9*8'

#print re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',a)
print re.search('\d+\.*\d*/\d+\.*\d*',a).group()