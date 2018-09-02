# # 1
# name=input('name:').strip()
# pwd=input('pwd:').strip()
# if name=='张三' and pwd=='123':
#     print('登录成功')
# else:
#     print('用户名或密码错误')
# #2
# name=input('name:').strip()
# pwd=input('pwd:').strip()
# if name=='张三':
#     print('管理员')
# elif name=='张三':
#     print('员工')
# else:
#     print('普通人')
#
# #3
# day=input('请输入今天是星期几:').strip()
# if day in ['星期一','星期二','星期三','星期四','星期五']:
#     print('上班')
# elif day in ['星期六','星期天']:
#     print('出去浪')
#
# #4
# user_from_db='egon'
# pwd_from_db='123'
# tag=True
# while tag:
#     inp_user=input('please input your username:')
#     inp_pwd=input('please input your password:')
#     if inp_user==user_from_db and inp_pwd==pwd_from_db:
#         print('login successfull')
#         while tag:
#             cmd=input('>>>:')
#             if cmd=='quit':
#                 tag=False
#                 break
#             print('%s run...'%cmd)
#     else:
#         print('user or password err')
#
# #5 while+else:
# n=1
# while n<5:
#     print(n)
#     n+=1
# else:
#     print('===>')
#
# 6 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s '%(i,j,i*j),end='')
#     print()

#7 金字塔:
# n=input('请输入层数:').strip()
# n=int(n)
# for x in range(1,n+1):
#     for i in range(n-x):
#         print(' ',end='')
#     for j in range(2*x-1):
#         print('*',end='')
#     print()

