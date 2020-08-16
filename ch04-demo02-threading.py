#-*- coding:utf-8 -*-
'''
    ch04-demo02-threading.py
    ------------------------
    threading多线程演示

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

#-*- coding:utf-8 -*-

# 线程类的创建

# 导入模块
import threading
import time

# 创建一个线程类
class MyThread(threading.Thread):

    # 构造方法
    def __init__(self, threadName, delay):
        # 重点：调用Thread父类的构造方法
        threading.Thread.__init__(self)
        # 创建实例变量(对象的属性)
        self.__threadName = threadName
        self.__delay = delay
        pass
    
    # 编写run()方法，该方法是当前线程类对象启动后会自动调用
    def run(self):
        print('[启动]>>> {0}启动运行....'.format(self.__threadName))
        counter = 0 # 计数器
        for i in range(self.__delay):
            print('  |- {0}:正在执行....{1}'.format(self.__threadName, counter))
            counter += 1 # 计数器自增1
            time.sleep(1)
            pass
        print('[停止]>>> {0}停止运行....\a'.format(self.__threadName))

# 脚本入口
if __name__ == '__main__':
    print('[启动]>>> mainThread主线程启动....')
    # 创建线程类对象
    thread01 = MyThread('Thread-1', 3)
    thread02 = MyThread('Thread-2', 5)
    # 启动线程
    thread01.start()
    thread02.start()
    # 模拟主线程的执行时间
    for i in range(10):
        print('mainThread主线程正在执行....')
        time.sleep(1)
        pass        
    print('[停止]>>> mainThread主线程停止....\a')