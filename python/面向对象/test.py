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
# print(obj1)
# obj2=Mysql()
# print(obj2)

#方式三:
# import settings
# class Mymeta(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         super(Mymeta,self).__init__(class_name,class_bases,class_dic)
#         self.__instance=self.__new__(self)
#         self.__init__(self.__instance,settings.IP,settings.PORT)
#     def __call__(self, *args, **kwargs):
#         if len(args)==0 and len(kwargs)==0:
#             return self.__instance
#         obj=self.__new__(self)
#         self.__init__(*args,**kwargs)
#         return obj
# class Mysql(object,metaclass=Mymeta):
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
# obj1=Mysql()
# obj2=Mysql()
# print(obj1)
# print(obj2)




# 元类的示例:



















































