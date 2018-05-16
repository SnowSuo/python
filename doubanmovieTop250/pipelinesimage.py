# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os 
import time
import json
import urllib.request
class DoubanmoivePipeline(object):
    #创建一个构造方法，用于创建所有项目输出文件夹
    def __init__(self):
    #设置文件夹名称
        self.folderName='outputImage'
        #判断文件夹是否存在
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)

    def process_item(self, item, spider):
        #输出提示
        print('>>> 获取电影封面资源地址')
        #获取网络资源数据
        data=urllib.request.urlopen(item['imageLink'][0]).read()
        #二进制模式写入数数据
        with open ((self.folderName + os.sep +item['title'][0]+'.jpg'),'wb') as imageFile:
            imageFile.write(data)
            print('网页源码写入完毕>>>')
                   
        return item
