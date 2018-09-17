""""""
"""
**homework**
**register.py
"""
# 输入用户名
User_Name = input("请输入您的用户名：")

# 用户名信息存储
with open("D:/python学习/python培训笔记/day7代码-20180913/day7/username.txt", "a+", encoding="gbk") as Reg_Name:
    Reg_Name.write(User_Name)
    Reg_Name.flush()
# 用户名读取
Reg_Name = open("D:/python学习/python培训笔记/day7代码-20180913/day7/username.txt", "r", encoding="gbk")
content = Reg_Name.readline()
Reg_Name.close()

# 进行注册身份校验
if content.count(User_Name) >= 2:
    print("用户名已经存在，请从新注册")
# 输入密码
else:
    User_Password_One = input("请输入您的密码：")
    User_Password_Two = input("请确认您的密码：")
    if User_Password_One == User_Password_Two:
        print("注册成功！")
        with open("D:/python学习/python培训笔记/day7代码-20180913/day7/username.txt", "a+") as Reg_Password:
            Reg_Password.write(User_Password_Two)
            Reg_Password.write("\n")
            Reg_Password.flush()
    else:
        print("两次密码不一致，请从新输入！")
