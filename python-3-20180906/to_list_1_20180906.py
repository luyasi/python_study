"""10.list 列表的转换"""
"""
1.init 、float、complex、bool都不能转换，该类数据不能迭代
2.string 可以做转换，把字符串中每一个字符当做元素添加到列表
3.tuple  可以转换，直接将小括号变成中括号
4.set    可以转换，直接将大括号变成中括号
5.dict   可以转换，只能转换字典的键，不能转换值。
"""
# var = 1
# var1 = list(var)
# print(var1,type(var1))
# var = 1.3
# var1 = list(var)
# print(var1)
# var = 0j
# var1 = list(var)
# print(var1,type(var1))
# var = True
# var1 = list(var)
# print(var1)
# str1 = "开开心心"
# var = list(str1)
# print(var,type(var))
# var1 = var[1]
# print(var1,type(var1))
# tuple1 = (1,2,3,4)
# var = list(tuple1)
# print(var,type(var))
# var = {1,2,3,4,4,5}
# var1 = list(var)
# print(var1,type(var1))
# var = {"a":1,"b":2,"c":3}
# val = list(var)
# print(val,type(val))
