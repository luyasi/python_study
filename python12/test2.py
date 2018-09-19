# from D:/python/学习/代码/python-12-20180919.test
from python12.test import persion

"""单继承"""
# class badman(persion):
#
#     #方法拓展，会沿用父类的属性
#     def __init__(self,name,age,money,hobby,bad):
#         super().__init__(name,age,money)
#         self.hobby = hobby
#         self.bad = bad
#
#     #方法复用，会覆盖父类的方法
#     def tell(self):
#         # super().tell()
#         print(self.name,self.age,self.money,self.hobby,self.bad)
#
# if __name__ == '__main__':
#     p1 = badman("ren",20,50,"dajia","hejiu")
#     p1.tell()
# # c1 = persion("ll",24,80)
# # c1.tell()

"""多继承"""


class Man(persion):
    def __init__(self, name, age, money):
        super().__init__(name, age, money)

    def tell(self):
        print("洒家乃%s，咱家今年%s岁了，劳资有存款%2f万元" % (self.name, self.age, self.money))

    def paoxiao(self):
        print("嗷嗷叫")


class Woman(persion):
    def __init__(self, name, age, money):
        super().__init__(name, age, money)

    def tell(self):
        print("奴家%s，芳龄%s，妾身存款%2d万元" % (self.name, self.age, self.money))

    def sajiao(self):
        print("嘤嘤嘤~")


class Gay(Woman, Man):  # 多继承下的顺序问题
    def tell(self):
        print("洒家乃%s，咱家今年%s岁了，劳资有存款%2f万元" % (self.name, self.age, self.money)
              )


if __name__ == '__main__':
    m = Man("taisen", 40, 2000)
    m.tell()
    m.paoxiao()
    w = Woman("panjinlian", 20, 10)
    w.tell()
    w.sajiao()
    g = Gay("kuke", 65, 10000)
    g.tell()
    g.sajiao()
