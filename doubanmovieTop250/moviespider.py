# -*- coding: utf-8 -*-
import scrapy
from doubanmoive.items import DoubanmoiveItem
from scrapy.http import Request


class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    #def start_requests(self):
        #yield Request(self.start_urls,callback=self.parse)
    
    def parse(self, response):
        #获取当前页面中的所有电影采集标签item
        movie_items=response.xpath('//div[@class="item"]')
        #使用for循环遍历每一个电影标签，并采集数据封装成一个采集项对象
        for item in movie_items:
            #创建一个空的类采集对象
            movie=DoubanmoiveItem()
            movie['rank']=item.xpath('div[@class="pic"]/em/text()').extract()
            movie['title']=item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            movie['rating_num']=item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            movie['comments']=item.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
            #if movie['comments']:
                #movie['comments']=movie['comments'][0].strip()
            movie['imageLink']=item.xpath('div[@class="pic"]/a/img/@src').extract()
            yield movie
        pass

        #获取当前url的下一页
        next_page=response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_page:
            request_url=response.urljoin(next_page)
            print(request_url)
            yield Request(request_url,self.parse)
