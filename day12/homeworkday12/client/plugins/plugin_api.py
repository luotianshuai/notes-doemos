#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import cpu,mem

def get_cpu_status():
    return cpu.monitory()

def get_mem_status():
    return mem.monitory()
