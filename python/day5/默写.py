#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s '%(j,i,i*j),end='')
    print()
#金字塔
n=int(input('n:').strip())
for x in range(1,n+1):
    for i in range(n-x):
        print(' ',end='')
    for j in range(2*x-1):
        print('*',end='')
    print()

