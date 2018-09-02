# class Father:
#     pass
# class FOO(Father):
#     pass
# f=FOO()
# print(isinstance(f,FOO))
# print(isinstance([1,2,3],list))
# print(issubclass(FOO,Father))
#
# class People:
#     def __init__(self,age,sex):
#         self.age=age
#         self.sex=sex
# p=People(18,'male')
# print(hasattr(p,'name'))
# print(hasattr(p,'age'))
# delattr(p,'age')
# print(p.__dict__)


# class Ftp:
#     def get(self):
#         print('get')
#     def put(self):
#         print('put')
#     def login(self):
#         print('login')
#     def run(self):
#         while True:
#             cmd=input('>>:')
#             if hasattr(self,cmd):
#                 mothod=getattr(self,cmd)
#                 mothod()
#             else:
#                 print('输入的方法不存在')
# obj=Ftp()
# obj.run()

# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return '<name:%s age:%s>'%(self.name,self.age)
# egon=People('egon',18)
# print(egon)

# import random
# def foo(n):
#     str_all=''
#     for i in range(n):
#         str1=str(random.randint(0,9))
#         str2=chr(random.randint(65,90))
#         str_all+=random.choice([str1,str2])
#     print(str_all)
# foo(4)

# import time
# file_size=50000
# now_size=0
# def foo(persent,with_size=50):
#     if persent>1:persent=1
#     res=('[%%-%ds]'%with_size)%('#'*int(persent*with_size))
#     print('\r%s%s%%'%(res,int(persent*100)),end='')
# while now_size<file_size:
#     time.sleep(1)
#     now_size+=1024
#     persent=now_size/file_size
#     foo(persent)

# print(exec("{'name':'egon'}"))
# with open('db.txt','r',encodin)
