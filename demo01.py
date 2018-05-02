#-*-  coding:utf-8 -*-
'''
    =============================
    获取豆瓣读书榜单，并将获取数据已json文件格式持久化保存

    @copyright：Chinasoft international .ETC
    @author：SnowSuo
    @date：2018-05-02

'''
#导入模块
import urllib.request
import re
import os
import json
#获取网页地址
url='https://book.douban.com/top250?icn=index-book250-all'
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
#拆分所需的字符串，定义正则表达式
regcontent=re.compile(r'<tr class="item">(.*?)</tr>',re.S)
regTitle=re.compile(r'<div class="pl2"><a.*?title="(.*?)">')
regLinks=re.compile(r'<a href="(.*?)".*?>')
regRatings=re.compile(r'<span class="rating_nums">(.*?)</span>')
regprice=re.compile(r'<p class="pl">(.*?)</p>')
lstcontent=regcontent.findall(content)

#创建一个列表对象，存放数据
data=[]
for item in lstcontent:
    #去掉多余空格
    regExp=re.compile(r'[\s\n]{2,}')
    #blockcode=regExp.sub('',item)

    #创建一个子弹对象，用于封装存放每一个记录的3个数据
    dictbook={}
    #获取每一个数据图书名称
    lstTitle=regTitle.findall(blockcode)
    print(lstTitle)
    dictbook['title']=lstTitle
    #获取每一本图书连接
    lstLink=regLinks.findall(blockcode)
    print(lstLink)
    dictbook['link']=lstLink
    #获取评分
    lstRating=regRatings.findall(blockcode)
    print(lstRating)
    dictbook['rating']=lstRating
    #获取书籍作者及价格
    lstPrice=regprice.findall(blockcode)
    print(lstPrice)
    #封装好的字典数据添加到list列表中
    data.append(dictbook)
    print('='*30)
#设置json文件的存储路径
dataDir=os.path.join(os.getcwd(),'.vscode/模块编程/data')
if not os.path.exists(dataDir):
    os.mkdir(dataDir)
#将数据写入json文件
with open(dataDir+os.sep+'bookdata.json','w',encoding='utf-8')as jsonfile:
    #使用json中dump快速序列化并写入指定文件
    json.dump(data,jsonfile,ensure_ascii=False)
    print('>>>>json文件写入完毕')