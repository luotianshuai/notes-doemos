#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'



import os
import sys
import platform
#添加BASE_DIR,添加顶级目录到路径中,方便调用模块
if platform.system() == 'windows':
    # BASE_DIR = '\\'.join()
    pass
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(BASE_DIR)

import scrapy
import hashlib
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from meinv.items import JieYiCaiItem

class JieYiCaiSpider(scrapy.spiders.Spider):
    count = 0
    url_set = set()

    name = "jieyicai"
    domain = 'http://www.jieyicai.com'
    allowed_domains = ["jieyicai.com"]

    start_urls = [
        "http://www.jieyicai.com",
    ]

    rules = [
        # 下面是符合规则的网址,但是不抓取内容,只是提取该页的链接(这里网址是虚构的,实际使用时请替换)
        # Rule(SgmlLinkExtractor(allow=(r'http://test_url/test?page_index=\d+'))),
        # 下面是符合规则的网址,提取内容,(这里网址是虚构的,实际使用时请替换)
        # Rule(LinkExtractor(allow=(r'http://www.jieyicai.com/Product/Detail.aspx?pid=\d+')), callback="parse"),
    ]

    def parse(self, response):
        md5_obj = hashlib.md5()
        md5_obj.update(response.url)
        md5_url = md5_obj.hexdigest()
        if md5_url in JieYiCaiSpider.url_set:
            pass
        else:
            JieYiCaiSpider.url_set.add(md5_url)

            hxs = HtmlXPathSelector(response)
            if response.url.startswith('http://www.jieyicai.com/Product/Detail.aspx'):
                item = JieYiCaiItem()
                item['company'] = hxs.select('//span[@class="username g-fs-14"]/text()').extract()
                item['qq'] = hxs.select('//span[@class="g-left bor1qq"]/a/@href').re('.*uin=(?P<qq>\d*)&')
                item['info'] = hxs.select('//div[@class="padd20 bor1 comard"]/text()').extract()
                item['more'] = hxs.select('//li[@class="style4"]/a/@href').extract()
                item['title'] = hxs.select('//div[@class="g-left prodetail-text"]/h2/text()').extract()
                yield item

            current_page_urls = hxs.select('//a/@href').extract()
            for i in range(len(current_page_urls)):
                url = current_page_urls[i]
                if url.startswith('/'):
                    url_ab = JieYiCaiSpider.domain + url
                    yield Request(url_ab, callback=self.parse)