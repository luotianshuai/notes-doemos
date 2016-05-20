#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
import re
import urllib
import os


class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/list-1-1.html",
    ]

    def parse(self, response):
        '''
        1 分析页面
        2 找到页面中符合规则的内容（校花图片），保存
        3 找到所有的a标签，再访问其他a标签，一层一层的搞下去
        '''



        hxs = HtmlXPathSelector(response)
        '''
        hxs = HtmlXPathSelector(response)
        #格式化源码
        #以前咱们从html页面中去获取某些数据的时候需要用正则,现在不用了scrapy给咱们提供了类选择器
        #只要创建一个对象然后他就会页面中去找,他支持  --链式编程--  类似于找:
        div[@class='xxx]的标签 如果在加个/a  就是div[@class='xxx]/a 就是div下的class='xxx'的下面的a标签
        '''

        # 如果url是 http://www.xiaohuar.com/list-1-\d+.html通过正则去判断,这里首选需要了解的是
        # 这个网站的URL设计就可以了,这是符合URL的
        if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):

            #这里是调用hxs然后去找到div下class='item_list infinite_scroll'下的div,
            #这个同样也是需要看下网页的设计结构,校花网的设计结构就是这样的嘿嘿....
            items = hxs.select('//div[@class="item_list infinite_scroll"]/div')


            for i in range(len(items)):
                #这个校花里的DIV是可以通过索引去取值的
                src = hxs.select(
                    '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
                    #@表示取里面的属性
                name = hxs.select(
                    '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
                school = hxs.select(
                    '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
                if src:
                    ab_src = "http://www.xiaohuar.com" + src[0]
                    file_name = "%s_%s.jpg" % (school[0].encode('utf-8'), name[0].encode('utf-8'))
                    #file_path = os.path.join("/Download/meinv/", file_name)
                    #这个方法下载文件,并且file_name为文件
                    urllib.urlretrieve(ab_src, file_name)

        # 获取所有的url，继续访问，并在其中寻找相同的url
        all_urls = hxs.select('//a/@href').extract()  #查找所有的A标签有href属性的URL
        #去循环他
        for url in all_urls:
            #并且这里在加了一个判断,也可以不加,并且符合
            if url.startswith('http://www.xiaohuar.com/list-1-'):
                #如果你返回了一个URL并且有callback就会去递归,还去执行self.parse
                yield Request(url, callback=self.parse)
