#-*-  coding:utf-8 -*-
'''
    ch01-homeworko1-sort.py
    =============================
   冒泡排序

    @copyright：Chinasoft international .ETC
    @author：suoyonggang
    @date：2018-05-03

'''
import random
def bubulsort(self):
    #外层循环控制比较轮次
    for i in range(10):
        #内层循环控住每轮比较次数
        for j in range(len(data)-i-1):
            #如果前项大于后项值，则将大的在列表后移一位
            if data[j]>data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
                pass
            pass
        pass
    print('排序后的序列为{0}'.format(data))

if __name__=='__main__':
    #创建空列表存放待排序数据集
    data=[random.randint(0,300) for i in range(10)]#列表推导式生成数字列表
    print('待排序数字列表.{0}'.format(data))
    bubulsort(data)
