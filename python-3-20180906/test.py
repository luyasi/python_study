"""1.列表数据类型"""
# 一些列元素的顺序组合，标识符为[]，里面的每个元素使用逗号分开，创建之后可以随时修改。

# list1 = ["a","b","c","d","e"]
# print(list1,type(list1))
# var = list1[0]
# print(var,type(var))
# var1 = list1[-4]
# print(var1,type(var1))

# 列表取值：对应的列表[对应的索引]，索引分正向索引和反向索引

# list2 = ["a","b","c",[123,"lys",1+3j],True]
# print(list2,type(list2))
# var = list2[3][1]
# print(var,type(var))
# list2[3][1] = "i love lys"
# var1 = list2[3][1]
# print(var1)
# print(list2)

"""2.元组是一系列数据的顺序集合，标识符为逗号，初始化之后的数据不能做修改"""
# tuple1 = ("a", "b", "c", 1, 2, 2.3, ("d", "e"), [5, 6])
# print(tuple1, type(tuple1))
# var1 = tuple1[1]
# print(var1)
# var2 = tuple1[6]
# print(var2, type(var2))
# print(tuple1[6][1])
#
# 元组一旦被定义，数据将不能做修改
# tuple1[2] = "f"
# print(tuple1)
# a = ()
# print(a,type(a))
# b = ("d",)   #一个元素的元组，需要用标识符逗号标识
# print(b,type(b))
# c = (1,2)
# print(c,type(c))

"""3.集合数据类型，是一系列数据的无序组合，所有元素不会重合，无标识符"""
# set1 = {1,2,3,4,"a","b","c",3,1}
# print(set1,type(set1))
#
# set2 = set()
# print(set2,type(set2))

"""4.字典数据类型，是具有键值映射关系的无序数据组合，可以进行修改，标识符{}"""
# dict1 = {"及时雨":"萧敬腾","神捕":"张学友","花和尚":"鲁智深","九纹龙":"屎尽"}
# print(dict1,type(dict1))

# var1 = dict1["及时雨"]
# # print(var1,type(var1))
# # var2 = dict1["豹子头"]
# # print(var2)

# dict1["豹子头"] = "林冲"  #修改一个不存在的字典键值，相当于添加这个键值对。
# print(dict1)

# dict2 = {"韩寒":"三重门","四大名著":{"吴承恩":"西游记","曹雪芹":"红楼梦","施耐庵":"水浒传","罗贯中":"三国演义"}}
# print(dict2)
# var = dict2["四大名著"]["罗贯中"]
# print(var,type(var))


# 小试牛刀
# li=["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# print(li,type(li))
# var = li[2][1][1]
# print(var)
# print(li[3])

# tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
# tu[0]="ALEX"

# dict={'k1':"v1","k2":"v2","k3":[11,22,33]}
# dict["k1"] = "alex"
# print(dict)
# print(dict["k2"])

"""5.数据类型转换"""
# 1.自动转换  有程序自动朝着更加精准的方向转换。
# 2.手动转换  按照开发者的意志进行转换。

# 自动转换
# int1 = 1
# float1 = 1.5
# print(int1,type(int1))
# print(float1,type(float1))
# sum = int1+float1
# print(sum,type(sum))

"""6、int类型转换"""
# 1.float      可以转换，转换之后去掉小数位。
# 2.complex    不能转换。
# 3.bool       可以转换，转换之后true变1，flase变0
# 4.str        整数组成的字符串才能转化成init
# 5.list       不能转换
# 6.tuple      不能转换
# 7.sed        不能转换
# 8.dict       不能转换
# var = 1.2
# var1 = int(var)
# print(var1,type(var1))
# var = 1+2j
# var1 = int(var)
# print(var1,type(var1))
# var = True
# var1 = int(var)
# print(var1,type(var1))
# var = "hello lys"
# var1 = int(var)
# print(var1,type(var1))
# var = "111"
# var1 = int(var)
# print(var1,type(var1))
# list1 = [1,2,3,4,5]
# var = int(list1)
# print(var,type(var))
# tuple1 = (1,2,3,4,5)
# var = int(tuple1)
# print(var,type(var))
# set1 = {1,2,3,4,5}
# var = int(set1)
# print(var,type(var))
# dict1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
# var = int(dict1)
# print(var,type(var))


"""7.float 浮点型的转换"""
"""
1.init      可以转换，相当于在数值后面加.0
2.complex   不可以转换
3.bool      可以转换，true变为1.0，flase变为0.0
4.list      不能转换
5.tuple     不能转换
6.sed       不能转换
7.dict      不能转换
"""
# var = 1
# var1 = float(var)
# print(var1,type(var1))
# var = 1+0j
# var1 = float(var)
# print(var1,type(var1))
# var = True
# var1 = False
# val = float(var)
# val1 = float(var1)
# print(val,type(val))
# print(val1,type(val1))
# list1 = [1,2,3,4,5]
# var = float(list1)
# print(var,type(var))
# tuple1 = (1,2,3,4,5)
# var = float(tuple1)
# print(var,type(var))
# set1 = {1,2,3,4,}
# var = float(set1)
# print(var,type(var))
# dict1 = {"a":1,"b":2,"c":3}
# var = float(dict1)
# print(var,type(var))

"""8.complex  复数的转换"""
"""
1.int      可以转换，转换之后在末尾加0j
2.float    可以转换，转换之后在末尾加0j
3.bool     可以转换，转换之后True变1+0j False变0j
4.str      只有纯数字组成的字符串才能转换
5.list     不能转换
6.tuple    不能转换
7.set      不能转换
8.dict     不能转换
"""
# var = -22
# var1 = complex(var)
# print(var1,type(var1))
# var = 0.01
# var1 = complex(var)
# print(var1,type(var1))
# var1 = True
# var2 = False
# varl1 = complex(var1)
# varl2 = complex(var2)
# print(varl1,type(varl1))
# print(varl2,type(varl2))
# var = "222"
# var1 = complex(var)
# print(var1,type(var1))
# var = [1,2,3]
# var1 = complex(var)
# print(var1,type(val1))
# var = (1,2,3)
# var1 = complex(var)
# print(var1,type(var1))
# var = {1,2,3,4}
# var1 = complex(var)
# print(var1,type(var1))
# var = {"a":1,"b":2,"c":3}
# var1 = complex(var)
# print(var1,type(val))


"""9、bool值的转换"""
# bool值转换为True或者False
# 确定哪些可以转换为False
"""
1.init  0
2.float 0.0
3.string  ""    空字符串
4.complex   0j
5.list  []      空列表
6.tuple ()      空元组
7.dist  {}      空字典
8.set set()     空集合
"""
# var = 0
# var1 = bool(var)
# print(var1,type(var1))
# var = 0.00
# var1 = bool(var)
# print(var1,type(var1))
# var = ""
# var1 = bool(var)
# print(var1,type(var1))
# var = 0+0j
# var1 = bool(var)
# print(var1,type(var1))
# list1 = [ ]
# var1 = bool(list1)
# print(var1,type(var1))
# tuple1 = ()
# var1 = bool(tuple1)
# print(var1,type(var1))
# dict1 = {}
# var1 = bool(dict1)
# print(var1,type(var1))
# set1 = set()
# var1 = bool(set1)
# print(var1,type(var1))

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

"""11、字符串的转换"""
"""
所有的数据类型都可以转换成字符串，转换成字符串相当于在外围添加“”
"""
# var = 1
# var1 = str(var)
# print(var1,type(var1))
# var = 1.2
# var1 = str(var)
# print(var1,type(var1))
# var = True#Flase
# var1 = str(var)
# print(var1,type(var1))
# var = 1+0j
# var1 = str(1+0j)
# print(var1,type(var1))
# list1 = [1,2,3,4]
# var = str(list1)
# print(var,type(var))
# tuple1 = (1,2,3,4)
# var = str(tuple1)
# print(var,type(var))
# set1 = {1,2,3,4}
# var = str(set1)
# print(var,type(var))
# dict1 = {"a":1,"b":2,"c":3}
# var = str(dict1)
# print(var,type(var))

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
