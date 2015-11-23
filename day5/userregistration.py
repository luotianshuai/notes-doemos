#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import pickle


product_list = [('Iphon',5800),('Bike',800),('Book',45),('Coffee',35),('iphon touch',1590),('MX4',1999)]

with open('buy_list','r') as f:
    print json.load(f)