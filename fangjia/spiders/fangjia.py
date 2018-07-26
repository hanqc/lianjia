# -*- coding: utf-8 -*-
import scrapy
from fangjia.items import FangjiaItem

class fangjiaSpider(scrapy.Spider):
    name = "fangjia"
    allowed_domins = ["xa.fang.lianjia.com"]
    start_urls = []
    def start_requests(self):
        urlhead = 'https://xa.fang.lianjia.com/loupan/'
        for i in range(10):
            url = urlhead+'pg%snht1' % i
            self.start_urls.append(url)
        for url in self.start_urls:
            print (url)
            yield scrapy.Request(url, callback=self.parse)
    def parse(self, response):  
        songDivs=response.xpath("//li[@class='resblock-list']")
        for liInfo in songDivs:
            name = liInfo.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-name']/a[@class='name']/text()").extract()[0] # 获得楼盘名称
            address = liInfo.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-location']/a/text()").extract()[0] # 获得楼盘地址
            price = liInfo.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-price']/div[@class='main-price']/span[@class='number']/text()").extract()[0]+liInfo.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-price']/div[@class='main-price']/span[@class='desc']/text()").extract()[0]
            url = liInfo.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-location']/a/@href").extract()[0] # 标签属性值
            item = FangjiaItem()
            item['FANGJIA_NAME'] = name
            item['FANGJIA_ADDRESS'] = address
            item['FANGJIA_PRICE'] = price
            item['FANGJIA_URL'] = 'http://cd.fang.lianjia.com'+url
            yield item
        pass