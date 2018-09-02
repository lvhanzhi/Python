# # 面向过程是什么:
# #     优点.缺点
# #
# # 面向过程是什么:
# #
# # 类是什么:
# #定义函数是只检测代码,不执行函数.
# #类体代码会在定义阶段就立刻执行,产生一个类的名称空间
# class OldboyStudent:
#     school='Oldboy'
#     def choose_course(self):
#         print('is choosing course')
#     print('===========>')
# #查看类的名称空间
# print(OldboyStudent.__dict__)
# print(OldboyStudent.__dict__['school'])
#
# print(OldboyStudent.school)
# print(OldboyStudent.choose_course(111))
# #增
# OldboyStudent.country='China'
# print(OldboyStudent.country)
# #改
# OldboyStudent.country='English'
# print(OldboyStudent.country)
# #删
# del OldboyStudent.school
# # print(OldboyStudent.school)
#
# #类的实例化,实例化的结果称为类的对象/实例
# student1=OldboyStudent()#调用一个类就会产生一个具体存在的对象/实例
# #类的实例化过程都发生了哪些事
# #如何在实例化的过程中为对象制定自己独有的特征
# student1.name='张三'
# #程序中对象到底是什么,如何使用

# 类的本质就是一个名称空间/容器


# 今日内容:
#     1.如何为对象定制独有的特征,__init__方法
#     2.属性查找
#     3.绑定方法
#     4.面向对象三大特征之一:继承与派生


# init方法为对象初始化自己独有的特征
# 方法一:
# class People:
#     country='China'
#     x=1
#     def run(self):
#         print('-------->',self)
# obj1=People()
# obj1.name='张三'
# obj1.aeg=18
# obj1.sex='男'
#
# print(obj1.__dict__)

# 方法二:
# class People:
#     country='China'
#     x=1
#     def run(self):
#         print('---------->',self)
# obj1=People()
# def chu_shi_hua(obj,name,age,sex):
#     obj.name=name
#     obj.age=age
#     obj.sex=sex
# chu_shi_hua(obj1,'张三',15,'男')
# print(obj1.__dict__)


# 方法三
# class People:
#     country='China'
#     x=1
#     def chu_shi_hua(obj,name,age,sex):
#         obj.name=name
#         obj.age=age
#         obj.sex=sex
#     def run(self):
#         print('------->',self)
# obj1=People()
# People.chu_shi_hua(obj1,'张三',14,'男')
# print(obj1.__dict__)


# 方法四
# class People:
#     country='China'
#     x=1
#     count=0
#     def __init__(obj,name,age,sex):
#         obj.name=name
#         obj.age=age
#         obj.sex=sex
#         People.count+=1
#     def run(self):
#         print('---------->',self)
# obj1=People('张三',1,'男')
# print(obj1.__dict__)
# print(obj1.count)
# print(People.count)


#类中定义的函数,是类的函数属性,是一个普通的函数,该传几个 值就传几个值
#类中定义的函数是共享给所有对象,对象可以使用,而且是绑定给对象用的
#绑定的作用是不用手动,直接调用的时候就会使用
#self 的作用主要是绑定


#在python3中统一了类和类型的概念



# l=[1,2,3]
# print(type(l))
# list.append(l,4)
# print(l)


#对象是一个高度整合的产物,整合了数据和处理数据的方法(绑定方法)

#对象查找的顺序:对象自己/对象的类/父类/父类...




















