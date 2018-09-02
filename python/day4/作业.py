# 默写:
# 循环嵌套
# db_name='egon'
# db_pwd='123'
# tag=True
# count=0
# while tag:
#     if count>=3:
#         print('已锁定')
#         break
#     name=input('用户名:').strip()
#     pwd=input('密码:').strip()
#     if name==db_name and pwd==db_pwd:
#         print('登录成功')
#         while tag:
#             cmd=input('请输入指令:').strip()
#             if cmd=='q':
#                 tag=False
#                 break
#             else:
#                 print('%s running....'%cmd)
#     else:
#         print('用户名或密码错误')
#         count+=1
# 必做:
#
# 1.
# 求1 - 100
# 的所有数的和
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)
#
# 2.
# 输出
# 1 - 100
# 内的所有奇数
# for i in range(1,101,2):
#     print(i)

#
# 3.
# 输出
# 1 - 100
# 内的所有偶数
# for i in range(2,101,2):
#     print(i)
#
# 5.
# 求1 - 2 + 3 - 4 + 5...
# 99
# 的所有数的和
# sum=0
# for i in range(1,100):
#     if i%2==0:
#         sum-=i
#     else:
#         sum+=i
# print(sum)
#
# 1.
# 打印出所有的1 - 1000
# 中的
# "水仙花数 "，所谓
# "水仙花数 "
# 是指一个三位数，
# 其各位数字立方和等于该数本身。例如153
# for i in range(100,1000):
#     g=i%10
#     s=(i//10)%10
#     b=(i//100)%10
#     aaa=(g**3)+(s**3)+(b**3)
#     if i==aaa:
#         print(i)

#
# 2.
# 每月存款500元
# 连续存款10年
# 年利率为
# 百分之5
# 请算出十年后本金和利息共多少
# 需要考虑复利就是第二年的本金是第一年的本金加第一年的利息
sum=0
year_money=500*12
for i in range(11):
    sum=(sum+year_money)*1.05
print(sum)



# 6.
# 用户登陆（三次机会重试）
# db_name='egon'
# db_pwd='123'
# tag=True
# count=0
# while tag:
#     if count>=3:
#         print('已锁定')
#         break
#     name=input('用户名:').strip()
#     pwd=input('密码:').strip()
#     if name==db_name and pwd==db_pwd:
#         print('登录成功')
#         while tag:
#             cmd=input('请输入指令:').strip()
#             if cmd=='q':
#                 tag=False
#                 break
#             else:
#                 print('%s running....'%cmd)
#     else:
#         print('用户名或密码错误')
#         count+=1

#
# 7.
# 打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s '%(j,i,i*j),end='')
#     print()
#
# 8.
# 打印以下列图案
# 8.1
# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(1,6):
#     for j in range(5-i+1):
#         print('*',end='')
#     print()
# 8.2
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(i):
#         print('*',end='')
#     print()
#
# 8.3
# * * * * *
# * * * *
# * * *
# * *
# *
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(5-i+1):
#         print('*',end='')
#     print()
# for i in range(2,6):
#     for j in range(i):
#         print('*',end='')
#     print()
#
# 9.
# 猜年龄游戏
# 要求：
# 允许用户最多尝试3次，3
# 次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
#
# 10.
# 猜年龄游戏升级版
# 要求：
# 允许用户最多尝试3次
# 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
# 如何猜对了，就直接退出
# tag=True
# count=0
# while tag:
#     if count>=3:
#         aply=input('是否想继续玩(y/n):').strip()
#         if aply=='y':
#             count=0
#         elif aply=='n':
#             tag=False
#             break
#         else:
#             print('非法输入')
#     else:
#         age=input('请输入你猜的年龄:').strip()
#         if age=='18':
#             print('恭喜你猜对了')
#             tag=False
#             break
#         else:
#             print('用户名或密码错误')
#             count+=1

#
# 选做博客题
# # 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
# name = " aleX"
# # 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip())
# # 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
# print(name.startswith('al'))
# # 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# print(name.endswith('X'))
# # 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# print(name.replace('l','p'))
# # 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# print(name.split('l'))
# # 6)    将 name 变量对应的值变大写,并输出结果 
# print(name.upper())
# # 7)    将 name 变量对应的值变小写,并输出结果 
# print(name.lower())
# # 8)    请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# # 9)    请输出 name 变量对应的值的前 3 个字符?
# print(name[0:3])
# # 10)    请输出 name 变量对应的值的后 2 个字符? 
# print(name[-2:])
# # 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# print(name.index('e'))
# # 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# name='oldboy'
# print(name[0:-1])