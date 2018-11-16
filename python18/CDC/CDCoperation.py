"""信用卡功能模块"""

# 导入模块
from python18.CDC.CDCcard import Card
from python18.CDC.CDCperson import Person
import os
import random
import pickle
import time


# 功能模块
class Operation(object):
    def __init__(self):
        self.Load_user()
        self.Load_userid()

    # 先判断文件是否存在，初始化用户字典，主键为卡号
    def Load_user(self):
        if os.path.exists("user.txt"):
            with open("user.txt", "rb") as f:
                self.user_dict = pickle.load(f)
        else:
            self.user_dict = {}

    # 先判断文件是否存在，初始化用户id字典，主键为身份证号
    def Load_userid(self):
        if os.path.exists("userid.txt"):
            with open("userid.txt", "rb") as f:
                self.user_id_dict = pickle.load(f)
        else:
            self.user_id_dict = {}

    """用户注册"""

    def Register(self):
        # 输入用户姓名
        name = input("请输入您的姓名：")
        # 输入用户身份证
        userid = input("请输入您的身份证号码：")
        # 输入手机号
        phone = input("请输入您的手机号：")
        # 设置密码
        passwd = self.Get_pwd()
        # 生成卡号
        cardid = self.Get_cardid()
        # 按照用户输入信息，生成卡实例
        card = Card(cardid, passwd, 10000)
        # 按照用户输入信息，生成用户实例
        user = Person(name, userid, phone, card)
        self.user_dict[cardid] = user
        self.user_id_dict[userid] = cardid
        print(("恭喜%s开户成功，卡号%s，当前可用额度%s") % (name, cardid, card.money))

    """查询用户信用卡信息"""

    def Query(self):
        card = self.Get_card_info()
        if not card:
            print("您输入的信用卡不存在！")
        else:
            if card.islock:
                print("您的信用卡当前为锁定状态!")
            else:
                # 校验用户密码
                if self.Check_pwd(card):
                    print("您的信用卡当前可用额度%s" % (card.money))

    """信用卡还款"""

    def Back_money(self):
        card = self.Get_card_info()
        user = self.user_dict[card.cardid]
        if not card:
            print("您的信用卡卡号不存在")
        else:
            # 检查信用卡是否被锁
            if card.islock:
                print("您的信用卡已被锁定，请先解锁！")
            else:
                print("您输入的信用卡当前账户名为：%s" % (user.name))
                sure = input("确认还款请按1，返回主菜单请按0")
                if sure == "1" and card.money < 10000:
                    # 记录还款时间
                    global back_money_time
                    back_money_time = time.time()
                    sum_time = back_money_time - get_money_time
                    # 记录利息
                    interest = sum_time * 0.0005 * (get_money)
                    # interest = self.Interest()
                    print("您信用卡还款利息部分为:%d,借款部分:%d" % (interest, 10000 - card.money))
                    # 输入还款金额
                    global back_money
                    back_money = int(input("请输入您的还款金额："))
                    if back_money < 0:
                        print("您输入的还款金额不正确，请从新输入")
                    elif sum_time > 50 or back_money < get_money * 0.1:
                        card.islock = True
                        print("因为你未及时还款对应额度或还款时间超过50秒，您的信用卡已经冻结。")
                    else:
                        # 还款金额加入到余额
                        card.money += back_money
                        # 计算还需要还款的金额
                        re_money = 10000 - card.money + interest
                        # 打印还款金额和时间
                        back_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        print("您成功还款%s元,还款时间为：%s" % (back_money, back_time))
                        # 初始化计算还款时间
                        re_sum_time = time.time() - back_money_time
                        # 初始化计算还款利息
                        re_interest = re_sum_time * 0.0005 * re_money
                        # 打印还需还款利息和金额
                        print("您还需还借利息部分：%d，借款部分：%d元，" % (re_interest, re_money))
                elif sure == "0":
                    return
                else:
                    print("您信用卡当前不需要还款。")

    """信用卡套现"""

    def Get_money(self):
        card = self.Get_card_info()
        if not card:
            print("您的信用卡卡号不存在！")
        else:
            if card.islock:
                print("您的信用卡已被锁定，请先解锁！")
            else:
                self.Check_pwd(card)
                global get_money
                get_money = int(input("请输入您需要消费或者套现的金额："))
                if get_money > 0 and get_money <= card.money:
                    # 余额减去套现金额
                    card.money -= get_money
                    # 计算和打印套现时间
                    global get_money_time
                    get_money_time = time.time()
                    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # 打印消费套现金额和时间
                    print("您已经成功消费或套现%s元，消费时间为：%s" % (get_money, get_time))
                    print("注意：消费或套现50秒后需要还款10%，未及时还款将冻结该卡！")
                    # get_money -= back_money
                else:
                    print("您输入的金额有误，或者超过最大消费金额")
                # return get_money

    # 信用卡计息
    # def Interest(self):
    #     sum_time = back_money_time - get_money_time
    #     get_money = self.Get_money()
    #     interest = sum_time * 0.0005 * get_money
    #     get_money -= back_money
    #
    #     return interest

    """信用卡转账"""

    def Trans_money(self):
        card = self.Get_card_info()
        if not card:
            print("您的信用卡卡号不存在！")
        else:
            if card.islock:
                print("您的信用卡已被锁定，请先解锁！")
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

    """信用卡改密"""

    def Change_pwd(self):
        card = self.Get_card_info()
        if not card:
            print("您的信用卡卡号不存在！")
        else:
            if card.islock:
                print("您的信用卡已被锁定，请先解锁！")
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

    """信用卡锁卡"""

    def Lock(self):
        card = self.Get_card_info()
        if not card:
            print("您的信用卡卡号不存在！")
        else:
            if card.islock:
                print("您的信用卡已被锁定!")
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

    """信用卡解锁"""

    def Unlock(self):
        card = self.Get_card_info()
        if not card:
            print("您的信用卡卡号不存在！")
        else:
            userid = input("请输入身份证号：")
            user = self.user_dict[card.cardid]
            if userid == user.userid:
                card.islock = False
                print("****解卡成功****")

    """信用卡换卡"""

    def New_card(self):
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
            # print(new_cardid)
            # 更换字典的键
            self.user_dict[new_cardid] = self.user_dict.pop(card.cardid)
            # 更换卡号
            card.cardid = new_cardid
            # 更换身份证对应的卡号
            self.user_id_dict[userid] = new_cardid
            print(card.cardid)

    # 设置和校验用户密码
    def Get_pwd(self):
        while True:
            pwd1 = input("请输入您的密码：")
            pwd2 = input("请确认您的密码：")

            if pwd1 == pwd2:
                return pwd1
            else:
                print("您输入的两次密码不一致，请从新输入。")

    # 随机生成信用卡号
    def Get_cardid(self):
        while True:
            cardid = random.randint(100000, 999999)
            if cardid not in self.user_dict:
                return cardid

    # 按照用户输入的卡号，进行检验，并返回信息
    def Get_card_info(self):
        cardid = int(input("请输入您的信用卡账号："))
        if cardid not in self.user_dict:
            return False
        else:
            user = self.user_dict[cardid]
            card = user.card
            return card

    # 校验用户密码，密码错误3次，冻结信用卡
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

    # 回写用户信息
    def Save(self):
        with open("user.txt", "wb") as f:
            pickle.dump(self.user_dict, f)
        with open("userid.txt", "wb") as f:
            pickle.dump(self.user_id_dict, f)
