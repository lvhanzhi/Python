# class Mymeta(type):
#     n=444
#     def __call__(self, *args, **kwargs):
#         obj=self.__new__(self)
#         self.__init__(obj,*args,**kwargs)
#         self.n=555
#         obj.n=666
#         return obj
# class Bar(object):
#     n=333
#     pass
# class Foo(Bar):
#     n=222
#     pass
# class OldboyTeacher(Foo,metaclass=Mymeta):
#     n=111
#     def __init__(self,name):
#         self.name=name
#         self.n=0
# egon=OldboyTeacher('egon')
# print(egon.n)
# #666  0  555  111 222 333
# print(OldboyTeacher.n)
# #555  111  222  333  444


# 单例模式:
#settings.py
# IP='127.0.0.1'
# PORT='3306'
#方式一:
# import settings
# class Mysql:
#     __instance=None
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#     @classmethod
#     def from_conf(cls):
#         if cls.__instance is None:
#             cls.__instance=cls(settings.IP,settings.PORT)
#         return cls.__instance
# obj1=Mysql.from_conf()
# obj2=Mysql.from_conf()
# obj3=Mysql('192.168.2.1','3306')
# print(obj1)#<__main__.Mysql object at 0x0000018C60598EB8>
# print(obj2)#<__main__.Mysql object at 0x0000018C60598EB8>
# print(obj3)#<__main__.Mysql object at 0x0000018C60598EF0>


# #方式二:
# import settings
# def singleton(cls):
#     cls.__instance=cls(settings.IP,settings.PORT)
#     def wrapper(*args,**kwargs):
#         if len(args)==0 and len(kwargs)==0:
#             return cls.__instance
#         return cls(*args,**kwargs)
#     return wrapper
# @singleton
# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
# obj1=Mysql()
# obj2=Mysql()
# obj3=Mysql('192.168.2.1','3306')
# print(obj1)#<__main__.Mysql object at 0x00000221877587F0>
# print(obj2)#<__main__.Mysql object at 0x00000221877587F0>
# print(obj3)#<__main__.Mysql object at 0x0000022187758EB8>


# #方式三:
# import settings
# class Mymetas(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         super().__init__(class_name,class_bases,class_dic)
#         self.__instance=self(settings.IP,settings.PORT)
#     def __call__(self, *args, **kwargs):
#         if len(args)==0 and len(kwargs)==0:
#             return self.__instance
#         else:
#             obj=self.__new__(self)
#             obj.__init__(*args,**kwargs)
#             return obj
# class Mysql(object,metaclass=Mymetas):
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
# obj1=Mysql()
# obj2=Mysql()
# obj3=Mysql('192.168.2.1','3306')
# print(obj1)#<__main__.Mysql object at 0x0000019BF9708EB8>
# print(obj2)#<__main__.Mysql object at 0x0000019BF9708EB8>
# print(obj3)#<__main__.Mysql object at 0x0000019BF97104A8>


#方式四:
# aaa.py
# import settings
# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
# __instance=Mysql(settings.IP,settings.PORT)


# def foo():
#     from aaa import __instance
#     print(__instance)
# def foo2():
#     from aaa import __instance
#     print(__instance)
# f1=foo()#<aaa.Mysql object at 0x0000027B1B339588>
# f2=foo2()#<aaa.Mysql object at 0x0000027B1B339588>



#方式一:
# import settings
# class Mysql:
#     __instance=None
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#     @classmethod
#     def from_conf(cls):
#         if cls.__instance is None:
#             cls.__instance=cls(settings.IP,settings.PORT)
#         return cls.__instance
# obj1=Mysql.from_conf()
# obj2=Mysql.from_conf()
# print(obj1)
# print(obj2)

#方式二:
# import settings
# def singleton(cls):
#     cls.__instance=cls(settings.IP,settings.PORT)
#     def wrapper(*args,**kwargs):
#         if len(args)==0 and len(kwargs)==0:
#             return cls.__instance
#         return cls(*args,**kwargs)
#     return wrapper
# @singleton
# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
# obj1=Mysql()
# obj2=Mysql()
# print(obj1)
# print(obj2)


#方式三:
# import settings
# class Mymeta(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         super().__init__(class_name,class_bases,class_dic)
#         self.__instance=self(settings.IP,settings.PORT)
#     def __call__(self, *args, **kwargs):
#         if len(args)==0 and len(kwargs)==0:
#             return self.__instance
#         obj=self.__new__(self)
#         obj.__init__(*args,**kwargs)
#         return obj
# class Mysql(object,metaclass=Mymeta):
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
# obj1=Mysql()
# obj2=Mysql()
# print(obj1)
# print(obj2)


#方式三:
# import aaa
# def foo1():
#     print(aaa.obj)
# def foo2():
#     print(aaa.obj)
# foo1()
# foo2()




