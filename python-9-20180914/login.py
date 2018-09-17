""""""
"""
**homework**
**login.py
"""
# 读取用户注册信息
Reg_Name = open("D:/python学习/python培训笔记/day7代码-20180913/day7/username.txt", "r")
content = Reg_Name.read()
Reg_Name.close()
content_1 = content.split("\n")
print(content)

# 获取用户登录信息
Login_User = input("请输入您的用户名:")
Login_Password_1 = input("请输入您的密码:")
if Login_User + Login_Password_1 in content:
    print("登陆成功")
else:
    print("输入密码错误，您还有2次机会")
    with open("D:/python学习/python培训笔记/day7代码-20180913/day7/username.txt", "a+") as Login_Password:
        Login_Password.write(Login_Password_1)
        # Login_Password.write()
        Login_Password.flush()
    Login_Password_2 = input("请输入您的密码:")
    if Login_User + Login_Password_2 in content:
        print("登陆成功")
    else:
        print("输入密码错误，您还有1次机会")
        with open("D:/python学习/python培训笔记/day7代码-20180913/day7/username.txt", "a+") as Login_Password:
            Login_Password.write(Login_Password_2)
            # Login_Password.write()
            Login_Password.flush()
        Login_Password_3 = input("请输入您的密码:")
        if Login_User + Login_Password_3 in content:
            print("登陆成功")
        else:
            print("输入密码错误，您还有0次机会")
            print("密码输入3次错误，账户已经被锁定")
            with open("D:/python学习/python培训笔记/day7代码-20180913/day7/username.txt", "a+") as Login_Password:
                Login_Password.write(Login_Password_3)
                # Login_Password.write()
                Login_Password.flush()
