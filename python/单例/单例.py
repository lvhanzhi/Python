# class A:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'intance'):
#             cls.intance=super().__new__(cls)
#         return cls.intance
#     def __init__(self):
#         pass
# print(A(),A())
# print(A())
# print(A())
#
#
# class A:
#     __instance=None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance==None:
#             cls.__instance=super().__new__(cls)
#         return cls.__instance
#     def __init__(self):
#         pass
# print(A(),A())
# print(A())
# print(A())


# class A:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'instance'):
#             cls.instance=super().__new__(cls)
#             cls.instance.ip='127.0.0.1'
#         return cls.instance
#     def __init__(self):
#         pass
# a1=A()
# print(a1)
# a2=A()
# print(a2)


def singleton(cls):
    def getInstance(*args,**kwargs):
        if not hasattr(cls,'instance'):
            cls.instance=cls()
            cls.instance.ip='127.0.0.1'
        return cls.instance
    return getInstance
@singleton
class A:
    pass
print(A(),A())






