# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os
import time


class DoubanmoivePipeline(object):

    def __init__(self):
         # 首先，设置logging日志的基本参数
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.fomatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # 其次，创建并设置文件处理器FileHandler对象
        self.dirPath = os.path.join(os.getcwd(), 'output/log')
        if not os.path.exists(self.dirPath):
            os.mkdir(self.dirPath)
        self.logFileName = time.strftime('%Y%m%d%H%M', time.localtime())+'.log'
        self.logPath = self.dirPath + os.sep + self.logFileName
        # 创建FileHandler对象
        self.fileHandler = logging.FileHandler(self.logPath)
        # 设置Filehandler对象的写入信息级别
        self.fileHandler.setLevel(logging.INFO)
        # 设置FileHandler对象的信息格式
        self.fileHandler.setFormatter(self.fomatter)
        self.logger.addHandler(self.fileHandler)

    def process_item(self, item, spider):
        self.logger.info('电影排名：{0}'.format(item['rank'][0]))
        self.logger.info('电影名称：{0}'.format(item['title'][0]))
        self.logger.info('电影评分：{0}'.format(item['rating_num'][0]))
        self.logger.info('电影评价：{0}'.format(item['comments']))
        self.logger.info('='*40)
        #logger.info('图片地址：{0}'.format(item['imageLink'][0]))
        #self.logger.info(item)
        return item
