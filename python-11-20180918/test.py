"""
字符串 -- 时间对象 time.strptime(字符串,"%Y-%m-%d %H:%M:%S")
字符串 -- 时间戳 time.mktime(time.strptime(字符串,"%Y-%m-%d %H:%M:%S"))
时间对象 -- 字符串 time.strftime("%Y-%m-%d %H:%M:%S",时间对象)
时间对象 -- 时间戳 time.mktime(时间对象)
时间戳 -- 字符串  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(时间戳))
时间戳 -- 时间对象 time.localtime(时间戳)
"""
"""时间模块"""
import time

"""time.time打印时间戳，从1970开始"""
# print(time.time())

"""time.localtime打印本地结构化时间"""
# print(time.localtime())

"""time.gmtime打印格林尼治机构化时间"""
# print(time.gmtime())

"""time.mktime将结构化时间转换成时间戳"""
# res = time.gmtime()
# print(res)
# res1 = time.mktime(res)
# print(res1)
"""time.ctime打印英式时间"""
# res = time.ctime()
# print(res)
"""time.strftime()格式化打印中文时间,将时间转换成字符串"""
# res = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# print(res,type(res))
"""time.strptime()格式化时间，将字符串转换成时间"""
# var = time.strptime(res,"%Y-%m-%d %X")
# print(var,type(var))
"""time.sleep()设置睡眠时间"""
# print(res)
# time.sleep(5)
# print(res)
"""time.clock返回cpu时间，从程序第一次运行clock"""
# res = time.clock()
# print(res)


"""异常处理"""
"""
try:
    可能发生错误的语句
except 异常类型：
    如果发生异常，执行此处语句
"""
# num = int(input("请输入一个数字"))
# try:
#     print(1/num)
# except ZeroDivisionError as E:
#     print(E)
#     print("除数不能为0")

# L = [1,2,3,4]
# try:
#     print(L[4])
# except IndexError as E:
#     print(E)
"""
try：
    有可能发生错误的语句
except 异常类型 as E：
    发生异常则执行该语句
else:
    没有发生异常则执行该语句
"""
# try:
#     print(1/0)
# except Exception as E:
#     print(E)
# else:
#     print("没错误")

"""
try:
    有可能出现错误的语句
except Exception as E:
    发生错误执行的语句
finally:
    不管错误或者正确都会执行该语句
"""
# try:
#     print(1/0)
# except Exception as E:
#     print(E)
# finally:
#     print("到底是正确还是错误？")


"""Exception 或者BaseException  来匹配except中的错误"""

# def func1(num):
#     print(1/num)
# def func2(num):
#     func1(num)
# def func3():
#     func2(0)
# try:
#     func3()   #主函数设置为可能错误项，将包含所有函数
# except Exception as E:
#     print(E)


"""装饰器"""
"""在不改变原函数的情况下，给函数拓展一个新功能"""

"""一般装饰器"""
# def outer(fn):  #fn = func
#     def inner():
#         start = time.time()
#         fn()
#         overtime = time.time() - start
#         print(overtime)
#     return inner
# @outer
# def func():
#     for i in range(9999999):
#         pass
#     print("hello")
# func()  #func = inner
#####
"""带参数的装饰器"""
