#1. 使用while循环输出1 2 3 4 5 6     8 9 10
i=1
while i<=10:
    print(i)
    i+=1
#2. 求1-100的所有数的和
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print("1到100的总和为%d"%(sum))
#3. 输出 1-100 内的所有奇数
i=1
while i<=100:
    if i%2!=0:
        print(i)
    i+=1
#4. 输出 1-100 内的所有偶数
i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1
#5. 求1-2+3-4+5 ... 99的所有数的和
sum=0
i=1
while i<=99:
    if i%2==0:
        sum-=i
    else:
        sum+=i
    i+=1
print(sum)
#6. 用户登陆（三次机会重试）
time=1
tag=True
while tag:
    name=input("请输入用户名：")
    password=input("请输入密码：")
    if name=="张三" and password=="123":
        print("登录成功")
        tag=False
    else:
        print("用户名或密码错误")
        time+=1
        if time==4:
            tag=False
            print("你没机会了")
#7：猜年龄游戏
# 要求：
#     允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
time=1
tag=True
while tag:
    age=input("请输入你猜的年龄：")
    if age=="12":
        print("恭喜你猜对了！！！")
        tag=False
    else:
        print("抱歉你没有猜对")
        time+=1
        if time==4:
            tag=False
            print("你没机会了")
#8：猜年龄游戏升级版
# 要求：
#     允许用户最多尝试3次
#     每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
#     如何猜对了，就直接退出
time=1
tag=True
while tag:
    age=input("请输入你猜的年龄：")
    if age=="12":
        print("恭喜你猜对了！！！")
        tag=False
    else:
        print("抱歉你没有猜对")
        time+=1
        if time%4==0:
            cmd=input("是否还想继续？是则回答Y或y，否则回答N或n")
            if cmd=="N" or cmd=="n":
                tag=False
