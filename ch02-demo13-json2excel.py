#-*- coding:utf-8 -*-
'''
    ch02-demo13-json2excel.py
    ---------------------------------
    josn 转换 excel

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

# 导入模块
import json
import os
import xlwt

'''
    @name: json2excel
    @args: str, str
    @return: none
    @date: 2018-04-25
'''
def json2excel(jsonPath, excelPath):
    'json转excel文件'
    # 设置列表变量
    data = []
    # 读取json文件
    # 步骤1：使用with语句以读取模式打开json文件
    with open(jsonPath, 'r') as jsonfile:
        # 步骤2：使用json.load()函数获取json文件数据并反序列化列表对象
        data = json.load(jsonfile)
        #print('>> 测试:\n{0}'.format(data))
        print('>> json文件读取完毕.')
        pass

    # 写入excel文件
    # 步骤1：获取工作簿对象workbook
    workbook = xlwt.Workbook(encoding='utf-8')
    # 步骤2：获取单页对象sheet
    sheet = workbook.add_sheet('人员信息')
    # 步骤3：写入标题行
    headers = [k for k in data[0]]
    for colIndex in range(len(headers)):
        sheet.write(0, colIndex, headers[colIndex])
    # 步骤4：写入数据内容
    contents = [[v for v in item.values()] for item in data]
    for rowIndex in range(1, len(contents)+1):
        for colIndex in range(len(headers)):
            sheet.write(rowIndex, colIndex, contents[rowIndex-1][colIndex])
    # 步骤5：工作簿保存
    workbook.save(excelPath)
    print('>> excel文件写入完毕.')
    pass

# 脚本入口
if __name__ == '__main__':
    # 步骤1：设置json文件的路径
    jsonPath = os.path.join(os.getcwd(), 'CH02_Demos/data/data2_bak.json') 
    # 步骤2：设置excel文件的路径
    excelPath = os.path.join(os.getcwd(), 'CH02_Demos/data/data2_bak.xls')
    # 步骤3：调用函数
    json2excel(jsonPath, excelPath)
    print('>> 文件格式转换完毕.')