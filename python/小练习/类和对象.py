# class Oldboystudent:
#     school='Oldboy'
#     def eat(self):
#         print('is eatting')
#     def sleep(self):
#         print("is sleeping")
#     def learn(self):
#         print("is learning")
# # del Oldboystudent.school
# print(Oldboystudent.school)





#为对象初始化自己的特征
#方法一:
# class People():
#     country='China'
#     def run(self):
#         print('--->',self)
# s1=People()
# s1.name='张三'
# print(s1.__dic__)


# class People:
#     def __init__(obj,name,age,sex):
#         obj.name=name
#         obj.age=age
#         obj.sex=sex
#     def run(self):
#         print('---------->',self)
# obj1=People('egon',18,'男')






#方式一:为对象初始化自己独有的特征
# class People:
#     country='China'
#     x=1
#     def run(self):
#         print('--------->',self)
# obj1=People()
# obj2=People()
# obj3=People()
#
# obj1.name='张三'
# obj2.name='李四'
# obj3.name='王五'
#
# obj1.age=18
# obj2.age=20
# obj3.age=30
#
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)


#方式二:为对象初始化自己独有的特征
class People:
    country='China'
    x=1
    def run(self):
        print('')







































