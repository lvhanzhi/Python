a=0
i=1
bbb=True
while bbb:
    while i <= 3:
        b = int(input("请输入年龄"))
        if b == a:
            print("恭喜你，猜对了！！！")
            break
            bbb=Flase
        else:
            print("猜错了")
        i += 1
    answer = input("是否还想继续玩？是则回答y,否则回答n")
    if answer == "y":
        i = 1
    else :
        break

