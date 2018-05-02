#-*- coding:utf-8 -*-
'''
    ch02-demo14-excel2json.py
    ---------------------------------
    excel 转换 json

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

# 导入模块
import json
import os
import xlrd

'''
    @name: excel2json
    @args: str, str
    @return: none
    @date: 2018-04-25
'''
def excel2json(excelPath, jsonPath):
    # 变量
    data = []
    # 读取excel文件    
    # 步骤1：获取到指定路径excel文件的工作簿对象workbook
    workbook = xlrd.open_workbook(excelPath)
    # 步骤2：获取当前的有效的数据单页对象sheet
    # 步骤2-1：获取单页对象集
    sheets = workbook.sheet_names()
    # 步骤2-2：获取可操作的数据单页
    worksheet = workbook.sheet_by_name(sheets[0])
    # 步骤3：读取sheet单页对象中的cell数据
    keys = [worksheet.cell_value(0, colIndex) for colIndex in range(worksheet.ncols)]
    # 外层循环控制行数
    for rowIndex in range(1, worksheet.nrows):
        # 内层循环控制列数
        values = [worksheet.cell_value(rowIndex, colIndex) for colIndex in range(worksheet.ncols)]
        # 生成当前循环到的字典数据
        item = dict(zip(keys, values))
        # 将每一个字典数据添加到data列表集合中
        data.append(item)

    #print('>> data:{0}'.format(data))
    print('>> excel数据读取完毕并完成格式转')

    # 写入json文件
    # 步骤1：打开json文件(获取程序与json文件的关联引用)
    with open(jsonPath, 'w') as jsonfile:
        # 使用json.dumps()序列化处理
        jsonData = json.dumps(data, ensure_ascii=False)
        # 步骤2：序列化数据并写入文件
        jsonfile.write(jsonData)
        print('>> json文件写入完毕.')
        pass

# 脚本入口
if __name__ == '__main__':
    # excel文件路径
    excelPath = os.path.join(os.getcwd(), 'CH02_Demos/data/test.xls')
    # json文件路径
    jsonPath = os.path.join(os.getcwd(), 'CH02_Demos/data/test_bak.json')
    # 调用函数
    excel2json(excelPath, jsonPath)
    print('>> excel转换json文件操作完毕.')
