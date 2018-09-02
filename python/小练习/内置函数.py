# print(abs(-12))
# print(all([""]))
# print(all([1]))
# print(any([1,""]))
# print(any([""]))
# print(any([]))
# print(bin(1))#二进制转换
# print(oct(11))#八进制转换
# print(hex(17))#十六进制转换
# res='你好'.encode('utf-8')
# print(res)
# res=bytes('你好',encoding='utf-8')
# print(res)
# print(chr(65))#将数字转成对应的字符
# print(ord('A'))#将字符转成对应的数字
# import time
# print(dir(time))
# print(divmod(10,3))
#
# l=['a','b','c']
# for item in enumerate(l):
#     print(item)

# l='[1,2,3]'
# print(eval(l))

# with open('内置函数文件.txt','r',encoding='utf-8') as f:
#     data=f.read()
#     data=eval(data)
#     print(type(data))


# s=frozenset({1,2,3})#不可变集合
# s=set({1,2,3})#可变集合


# #查看全局作用域的名字
# a=11111111
# print(globals())
#
# #查看局部作用域的名字
# print(locals())

# hash([1,2,3])
# print(sum(range(111)))


# module=input("请输入你要导入的模块名:").strip()
# m=__import__(module)
# m.sleep(2)
# print("打不过我吧,没有办法,啦啦啦")


# x = 1
#
#
# def outter():
#     def wrapper():
#         print(x)
#
#     return wrapper
#
#
# f = outter()
#
#
# def bar():
#     x = 11
#     f()
# bar()






















