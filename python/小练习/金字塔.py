x=int(input("请输入个数："))
for i in range(1,x+1):
    for j in range(1,x-i+1):
        print(" ",end='')
    for y in range(1,2*i):
        print("*",end='')
    print()