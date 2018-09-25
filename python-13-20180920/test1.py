""""""
"""多态"""
"""
需求：
1、创建一支军队，包含骑兵，弓箭手，法师
2、所有兵种都能进攻和防守，但是形态各异
3、通过输入命令，控制每个兵种的攻守细节
"""
# class Cavalry(object):
#     def attack(self):
#         print("骑士进攻")
#     def defend(self):
#         print("骑士防守")
#
# class Archer:
#     def attack(self):
#         print("射手进攻")
#     def defend(self):
#         print("射手防守")
#
# class Master:
#     def attack(self):
#         print("法师进攻")
#     def defend(self):
#         print("法师防守")
#
# if __name__ == '__main__':
#     Army = []
#
#     c1 = Cavalry()
#     a1 = Archer()
#     m1 = Master()
#
#     Army.append(c1)
#     Army.append(a1)
#     Army.append(m1)
#
#     command = input("请将军指挥：")
#     if command == "进攻":
#         for var in Army:
#             var.attack()
#     elif command == "防守":
#         for var in Army:
#             var.defend()
#     elif command == "骑士进攻":
#         for var in Army:
#             if isinstance(var,Cavalry):
#                 var.attack()
#             else:
#                 var.defend()


"""@property 把一个方法当做一个私有属性来使用"""

# class persion():
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#
#     # def getage(self):
#     #     print(self.__age)
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,age):
#         self.__age = age
#
# if __name__ =='__main__':
#     p = persion("xiaohon",20)
#
#     p.age = 21
#     print(p.age)

# class Screen(object):
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         self.__width = width
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
#     @property
#     def resolution(self):
#         return self.width * self.height
#
# if __name__ == '__main__':
#     s = Screen()
#     s.height = 768
#     s.width = 1024
#     # s.resolution =786432
#     print(s.resolution)

"""动态添加属性和方法"""
# from types import MethodType  #可以把指定的方法绑到类上
# class Persion(object):
#     pass
# def tell(self):
#     print("名字是%s"%(self.name))
#
# if __name__ == '__main__':
#     p =Persion()
#     p.name = "tom"  #动态添加的属性，只能当前实例使用，其他实例不能使用
#     print(p.name)
#     # p1 = Persion()
#     # print(p1.name)
#     #第一个参数是要绑到的方法，第二个参数是需要绑到的实例
#     p.spack = MethodType(tell,p)
#     p.spack()

"""限制添加属性"""
"""__slots__只在当前类中有效，在继承的子类中无效"""
# class Persion(object):
#     __slots__ = ("name","age","money")
#     def __init__(self,name,age,money):
#         self.name = name
#         self.age = age
#         self.money = money

# if __name__ =='__main__':
#     p = persion("hello",18,28)
#     p.fly = 100
#     print(p.fly)

# class Student(object):
#     pass
# def set_age(self,age):
#     self.age = age
# from types import MethodType
# s = Student()
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age)
# s = Student()
# s.name = "Michael"
# print(s.name)

# 给类绑定方法
# class Student(object):
#     pass
#
# def set_score(self,score):
#     self.score = score
# Student.set_score = set_score
#
# s = Student()
# s.score = 100
# print(s.score)
# s2 = Student()
# s2.score = 99
# print(s2.score)

"""__repr__和__str__"""
"""
__str__:在实例初始化后，打印实例会自动调用
__repr__：在没__str__d的时候，和__str__功能一样
          在交互界面初始化实例，按回车的时候会打开
"""
# class Test(object):
#     def __init__(self,name = "jack",age = 16):
#         self.name = name
#         self.age = age
#
# class Teststr(Test):
#     def __repr__(self):
#         return "__repr__:%s:%s"%(self.name,self.age)
#     # def __str__(self):
#     #     return "__str__:%s:%s"%(self.name,self.age)
#
# if __name__ == '__main__':
#     t = Teststr()
#     print(t)

"""运算符重载"""
"""在多个实例之间使用运算符"""

# class Persion(object):
#     def __init__(self, num):
#         self.num = num
#
#     def __add__(self, other):
#         return Persion(self.num + other.num)
#
#     def __sub__(self, other):
#         return Persion(self.num - other.num)
#
#     def __str__(self):
#         return "num =" + str(self.num)
#
# if __name__ == '__main__':
#     p1 = Persion(12)
#     p2 = Persion(13)
#
#     print(p1-p2)
#     p3 = p1 + p2
#     print(p3.num)


"""@staticmethod 和@classmethod"""
# class Persion():
#     name = "jack"
#     def __init__(self,name):
#         self.name = name
#
#     #self实例方法
#     def tell(self):
#         print(self.name)
#
#     #cls类方法
#     @classmethod
#     def say(cls):
#         print(cls.name)
#
#     #静态方法
#     @staticmethod
#     def talk(i):
#         print(i)
#
# if __name__ == '__main__':
#     # p = Persion("rose")
#     # p.name = "tom"
#     # p.tell()
#     # p.say()
#     # p.talk()
#     # Persion.tell(p)
#     Persion.talk("1")
#     Persion.say()

"""类方法和静态方法"""
# class Dates(object):
#     def __init__(self,year = 0,month = 0,day = 0):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def get_date(cls,string_date):
#         years,months,days = string_date.split("-")
#         date1 = cls(years,months,days) #实例化
#         return date1
#
#     def out_date(self):
#         print("yesr",self.year)
#         print("month",self.month)
#         print("day",self.day)
#
# if __name__ == '__main__':
#         # years = input("请输入年份：")
#         # d = Dates(years)
#         # d.out_date()
#
#         t = Dates.get_date("2018-9-20")
#         t.out_date()
