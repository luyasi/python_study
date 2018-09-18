# 打印商品列表
Goods_List = [["iphone", 10000], ["ipad", 3000], ["mac", 15000], ["iwatch", 2000]]
print("****************************苹果专卖店************************")
for Goods_Code, Goods in enumerate(Goods_List):
    print(Goods_Code + 1, Goods[0], Goods[1])
print("输入0结束购物")
print("**************************************************************")

# 初始化购买清单和消费额
Buys_List = []
Buys_Pay = 0

# 进入购买
Money = int(input("请输入您的卡内余额："))
if Money > 0:
    while True:
        Goods_Num = int(input("请输入商品代码："))
        if Goods_Num == 0:
            print("您购买的商品如下：")
            for Buys in Buys_List:
                print(Buys)
            print("本次总共消费%s元，卡内余额%s元，欢迎再次光临" % (Buys_Pay, Money))
            break
        elif Goods_Num > 0 and Goods_Num <= len(Goods_List):
            if Money >= Goods_List[Goods_Num - 1][1]:
                Money -= Goods_List[Goods_Num - 1][1]
                print("购买%s成功，本次总共消费%s元，卡内余额%s元" % (Goods_List[Goods_Num - 1][0], Goods_List[Goods_Num - 1][1], Money))
                Buys_List.append(Goods_List[Goods_Num - 1][0])
                Buys_Pay += Goods_List[Goods_Num - 1][1]
            else:
                print("您卡内余额为%s元,无法购买商品" % (Money))
        else:
            print("商品代码输入有问题，请从新输入")
else:
    print("请先充值，谢谢！")
