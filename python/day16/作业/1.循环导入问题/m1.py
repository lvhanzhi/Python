# import m2
# print('run m1...')
# x=1
# print('y=%s'%m2.y)

# 方式一:
# print('run m1...')
# x=1
# import m2
# print('y=%s'%m2.y)

# 方式二:
print('run m1...')
x = 1
def foo():
    import m2
    print('y=%s' % m2.y)
    m2.foo2()
foo()