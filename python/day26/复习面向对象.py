# class OldboyStudent:
#     school='Oldboy'
#     def choose_course(self):
#         print('is choosing course')
# print(OldboyStudent.__dict__)
# print(OldboyStudent.__dict__['school'])
# print(OldboyStudent.school)
# print(OldboyStudent.choose_course)
# OldboyStudent.choose_course(1)
# OldboyStudent.country='English'
# print(OldboyStudent.country)
# del OldboyStudent.school

# class Foo:
#     pass
# class Foo2(Foo):
#     pass
# f=Foo2()
# # print(Foo)
# # obj=Foo()
# # print(type(obj))
# print(Foo.__name__)
# print(Foo.__dict__)
# print(dir(Foo))
# print(Foo.__module__)
# print(f.__class__.__name__)
# print(isinstance(f,Foo2))

# class People:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         People.count+=1
# egon=People('egon')
# print(egon.count)
# alex=People('alex')
# print(alex.count)

# class Person:
#     def __init__(self,name,attack,life_value):
#         self.name=name
#         self.attack=attack
#         self.life_value=life_value
#     def attacking(self):
#         dog.life_value=dog.life_value-self.attack
# class Dog:
#     def __init__(self,name,attack,life_value):
#         self.name=name
#         self.attack=attack
#         self.life_value=life_value
#     def attacking(self):
#         egon.life_value=egon.life_value-self.attack
# egon=Person('egon',20,100)
# dog=Dog('dog',10,100)
# print('egon的生命',egon.life_value)
# print('dog的生命',dog.life_value)
# egon.attacking()
# print('egon的生命',egon.life_value)
# print('dog的生命',dog.life_value)


# class Birthday:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
# class Course:
#     def __init__(self,name,price,period):
#         self.name=name
#         self.price=price
#         self.period=period
# class Teacher:
#     def __init__(self,name,year,month,day,price,period,salary):
#         self.name=name
#         self.salary=salary
#         self.birthday=Birthday(year,month,day)
#         self.course=Course(name,price,period)
# egon=Teacher('egon',1998,5,5,19800,5.5,2000)

# class Birthday:
#     def __init__(self,year,mothday,day):
#         self.year=year
#         self.mothday=mothday
#         self.day=day
# class Course:
#     def __init__(self,name,period,price):
#         self.name=name
#         self.period=period
#         self.price=price
# class Teacher:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# egg=Teacher('egon',28,'male')
# egg.birthday=Birthday(2018,8,14)
# print(egg.birthday.year)
# egg.course=Course('python',5.5,158000)
# print(egg.course.name)

# class A:
#     def test(self):
#         print('a')
# class B(A):
#     def test(self):
#         print('b')
# obj=B()
# print(B.mro())

# class People:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class Student(People):
#     def __init__(self,name,age,sex):
#         People.__init__(self,name,age,sex)
# stu=Student('tom',18,'male')
# print(stu.__dict__)

# class People:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class Teacher(People):
#     def __init__(self,name,age,sex):
#         super(Teacher,self).__init__(name,age,sex)
# tea=Teacher('egon',18,'male')
# print(tea.__dict__)