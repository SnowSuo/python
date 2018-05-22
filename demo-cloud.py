#-*-  coding:utf-8 -*-
'''
    demo-cloud.py
    =============================
    词云图片制作

    @copyright：Chinasoft international .ETC
    @author：SnowSuo
    @date：2018-05-22
'''
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from scipy.misc import imread
#from PIL import Image 
import os
#from os import path
def draw_wordcloud():
    #读入一个TXT文件
    filepath='D:\dev\python36\homework\M3-Demo\cloud\kebi.txt'
    with open(filepath,'r') as fp:
        mytext=fp.read()
    #进行中文分词
    mytext=" ".join(jieba.cut(mytext))
    #设置词云形状（一般使用png图片格式）
    color_mask=plt.imread('D:\dev\python36\homework\.vscode\模块编程\data\中国.jpg')
    cloud=WordCloud(background_color='white',
        #设置词云形状
        mask=color_mask,
        #设置最大词汇
        max_words=1000,
        #停用词
        stopwords=STOPWORDS,
        #设置字体最大值
        max_font_size=60,
        #设置字体格式
        font_path='C:\Windows\Fonts\simhei.ttf',
        #设置有多少种随机生成状态
        random_state=42,
        #设置关键字颜色
        color_func=None,
    ).generate(mytext)#产生词云
    #plt.imshow(cloud)
    image_colors=ImageColorGenerator(color_mask)
    #cloud.recolor(color_func=image_colors)#根据背景图片获取字体颜色
    plt.imshow(cloud)
    #关闭坐标轴
    plt.axis('off')
    #保存图片
    cloud.to_file('D:\dev\python36\homework\.vscode\模块编程\data\cloud.jpg')
    plt.show()
if __name__=='__main__':
    draw_wordcloud()
