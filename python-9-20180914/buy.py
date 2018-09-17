""""""
"""
**homework**
**buy.py
"""
# 商品列表
Goods = [[1, "iphone", 5000], [2, "bike", 800], [3, "ipad", 6000], [4, "computer", 8000]]
Balance_Sum = int(input("please enter the balance in your card:"))

# 打印商品列表
val1 = "lys'supermarket"
print(val1.center(40, "="))
for Num, Good, Money in Goods:
    print(Num, Good, Money)
print("End of 0")
val2 = "="
print(val2 * 40)

# 统计消费商品和消费金额
Buy_Cost = 0
Buy_goods = set()
# 进入消费语句
while True:
    Good_Num = int(input("please enter your good number:"))
    if Good_Num == 0:
        print("您本次购买的商品如下：")
        for good in Buy_goods:
            print(good)
        print("您本次总共消费;", Buy_Cost, "元，卡内余额为：", Balance_Sum, "元")
        print("本次购物结束，欢迎下次光临")
        break

    good, price = '', 0
    for var in Goods:
        if Good_Num == var[0]:
            good = var[1]
            price = var[2]
            if Balance_Sum < price:
                print("余额不足！")
                continue
            Buy_goods.add(good)
            Buy_Cost += price
            Balance_Sum = Balance_Sum - price
            print("购买", good, "成功，本次消费", price, "元，卡内余额", Balance_Sum, "元")
