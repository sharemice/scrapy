# -*- coding: utf-8 -*-
import scrapy
from testone.items import TestoneItem
from scrapy.loader import ItemLoader 
class RosiokSpider(scrapy.Spider):
    name = "rosiok"
    allowed_domains = ["rosiok.com"]
    start_urls = ['http://rosiok.com/']
  
    def start_requests(self):
	for c in self.start_urls:
		yield scrapy.Request(c,callback=self.parse)

    def parse(self, response):
	 for a  in response.css('a::attr(href)').extract():
                       next_page=response.urljoin(a)
                       yield scrapy.Request(next_page,callback=self.parse)
         for b in response.css('img::attr(src)').extract():
                       il = ItemLoader(item=TestoneItem())
                       il.add_css('img_url','img::attr(src)',response=response)
                       yield il.load_item()

#     def parse(self,response):
#               for a  in response.css('a::attr(href)').extract():
#                       next_page=response.urljoin(a)
#                       print next_page
#                       yield scrapy.request(next_page,callback=self.parse)
#               for b in response.css('img::attr(src)').extract():
#                       il = ItemLoader(item=TestoneItem(),response=response)
#                       il.add_css('img_url','img::attr(src)')
#                       return il.load_item()
#
