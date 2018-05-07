#-*- coding:utf-8 -*-
'''
    ch03-homework.rentinghouse.py
    ------------------------
    实现录入出租屋信息
    实现在出租房屋查询检索。
    实现 查询并显示全部出租房屋信息
    实现 按照价格区间进行查询显示（输入价格范围）选做
    实现所有房屋的租金 rhprice 字段全部提升10%。

    @Copyright: Chinasoft International · ETC
    @Author: suoyonggang
    @Date: 2018-05-07
'''

import pymysql
import os

#设置链接参数
dbserverIp='localhost'
user='root'
password='123'
dbname='houserentals'
print('数据库参数写入完毕')

def dbExecuteSQL(sql):
    #使用connect（）函数获取一个有效的数据库链接对象
    connection=pymysql.connect(host=dbserverIp,port=3306,user=user,password=password,db=dbname,charset='utf8')
    print(type(connection))
    if connection:
        print('>>数据库链接成功')
    else:
        print('>>数据库链接失败')
    #创建一个游标对象affectrow
    cusor =connection.cursor()
    print('游标对象创建成功')
    #使用游标对象发送sql语句
    affectrow=cusor.execute(sql)
    #提交事务
    connection.commit()
    print('>>事务提交')
    msg='OK,数据插入成功' if affectrow else '数据插入失败'
    print('>>%s'%msg)
    #关闭数据库
    connection.close()
    print('>>数据库链接关闭')

def dbQuerySQL(sql):
    try:
        # 步骤1：获取一个有效的数据库连接引用对象
        connection=pymysql.connect(host=dbserverIp,port=3306,user=user,password=password,db=dbname,charset='utf8')                     
        print('>> 数据库连接成功.')
        # 步骤2：获取一个游标对象
        cursor = connection.cursor()
        # 步骤3：执行SQL语句
        cursor.execute(sql)
        print('>> SQL: %s' %(sql))
        # 步骤4：使用fetchall()获取查询结果
        result = cursor.fetchall()
        # 返回结果
        return result
    except:
        return None
    finally:
        # 步骤6：关闭数据库连接引用对象
        connection.close()
        print('>> 关闭数据库连接.')
# 脚本程序入口
if __name__ == '__main__':
    while True:
        # 显示信息
        os.system('cls')
        print('-' * 30)
        print('出租屋信息录入')
        print('-' * 30, '\n')
        
        # 接收用户输入的数据
        rhaddress = input('房屋地址:> ')
        rharea = float(input('房屋面积:> '))
        rhfloor = int(input('房屋楼层:> '))
        rhprice = float(input('出租价格:> '))
        lessor_leid = int(input('租户编号:> '))
        
        # SQL语句编写
        sql = 'insert into rentinghouse values(null, \'%s\', %f, %d, %f, %d)' \
              %(rhaddress, rharea, rhfloor, rhprice,lessor_leid)
        # 数据添加，调用添加函数
        dbExecuteSQL(sql)
        # 提示用户是否继续输入
        choice = input('是否继续(y/n)? ')
        if choice.lower() == 'n':
            break
        pass
 
    # 查询数据库显示最终的结果
    sql = 'select * from rentinghouse'
    # 调用dbQuerySQL()函数实现数据库的查询
    result = dbQuerySQL(sql)
    print('\n 当前出租屋的全部信息：')
    # 循环遍历输出
    for item in result:
        print(item[0], item[1], item[2], item[3], item[4], item[5])
    print('>> 系统退出.')
    #执行更新操作，提升租金
    sql='update rentinghouse set rhprice=rhprice*1.1'
    # 调用dbQuerySQL()函数实现数据库的查询
    result = dbQuerySQL(sql)
    print('\n 当前出租屋的全部信息：')
    # 循环遍历输出
    for item in result:
        print(item[0], item[1], item[2], item[3], item[4], item[5])
    print('>> 系统退出.')
    #实现 按照价格区间进行查询显示（输入价格范围）
    sql='select * from rentinghouse where rhprice and rhprice>1000 and rhprice<2000'
    # 调用dbQuerySQL()函数实现数据库的查询
    result = dbQuerySQL(sql)
    print('\n 当前出租屋的全部信息：')
    # 循环遍历输出
    for item in result:
        print(item[0], item[1], item[2], item[3], item[4], item[5])
    print('>> 系统退出.')

