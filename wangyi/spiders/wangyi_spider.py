#-*- coding: utf-8 -*-
import scrapy 
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from wangyi.items import WangyiItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re

class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    allowed_domains = ['v.163.com']

    def start_requests(self):
        start_urls = [
            "http://v.163.com/special/opencourse/ios7.html",
        ]
        for url in start_urls:
            yield Request(url, callback=self.parse_wangyi)
     #        break

      
    def parse_wangyi(self,response):
        item = WangyiItem()
        title= response.css("table#list2 td.u-ctitle::text").extract()
        
        tit = []
        for i in title:
            tit.append(i.strip()) 
        #print tit
        item['title'] = [i for i in tit if i!= ""]
        item['url'] = response.css("table#list2 td.u-ctitle a::attr(href)").extract()
        item['pic'] = response.css("table#list2 td.u-ctitle img::attr(src)").extract()
        return item
