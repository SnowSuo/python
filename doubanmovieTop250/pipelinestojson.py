# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os 
import time
import json
class DoubanmoivePipeline(object):
    #创建一个构造方法，用于创建所有项目输出文件夹
    def __init__(self):
    #设置文件夹名称
        self.folderName='output'
        #判断文件夹是否存在
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)

    def process_item(self, item, spider):
        #输出提示
        print('>>> write to json file...')
        #获取当前日期
        now=time.strftime('%Y%m%d',time.localtime())
        #设置json文件名
        jsonFileName='doubanmovie'+now+'.json'
        #打开json文件以追加方式
        try:
            with open (self.folderName +os.sep+jsonFileName,'a')as jsonfile:
                #当前数据序列化
                data=json.dumps(dict(item),ensure_ascii=False)+ '\n'
                #写入json文件
                jsonfile.write(data)
        except IOError as err:
            #输出报错信息
            raise('json file erro:{0}'.format(str(err)))
        finally:
            #关闭文件
            jsonfile.close()        
        return item
