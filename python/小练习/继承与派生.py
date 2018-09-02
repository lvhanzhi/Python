# 1.什么是继承
    #继承就是创造一个新类的方法,被创造的类叫子类,被继承的类叫父类
#     继承的特征:
#       子类继承父类的属性
# 2为什么要用继承
#   减少代码的冗余
# 3如何继承
#在pthon中子类可以继承多个父类
    # 在python3中如果没有继承的父类,就会继承object类
    # 在python2中如果没有继承父类,就不会继承object类
# class father:
#     pass
# class son(father):
#     pass
# print(son.__bases__)


# class People:
#     school='oldboy'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# class Teacher(People):
#     def grade(self):
#         print('%s打分'%self.name)
#
# class Student(People):
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def curricula(self):
#         print('%s正在选课'%self.name)
#
# student1=Student('二狗',8,'男')
# teacher1=Teacher('张老师',5,'男')
#
# print(student1.school)
# print(teacher1.name)


#__init__方法:在调用类/实例化时自动触发,为对象初始化自己独有的特征
#派生:在子类中调用新属性,在使用中,以自己为准



# class oldboy_people:
#     country='China'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class student(oldboy_people):
#     def __init__(self,id,name,age,sex):
#         self.id=id
#         oldboy_people.__init__(self,name,age,sex)
#
# s1=student(1,'二狗',15,'男')
# print(s1.__dict__)




#菱形继承:当一个子类继承多个父类,多个父类最终继承同一个类,称为菱形继承

#旧式类深度优先:一条路走到底,再走旁边的分支
#新式类广度优先:走到最后第二个,再走旁边分支

#c3算法
# class A:
#     def  test(self):
#         print('a')
# class B(A):
#     def test(self):
#         print(b)
# obj=B()
# print(B.mro())



#在子类派生的新方法中重用父类功能的两种方式
#方式一:指名道姓法,直接用,与继承无关

# class People:
#     countyr='China'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# class Teacher(People):
#     def __init__(self,name,age,sex):
#         People.__init__(self,name,age,sex)
#
# s1=Teacher('张三',5,'male')
# print(s1.__dict__)



#方式二:严格以继承属性来查找
#super()会得到一个特殊的对象,该对象就是专门用来访问父类中的属性(按照继承关系)
# super(Teacher.self).__init__(name,age,sex),在python2中要写完整
# class People:
#     countyr='China'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# class Teacher(People):
#     def __init__(self,name,age,sex):
#         super().__init__(name,age,sex)
#
# s1=Teacher('张三',5,'male')
# print(s1.__dict__)



class A:
    def f1(self):
        print('A.f1')
class B:
    def f2(self):
        super().f1()
class C(B,A):
    pass
obj=C()
obj.f2()














