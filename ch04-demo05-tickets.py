#-*- coding:utf-8 -*-
'''
    ch04-demo05-tickets.py
    ------------------------
    火车票抢票

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

import time
import threading
import random

# 全局变量,票数
tickets = 10

# 创建线程列表序列
threads = []

# 创建线程锁
condition = threading.Condition()

# 自定义一个函数
def buyTicket(threadName, delay):
    global tickets
    while tickets > 0 :
        if condition.acquire(): # 添加锁
            if (11-tickets) <= 10:             
                print('>>> {0} 抢到程票{1}.'.format(threadName, (11-tickets)))
                time.sleep(delay)
                tickets -= 1 # 票总数自减1
        condition.release() # 释放锁
        pass

# 线程类
class MyThread(threading.Thread):

    # 构造方法
    def __init__(self, threadName, delay):
        threading.Thread.__init__(self)
        self.__threadName = threadName
        self.__delay = delay
        pass

    # 线程对象run()方法
    def run(self):
        # 调用购票函数
        buyTicket(self.__threadName, self.__delay)
        pass

# 脚本入口
if __name__ == '__main__':
    print("[启动]>>> 火车站启动开放C1101次的车票....")
    #创建新线程
    thread1 = MyThread("售票点-1", 1)
    thread2 = MyThread("售票点-2", 2)
    thread3 = MyThread("售票点-3", 1.5)

    #开启新线程
    thread1.start()
    thread2.start()
    thread3.start()

    #添加新线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)

    #等待所有线程完成
    for t in threads:
        t.join()
    
    print("[停止]>>> 抢票结束，本次车票全部售罄....\a")