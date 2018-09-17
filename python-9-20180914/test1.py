""""""
"""OS模块"""
import os

"""os.name输出字符串指示正在使用的平台，window是nt，linux是posix"""
# print(os.name)
"""os.getcwd获取当前的工作目录"""
# print(os.getcwd())
"""os.listdir获取目录下所有的目录和文件，并不区分类型"""
# print(os.listdir("D:/python学习/代码"))
"""os.mkdir创建文件夹,不能递归创建目录"""
# os.mkdir("../python-10/python-11/python-12")
"""os.makedirs递归创建目录"""
# os.makedirs("../python-10/python-11/python-12")
"""os.rmdir删除空目录"""
# os.rmdir("../python-10/python-11/python-12")
"""os.remove删除文件"""
# os.remove("../username")
"""os.system执行shell命令"""
# os.system("ping www.baidu.com")
"""os.chdir改变当前路径"""
# print(os.getcwd())
# os.chdir("../python-10")
# print(os.getcwd())
"""os.rename更改文件名"""
# os.chdir("../python-10/python-11")
# os.rename("username","username1")
"""os.walk返回三个值（dirpath,dirnames,filenames）"""
# result = os.walk("../")
# for dirpath,dirnames,filenames in result:
#         print(dirpath)
"""os.path.abspath返回文件的绝对路径，非真实的绝对路径，为补全路径"""
# print(os.path.abspath("username1"))
# print(os.getcwd())
"""os.path.split返回分割的文件名，返回一个元组"""
# print(os.path.split("D:/python学习/代码/python-10/python-11/username1"))
"""os.path.exists判断路径是否存在，目录和文件都可以判断"""
# print(os.path.exists("D:/python学习/代码/python-10/python-11/"))
"""os.path.join连接文件目录"""
# print(os.path.join("D:/python学习/代码/python-10/python-11","username1"))
"""os.path.isdir判断路径是否是一个目录"""
# print(os.path.isdir("D:/python学习/代码/python-10/python-11/username1"))
"""os.path.isfile判断路径是否是一个文件"""
# print(os.path.isfile("D:/python学习/代码/python-10/python-11/"))
"""os.path.getsize返回文件大小,返回文件字节"""
# print(os.path.getsize("D:/python学习/代码/python-9-20180914/test.py"))

"""递归"""
# 计算5*4*3*2*1
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return func(n-1) * n
#
# res = func(10)
# print(res)

# 斐波拉切数列
# 1,1,2,3,5,8,13,21,34...n?
# def func(n):
#     if n == 1 or n == 2:
#         return  1
#     else:
#         return func(n-1) + func(n-2)
#
# print(func(10))

# 汉诺塔
# n,x,y,z
# def func(n,x,y,z):
#     if n == 1:
#         print(x,"到",z)
#     else:
#         func(n-1,x,z,y)
#         print(x,"到",z)
#         func(n-1,y,x,z)
#
# var = func(9,"x","y","z")
# print(var)
