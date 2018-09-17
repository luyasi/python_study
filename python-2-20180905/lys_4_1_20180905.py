# python变量介绍
# python中给变量赋值是用=，==是做条件判断使用
# a = "hello world"
# print(a)
# print("a")

# python变量的命名方式和要求
# 1.python3中支持中文命名变量，但是不建议使用；
# 2.只能以数字、字母、下划线命名变量；
# 3.数字不能作为命名开头；
# 4.下划线开头的变量有特殊意义；
# 5.python严格区分大小写；
# 6.变量命名要具有描述性；
# 7.变量命名不能和关键字和内部函数冲突。

# 帅="python"
# print(帅)

# a @ 1 = "python"
# print(a @ 1)

# 1a="python"
# print(1a)

# __a="python"
# print(__a)

# name="tom"
# Name="jack"
# print(name)
# print(Name)

# python中使用id(0)查看变量值的内存地址
# age1 = age2 = age3 = -1000
# print(age1, id(age1))
# print(age2, id(age2))
# print(age3, id(age3))
#
# age4 = -5.1
# age5 = -5.1
# age6 = -5.1
# print(age4, id(age4))
# print(age5, id(age5))
# print(age6, id(age6))

# name,age,sex="yasi",18,"man"
# print(name,age,sex)

# python中*前加变量表是未知变量，当作是一个垃圾站
a, b, *c = 1, 2, 3, 4, 5, 6, 7
print(a, b, c)
