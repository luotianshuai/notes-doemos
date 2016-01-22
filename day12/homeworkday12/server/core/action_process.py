#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import json
import serialize

def action_process(server_instance,business_type,client_data):
    func = getattr(serialize,business_type)
    func(server_instance,client_data)

def action_work(server_instance,keys_name,hostserver):
    func = getattr(serialize,hostserver)
    func(server_instance,keys_name)