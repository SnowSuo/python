# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os 
import time
import xlrd
import xlwt
from xlutils.copy  import copy


class DoubanmoivePipeline(object):
    #创建一个构造方法，用于创建所有项目输出文件夹
    def __init__(self):
    #设置文件夹名称
        self.folderName='output'
        #判断文件夹是否存在
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)
        #获取当前日期
        now=time.strftime('%Y%m%d',time.localtime())
        #设置excel文件名
        excelFileName='doubanmovie'+now+'.xls'
        self.excelPath=self.folderName +os.sep+excelFileName
        #构建工作簿
        self.workbook=xlwt.Workbook(encoding='utf8')
        #创建sheet单页
        self.sheet=self.workbook.add_sheet('豆瓣电影数据')
        #设置excel内容标题
        headers=['电影排名','电影名称','电影评分','电影评价','图片封面地址']
        #设置标题样式
        headerStyle=xlwt.easyxf('font:color-index black,bold on')
        #循环写入标题
        for colIndex in range(0,len(headers)):
            self.sheet.write(0,colIndex,headers[colIndex],headerStyle)
            pass
        #保存创建好excel文件
        self.workbook.save(self.excelPath)
       
        pass
    rowIndex=1

    def process_item(self, item, spider):
        #输出提示
        print('>>> write to excel file...')
        #读取创建好的excel文件
        oldworkbook=xlrd.open_workbook(self.excelPath,formatting_info=True)
        #拷贝副本
        newworkbook=copy(oldworkbook)     
        #获取excel要操作的sheet单页
        sheet=newworkbook.get_sheet(0)  
        #将采集的数据转换成列表
        line=[item['rank'],item['title'],item['rating_num'],item['comments'],item['imageLink']]
        #使用for循环遍历excel中每一小格
        for colIndex in range(0,len(item)):
            #将数据写入到指定行中
            sheet.write(self.rowIndex,colIndex,line[colIndex])
            pass
        newworkbook.save(self.excelPath)
        #全局行自增1
        self.rowIndex=self.rowIndex+1
        return item
