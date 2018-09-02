# class OldboyPeople:
#     school='oldboy'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class Student(OldboyPeople):
#     def __init__(self,name,age,sex,score=0):
#         OldboyPeople.__init__(self,name,age,sex)
#         self.score=score
#         self.courses=[]
#     def choose_course(self):
#         print('%s正在选课'%self.name)
#     def see_course_info(self):
#         for obj in self.courses:
#             course_info=obj.tell_course_info
#
# class Course:
#     def __init__(self,name,money,shichang):
#         self.name=name
#         self.money=money
#         self.shichang=shichang
#     def tell_course_info(self):
#         print('<课程名字:%s 价格:%s 时间:%s>'%(self.name,self.money,self.shichang))


# class Foo:
#     def f1(self):
#         print('Foo.f1')
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
# obj=Bar()
# obj.f2()
# # Foo.f2
# # Bar.f1
# 类在定义阶段就检测语法,把__开头的属性转成 _类名__属性名
# class Foo:
#     def __f1(self):
#         print('Foo.f1')
#     def f2(self):
#         print('Foo.f2')
#         self.__f1()
# class Bar(Foo):
#     def __f1(self):
#         print('Bar.f1')
# obj=Bar()
# obj.f2()
# #Foo.f2
# #Foo.f1

# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def tell_info(self):
#         print('姓名:%s 年龄:%s'%(self.__name,self.__age))
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#             print('名字必须是字符串类型')
#             return
#         elif not isinstance(age,int):
#             print('年龄必须是整型')
#             return
#         self.__name=name
#         self.__age=age
# egon=People('egon',18)
# egon.tell_info()
# egon.set_info(11,11)
# egon.tell_info()
# egon.set_info('alex',11)
# egon.tell_info()

# class People:
#     def __init__(self,height,weight):
#         self.height=height
#         self.weight=weight
#     @property
#     def BIM(self):
#         print(self.weight/(self.height**2))
# egon=People(1.5,42.35)
# egon.BIM

# class Foo1:
#     pass
# class Foo2:
#     pass
# class Foo3:
#     pass
# class Bar:
#     pass
# obj_from_bar=Bar()
# obj1=Foo1()
# obj2=Foo2()
# obj3=Foo3()
# obj1.attr1=obj_from_bar
# obj2.attr2=obj_from_bar
# obj3.attr3=obj_from_bar

# class OldboyPeople:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class Course:
#     def __init__(self,c_name,c_price,c_period):
#         self.c_name=c_name
#         self.c_price=c_price
#         self.c_period=c_period
#     def tell_course(self):
#         print('<课程名字:%s 课程价格:%s 课程时长:%s>'%(self.c_name,self.c_price,self.c_period))
# class OldboyStudent(OldboyPeople):
#     def __init__(self,name,age,sex,score=0):
#         OldboyPeople.__init__(self,name,age,sex)
#         self.score=score
#         self.courses=[]
#     def choose_course(self):
#         print('%s正在选课')
#     def tell_course_info(self):
#         print(('%s的课程'%self.name).center(50,'*'))
#         for i in self.courses:
#             i.tell_course()
#         print('*'*60)
# class OldboyTeacher(OldboyPeople):
#     def __init__(self,name,age,sex,revel):
#         OldboyPeople.__init__(self,name,age,sex)
#         self.revel=revel
#         self.courses=[]
#     def core(self,stu,num):
#         stu.score=num
#     def tell_course_info(self):
#         print(('%s教授的课程'%self.name).center(50,'*'))
#         for i in self.courses:
#             i.tell_course()
#         print('*'*60)
# python=Course('python全站开发',18000,'5个月')
# linux=Course('linux架构师',18000,'5个月')
# stu1=OldboyStudent('tom',18,'male')
# stu1.courses.append(linux)
# stu1.courses.append(python)
# stu1.tell_course_info()
#
# tea1=OldboyTeacher('egon',18,'male','10')
# tea1.courses.append(python)
# tea1.tell_course_info()


# class Animal:
#     def speak(self):
#         pass
# class People(Animal):
#     def shuo(self):
#         print('say hello')
# class Dog(Animal):
#     def jiao(self):
#         print('汪汪汪')
# class Pig(Animal):
#     def chang(self):
#         print('哼哼哼')
# obj1=People()
# obj2=Dog()
# obj3=Pig()
# obj1.speak()
# obj2.speak()
# obj3.speak()
# def speak(animal):
#     animal.speak()
# speak(obj1)

# import abc
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def speak(self):
#         pass
# class Cat(Animal):
#     def speak(self):
#         pass
# cat=Cat()



class People:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name
    def del_name(self):
        del self.__name
    name=property(get_name,set_name,del_name)
p=People('egon')
print(p.name)