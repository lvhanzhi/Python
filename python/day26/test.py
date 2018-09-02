# class People:
#     def foo(self):
#         print(self)
#     @classmethod
#     def foo2(cls):
#         print(cls)
#     @staticmethod
#     def foo3():
#         print('foo3')
# p=People()
# print(p.foo)#<bound method People.foo of <__main__.People object at 0x00000231398696D8>>
# print(People.foo2)#<bound method People.foo2 of <class '__main__.People'>>
# print(p.foo2)#<bound method People.foo2 of <class '__main__.People'>>
# print(People.foo3)#<function People.foo3 at 0x000001C4FF1F3488>
# print(p.foo3)#<function People.foo3 at 0x000001E12A513488>


# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#     def tell_info(self):
#         print('<ip:%s port:%s>'%(self.ip,self.port))
# obj=Mysql('1.1.1.1',3306)
# obj.tell_info()

# import settings
# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#     def tell_info(self):
#         print('<ip:%s port:%s>'%(self.ip,self.port))
#     @classmethod
#     def from_conf(cls):
#         return Mysql(settings.IP,settings.PORT)
#
# obj=Mysql.from_conf()
# obj.tell_info()

# 实例化的两种方式:
# 1.类加括号
# obj=Mysql('1.1.1.1',3306)
# 2.在类里面直接返回:
# import settings
# class Mysql:
#     @classmethod
#     def from_conf(cls):
#         return Mysql(settings.IP,settings.PORT)
# obj=Mysql.from_conf()

import uuid
class Mysql:
    @staticmethod
    def create_id():
        return uuid.uuid4()
print(Mysql.create_id())
#a6fe2472-b9a9-4ae0-ba85-1c5078a67af7