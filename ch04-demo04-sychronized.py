#-*- coding:utf-8 -*-
'''
    ch04-demo04-sychronized.py
    ------------------------
    线程同步

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

# 导入模块
import time
import threading

# 创建线程锁
threadLock = threading.Lock()

# 创建线程列表序列
threads = []

# 自定义函数
def print_time(threadName,delay):
    for i in range(delay):
        time.sleep(1)
        print("%s -- %s -- %s" %(threadName,i,time.ctime(time.time())))
        pass

# 线程类
class Mythread(threading.Thread):

    # 构造方法
    def __init__(self,threadName,delay):
        # 调用父类Thread的构造方法
        threading.Thread.__init__(self)
        self.__threadName = threadName
        self.__delay = delay

    # 线程对象启动时自动调用的run()方法
    def run(self):
        print("[启动]>>> {0}:开启线程...".format(self.__threadName))
        #获取锁用于线程同步
        threadLock.acquire() 
        print('>>>> {0}锁定同步....'.format(self.__threadName))
        print_time(self.__threadName,self.__delay)
        #释放锁，开启下一个线程
        threadLock.release()
        print('>>>> {0}释放锁....'.format(self.__threadName))
        pass

# 脚本入口
if __name__ == '__main__':
    print("[启动]>>> mainThread主线程启动....")
    #创建新线程
    thread1 = Mythread("Thread-1", 4)
    thread2 = Mythread("Thread-2", 6)

    #开启新线程
    thread1.start()
    thread2.start()

    #添加新线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    #等待所有线程完成
    for t in threads:
        t.join()

    print("[停止]>>> mainThread主线程停止....\a")