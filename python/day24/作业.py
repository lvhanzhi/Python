# 3.定义一个People类，拥有name、age两个属性和一个eat方法，属性值及方法体可以自定义
# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print('eating')
# 4.根据第3题，重新定义一个People类，该类可以创建两个对象p1、p2，两个对象在一创建后就拥有不同的name、age值，如何设计
# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print('eating')
# p1=People('egon',18)
# p2=People('alex',18)

# 6、下面这段代码的输出结果将是什么？请解释原因。
# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)#1 1 1
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)#1 2 1
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)#3 2 3
#子类没有的属性去父类找,子类的属性变了,同级子类的属性不变,父类的属性变了,子类跟着变

# 7.下面这段代码的输出结果将是什么？请解释原因。
# class Sup(object):
#     x = 1
#     def test(self):
#         print("test - sup")
#
# class Sub1(Sup):
#    def test(self):
#     print("test - sub1")
#
# class Sub2(Sup):
#     x = 2
#
# s = Sup()
# s1 = Sub1()
# s2 = Sub2()
#
# print(s.x)#1
# s.test()#test - sup
# print(s1.x)#1
# s1.test()#test - sub1
# print(s2.x)#2
# s2.test()#test - sup


# 8.下面这段代码的输出结果将是什么？请解释原因。
# class A:
#     def test(self):
#         print("test - A")
# class B:
#     def test(self):
#         print("test - B")
# class C(A, B):
#     pass
# c = C()
# c.test()#test - A

# 9.定义一个X类，有test方法，语句体"test - X"在该方法中打印，定义一个Y类继承X类，语句体"test - Y"在该方法中打印，定义一个Z类继承Y类，语句体"test - Z"在该方法中打印。
# 	现要求：实例化Z类对象：z = Z()，调用test方法：z.test()
# 	打印结果为三句，顺序如下：
# 		--  test - Z
# 		    test - X
# 		    test - Y
# 	如何来设计。

# class X:
#     def test(self):
#         print('test - X')
# class Y(X):
#     def test(self):
#         super().test()
#         print('test - Y')
# class Z(Y):
#     def test(self):
#         print('test - Z')
#         super().test()
# z=Z()
# z.test()

# 10
# http://www.cnblogs.com/linhaifeng/articles/7340497.html#_label1
class Riven:
    def __init__(self,nickname,aggressivity=54,life_value=414,money=1001,armor=3):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
        self.armor=armor
    def attack(self,enemy):
        damage_vlaue=self.aggressivity-enemy.armor
        enemy.life_value-=damage_vlaue
class Garen:
    def __init__(self,nickname,aggressivity=58,life_value=455,money=100,armor=10):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
        self.armor=armor
    def attack(self,enemy):
        damage_vlaue=self.aggressivity-enemy.armor
        enemy.life_value-=damage_vlaue
class BlackCleaver:
    def __init__(self,price=475,aggrev=9,life_value=100):
        self.price=price
        self.aggrev=aggrev
        self.life_value=life_value
    def update(self,obj):
        obj.money-=self.price
        obj.aggressivity+=self.aggrev
        obj.life_value+=self.life_value
    def fire(self,obj):
        obj.life_value-=1000
r1=Riven('草丛伦')
g1=Garen('盖文')
b1=BlackCleaver()
print(r1.aggressivity,r1.life_value,r1.money)
if r1.money>b1.price:
    r1.b1=b1
    b1.update(r1)
print(r1.aggressivity,r1.life_value,r1.money)
print(r1.life_value)
print(g1.life_value)
r1.attack(g1)
print(r1.life_value)
print(g1.life_value)