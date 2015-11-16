#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json

def fetch(backend):
	fetch_list = []
	with open('ha') as obj:
		flag = False
		for line in obj:
			# line 每一行，
			if line.strip() == "backend %s" % backend:
				flag = True
				continue
			# 判断，如果当前是 backend开头，不再放
			if flag and line.strip().startswith('backend'):
				break
			if flag and line.strip():
				fetch_list.append(line.strip())
	return fetch_list

#result = fetch("buy.oldboy.org")
#print result
def add1(dict_info):
    #s = '{"bakend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
	backend_title = dict_info.get('backend')
	current_title = "backend %s" % backend_title
	crrent_record = "server %s %s weight %s maxconn %s" % (dict_info['record']['server'],dict_info['record']['server'],dict_info['record']['weight'],dict_info['record']['maxconn'])
	# 获取制定backend下的所有记录
	fetch_list = fetch(backend_title)
	# backend是否存在
	if fetch_list:
		#pass # 存在backend，则只需再添加记录
		# 1,要插入的记录，存在
		# 1,要插入的记录，不存在
		if crrent_record in fetch_list:
			pass
		else:
			fetch_list.append(crrent_record)
		# fetch_list,处理完的新列表
		with open('ha') as read_obj, open('ha.new', 'w') as write_obj:
			flag = False
			has_write = False
			for line in read_obj:
				if line.strip() == current_title:
					write_obj.write(line)
					flag = True
					continue
				if flag and line.strip().startswith('backend'):
					flag = False
				if flag:
					# 中，把列表所有数据写入
					if not has_write:
						for new_line  in fetch_list:
							temp = "%s %s \n" %(" "*8, new_line)
							write_obj.write(temp)
						has_write = True
				else:
					# 上，下
					write_obj.write(line)
	else:
		#pass # 不存在backend，添加记录和backend
		# current_title,crrent_record
		# 直接打开文件，a
		with open('ha') as read_obj, open('ha.new', 'w') as write_obj:
			for line in read_obj:
				write_obj.write(line)
			write_obj.write('\n')
			write_obj.write(current_title+'\n')
			temp = "%s %s \n" %(" "*8, crrent_record)
			write_obj.write(temp)

	#os.rename("ha", 'ha.bak')
	#os.rename("ha.new", 'ha')

s = '{"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}'
data_dict = json.loads(s)
add1(data_dict)



