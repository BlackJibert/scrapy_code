# -*- coding: utf-8 -*-
import scrapy


class TiebaSpider(scrapy.Spider):
    name = "tieba"
    # allowed_domains = ["tieba.com"]
    # start_urls = ['http://tieba.com/']
    base_url = "https://tieba.baidu.com/f?ie=utf-8&kw=china"

    def start_requests(self):
        print("hello")

        pass

    def parse(self, response):
        pass
