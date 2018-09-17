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
