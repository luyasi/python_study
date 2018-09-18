f = open("user.txt", "a+")
name_list = []
a = 0
while a == 0:
    name = input("请输入您的用户名:")
    if name != "" and " " not in name:
        f.seek(0, 0)
        content = f.readlines()
        for var in content:
            # 取账号和密码
            account = var.split(":")[0]
            name_list.append(account)
        if name not in name_list:
            while True:
                pwd = input("请输入您的密码:")
                if pwd != "" and " " not in pwd:
                    pwd1 = input("请确认您的密码:")
                    if pwd == pwd1:
                        str1 = "%s:%s\n" % (name, pwd)
                        f.write(str1)
                        print("恭喜您注册成功!")
                        f.flush()
                        a = 1
                        break
                    else:
                        print("两次密码输入不一致,请重新输入!")
            else:
                print("密码包含非法字符!")
        else:
            print("用户名已被占用,请重新注册!")
    else:
        print("用户名中包含非法字符!")
f.close()
