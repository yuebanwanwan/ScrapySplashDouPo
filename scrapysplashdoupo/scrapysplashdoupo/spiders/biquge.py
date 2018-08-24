# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
from scrapy import Spider
from scrapy_splash import SplashRequest
from scrapysplashdoupo.items import DouPoItem

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.biquge.com.tw']
    base_urls = 'http://www.biquge.com.tw/1_1999/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }

    def start_requests(self):
        response = requests.get(self.base_urls, headers=self.headers)
        html = etree.HTML(response.text)
        if response.status_code == 200:
            charptersip = html.xpath('//div[@id="list"]//dd/a/@href')
            if charptersip:
                for charptes in charptersip:
                    base = 'http://www.biquge.com.tw'
                    yield SplashRequest(url=base + charptes ,callback=self.parse)


    def parse(self, response):
        item = DouPoItem()
        item['title'] = response.xpath('//title/text()').extract_first().strip()
        item['content'] = ''.join(response.xpath('//div[@id="content"]//text()').extract()).strip()
        yield item
