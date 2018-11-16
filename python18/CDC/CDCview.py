# 打印信用卡功能界面界面
import time


class View:
    def Login(self):
        """确认管理员账户密码"""
        name = input("请输入管理员账户：")
        passwd = input("请输入管理员密码：")
        if name == "admin" and passwd == "123456":
            self.Login_view()
            time.sleep(2)
            self.Operation_view()
            return True
        else:
            print("管理员账户或密码错误，请从新输入。")

    def Login_view(self):
        print("************************************")
        print("*                                  *")
        print("*                                  *")
        print("*         LYS  CREDIT CARD         *")
        print("*                                  *")
        print("*                                  *")
        print("************************************")

    def Operation_view(self):
        print("************************************")
        print("*     开户（1）     查询（2）         *")
        print("*     还款（3）     套现（4）         *")
        print("*     转账（5）     改密（6）         *")
        print("*     锁卡（7）     解卡（8）         *")
        print("*     补卡（9）     退出（0）         *")
        print("************************************")
