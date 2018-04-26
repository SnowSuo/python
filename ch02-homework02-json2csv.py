#-*- coding:utf-8 -*-
'''
    ch02-demo12-json2csv.py
    ------------------------
    json转jcsv

    @Copyright: Chinasoft International·ETC
    @author: suoyonggang
    @date: 2018-04-25
'''

# 导入模块
import csv
import os
import json
'''
    @name: jsonTocsv
    @args: str, str
    @return: none
    @date: 2018-04-25
'''
def jsonTocsv(jsonPath, csvPath):
    # 数据集
    data = []
    # 读取json文件数据    
    # 使用with语句
    with open(jsonPath, 'r') as jsonfile:
        # 调用json.load()函数获取json数据并反序列化list[dict]
        data = json.load(jsonfile)
        print(' json文件读取完毕')
        pass
    # 写入csv文件数据    
    #使用with语句
    with open(csvPath, 'w', newline='') as csvfile:
        # 获取数据集的统一keys值
        keys = [k for k in data[0]]
        # 调用csv.DictWriter()函数创建DitWriter对象
        dictWriter = csv.DictWriter(csvfile, fieldnames = keys)
        # 调用writeheader()函数写入标题行
        dictWriter.writeheader()
        print('标题行写入完毕.')
        # 使用for循环遍历data列表
        for item in data:
            # 使用write()函数直接将字典类型写入csv文件
            dictWriter.writerow(item)
        print('数据写入完毕.')
        pass
# 脚本入口
if __name__ == '__main__':
    # json文件路径
    jsonPath = os.path.join(os.getcwd(), '.vscode\模块编程\myjson.json')
    # csv文件路径
    csvPath = os.path.join(os.getcwd(), '.vscode\模块编程\mycsv.csv')
    # 调用函数实现json->csv转换
    jsonTocsv(jsonPath, csvPath)