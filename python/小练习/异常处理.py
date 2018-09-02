# s="hello"
# try:
#     int(s)
# except ValueError as e:
#     print(e)
#


# 万能异常类
# s="hello"
# try:
#     int(s)
# except Exception as e:
#     print(e)


# IndexError
# s=[1,2,3,4,5]
# try:
#     print(s[8])
# except IndexError as e:
#     print(e)


# KeyError


# 主动触发异常
# try:
#     raise TypeError("类型错误")
# except Exception as e:
#     print(e)
#


# 自定义异常
# class EgonException(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return  self.msg
# try:
#     raise  EgonException('类型错误')
# except EgonException as e:
#     print(e)


try:
    age = input('age:')
    age = int(age)
except ValueError as e:
    print('aaa')
    print(e)
