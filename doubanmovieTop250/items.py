# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoiveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    rank=scrapy.Field()#电影排名
    title=scrapy.Field()#电影标题
    rating_num=scrapy.Field()#电影评分
    comments=scrapy.Field()#电影评语
    imageLink=scrapy.Field()#电影封面

    pass
