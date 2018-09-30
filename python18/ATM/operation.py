from python18.ATM.card import Card
from python18.ATM.person import Person
import os
import random
import pickle


class Operation(object):
    def __init__(self):
        self.Load_user()
        print(self.user_dict)

    def Load_user(self):
        """先判断文件是否存在"""
        if os.path.exists("user.txt"):
            with open("user.txt", "rb") as f:
                self.user_dict = pickle.load(f)
        else:
            self.user_dict = {}

    def Load_userid(self):
        if os.path.exists("userid.txt"):
            with open("userid.txt", "rb") as f:
                self.userid_dict = pickle.load(f)
        else:
            self.user_id_dict = {}

    def Register(self):
        """注册"""
        # 输入姓名
        name = input("请输入您的姓名：")
        # 输入身份证号
        userid = input("请输入您的身份证号：")
        # 输入手机号
        phone = input("请输入您的手机号：")
        # 设置密码
        passwd = self.Get_pwd()
        # 生成卡号
        cardid = self.Get_cardid()

        # 生成卡
        card = Card(cardid, passwd, 10)

        # 通过卡找到用户
        user = Person(name, userid, phone, card)
        self.user_dict[cardid] = user
        self.user_id_dict[userid] = cardid
        print("恭喜%s开卡成功，卡号%s，当前余额%s" % (name, cardid, card.money))

    def Get_pwd(self):
        while True:
            pwd1 = input("请输入您的密码：")
            pwd2 = input("请确认您的密码：")

            if pwd1 == pwd2:
                return pwd1
            else:
                print("两次密码不一致，请从新输入。")

    def Get_cardid(self):
        while True:
            cardid = random.randint(100000, 999999)
            if cardid not in self.user_dict:
                return cardid

    def Query(self):
        """查询功能"""
        # 拿到一张卡
        card = self.Get_card_info()
        if not card:
            print("卡不存在")
        else:
            if card.islock:
                print("卡被锁了！")
            else:
                # 检测密码
                if self.Check_pwd(card):
                    print("卡内余额%s" % (card.money))

    def Check_pwd(self, card):
        # 检测卡密码
        count = 1
        while count < 4:
            pwd = input("请输入您的密码:")
            # 判断用户输入的密码和卡内的密码是否一致
            if pwd == card.passwd:
                return True
            else:
                count += 1
                print("密码输入错误，还有%s次机会" % (4 - count))
                if count == 4:
                    card.islock = True
                    print("密码输入3次失败，卡被冻结")

    def Get_card_info(self):
        cardid = int(input("请输入您的卡号："))
        if cardid not in self.user_dict:
            return False
        else:
            # 通过卡找到用户
            user = self.user_dict[cardid]
            # 通过用户找到卡
            card = user.card
            return card

    def Save_money(self):
        """存钱"""
        # 拿到一张卡
        card = self.Get_card_info()
        # 通过卡找到用户
        user = self.user_dict[card.cardid]
        if not card:
            print("卡号不存在!")
        else:
            # 检查卡号是否被锁
            if card.islock:
                print("卡被冻结，请先解锁!")
            else:
                print("您输入的账户名为:%s" % (user.name))
                sure = input("确认存款请按1，返回菜单请按0")
                if sure == "1":
                    # 输入存款金额
                    money = int(input("请输入需要存款的金额："))
                    if money < 0:
                        print("输入的存款金额不正确，请从新输入")
                    else:
                        card.money += money
                        print("成功存入%s元" % (money))
                elif sure == "0":
                    return

    def Get_money(self):
        """取钱"""
        # 拿到一张卡
        card = self.Get_card_info()
        if not card:
            print("卡号不存在!")
        else:
            if card.islock:
                print("卡被冻结，请先解锁!")
            else:
                self.Check_pwd(card)
                money = int(input("请输入取款金额:"))
                if money > 0 and money <= card.money:
                    card.money -= money
                    print("成功取款%s元，卡内余额%s元" % (money, card.money))
                else:
                    print("输入金额有误，请从新输入")

    def Trans_money(self):
        card = self.Get_card_info()
        if not card:
            print("卡号不存在")
        else:
            if card.islock:
                print("卡被冻结，请先解卡！")
            else:
                if self.Check_pwd(card):
                    otherid = int(input("请输入对方账号："))
                    if otherid not in self.user_dict:
                        print("转账账号不存在!")
                    else:
                        other_user = self.user_dict[otherid]
                        sure = input("您将给%s进行转账，确认请安1，返回主菜单请按其他键" % (other_user.name))
                        if sure == "1":
                            money = int(input("请输入转账金额："))
                            if money > 0 and money <= card.money:
                                card.money -= money
                                other_user.card.money += money
                                print("您向%s成功转账%s元" % (other_user.name, money))
                            else:
                                print("转账金额有误！")
                        else:
                            return

    def Change_pwd(self):
        """修改密码"""
        card = self.Get_card_info()
        if not card:
            print("卡不存在")
        else:
            if card.islock:
                print("账户被冻结，请先解卡!")
            else:
                choice = input("请选择改密方式：原密码修改：1 身份信息验证修改：2")
                if choice == "1":
                    if self.Check_pwd(card):
                        passwd = self.Get_pwd()
                        card.passwd = passwd
                        print("****修改密码成功****")
                elif choice == "2":
                    userid = input("请输入身份证号码:")
                    user = self.user_dict[card.cardid]
                    if userid == user.userid:
                        passwd = self.Get_pwd()
                        card.passwd = passwd
                        print("****修改密码成功****")
                    else:
                        print("身份信息有误！")
                else:
                    print("请输入正确的选项！")

    def Lock(self):
        """锁卡"""
        card = self.Get_card_info()
        if not card:
            print("卡不存在！")
        else:
            if card.islock:
                print("卡已经被冻结")
            else:
                choice = input("使用密码锁卡：1  使用身份信息验证锁卡：2")
                if choice == "1":
                    if self.Check_pwd(card):
                        card.islock = True
                        print("****锁卡成功****")
                elif choice == "2":
                    userid = input("请输入身份证号码：")
                    user = self.user_dict[card.cardid]
                    if userid == user.userid:
                        card.islock = True
                        print("****锁卡成功****")

    def Unlock(self):
        """解锁"""
        card = self.Get_card_info()
        if not card:
            print("卡不存在!")
        else:
            userid = input("请输入身份证号：")
            user = self.user_dict[card.cardid]
            if userid == user.userid:
                card.islock = False
                print("****解卡成功****")

    def New_card(self):
        """补卡"""
        userid = input("请输入您的身份证号：")
        if userid in self.user_id_dict:
            # 通过身份证找到卡号
            cardid = self.user_id_dict[userid]
            # 通过卡号找到用户
            user = self.user_dict[cardid]
            # 通过用户找到卡
            card = user.card
            # 生成卡号
            new_cardid = self.Get_cardid()
            print(new_cardid)
            # 更换字典的键
            self.user_dict[new_cardid] = self.user_dict.pop(card.cardid)
            # 更换卡号
            card.cardid = new_cardid
            # 更换身份证对应的卡号
            self.user_id_dict[userid] = new_cardid
            print(card.cardid)

    def Save(self):
        """存储用户信息"""
        with open("user.txt", "wb") as f:
            pickle.dump(self.user_dict, f)
        with open("userid.txt", "wb") as f:
            pickle.dump(self.user_id_dict, f)
