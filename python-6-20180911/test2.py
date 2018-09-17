""""""
"""函数"""
"""
def 函数名(形参1，形参2，形参3...形参n):
    功能
    retrun 表达式
def : 定义函数的关键字
函数名 : 定义的函数的名字,函数名要遵循变量的命名规则
():定义函数的时候,括号内的参数叫做形参，每个形参要用逗号分隔开,形参的值是从函数的调用者那里获得，初学阶段可以把形参理解为就是一个变量
功能:我们这个函数的作用
return:返回值,返回值可以有，也可以没有,如果没有，默认返回一个None，return之后代表着你的函数结束，return下边不能再有其它功能
表达式:要返回给函数调用者的信息
函数执行:函数名()
"""
# def mu99(m):

#     i = 1
#     while i < m+1:
#         j = 1
#         while j <= i:
#             print("%sx%s=%2d"%(i,j,i*j),end=" ")
#             j += 1
#         print()
#         i += 1
#
# mu99(8)

# def name(firstname,lastname):
#     fullname = firstname + lastname
#     print(fullname)
#     return fullname
#
#
# val = name("hello","world")
# print(val)

"""局部变量和全局变量"""
"""
全局变量：顶格写的变量是全局变量，在任何地方都可以使用
局部变量：在代码组中定义的变量，局部变量正常下只能在局部使用。
"""
# A = "我是全局变量"
# # def name():
# #     global B
# #     B = "我是局部变量"
# #     print(A)
# #     print(B)
# # name()
# # print(A)
# # print(B)

"""不定长参数"""
# def operation(a,b,c,d,e):
#     sum1 = a + b + c + d + e
#     return sum1
# res = operation(1,2,3,4,5)
# print(res)

# *垃圾回收站 不能接收关键字参数，带*的参数要放在形参的最后边
# def operation(*args):
#     sum1 = 0
#     for val in args:
#         sum1 += val
#     return sum1
#
# res = operation(1,2,3,4,5,6,7,8,9,10)
# print(res)
# a = *args
# b = **kwargs
# *args 是元组数据类型
# **kwargs 是字典数据类型

# def op(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# op(1,2,3,4,"a",{"a" : 1,"A" : "lys"})

"""闭包"""
"""
内部函数调用外部函数变量（非全局变量）则称内部函数为闭包
调用一个函数，返回一个新的函数，返回的函数就叫做闭包
"""
# def outer(num1):
#     def inner(num2):
#         return num1 + num2
#     return inner
# res  = outer(20)
# result =res(10)
# print(result)

"""
闭包函数引用外部局部变量的前提，闭包内未定义
"""
# def outer():
#     a = [1]
#     def inner():
#         a[0] = a[0] + 1
#         return a[0]
#     return  inner
# res = outer()
# result = res()
# print(result)

"""字符串切片"""
# for val in range(1,100):
#     print(val)
# var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#
# print(var[25:31])
# print(var[70:83:3])
# print(var[90:84:-1])
# print(var[99:73:-5])
# print(var[-10:-30:-2])
# print(var[150:200])  #超出范围的取值为空

# import pprint
# pprint.pprint( [i for i in dir(str) if not i.startswith("__")])
# str1 = "i love lys"
# str2 = "really"
# print(dir(str1))  #查看字符串处理函数
# print(str1.capitalize())  #capitalize 字符串首字母大写
# print(str1.upper())       #upper 字符串所有字母大写
# print(str1.lower())       #lower 字符串所有字母小写
# print(str1.swapcase())    #swapcase  字符串所有字母大小写互换
# print(len(str1))          #len(str)    计算字符串长度
# print(str1.count("l"))    #count(" ") 统计字符串中指定字符出现的次数，严格区分大小写
# print(str1.find("l",3,7)) #find("str")计算字符串第一次出现的位置
# print(str1.startswith("l",7)) #startwith() 确认字符串是否以指定字符开头
# print(str1.endswith("I",1,4)) #endswith() 确认字符串是否以指定字符结尾
# print(str1.isupper())      #isupper()  确认字符串是否都是大写
# print(str1.islower())      #islower()  确认字符串是否都是小写
# print(str1.isalnum())     #isalnum()  确认字符串是否是数字、字母、汉字组成
# print(str1.isalpha())     #isalpha()  确认字符串是否是字母和文字组成
# print(str1.isdigit())     #isdigit()  确认字符串是否是十进制数字组成
# print(str1.isnumeric())   #isnumeric() 确认字符串是否是由数字组成
# print(str1.isdecimal())   #isdecimal()  确认字符串是否由数值组成的字符串
# print(str1.isspace())     #isspace() 确认字符串是否是空格组成
# print(str1.istitle())     #istitle() 确认字符串每个元素是否是大写开头
# print(str1.split("l"))    #split()  按照指定字符切割字符串，默认按照空格切割
# print(str1.splitlines())  #splitlines() 按照换行符切割字符串
# print(str1.join(str2))
# print("~".join(str1))     #将str1作为指定符号拼接到str2
# str3 = "我 的 名字 叫 陆雅斯"
# list3 =(str3.split())
# print(" ".join(list3))
# str1 = "thtist"
# print(str1.zfill(5))     #zfile()默认使用0对字符串进行左填充
# print(str1.center(12,"#"))#center()指定字符填充字符串，字符串居中
# print(str1.ljust(10,"$")) #ljust()字符串居左填充
# print(str1.rjust(10,"$")) #rjust()字符串居右填充
# print(str1)
# print(str1.strip("t"))   #strip()去掉字符串两边的指定字符，默认去掉换行
# print(str1.lstrip("t")) #lstrip()去掉字符串左边的指定字符
# print(str1.rstrip("t"))#rstrip()去掉字符串右边的指定字符
# str1 = "this is a testtttt"
# str2 = str1.maketrans("t","y")
# print(str2)
# str3 = str1.translate(str2)
# print(str3)          #maketrans("查找字符"，"替换字符") 制作字符串替换的映射表  translate()进行字符串替换
# str2 = str1.replace("t","y",4)
# print(str2)           #replace("旧值","新值","被替换的个数")
