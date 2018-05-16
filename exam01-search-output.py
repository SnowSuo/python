#-*-  coding:utf-8 -*-
'''
    exam01-search-output.py 
    =============================
   实现指定文件夹中所有文件信息检索遍历并保存到files.log日志文件中
    @copyright：Chinasoft international .ETC
    @author：suoyonggang
    @date：2018-05-15

'''
#导入模块
import os
import time
#定义一个文件工具类用于文件检索
class FileTools():
    #类实现方法创建
    #使用os.walk（）实现对指定文件深度遍历
    def Dirpath(filepath):
        for root,dirs,files in os.walk(filepath):
            print('|-文件路径：{0}'.format(root))#获取文件夹中的所有目录及子目录
            print('| |-路径下的文件夹：%s'%dirs)#当前文件夹中的子文件夹
            print('| | |-文件夹中的文件：%s'%files)#当前子文件夹中的文件名称
            pass
# 日志文件信息类
class LogTools():
    # 定义一个写入日志文件的方法
    def scanDisk(self, filepath, logName):
        fileDir = os.path.join(os.getcwd(), '.vscode\homework')
        # 获取文件夹信息并写入日志文件
        with open(fileDir + os.sep + logName, 'a', encoding='utf8') as fp:
            # 使用os.walk()函数
            for root, dirs, files in os.walk(filepath):
                fp.write('<{0}>\n'.format(time.strftime('%y-%m-%d %H:%M:%S', time.localtime())))
                fp.write('文件夹路径: %s\n' % root)   # 获取文件夹中的所有目录及子目录名称
                fp.write('路径下的文件夹: {0}\n'.format(dirs))  # 获取当前文件夹中的子文件夹名称
                fp.write('文件夹中的文件: {0}\n'.format(files))  # 获取当前子文件夹中的文件名称
                pass

##脚本程序入口
if __name__=='__main__':
    filepath=input('输入指定文件路径：>-')
    FileTools.Dirpath(filepath)
    tools = LogTools()
    tools.scanDisk(filepath, 'logging.log')
    print('日志写入完毕')
