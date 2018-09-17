""""""
"""format格式化字符串"""
"""
format 通过{}和:来代替%
"""
# str1 = "{} say hello to {}"
# str2 = str1.format("jack","rose")
# print(str2)

# str1 = "{0[1]} say goodbye to {0[0]}"
# str2 = str1.format(["tom","jerry"])
# print(str2)

# 按照关键字来传参，是一般使用办法
# str1 = "{name1} say hello to {name2}"
# str2 = str1.format(name2="jack", name1="rose")
# print(str2)

"""format的填充功能"""
"""
^ 文本居中
< 文本左对齐
> 文本右对齐
"""
# str1 = "this"
# str2 = "{:@^10}".format(str1)
# print(str2)
# print("{:$<10}".format(str1))
# print("{:&>10}".format(str1))
# format填充的字符个数为总个数，包含原文本

"""format四舍五入功能"""
# print("{:.3f}".format(123.12395))
# print("{:.2f}".format(123.456))
"""format做千位分隔符"""
# print("{:,}".format(1000000))
# print("{:,}".format(10000000))
"""format做进制转换"""
# print("{:b}".format(18))  #{:b}转二进制
# print("{:d}".format(18))  #{:d}转十进制
# print("{:o}".format(18))  #{:o}转八进制
# print("{:x}".format(18))  #{:x}转十六进制

"""内建函数"""
"""locals打印环境中的所有变量"""
# str2 = "str1"
# print(locals())

"""数学运算相关"""
# a = [-5,-2]
# print(abs(a[0]))  #abs 取绝对值

# a = range(101)
# print(sum(a))     #sum  求和

# a = [-5,-2,2,5]
# print(max(a))     #max 求最大值
# print(min(a))     #min 求最小值

# print(pow(2,5,6)) #pow  求幂取余

# print(round(3.1495,2))   #round() 四舍五入

# res = range(10,1,-2)
# for i in res:
#     print(i)            #range(产生连续数据的序列)
# print(repr("he llo"))
# num1 = 1
# str1 = "num1+1"
# print(eval(str1))         #eval 将一个字符串当做python代码执行


"""list数据类型操作"""
"""list运算"""
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# print(list1 + list2)
# print(list1 * 4)
"""list切片"""
# list1 = ["hello","good","happy","great"]
# print(list1[2][0:2])
# print([list1[0][4:],list1[1][0:1]])
# print(list1[-1][-4:-1])

# val = "happy"
# print(val  not in list1)

# for i in list1:
# #     print(i)
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1
# print(len(list1))
# L = [[1,2],[4,5],[7,8,9]]
# for var,val,vas in L:
#     print(var,val,vas,type(var))
# for var in L:
#     print(var)
#     for val in var:
#         print(val)

"""列表的11中操作方法"""
"""append() 向列表末尾添加新的元素"""
# list1 = [1,2,3,4,5]
# val = list1.append([1,2])  #append只能添加单个元素
# print(list1)
"""insert()在指定位置之前添加元素"""
# list1 = [1,2,3,4,5]
# list1.insert(-1,3)
# list1.insert(2,3)
#
# print(list1)
"""extend()将一个列表继承另一个列表"""
# list1 = [1,2,3]
# list2 = [4,5,6,"hello"]
# list1.extend(list2) #将函数内的列表继承到另一个列表
# print(list1)
# print(list2)
"""pop()按照键值删除一个元素"""
# list1 = [1,2,3,4,5]
# print(list1.pop(1))
# print(list1)
"""remove()按照元素名删除指定元素"""
# list1 = [1,2,3,4,5,"ll","lys","ll"]
# print(list1.remove("ll")) #相同数据默认删除第一个，删除效率比pop低
# print(list1)
"""index()获取某个元素在列表中的索引"""
# list1 = [1,2,3,4,5,"hello",0,0,"hello"]
# print(list1.index("hello",6,))
"""count()计算某个元素出现的次数"""
# list1 = [1,2,3,4,5,"hello","hello",5]
# print(list1.count(5))
"""sort()对列表元素进行排序"""
# list1 = [1,3,4,6,2,5,8]
# list1.sort() #默认按照从小到大排序
# list1.sort(reverse=False)  #指定reverse = True 按照从大到小排序
# list.sort(key=,reverse=)   #key = 指定函数后在对列表进行排序
# print(list1)
"""reverse()列表反转操作"""
# list1 = [1,2,3,4,5]
# list1.reverse()
# print(list1)
"""clear()清空列表"""
# list1 = [1,2,3,4,5]
# list1.clear()
# print(list1)
"""copy()拷贝列表"""

"""列表推导式"""
# L = [1,2,3,4,5,6,7,8,9]
# L1 = []
# for var in L:
#     L1.append(var**2)
# print(L1)
#
# res = [var**2 for var in L]
# print(res)

# 求x,y组成的元组  x是0-10之间的偶数  y是0-10之间的奇数
# res = [(x,y) for x in range(10) if x%2 == 0 for y in range(10) if y%2 == 1]
# print(res)

# 求"ABC"和"123"组成两位字符串
# res = [x+y for x in "ABC" for y in "123"]
# print(res)

# M = [[1,2,3],[4,5,6],[7,8,9]]
# # res = [val for val in [M[0][0],M[1][0],M[2][0]]]
# # print(res)
# res = [var[0] for var in M]
# print(res)
# # 0,0
# # 1,1
# # 2,2
# res = [M[i][i] for i in range(len(M))]
# print(res)
# # res = [val[1] for var in (0,1,2) for val in M ]
# # print(res)

# L = ["contiune","else","if","break","pass","def"]
# val = [len(var) for var in L]
# print(val)

"""深浅拷贝"""
"""
copy.copy() 浅拷贝
copy.deepcopy() 深拷贝
"""
# import  copy
# a = [1,2,3,4,[5,6]]
# b = a
# print(b)
# a.append(7)
# print(a)
# print(b)
# c = copy.copy(a)
# d = copy.deepcopy(a)
# print(c)
# a[4].append(8)
# print(a)
# print(b)
# print(c)
# print(d)
