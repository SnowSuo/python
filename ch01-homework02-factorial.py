#-*-  coding:utf-8 -*-
'''
    ch01-homeworko2-factortial.py
    =============================
   递归实现阶乘

    @copyright：Chinasoft international .ETC
    @author：suoyonggang
    @date：2018-05-03

'''
def factortial(n):
    if n==1:
        return 1
    return n*factortial(n-1)
res=factortial(6)
print(res)