#-*- coding:utf-8 -*-
'''
    exam02-bbs-posts.py
    ------------------------
    论坛发帖显示功能实现

    @Copyright: Chinasoft International · ETC
    @Author: suoyonggang
    @Date: 2018-05-15
'''

# 导入模块
import os
import pymysql

def addPosts(sql):
    # 设置全局连接对象
    connection = ''
    try:
        # 步骤1：获取一个有效的数据库连接引用对象
        connection = pymysql.connect(host='localhost', port=3306, \
                                    user='root', password='123', \
                                    db='bbs', charset='utf8')
        print('>> 数据库连接成功.')
        # 步骤2：获取一个游标对象
        cursor = connection.cursor()
        print('>> SQL: %s' %(sql))
        # 步骤4：执行SQL语句
        affectedRows = cursor.execute(sql)
        print('>> SQL语句执行正常,操作影响%d行.' %affectedRows)
        # 步骤5：事务提交
        connection.commit()
        print('>> 事务提交成功.')
        return affectedRows
    except:
        # 事务回滚
        connection.rollback()
        print('>> SQL执行异常，事务回滚……')
        return -1
    finally:
        # 步骤6：关闭数据库连接引用对象
        connection.close()
        print('>> 关闭数据库连接.')

def showPosts(sql):
    # 设置全局连接对象
    connection = ''
    try:
        # 步骤1：获取一个有效的数据库连接引用对象
        connection = pymysql.connect(host='localhost', port=3306, \
                                    user='root', password='123', \
                                    db='bbs', charset='utf8')                         
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
#定义函数添加用户数据
#def addPosts():
# 脚本程序入口
if __name__ == '__main__':
    while True:
        # 显示信息
        os.system('cls')
        print('#' * 30)
        print('论坛发帖内容录入')
        print('#' * 30, '\n')
        
        # 接收用户输入的数据
        title = input('帖子标题:> ')
        publish= input('发帖时间:> ')
        author = input('发帖作者:> ')
        context = input('帖子内容:> ')   
        # SQL语句编写
        sql = 'insert into posts values(null, \'%s\', \'%s\', \'%s\', \'%s\')' \
              %(title,publish,author,context)
        # 数据添加
        affectedRows = addPosts(sql)
        # 响应操作结果
        msg = '\n消息: OK.记录添加成功.\a' if affectedRows>0 else '\n消息: Error.记录添加失败.\a'
        print('\n',msg)

        # 提示用户是否继续输入
        choice = input('是否继续(y/n)? ')
        if choice.lower() == 'n':
            break
        pass  
     # 查询数据库显示最终的结果
    sql = 'select * from posts'
    # 调用showPosts()函数实现数据库的查询
    result = showPosts(sql)
    print('\n 当前帖子全部内容：')
    # 循环遍历输出
    for item in result:
        print(item[0], item[1], item[2], item[3])
    print('>> 系统退出.')


