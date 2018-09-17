""""""
"""1.元组的操作"""
"""元组的遍历"""
# tuple1 = (1,2,3,4,5)
# for i in tuple1:
#     print(i**2)

# i = 0
# while i < len(tuple1):
#     print(tuple1[i])
#     i += 1

# tuple2 = ((1,2),(3,4),(6,7))
# for (i,j) in tuple2:
#         print(i,j)
# (a,b) = (1,2)

# tuple1 = (1,2,3,4,5,3,"hello")
"""tuple.index()按照元素返回元组的索引值"""
# print(tuple1.index(3,3))
"""tuple.count()统计元组元素出现的次数"""
# print(tuple1.count("hello"))


"""2.字典的操作"""
"""创建字典"""
# dict1 = {"a":1,"b":2,"c":3}
# print(dict1,type(dict1))

# dict1 = dict({"a":1,"b":2,"c":3})
# print(dict1,type(dict1))

# dict1 = dict([["a",1],["b",2]])
# print(dict1)

# dict1 = dict(a=1,b=2,c=3)
# print(dict1)

# dict1 = dict(zip([1,2,3,4],["l","y","s","k","w"]))
# print(dict1,type(dict1))

# dict1 = {"吴晓伟":"天海翼","郑帅":"饭岛爱","闫帆":"苍老师","邹奉明":"张瑞"}
# for key in dict1:   #字典默认遍历键值
#     print(key)

# for value in dict1.values():  #dict.values() 遍历字典值
#     print(value)

# for var in dict1.items():      #dict.items()  遍历字典键和值，返回元组类型
#     print(var,type(var))

"""字典的内置函数"""
"""clear清空字典"""
# dict1 = {"a":1,"b":2,"c":3,"d":4}
# dict1.clear()
# print(dict1,type(dict1))

"""copy复制字典"""
# dict2 = dict1.copy()   #浅拷贝
# print(dict2)

"""fromkeys使用指定的键创建字典"""
# ls1 = (1,2,3)
# ls2 = ("a","b","c")
# res = dict.fromkeys(ls1,ls2)
# print(res)
"""get()按照键值获取值"""
# print(dict1.get("e","bucunzaijianzhi"))
"""items()将字典的键值转换成元组"""
# print(dict1.items())
"""values()将字典的值组成一个序列"""
"""keys()将字典的键组成一个序列"""

"""pop()移除字典中指定的元素"""
# dict1 = {"a":1,"b":2,"c":3,"d":4}
# print(dict1.pop("f","不存在"))
# print(dict1)

"""popitem() 移除字典中的键值对,是随机删除"""
# print(dict1.popitem())
# print(dict1.popitem())
# print(dict1)
# dict1 = {"a":1,"b":2,"c":3,"d":4}

"""setdefault向字典中添加一个元素"""
# dict1 = {"a":1,"b":2,"c":3,"d":4}
# dict1.setdefault("e")
# print(dict1)
# setdefault 添加，键存在不做操作，键不存在则添加，不写值，默认是none
"""update修改字典中的值"""
# dict1.update(a=2)
# dict1.update({"a":1})
# dict1.update(e = 1)
# print(dict1)
# dict2 = {"d":5,"e":6}
# dict1.update(dict2)
# print(dict1)
# update() 修改字典中的值，键不存在则创建新的键值对


"""5.集合的操作"""
# set1 = {1,2,3,4,(4,5,6)}
# print(set1)
# print(dir(set1))
# for i in set1:
#     print(i)
"""add()向集合中添加一个元素"""
# set1.add(8)
# print(set1)

"""pop()向集合随机删除一个元素"""
# set1.pop()
# print(set1)
"""remove()删除集合中的某一个元素"""
# set1.remove(2)
# print(set1)
"""discard()删除集合中的某个元素"""
# set1.discard(7)
# print(set1)
"""clear()清空集合"""
# set1 = {1,2,3,4,(4,5,6)}
# set1.clear()
# print(set1)
"""copy()复制集合"""
# set1.add(7)
# set2 = set1.copy()
# set1.add({"a":1})
# print(set2)

"""difference()差集"""
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
z = {3, 4}
l = {7, 8}
# print(x.difference(y))  #x对y的差集
# print(y.difference(x))  #y对x的差集
# x.difference_update(y)   #将差值赋值给x
# print(x)
# print(y)
"""intersection()交集"""
# print(x.intersection(y)) #x和y的交集
# x.intersection_update(y) #将交集赋值给x
# print(x)
# print(y)
"""union()并集"""
# print(x.union(y))   #x和y的并集
# x.update(y)        #将并集赋值给x
# print(x)
# print(y)
"""issuperset()检测一个集合是否是另一个集合的超集"""
# print(x.issuperset(z))
"""issubset()检测一个集合是否是另一个集合的子集"""
# print(z.issubset(y))
"""isdisjoint()检测两个集合是否不相交"""
# print(x.isdisjoint(l))
"""symmetric_difference()对称差集操作"""
# print(x.symmetric_difference(y)) #去交集后
# x.symmetric_difference_update(y) #对称差集赋值给x
# print(x)
# print(y)

"""frozenset()冰冻集合"""
# s = frozenset({1,2,3,4})
# print(s,type(s))


"""4.文件操作"""

"""open("path","method")"""
"""path 路径，window系统上使用双斜杠"""
"""method 打开权限
w：写  a：追加  r：读取
w+：读写 覆盖以前内容
r+：读写 不能创建新文件
a+：可以创建新文件，不会覆盖
wb：二进制写
rb：二进制读
ab：二进制追加
"""
# file_test = open("C:\\Users\\陆雅思\\Desktop\\test.txt","r",encoding="utf-8")
# file_test.write("好好学习 天天向上 白天黑夜")
# file_test.seek(0,0)
# print(file_test.read())
# file_test.close()

"""read()读取全文，readline()读取光标后的一行，readlines()将内容转换成列表读取"""
# f = ，open("C:\\Users\\陆雅思\\Desktop\\test.txt","r",encoding="utf-8")
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("user.txt","wb")
# f.write("这是一个测试".encode("gbk"))
# f.flush()
# # f.read().decode('utf-8')
# f.close()
#
# l = open("user.txt","rb")
# var = l.read().decode("gbk")
# print(var)
# l.close()

# 刷新缓冲区的方式
# 1、缓冲区被占满了
# 2、关闭文件的时候自动刷新
# 3、程序运行结束
# 4、手动刷新缓冲区  flush()

# with语法，不用手动关闭文件，执行结束，自动关闭文件
# with open("user.txt","w",encoding="utf-8") as f:
#     f.write("这是一个测试")


"""pikcle模块"""
"""
dump
load
dumps
loads
"""
import pickle

# L = [1,2,3,4,5]
# res = pickle.dumps(L)
# print(res)
# con = pickle.loads(res)
# print(con)

# with open("test.txt","wb") as file_name:
#     str = "这是一个测试"
#     pickle.dump(str,file_name)

# with open("test.txt","rb") as file_name:
#     res = pickle.load(file_name)
#     print(res)
