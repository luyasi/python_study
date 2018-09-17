"""sed 转换"""
"""
1.int、float、complex、bool 都不能转换。
2.str、list可以转换
3.dict 只能转换键
"""
# var = 1
# val = set(var)
# print(val,type(val))
# var = 0.1
# val = set(var)
# print(val,type(val))
# var = 1+0j
# val = set(var)
# print(val,type(val))
# var = True
# val = set(var)
# print(val,type(val))
# var = "hello world"
# val = set(var)
# print(val,type(val))  #字符串变成无序的
# var = [1,2,3,4,"a",1,2,3,4,5,"b"]
# val = set(var)
# print(val,type(val))
# var = {"a":1,"b":2,"c":3}
# val = set(var)
# print(val,type(val))

"""dict转换"""
"""
1.int、float、complex、bool 都不能转换
2.其他数据类型按照格式进行转换
3.空字符串可以转换
"""
# var = 1
# val = dict(var)
# print(val,type(val))
# var = 1.1
# val = dict(var)
# print(val,type(val))
# var = 0j
# val = dict(var)
# print(val,type(val))
# var = True
# val = dict(var)
# print(val,type(val))
# var = "i:0 love:1 lys:2"
# val = dict(var)
# print(val,type(val))
# var = [(1,2),(3,4)]
# val = dict(var)
# print(val,type(val))
# var1 = val[1]
# print(var1,type(var1))
# var = {(1,2),(3,4),(5,6)}
# val = dict(var)
# print(val,type(val))
# var = ""
# val = dict(var)
# print(val,type(val))

"""算数运算符"""
"""
+  加法
-  减法
*  乘法
/  除法
%  取余
// 取整
** 幂运算
"""
# var = 8
# val = 5
# print(var + val)
# print(var - val)
# print(var*val)
# print(var/val)
# print(var%val)
# print(var//val)
# print(val**2)
# 1!=2

"""关系比较运算符"""
"""
>  大于
>= 大于等于
<  小于
<= 小于等于
!= 不等于
=  赋值
== 等于
"""
# num1 = 5
# num2 = 5
# print(num1 > num2)
# print(num1>=num2)
# print(num1!=num2)
# print(num1<=num2)

"""赋值运算"""
"""
= 赋值
+= ,-=,*=,/*,%=,//=,**=
"""
# val = 2
# # val = var +1
# val **=2
# print(val)

"""逻辑运算"""
"""
and     逻辑与运算，有假则假
or      逻辑或运算，有真则真
not     逻辑非运算，真变假，假变真
xor     逻辑异或运算,相同取假，不同取真
"""
# var = False
# val = False
# res = var and val
# print(res)
# var = True
# val = False
# res = not var
# print(res)
# var = True
# val = True
# res = var ^ val
# print(res)

"""成员运算"""
"""
in , not in  在/不在容器
"""
# var = "hello python"
# val = "de"
# res = val in var
# print(res)

# var = {"a":1,"b":2,"c":3,"1":2}
# val = "1"
# print(val in var)

"""自身检查"""
"""
is/is not  是/不是
"""
# var = "lys"
# val = "lys"
# print(var is  not val)

"""按位运算"""
"""
& 按位与运算
| 按位或运算
^ 按位异或运算
~ 按位取反运算
<< 按位左移
>> 按位右移
"""

"""流程控制语句"""
"""
1.流程分类：顺序结构、分支结构、循环结构
2.分支结构包括：单向分支、双向分支、多向分支、巢状分支
"""
"""单向分支
if 条件语句:
    功能1 
    功能2
    功能3
    ...
"""
# name = "admin"
# if name == "admin":
#     print("welcome admin")

"""双向分支
if 条件语句:
    功能1
else:
    功能2
如果条件1为真，执行功能1
如果条件1为假，执行功能2
"""
# username = input("please input your name:")
# if username == "admin":
#     print("welcome admin")
# else:
#     print("who you are?")

"""多向分支
if   条件1:
         功能1
elif 条件2:
         功能2
else:
         功能3
如果条件1为真，执行功能1
如果条件1为假，向下执行
如果条件2为真，执行功能2
如果条件2为假，向下执行
所有条件都是假，执行功能3
"""

"""彩票购买"""
import random

# lucknumber = random.randint(10, 99)
# lucknumber_s = lucknumber // 10
# lucknumber_g = lucknumber % 10
# num = int(input("please input you chose:"))
# num_s = num // 10
# num_g = num % 10
# if num == lucknumber:
#     print("luck!one")
# elif num_s == lucknumber_g and num_g == lucknumber_s:
#     print("luck!two")
# elif num_s == lucknumber_s or num_g == lucknumber_g or num_s == lucknumber_g or num_g == lucknumber_s:
#     print("luck!three")
# else:
#     print("badluck!")

"""巢状分支
if 条件1:
    if 条件2:
        功能1
    else:
        功能2
else:
        功能3
如果条件1和条件2为真，执行功能1，
    条件1真、条件2为假，执行功能2，
    条件1假、不执行条件2，执行功能3
"""
height = int(input("请输入你的升高："))
if height >= 180:
    money = int(input("请输入的收入："))
    if money >= 10000000:
        print("高富帅！")
    else:
        print("高穷丑")
else:
    print("矮穷矬")
