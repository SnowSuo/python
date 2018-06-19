from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import os
import requests
from selenium.webdriver.support.ui import WebDriverWait
import random

dirPath=os.path.join(os.getcwd(),'picture')
    #判断文件夹是否存在
if not os.path.exists(dirPath):
    os.mkdir(dirPath)

browser = webdriver.Chrome()
wait=WebDriverWait(browser,30)

url = 'http://www.meizitu.com/a/5492.html'
browser.get(url)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
html=browser.page_source
soup=BeautifulSoup(html,'lxml')
image_url=soup.find(id="picture").find_all(name='img')
for item in image_url:
    url=item.attrs['src']
    data=requests.get(url,headers=headers).content
    with open ((dirPath + os.sep + str(random.randint(1,999))+url.split('/')[-1]) ,'wb+') as imageFile:
        imageFile.write(data)
        print('图片下载完毕')

 

