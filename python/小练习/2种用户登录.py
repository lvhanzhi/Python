# 第一种：
# while True:
#     name=input("请输入用户名：")
#     password=input("请输入密码：")
#     if name=="张三" and password=="123":
#         prnit("登录成功")
#     else:
#         print("用户名或密码不正确")
#         continue
#     break


# 第二种
tag=True
while tag:
    name=input("请输入用户名：")
    password=input("请输入密码：")
    if name=="张三" and password=="123":
        print("登录成功")
        cmd=input(">>:")
        if cmd=="quit":
            tag=False
    else :
        print("用户名或密码错误")