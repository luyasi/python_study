# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#     def prin_score(self):
#         print("%s:%s"%(self.__name,self.__score))
#
#     def get_grade(self):
#         if self.__score > 90:
#             return 'A'
#         elif self.__score > 60:
#             return 'B'
#         else:
#             return 'C'
#
# lisa = Student("Lisa",99)
# bob = Student("Bob",50)
# print(lisa.prin_score())
# print(lisa.name,lisa.score,lisa.get_grade())
# print(bob.name,bob.score,bob.get_grade())

""""""

"""算法"""
"""
算法：计算机处理信息的本质，是一种解决问题的方法和思想。
算法的五大特性：输入、输出、又穷性、确定性、可行性

程序 = 数据结构 + 算法

常用的五种数据运算：插入、删除、修改、排序、查找。
"""

"""
排序算法：是一种能将一串数据按照特定顺序进行排列的一种算法。
稳定排序
不稳定排序
"""

"""冒泡排序"""
# list1 = [54,26,93,17,77,31,44,55,20]

# def bubble_sort(list1):
#     for i in range(len(list1) - 1):
#         for j in range(len(list1) - i - 1):
#             if list1[j] > list1[j + 1]:
#                 list1[j],list1[j+1] = list1[j+1],list1[j]
#     return list1
#
# print(bubble_sort(list1))

"""插入排序"""
# list1 = [54,26,93,17,77,31,44,55,20]
# def insert_sort(list1):
#     for i in range(1,len(list1)):  #i 控制循环插入的次数
#         while i > 0:               #while循环控制插入的位置
#             if list1[i] < list1[i - 1]:
#                 list1[i],list1[i - 1] = list1[i - 1],list1[i]
#                 i -= 1
#             else:
#                 break
#     return list1
# print(insert_sort(list1))

# def insert_sort(list1):
#     for i in range(1,len(list1)):
#         for j in range(i,0,-1):
#             if list1[j] < list1[j-1]:
#                 list1[j],list1[j-1] = list1[j-1],list1[j]
#     return list1
#
# print(insert_sort(list1))

"""
树：是一种抽象数据类型

特点：
1.每个节点有零个或者多个子节点。
2.没有父节点的节点是根节点。
3.每一个非根节点有且只有一个父节点。
4.除了根节点外，每个子节点可以分为多个不相交的子树。

树的相关概念：
1.节点的度：一个节点含有的子树的个数称为该节点的度。
2.树的度：一棵树中，最大节点的度称为树的度。
3.叶节点：度为零的节点。
4.父节点：如果一个节点含有子节点，那么这个节点是父节点。
5.子节点：一个节点含有的子树的根节点称为该节点的子节点。
6.兄弟节点：相同父节点。
7.堂兄弟节点：父节点是同一层。
8.节点的层次：从根开始，根为第一层。
9.树的深度：树中节点最大的层次。
10.节点的祖先：从根到该节点所经历的所有分支。
11.森林：由n棵互不相交的树组合。

树的种类：
1.无序树
2.有序树
    1.二叉树
    2.霍斯曼树
    3.B树
"""
