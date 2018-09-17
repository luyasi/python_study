"""输出100次语句"""
# i = 0
# while i < 100:
#         i += 1
#         print("hello world:",i)

# for i in range(1,101):
#     print("hello world:",i)

"""while循环猜彩票"""
# import  random
# lucknum = random.randint(10,99)
# lucknum_s = lucknum // 10
# lucknum_g = lucknum % 10
# while True:
#     print("输入-1结束抽奖！")
#     inputnum = int(input("please input your lucknum:"))
#     inputnum_s = inputnum // 10
#     inputnum_g = inputnum % 10
#     if inputnum == -1:
#         break
#     elif inputnum == lucknum:
#         print("one")
#         break
#     elif inputnum_s == lucknum_g and inputnum_g == lucknum_s:
#         print("two")
#         break
#     elif inputnum_s == lucknum_s or inputnum_g == lucknum_g or inputnum_s == lucknum_g or inputnum_g == lucknum_s:
#         print("three,come on")
#         break
#     else:
#         print("come on !")

"""while猜数字"""
# import  random
# num1 = random.randint(0,10)
# while True:
#     print("输入-1结束竞猜")
#     num2 = int(input("请输入一个数字:"))
#     if num2 == -1 or num2 >10 or num2 < 0:
#         print("请从新输入：")
#         continue
#     elif num2 == num1:
#         print("beengo")
#         break
#     elif num2 > num1:
#         print("大")
#         continue
#     else:
#         print("小")
#         continue

"""正左三角形"""
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#         j +=1
#     print()
#     i += 1

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#     print()

"""正右三角"""
# i = 1
# while i < 10:
#     k = 9
#     while i < k:
#         print(end=" " * 7)
#         k -= 1
#     j = i
#     while j <= i and j > 0:
#         print("%sx%s=%2d" % (i, j, i * j), end=" ")
#         j -= 1
#     print()
#     i += 1

# for i in range(1, 10):
#     for k in range(1, 10 - i):
#         print(end=" " * 7)
#     for j in range(1, i + 1):
#         print("%sx%s=%2d" % (i, j, i * j), end=" ")
#     print()

"""倒左三角"""
# i = 9
# while i > 0:
#     j = 1
#     while j <= i:
#         print("%sx%s=%2d" % (i, j, i * j), end=" ")
#         j += 1
#     print()
#     i -= 1

# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#     print()

"""倒右三角"""
# i = 9
# while i > 0:
#     k = 9
#     while i < k:
#         print(end=" "*7)
#         k -= 1
#     j = i
#     while j <= i and j > 0:
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#         j -= 1
#     print()
#     i -= 1

# for i in range(9,0,-1):
#     for k in range(1,10-i):
#         print(end=" "*7)
#     for j in range(i,0,-1):
#         print("%s+%s=%2d"%(i,j,i*j),end=" ")
#     print()

# for i in range(9,0,-1):
#     for k in range(1,10-i):
#         print(end=" "*7)
#     for j in range(i,0,-1):
#         print("%s+%s=%2d"%(i,j,i*j),end=" ")
#     print()

"""小球降落"""
# hight = 100
# sum1 = 0
# while True:
#     if  hight < 1:
#         sum1 = sum1 - hight
#         break
#     else:
#         sum1 = sum1 + hight + hight/2
#         hight = hight/2
# print(sum1)
