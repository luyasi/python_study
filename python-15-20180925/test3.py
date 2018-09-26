""""""
"""面向对象"""

"""访问限制，私有属性"""
# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self,score):
#         self.__score = score
#
#     def print_score(self):
#         print("%s:%s"%(self.__name,self.__score))
#
# s = Student("bob",100)
# s.set_score(99)
# print(s.get_score())
# print(s.get_name())
# print(s._Student__name)  #私有属性在外部可以通过"_class__name"访问。

"""继承和多态"""


class Animal(object):
    def run(self):
        print("animal is running")


class Dog(Animal):
    def run(self):
        print("dog is running")


class Cat(Animal):
    pass


d = Dog()
d.run()
