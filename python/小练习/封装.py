# 封装:
#     如何隐藏属性:在属性前加上__开头
#             这种隐藏是对外不对内的,即在类的内部可以直接访问,而在类的外部则无法直接访问
#     封装的真实意图与用法
#     property
#
# 绑定方法与非绑定方法
#
# 什么是封装:
#     封:属性对外是隐藏的,但对内是开放的
#     装:申请一个名称空间,往里装一系列名字/属性
#
# 为什么要封装:
#     封装数据属性的目的
#         首先定义属性的目的就是为了给类外部的使用的,
#         隐藏之后就是为了不让外部直接使用,需要类内部开辟一个接口
#         然后让类外部的使用通过接口来间接地操作隐藏的属性
#         精髓在于:我们可以在接口上附加任意逻辑,从而严格控制使用者对属性的操作
#
#         封装函数属性:
#             首先定义属性的目的就是为了给类外部使用的,
#             隐藏函数属性是为了不让外部直接使用,需要类内部开辟一个接口
#             然后在接口内去调用隐藏的功能
#             精髓在于:隔离了复杂度
# class People:
#     __country='China'#封装类属性的私有属性(就是类属性前加__)
#     def __init__(self,name):
#         self.__name=name#封装类对象的私有属性
#     def __eat(self):#封装类方法的私有属性
#         print('eatting...')
# p=People('egon')
# print(p._People__country)
# print(p._People__name)
# p._People__eat()
#
# class People:
#     __country = 'China'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print('eat...')
#         print(People.__country)
#
#
# p = People('张三', 88, 'male')
#
#
# print(p.__country)
# p.eat()
# print(p._People__country)
#
#
# 查:
# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def tell_info(self):
#         print(self.__name,self.__age)
# peo1=People('egon',18)
# peo1.tell_info()
#
#
# 改
# class People:
#     country = 'China'
#
#     def __init__(self, name, age, sex):
#         self.__name = name
#         self.__age = age
#         self.__sex = sex
#
#     def set_name(self, x):
#         if type(x) is not str:
#             print('名字必须是str类型')
#             return
#         self.__name = x
#
#
# p1 = People('张三', 88, 'male')
# p1.set_name(1)
# print(p1.__dict__)
#
#
# 自己添加一个错误
# raise TypeError('类型错误')