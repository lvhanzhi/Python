# xxx=444
# class Parent1(object):
#     xxx=333
# class Sun1(Parent1):
#     xxx=222
#     yyy=1
# obj1=Sun1()
# obj1.xxx=111
# print(obj1.xxx)
# print(Sun1.mro())
# print(Sun1.__dict__)


# class People(object):
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class Student(People):
#     def choice_couse(self):
#         print('选课')
# class Teacher(People):
#     def couse(self):
#         print('上课')
# s1=Student('张三',18,'male')
# t1=Teacher('egon',18,'male')
# print(s1.__dict__)
# print(t1.__dict__)



#重用的两种方式:
# 方式一:指名道姓的调用类里面的方法
# class People(object):
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class Student(People):
#     def __init__(self,name,age,sex,core):
#         People.__init__(self,name,age,sex)
#         self.core=core
#     def choice_couse(self):
#         print('选课')
# class Teacher(People):
#     def couse(self):
#         print('上课')
# s1=Student('张三',18,'male',100)
# t1=Teacher('egon',18,'male')
# print(s1.__dict__)
# print(t1.__dict__)

# 方式二:
#


#查找顺序:
# class Bar1:
#     def f1(self):
#         print('Bar f1')
#     def f2(self):
#         print('Bar f2')
#         self.f1()
# class Bar2(Bar1):
#     def f1(self):
#         print('Bar2 f1')
# obj=Bar2()
# obj.f2()
#Bar f2
#Bar2 f1

# class A:
#     def f1(self):
#         print('A.f1')
#         super().f2()
#
# class B:
#     def f2(self):
#         print('B.f2')
#
# class C(A,B):
#     def f2(self):
#         print('C.f2')
#
# obj=C()
# print(C.mro())
# obj.f1()
# """
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# A.f1
# B.f2
# """