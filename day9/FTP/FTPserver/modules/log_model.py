#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging


def log_models(logname,infos):
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG) #定义全局日志级别

    ch = logging.StreamHandler() #定义屏幕日志
    ch.setLevel(logging.DEBUG) #定义屏幕日志级别

    fh = logging.FileHandler('log.txt') #定义日志保存文件
    fh.setLevel(logging.DEBUG) #定义文件日志保存级别

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch.setFormatter(formatter) #屏幕输出格式套用自定义的日志格式
    fh.setFormatter(formatter) #日志输出格式套用自定义的日志格式

    logger.addHandler(ch) #把屏幕输出日志交给logger接口执行
    logger.addHandler(fh)#把文件输出日志交给logger接口执行

    logger.debug(infos)
