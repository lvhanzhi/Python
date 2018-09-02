def f1():
    max=2
    def f2():
        max=3
        print(max)
    f2()
f1()
print(max)