from python18.CDC.CDCview import View
from python18.CDC.CDCoperation import Operation

v = View()


def CDCmain():
    if v.Login():
        o = Operation()
        while True:
            choice = input("请输入你需要办理的信用卡业务：")
            if choice == "1":  # 信用卡开户
                o.Register()
            elif choice == "2":  # 信用卡查询
                o.Query()
            elif choice == "3":  # 信用卡还款
                o.Back_money()
            elif choice == "4":  # 信用卡取钱
                o.Get_money()
            elif choice == "5":  # 信用卡转账
                o.Trans_money()
            elif choice == "6":  # 信用卡改密
                o.Change_pwd()
            elif choice == "7":  # 信用卡锁卡
                o.Lock()
            elif choice == "8":  # 信用卡解卡
                o.Unlock()
            elif choice == "9":  # 信用卡补卡
                o.New_card()
            elif choice == "0":  # 退出
                o.Save()
                break


if __name__ == '__main__':
    CDCmain()
