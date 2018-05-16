# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DoubanmoivePipeline(object):
    
    def process_item(self, item, spider):
        dbserverIp='localhost'
        user='root'
        password='123'
        dbname='crawl'
        connection=pymysql.connect(host=dbserverIp,port=3306,user=user,password=password,db=dbname,charset='utf8')
        if connection:
            print('>>数据库链接成功')
        else:
            print('>>数据库链接失败')
        #创建一个游标对象affectrow
        cusor =connection.cursor()
        print('游标对象创建成功')
        #设置sql语句
        rank=int(item['rank'][0])
        title=item['title'][0]
        rating_num=item['rating_num'][0]
        comments=item['comments'][0]
        sql='insert into movieinfo values(null,%d,\'%s\',\'%s\',\'%s\')'\
                                        %(rank,title,rating_num,comments)
        print('Mysql>>%s'%sql)
        #使用游标对象发送sql语句
        affectrow=cusor.execute(sql)
        #提交事务
        connection.commit()
        print('>>事务提交')
        msg='OK,数据插入成功' if affectrow>0 else '数据插入失败'
        print('>>%s'%msg)
        #关闭数据库
        connection.close()
        print('>>数据库链接关闭') 
        return item
