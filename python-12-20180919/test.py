""""""


class persion():
    name = "yasi"
    age = 18
    money = 23
    home = "home"

    # 构造方法，在类被实例初始化的时候调用
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def tell(self):
        print("名字%s，年龄%s，存款%2d，房子%s" % (self.name, self.age, self.money, self.home))


#
if __name__ == '__main__':
    t1 = persion("name", 18, 100000)  # 实例化一个类
    t1.tell()  # 调用类中的函数

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
# t = Test()
# t.prt()

"""类的构造方案和析构方案"""
# class persion:
#
#
# #构造方法，类被实例化的时候调用
#     def __init__(self,name,age,money):
#         self.name = name
#         self.age = age
#         self.money = money
#  #析构方法，类被回收的时候调用
#     def __del__(self):
#         print("__del__被回收")
#
#     def tell(self):
#         print("姓名%s，年龄%s，收入%s"%(self.name,self.age,self.money))
#
# p1 = persion("lys",24,500)
# # p1.tell()
# del p1

"""类的共有属性、私有属性，共有方法、私有方法"""
# class persion:
#     def __init__(self,name,age,money):
#         #共有属性
#         self.name = name
#         self.age = age
#         #私有属性
#         self.__money = money
# def call(self):
#     print(self.name,self.age,self.money)

#     def setmoney(self,money):
#         pw = int(input("请输入密码"))
#         if pw == 123:
#             print(self.__money)
#         else:
#             print("无权限访问")
#     # def call(self):
#     #     print(self.name,self.age,self.money)
#
#
#
# c1 = persion("yasi",18,200)
# c1.setmoney(200)
# # c1.call()
