# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MeinvPipeline(object):
    def process_item(self, item, spider):
        return item

import json
from twisted.enterprise import adbapi
import MySQLdb.cursors
import re

mobile_re = re.compile(r'(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}')
phone_re = re.compile(r'(\d+-\d+|\d+)')

class JsonPipeline(object):

    def __init__(self):
        self.file = open('jieyicai.json', 'wb')


    def process_item(self, item, spider):
        line = "%s  %s\n" % (item['company'][0].encode('utf-8'), item['title'][0].encode('utf-8'))
        self.file.write(line)
        return item
#
# class DBPipeline(object):
#
#     def __init__(self):
#         self.db_pool = adbapi.ConnectionPool('MySQLdb',
#                                              db='DbCenter',
#                                              user='root',
#                                              passwd='luotianshuai',
#                                              cursorclass=MySQLdb.cursors.DictCursor,
#                                              use_unicode=True)
#
#     def process_item(self, item, spider):
#         query = self.db_pool.runInteraction(self._conditional_insert, item)
#         query.addErrback(self.handle_error)
#         return item
#
#     def _conditional_insert(self, tx, item):
#         tx.execute("select nid from company where company = %s", (item['company'][0], ))
#         result = tx.fetchone()
#         if result:
#             pass
#         else:
#             phone_obj = phone_re.search(item['info'][0].strip())
#             phone = phone_obj.group() if phone_obj else ' '
#
#             mobile_obj = mobile_re.search(item['info'][1].strip())
#             mobile = mobile_obj.group() if mobile_obj else ' '
#
#             values = (
#                 item['company'][0],
#                 item['qq'][0],
#                 phone,
#                 mobile,
#                 item['info'][2].strip(),
#                 item['more'][0])
#             tx.execute("insert into company(company,qq,phone,mobile,address,more) values(%s,%s,%s,%s,%s,%s)", values)
#
#     def handle_error(self, e):
#         print 'error',e