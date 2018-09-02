# property 装饰器用于将被装饰的方法伪装成一个数据属性,在使用时可以不用加括号而直接调用
# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#     @property
#     def bmi(self):
#         return self.weight/(self.height**2)
# p=People('张三',50,1.5)
# print(p.bmi)
#
#
# class People:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         if not isinstance(name,str):
#             raise TypeError('名字必须是str')
#         self.__name=name
#     @name.deleter
#     def name(self):
#         raise TypeError('不能删除')
# p=People('张三')
# p.name='李四'
# del p.name
# print(p.name)
#
#
#
#
#
# class People:
#     def __init__(self,name):
#         self.name=name
#
# p=People('张三')
# del p.name
# print(p.__dict__)