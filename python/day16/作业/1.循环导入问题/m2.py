# import m1
# print('run m2...')
# y=1
# print('x=%s'%m1.x)

# 方式一:
# print('run m2...')
# y=2
# import m1
# print('x=%s'%m1.x)

print('run m2...')
y=2
def foo2():
    import m1
    print('x=%s'%m1.x)
