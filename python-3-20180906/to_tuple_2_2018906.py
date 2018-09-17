"""12.元组的转换"""
"""
所有的数字类型都不能转换为元组类型，所有的容器类型都可以转换为元组，字典类型只会转换键。
"""
# var = 1
# var1 = tuple(var)
# print(var1,type(var1))
# var = 11.5
# var1 = tuple(var)
# print(var1,type(var1))
# var = 0j
# var1 = tuple(var)
# print(var1)
# var = True
# var1 = tuple(var)
# print(var1,type(var1))
# list1 = [1,2,3,4,"a"]
# var1 = tuple(list1)
# print(var1,type(var1))
# set1 = {1,2,3,4,"a",1}
# var1 = tuple(set1)
# print(var1,type(var1))
# dict1 = {"a":1,"b":2,"c":3}
# var1 = tuple(dict1)
# print(var1,type(var1)) #只会取到键，不会取到值~~~
str1 = "i love lys"
str2 = tuple(str1)
print(str2, type(str2))
