# from functools import wraps
# def outter(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wrapper
# @outter
# def foo():
#     """
#     这是注释
#     :return:
#     """
#     print('running...')
# print(foo.__name__)


# nums=[11,33,22,9,31]
# print(sorted(nums,reverse=True))


# salaries = {
#     'egon': 300000,
#     'alex': 100000000,
#     'wupeiqi': 10000,
#     'yuanhao': 2000
# }
# # print(sorted(salaries,key=lambda name:salaries[name],reverse=True))
#
#
# print(sorted(salaries, key=lambda name: salaries[name], reverse=True))
#
#
# # print((lambda x,y:x+y)(0,10))
# def add(x, y): return x + y
#
#
# print(list(map(add, 'zhoujy', 'A')))



# res=map(lambda x,y:x+y,range(1,11),range(1,11))
# for i in res:
#     print(i)


# res=filter(lambda x:x>5,range(1,11))
# for i in res:
#     print(i)

# from functools import reduce
# res=reduce(lambda x,y:x+y,range(1,11),5)
# print(res)








# res=filter(lambda x:x>5,range(10))
# for i in res:
#     print(i)


from functools import reduce
res=reduce(lambda x,y:x+y,range(1,3),)
print(res)











































