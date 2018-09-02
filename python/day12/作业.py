# 作业：
# 1使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)
# def foo(x,y):
#     if x==0:
#         print(x)
#         print(y)
#     print(x+y)
#     foo(y,x+y)
# foo(0,1)


# 2一个嵌套很多层的列表，如l =［1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]］，用递归取出所有的值
# l =[1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]
# def foo(l):
#     for i in l:
#         if type(i) is list:
#             foo(i)
#         else:
#             print(i)
# foo(l)
# 3编写用户登录装饰器，在登录成功后无需重新登录，同一账号重复输错三次密码则锁定5分钟
# import os,time
# def user_info(name):
#     with open('db.txt','r',encoding='utf8')as f:
#         for line in f:
#             line=line.strip('\n').split(',')
#             if name==line[0]:
#                 return line
#         else:
#             return None
# def login(func):
#     def wrapper(*args,**kwargs):
#         name=input('请输入用户名:').strip()
#         user=user_info(name)
#         if user:
#             if user[2]>='3' and user[3]=='None':
#                 now_time = time.time()
#                 with open('db.txt', 'r', encoding='utf8')as read_f, \
#                         open('db.txt.swap', 'w', encoding='utf8')as write_f:
#                     for line in read_f:
#                         line = line.strip('\n').split(',')
#                         if line[0] == name:
#                             line[3] = str(now_time)
#                             line = ','.join(line) + '\n'
#                         write_f.write(line)
#                 os.remove('db.txt')
#                 os.rename('db.txt.swap','db.txt')
#             elif user[2]>='3' and float(user[3])+300<=time.time():
#                 with open('db.txt', 'r', encoding='utf8')as read_f, \
#                         open('db.txt.swap', 'w', encoding='utf8')as write_f:
#                     for line in read_f:
#                         line = line.strip('\n').split(',')
#                         if line[0] == name:
#                             line[2]='1'
#                             line[3] = 'None'
#                             line = ','.join(line) + '\n'
#                         write_f.write(line)
#                 os.remove('db.txt')
#                 os.rename('db.txt.swap','db.txt')
#             if user[-1]=='None':
#                 pwd = input('请输入密码:').strip()
#                 if user[1] == pwd:
#                     print('恭喜登录成功')
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('用户名或密码错误')
#                     with open('db.txt', 'r', encoding='utf8')as read_f, \
#                             open('db.txt.swap', 'w', encoding='utf8')as write_f:
#                         for line in read_f:
#                             line = line.strip('\n').split(',')
#                             if line[0] == name:
#                                 line[2] = str(int(line[2]) + 1)
#                                 line = ','.join(line) + '\n'
#                             write_f.write(line)
#                     os.remove('db.txt')
#                     os.rename('db.txt.swap', 'db.txt')
#             else:
#                 print('还未解锁')
#         else:
#             print('该用户不存在')
#     return wrapper
# @login
# def foo():
#     print('running...')
# foo()
# 4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
# with open('a.txt','r',encoding='utf8')as f:
#     print(sum(len(line.strip('\n')) for line in f))
#     f.seek(0)
#     print(sum(len(line.strip('\n')) for line in f))
# 光标在最后面了
# 5、文件shopping.txt内容如下
# mac, 20000, 3
# lenovo, 3000, 10
# tesla, 1000000, 10
# chicken, 200, 1
# 求总共花了多少钱？
# sum=0
# with open('shopping.txt','r',encoding='utf8')as f:
#     for line in f:
#         line=line.strip('\n').split(',')
#         sum+=(int(line[1])*int(line[2]))
# print(sum)
# 打印出所有商品的信息，格式为[{'name': 'xxx', 'price': 333, 'count': 3}, ...]
# l=[]
# with open('shopping.txt','r',encoding='utf8')as f:
#     for line in f:
#         dic = {}
#         line=line.strip('\n').split(',')
#         dic['name']=line[0]
#         dic['price']=line[1]
#         dic['count']=line[2]
#         l.append(dic)
# print(l)
# 求单价大于10000的商品信息, 格式同上
# for i in l:
#     if int(i['price'])>10000:
#         print(i)
