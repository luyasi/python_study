# L = ["2","4","6","7"]
#
# var = list(map(int,L))
# print(var)
#
# def red(n,m):
#     val = n*10 + m
#     return val
#
from functools import reduce
# value = reduce(red,var)
# print(value)

# L =["JaCk","LoseR","jEEry","pYthOn"]
#
#
# def str1(i):
#     i = i.lower()
#     i = i.capitalize()
#     return i
#
#
# var = list(map(str1, L))
# print(var)

# var = "1ab2cde456f8"
#
# val = [n for n in var if n.isdigit() ]
# def add(x,y):
#     return  x + y
# valu = int(reduce(add,val))
# print(valu,type(valu))

# print(val)
# def digtr(var):
# list1 = []
# for i in var:
#    if i.isdigit():
#         # return i
#         list1.append(i)
# print(list1)
# def red(n,m):
#         val = n*10 + m
#         return val

# valu = list(map(digtr,var))
# valw = reduce(red,valu)
# print(valw)

# L = [4,2,5,3,6,1]
# # L.sort()
# # print(L)
# #
# # K = sorted(L)
# # print(K)

# k = "lyshelLo"
# print(k.title())
#
# L= ["1","ad3","c2","h2o",["co2","k2mno4",1,"na2"],34]
# # 13222242
# list1 = []


# L = ["1","2","5","3","4","7","9","8"]
# L1 = list(map(int,L))
#
# def func(boo):
#     if boo % 2 == 0:
#         return True
#     else:
#         return False
#
# res =filter(func,L1)
# res1 = sorted(res,reverse=True)
# func2 = lambda x,y:x*10+y
# res3 = reduce(func2,res1)
# print(res3)
#
# def func(boo):
#     if boo % 2 == 1:
#         return True
#     else:
#         return False
#
# res4 =filter(func,L1)
# res5 = sorted(res4,reverse=False)
# res6 =  reduce(func2,res5)
# print(res6)

# 43211234
# def func(n):
#     if n == 1:
#         return 4
#     else:
#         return abs(func(n-1)-1)
# val = func(6)
# print(val)
# li = [1,2,3,4,5,6,7,8,8]
# li2 = []
# li3 = []
# for x in li:
#     for y in li:
#         if x != y:
#             A = "%s%s"%(x,y)
#             li2.append(A)
# # print(li2.count())
# print(len(set(li2)))
# li2 = []
# li3 = []
# for i in li:
#     for x in li:
#         if i != x:
#             a = "%d%d" % (i,x)
#             li2.append(a)
# for y in li2:
#     if y not in li3:
#         li3.append(y)
# print(li3)
# print(len(li3))
