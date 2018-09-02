# 无参装饰器
# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         star_time=time.time()
#         res=func(*args,**kwargs)
#         end_time=time.time()
#         print(end_time-star_time)
#         return res
#     return wrapper
# @timmer
# def foo():
#     time.sleep(2)
# foo()

# 有参装饰器
# def auth(driver='file'):
#     def auth2(func):
#         def wrapper(*args, **kwargs):
#             name = input("user:")
#             pwd = input("pwd:")
#
#             if driver=='file':
#                 if name == 'egon' and pwd == '123':
#                     print('loginsuccessful')
#                     res = func(*args, **kwargs)
#                     return res
#             elif driver == 'ldap':
#                 print('ldap')
#
#         return wrapper
#
#     return auth2
#
#
# @auth
#
#
# def foo(name):
#     print(name)
# foo('egon')


# def outter(driver='file'):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             name = input("用户名:")
#             pwd = input("密码:")
#             if driver == 'file':
#                 if name == "1" and pwd == "2":
#                     print("登录成功")
#                     res = func(*args, **kwargs)
#                     return res
#             elif driver == 'ldap':
#                 print('ldap')
#
#         return inner
#
#     return wrapper
#
#
# @outter(driver='file')
# def foo(name):
#     print(name)
#
#
# foo('aaa')




#迭代器
# a=[1,2,3]
# iter=a.__iter__()
# i=1
# while i<=len(a):
#     print(iter.__next__())
#     i+=1

# a='hello'
# iter=a.__iter__()
# while True:
#     try:
#         print(iter.__next__())
#     except StopIteration:
#         break

def chicken():
    print('=====>first')
    yield 1
    print('=====>second')
    yield 2
    print('=====>third')
    yield 3
obj=chicken()
# res=obj.__next__()
print(res)
res=obj.__next__()
print(res)
res=obj.__next__()
print(res)







