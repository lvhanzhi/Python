# 1.简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型
#     编译型相当于谷歌翻译,先翻译,翻译之后直接使用,下次不用再进行翻译.运行速度快,开发速度慢(c语言)
#     解释型是边解释边运行的,下次再使用时还要进行解释,开发速度快,运行速度慢(python)
# 2.执行 Python 脚本的两种方式是什么
#     交互式和python D:\test.txt
# 3.Pyhton 单行注释和多行注释分别用什么?
#     单行注释用#,多行注释用"""  """
# 4.布尔值分别有什么?
#     True False
# 5.声明变量注意事项有那些?
#     可以用数字/英文/下划线组成
#     不能以数字开头
#     不能用关键字作为变量名
# 6.如何查看变量在内存中的地址?
#     id()
# 7.写代码
#     实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
# name=input('请输入用户名:').strip()
# pwd=input('请输入密码:').strip()
# if name=='seven' and pwd=='123':
#     print('登录成功')
# else:
#     print('登录失败')
#     实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
# count=0
# while True:
#     if count>=3:
#         break
#     name=input('请输入用户名:').strip()
#     pwd=input('请输入密码:').strip()
#     if name == 'seven' and pwd == '123':
#         print('登录成功')
#         break
#     else:
#         print('登录失败')
#         count+=1
#     实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
# count=0
# while True:
#     if count>=3:
#         break
#     name=input('请输入用户名:').strip()
#     pwd=input('请输入密码:').strip()
#     if (name == 'seven' or name=='alex') and pwd == '123':
#         print('登录成功')
#         break
#     else:
#         print('登录失败')
#         count+=1

# 8.写代码
#     a. 使用while循环实现输出2-3+4-5+6...+100 的和
# sum=0
# i=2
# while i<=100:
#     if i%2==0:
#         sum+=i
#     else:
#         sum-=i
#     i += 1
# print(sum)
#     b. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12 使用 while 循环实现输出 1-100 内的所有奇数
# i=1
# while i<=12:
#     print(i)
#     i+=1

# i=1
# while i<=100:
#     if i%2!=0:
#         print(i)
#     i+=1
#     e. 使用 while 循环实现输出 1-100 内的所有偶数
# i=1
# while i<=100:
#     if i%2==0:
#         print(i)
#     i+=1
# 9.现有如下两个变量,请简述 n1 和 n2 是什么关系?
#       n1 = 123456
#       n2 = n1
#       id(n2)==id(n1)

# 2 作业：编写登陆接口
#
#     基础需求：
#         让用户输入用户名密码
#         认证成功后显示欢迎信息
#         输错三次后退出程序
# dic={
#     '张三':{
#         'pwd':'123',
#         'count':0
#     },
#     '李四':{
#         'pwd':'123',
#         'count':0
#     },
#     '王五':{
#         'pwd':'123',
#         'count':0
#     }
# }
# while True:
#     name=input('name:').strip()
#     if not name in dic:
#         print('用户名不存在')
#         continue
#     pwd=input('pwd:').strip()
#     if pwd==dic[name]['pwd']:
#         print('登录成功')
#         break
#     else:
#         print('密码错误')
#         dic[name]['count']+=1
#         if dic[name]['count'] >= 3:
#             break


# 升级需求：
#
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）
db_txt=r'db.txt'
dic={
    '张三':{
        'pwd':'123',
        'count':0
    },
    '李四': {
        'pwd': '123',
        'count': 0
    },
    '王五': {
        'pwd': '123',
        'count': 0
    }
}
while True:
    name=input('name:').strip()
    if not name in dic:
        print('该用户不存在')
        continue
    with open(db_txt,'r',encoding='utf8')as f:
        info=f.read()
        info=info.split(',')
        if name in info:
            break

    pwd=input('pwd:').strip()
    if pwd==dic[name]['pwd']:
        print('登录成功')
        break
    else:
        dic[name]['count']+=1
        if dic[name]['count']==3:
            with open(db_txt,'a',encoding='utf8')as f:
                f.write(name+',')