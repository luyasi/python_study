""""""
"""冒泡排序"""
import random
import time

# list1 = [54,26,93,17,77,31,44,55,20]
list1 = list(range(10000))
random.shuffle(list1)
# print(list1)

# def bubble_sort(list1):
#     for i in range(len(list1) - 1):
#         for j in range(len(list1) - i -1):
#             if list1[j] > list1[j +1]:
#                 list1[j],list1[j+1] = list1[j+1],list1[j]
#     return list1
# bubble_sort(list1)

# print(bubble_sort(list1))

#
#
# """插入排序"""
# # list1 = [54,26,93,17,77,31,44,55,20]
time1 = time.time()
print(time1)


def insert_sort(list1):
    for i in range(1, len(list1)):
        for j in range(i, 0, -1):
            if list1[j] < list1[j - 1]:
                list1[j], list1[j - 1] = list1[j - 1], list1[j]
    return list1


insert_sort(list1)
time2 = time.time()
print(time2)
time3 = time2 - time1
print(time3)
print("OK")
# print(insert_sort(list1))
