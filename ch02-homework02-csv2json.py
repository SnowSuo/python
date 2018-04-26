#-*- coding:utf-8 -*-
'''
    ch02-demo11-csv2json.py
    ------------------------
    csv转json

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

# 导入模块
import csv
import os
import json


'''
    @name: csv2json
    @args: str, str
    @return: none
    @date: 2018-04-25
'''
def csv2json(csvPath, jsonPath):
    '将csv文件转换成json文件'
    # 变量
    lstItem = []

    # 读取csv文件
    with open(csvPath, 'r') as csvfile:
        # csv.DictReader()函数读取文件数据
        reader = csv.DictReader(csvfile)
        print(type(reader))
        # 循环输出
        lstItem = [dict(item) for item in reader])
        print('csv文件读取完毕')
   
    # 写入json文件
    with open(jsonPath, 'w') as jsonfile:
        # 使用json.dumps()函数序列化
        jsonData = json.dumps(lstItem, ensure_ascii=False)
        # 使用jsonfile.write()函数写入文件
        jsonfile.write(jsonData)
        print('json文件写入完毕')
        pass

# 脚本入口
if __name__ == '__main__':
    # 准备参数
    # csv文件路径
    csvPath = os.path.join(os.getcwd(), 'CH02_Demos\data\data2.csv')
    # json文件路径
    jsonPath = os.path.join(os.getcwd(), 'CH02_Demos\data\data2_bak.json')
    # 调用转换函数
    csv2json(csvPath, jsonPath)