from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import lxml
browser = webdriver.Chrome()
class mzitu(): 
    def __init__(self):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"}
    def all_url(self, url):
        
        browser.get(url)
        html=browser.page_source
        all_a = BeautifulSoup(html, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print('开始保存：', title) 
            path = str(title).replace("?", '_') 
            self.FilePath(path) #调用创建文件夹函数
            href = a['href']
            print(href)
            self.html(href)
    def html(self, href):   
        html = browser.get(href)
        html=browser.page_source
        self.headers['referer'] = href
        max_span = BeautifulSoup(html, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            print(page_url)
            self.img(page_url) #调用img函数
 
    def img(self, page_url): #这个函数处理图片页面地址获得图片的实际地址
        img_html =requests.get(page_url).text
        img_url = BeautifulSoup(img_html, 'lxml').find('div', class_='main-image').find('img')['src']
        print(img_url)
        self.save(img_url)
 
    def save(self, img_url): #这个函数保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        with open(name +'.jpg','wb')as fp:
            fp.write(img)
            print('图片下载完成')
    
    def FilePath(self, path): #这个函数创建文件夹
        path = path.strip()
        dirPath = os.path.exists(os.path.join("D:\mzitu", path))
        if not dirPath:
            print('创建文件夹', path)
            os.makedirs(os.path.join("D:\mzitu", path))
            os.chdir(os.path.join("D:\mzitu", path)) #切换到目录
            return True
        else:
            print('名字叫做', path, '的文件夹已经存在了！')
            return False
 
    def request(self, url): #这个函数获取网页的response 然后返回
        content = requests.get(url, headers=self.headers).content
        return content
if __name__=='__main__':
    Mzitu = mzitu() 
    Mzitu.all_url('http://www.mzitu.com/old') 