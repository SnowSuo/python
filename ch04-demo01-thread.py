#-*- coding:utf-8 -*-
'''
    ch04-demo01-thread.py
    ------------------------
    _thread多线程演示

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

# 导入_thread模块
import _thread
import time

'''
    @name: workThread
    @args: str
    @return none
    @date: 2018-04-25
'''
# 自定义一个函数
def workThread(threadName, delay):
    print('[启动]>>> {0}....'.format(threadName))
    counter= 0 # 计数器
    for i in range(delay):
        print('   |- {0}正在执行中....{1}'.format(threadName, counter))
        counter += 1 # 计数器自增1
        time.sleep(1) # 函数执行中断1秒(线程挂起1秒)
    print('[停止]>>> {0}....\a'.format(threadName))

# main程序入口
if __name__ == '__main__':
    print('>>>> 主线程mainThread启动....')
    # 将两个函数放入子线程中并启动
    _thread.start_new_thread(workThread, ('Thread-1', 3,))
    _thread.start_new_thread(workThread, ('Thread-2', 5,))    
    # 控制主线程的执行时间
    for i in range(4):
        print('mainThread正在执行.....')
        time.sleep(1)
    print('>>>> 主线程mainThread停止.\a')