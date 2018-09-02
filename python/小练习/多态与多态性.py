# 多态:多态指同一种事物的多种形态
# 多态的父类不能被实例化
# 为何要用多态:
# 多态性:
#     继承同一个类的多个子类中有相同的方法名
#     那么子类产生的对象就可以不用考虑具体的类型而直接调用功能


# import abc
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def speak(self):
#         pass
# class People(Animal):
#     def speak(self):
#         print('wawawa')
# class Pig(Animal):
#     def speak(self):
#         print('aaa')
#
# p1=People()
# p1.speak()


#python 推崇的是鸭子类型,只要你叫的像鸭子.并且你走路的样子也像鸭子,那你就是鸭子

class TxtFile:
    def read(self):
        pass
    def write(self):
        pass
class DiskFile:
    def read(self):
        pass
    def write(self):
        pass




















