# 定义一个计数器，当返回值等于3的时候禁止登陆
times = 0

# 定义三个列表，接受返回的用户名、密码、和黑名单值
Name_List = []
User_Password = []
Black_User = []
A = 0

# 获取用户名和密码进行比对
while A == 0:
    Login_Name = input("请输入您的用户名：")

    # 读取用户名注册文件
    with open("./user.txt", "r") as User_List:
        User_List.seek(0, 0)
        content = User_List.readlines()
        for var in content:
            Account = var.split(":")[0]
            Name_List.append(Account)
            Password = var.split(":")[1][:-1]
            User_Password.append(Password)
        if Login_Name in Name_List:
            with open("black.txt", "a+") as Black_List:
                Black_List.seek(0, 0)
                content = Black_List.readlines()
                for Login_Name in content:
                    Black_User.append(Login_Name[:-1])
                    if Login_Name not in Black_User:
                        while times < 3:
                            Password = input("请输入你的密码：")
                            name_index = Name_List.index(Login_Name)
                            if Password == User_Password[name_index]:
                                print("登录成功")
                                A = 1
                                break
                            else:
                                print("密码输入错误，请从新输入，您还剩%s次机会" % (2 - times))
                                times += 1
                                if times == 3:
                                    print("密码输入三次失败,账户被冻结")
                                    with open("black.txt", "a") as f:
                                        f.write(Login_Name + "\n")
                                    A = 1
                                    break
                    else:
                        print("账户被冻结，请联系管理员")
        else:
            print("用户名不存在")
