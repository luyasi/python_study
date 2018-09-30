from python18.ATM.view import View
from python18.ATM.operation import Operation

v = View()


def main():
    if v.Login():
        o = Operation()
        while True:
            choice = input("请输入你需要办理的业务：")
            if choice == "1":  # 开户
                o.Register()
            elif choice == "2":  # 查询
                o.Query()
            elif choice == "3":  # 存钱
                o.Save_money()
            elif choice == "4":  # 取钱
                o.Get_money()
            elif choice == "5":  # 转账
                o.Trans_money()
            elif choice == "6":  # 改密
                o.Change_pwd()
            elif choice == "7":  # 锁卡
                o.Lock()
            elif choice == "8":  # 解卡
                o.Unlock()
            elif choice == "9":  # 补卡
                o.New_card()
            elif choice == "0":  # 退出
                o.Save()
                break


if __name__ == '__main__':
    main()
