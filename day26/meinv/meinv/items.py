# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeinvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JieYiCaiItem(scrapy.Item):
    company = scrapy.Field()
    title = scrapy.Field()
    qq = scrapy.Field()
    info = scrapy.Field()
    more = scrapy.Field()