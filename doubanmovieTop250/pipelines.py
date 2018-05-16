# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoivePipeline(object):
    def process_item(self, item, spider):
        print('电影排名：{0}'.format(item['rank'][0]))
        print('电影名称：{0}'.format(item['title'][0]))
        print('电影评分：{0}'.format(item['rating_num'][0]))
        print('电影评价：{0}'.format(item['comments'][0]))
        print('图片地址：{0}'.format(item['imageLink'][0]))

        return item
