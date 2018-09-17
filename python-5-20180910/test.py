"""
while循环语句
for ..in..循环语句
"""

# num1 = 0
# while num1 < 100:
#         num1 = num1 + 1
#         print("hello lys",num1)

"""猜彩票"""
# import random
#
# lucknumber = random.randint(10, 99)
# lucknumber_s = lucknumber // 10
# lucknumber_g = lucknumber % 10
# while True:
#     print("输入-1结束程序")
#     num = int(input("please input you chose:"))
#     num_s = num // 10
#     num_g = num % 10
#     if num == -1:
#         break
#     if num == lucknumber:
#         print("luck!one")
#         break
#     elif num_s == lucknumber_g and num_g == lucknumber_s:
#         print("luck!two")
#         break
#     elif num_s == lucknumber_s or num_g == lucknumber_g or num_s == lucknumber_g or num_g == lucknumber_s:
#         print("luck!three")
#         break
#     else:
#         print("badluck!")

"""猜数字"""
# import  random
#
# num1 = random.randint(0,10)
# print("输入-1结束程序")
# while True:
#     guess = int(input("请输入一个0到10的数字："))
#     if guess == -1:
#         break
#     if guess > 10:
#         continue
#     if guess > num1:
#         print("数字大了")
#     elif guess < num1:
#         print("数字小了")
#     else:
#         print("猜对了")
#         break

"""pass 占位符"""
# def func():
# #     pass

"""正左三角"""
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#         j += 1
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
#         print(end=" "*7)
#         k -=1
#     j = 1
#     while j <= i:
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#         j +=1
#     print()
#     i += 1

# for i in range(1,10):
#     for k in range(1,10-i):
#         print(end=" "*7)
#     for j in range(1,i+1):
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#     print()


"""倒左三角"""
# i = 9
# while i >= 1:
#      j = 1
#      while j <= i:
#          print("%sx%s=%2d"%(i,j,i*j),end=" ")
#          j +=1
#      print()
#      i -=1

# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#     print()

"""倒右三角"""
# i = 9
# while i >= 1:
#     k = 9
#     while i < k:
#         print(end=" "*7)
#         k -= 1
#     j = i
#     while j>0 and j <= i:
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#         j -= 1
#     print()
#     i -= 1

# for i in range(9,0,-1):
#     for k in range(1,10-i):
#         print(end=" "*7)
#     for j in range(i,0,-1):
#         print("%sx%s=%2d"%(i,j,i*j),end=" ")
#
#     print()

"""小球降落"""
# for i in (100,50,25,12.5,6.25,3.125,1.5625,0.78125)
# i = 100
# sum = 0
#
# while True:
#     if i < 1:
#         sum = sum -i
#         break
#     else:
#         sum = sum + i + i/2
#         i = i/2
# print(sum)


"""1加到100"""
# sum =0
# for i in range(1,101):
#     sum +=i
# print(sum)

# sum = 0
# i = 0
# while i <101:
#     sum =sum + i
#     i = i +1
# print(sum)
