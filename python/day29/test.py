# try:
#     a[10]
# except NameError:
#     print('NameError')

# try:
#     a[10]
#     print('start...')#如果上面代码有异常就不会执行这里的代码
# except NameError as e:
#     print('NameError',e)
# except KeyError as e:
#     print('KeyError',e)
# except Exception as e:#万能异常
#     print('这是个万能异常')
# else:
#     print('如果没有异常就会执行')
# finally:
#     print('不管有没有异常都会执行')
# print('end...')







# try:
#     print('===1')
#     d={'name':'egon','age':18}
#     # d['sex']
#     print('==2')
#     l=[1,2]
#     # l[1000]
#     print('=====3')
# except IndexError as e:
#     print('IndexError',e)
# except KeyError as e:
#     print('KeyError',e)
# except Exception as e:
#     print('Exception',e)
# else:
#     print('如果没有抛出异常就会执行')
# finally:
#     print('不管有没有异常都会执行')


#自定义异常类型
# class MyExcoption(BaseException):
#     def __init__(self,msg):
#         super().__init__()
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# raise MyExcoption('自己定义的错误')


#断言
# print('上半部分')
# l=[1,2,3]
# assert len(l)>=0
# print('下半部分')




# class OldboyTeacher:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=self
#     def score(self):
#         print('%s is scoring'%self.name)
# egon=OldboyTeacher('egon',18,'male')
# print(type(egon))
# print(type(OldboyTeacher))


# class_name='OldboyTeacher'
# class_body="""
# def __init__(self,name,age,sex):
#     self.name=name
#     self.age=age
#     self.sex=self
# def score(self):
#     print('%s is scoring'%self.name)
# """
# class_dic={}
# exec(class_body,{},class_dic)
# OldboyTeacher=type(class_name,(object,),class_dic)
# tea=OldboyTeacher('egon',18,'male')
# print(tea.__dict__)


# class Mymeta(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         print(class_name)
#         if class_name.islower():
#             raise  TypeError('类名必须使用驼峰体')
#         doc=class_dic.get(__doc__)
#         if doc is None or len(doc)==0:
#             raise  TypeError("类体中必须要有文档注释")
#
#
#
#
#
# class OldboyTeacher(object,metaclass=Mymeta):
#     """"""
#     def __init__(self,name):
#         self.name=name
# egon=OldboyTeacher('egon')
# print(egon.name)





# class Mymeta(type):
#     def __call__(self, *args, **kwargs):
#         obj=self.__new__(self)
#         self.__init__(obj,*args,**kwargs)
#         return obj
# class OldboyTeacher(object,metaclass=Mymeta):
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# egon=OldboyTeacher('egon',18,'male')
# # print(egon)
# print(egon.__dict__)


#主动触发异常
# print('------>1')
# raise TypeError('类型错误')
# print('------>2')

# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def get_info(self):
#         return '<name:%s age:%s>'%(self.__name,self.__age)
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#             raise TypeError('用户名必须是字符串类型')#主动触发异常
#         if not isinstance(age,int):
#             raise TypeError('年龄必须是int类型')#主动触发异常
#         self.__name=name
#         self.__age=age
# egon=People('egon',18)
# print(egon.get_info())
# egon.set_info('alex','18')
# print(egon.get_info())


# class MyException(BaseException):
#     def __init__(self,msg):
#         super().__init__()
#         self.msg=msg
#     def __str__(self):
#         return '<%s>'%self.msg
# raise MyException('自定义异常')#会自动打印MyException


#断言
# print('上半部分,产生数据')
# l=[1,2,3]
# assert len(l)>5  #如果l的长度大于5就会抛出异常
# print('下半部分,处理数据')

# a=(1)
# # b=(1,2)
# # print(a,type(a))#1 <class 'int'>
# # print(b,type(b))#(1, 2) <class 'tuple'>


# class MyMeta(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         super().__init__(class_name,class_bases,class_dic)
#         if class_name.islower():
#             raise TypeError('类名必须是驼峰体')
#     def __call__(self, *args, **kwargs):
#         obj=self.__new__(self)
#         self.__init__(obj,*args,**kwargs)
#         obj.__dict__={('__%s')%k:v for k,v in obj.__dict__.items()}
#         return obj
# class People(object,metaclass=MyMeta):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_info(self):
#         print('姓名:%s 年龄:%s '%(self.name,self.age))
# egon=People('egon',18)
# egon.get_info()





#方式一:
# import settings
# class Mysql:
#     __instance=None
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#     @classmethod
#     def come_conf(cls):
#         if cls.__instance is None:
#             cls.__instance=cls(settings.IP,settings.PORT)
#         return cls.__instance
# obj1=Mysql.come_conf()
# obj2=Mysql.come_conf()
# print(id(obj1))
# print(id(obj2))


#方式二:
# import settings
# def single(func):
#     def wrapper(*args,**kwargs):
#         if len(args)==0 and len(kwargs)==0:
#             __instance=func(settings.IP,settings.PORT)
#             return __instance
#         else:
#             return func(*args,**kwargs)
#     return wrapper
#
# @single
# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
# obj1=Mysql()
# obj2=Mysql()
# print(obj1)
# print(obj2)


# 方式三
import settings
class MyMeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        super().__init__(class_name,class_bases,class_dic)
        self.__instance = self.__new__(self)
        self.__init__(self.__instance, settings.IP, settings.PORT)
    def __call__(self, *args, **kwargs):
        if len(args)==0 and len(kwargs)==0:
            return self.__instance
        obj=self.__new__(self)
        obj.__init__(obj,*args,**kwargs)
        return obj
class Mysql(object,metaclass=MyMeta):
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
obj1=Mysql()
print(obj1)
obj2=Mysql()
print(obj2)




























