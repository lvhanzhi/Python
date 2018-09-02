# # 1.创建字符串变量的三种写法及其区别
# # 代码：
# a='123'
# b="123"
# c="""123"""
# # 区别：
# 三引号是固定格式输出
# print('a"b"c')
# print("a'b'c")
#
# # 2.
# # 简述，计算机编程语言的分类及特点
# 1.机器语言:执行速度快,开发速度慢,需要知道计算机底层,用二进制
# 2.汇编语言:执行速度慢于机器语言,开发速度快于机器语言,用简单的字符代替二进制,需要知道计算器底层
# 3.高级语言
#     3.1编译型:需要编译器,再次执行时直接使用,执行速度慢于汇编语言,开发速度高于汇编语言
#     3.2解释型:需要用到解释器,解释一行执行一行,执行速度慢于编译型,开发速度高于编译型
#
# # 3.何时使用变量，何时使用常量，并举例子
# 生日是常量,年龄是变量
# # 4.使用字典保存各省的省会是什么以及省会的信息，
# # 例如
# # 北京市
# # 省会：直辖市
# # 面积：XX
# # 人口：XX
# # 浙江省： 省会：杭州市
# # 面积：XX
# # 人口：XX
# # 最后取出北京市按以下格式打印
# # == == == == = 北京 == == == ==
# # 省会：直辖市
# # 面积：xxx
# # 人口：xxx
# # == == == == = end == == == ==
# dic={
#     '北京市':{
#         '省会':'直辖市',
#         '面积':'XX',
#         '人口':'XX',
#     },
#     '浙江省':{
#             '省会':'杭州市',
#             '面积':'XX',
#             '人口':'XX',
#         },
# }
# print("""
#  == == == == = 北京 == == == ==
#  省会：%s
#  面积：%s
#  人口：%s
#  == == == == = end == == == ==
# """%(dic['北京市']['省会'],dic['北京市']['面积'],dic['北京市']['人口']))
# # 5.
# # 使用逻辑运算符处理生活中任意事情
# # 例如，成功取钱的
# # 条件
# # 密码正确
# # 并且
# # 余额充足
# # 成功约会的
# # 条件
# # 个子高
# # 颜值高
# # 或者
# # 有钱
# #
# user=['tom','123',15000]
# while True:
#     name=input('name:').strip()
#     pwd=input('pwd:').strip()
#     if name==user[0] and pwd==user[2]:
#         print('登录成功')
#         money=input('请输入金额:').strip()
#         if user[2]>=money:
#             user[2]-=money
#             print('成功取钱%s,余额%s'%(money,user[2]))
#         else:
#             print('余额不足')
#         break
#     else:
#         print('用户名或密码错误')
#         continue
# # 6.
# # 设计程序实现如下功能，要求用户输入两个数
# # 加减乘除
# # 可使用四个文件每个文件完成一种运算
# # 或使用if
# x=input('x:').strip()
# symbol=input('>>:').strip()
# y=input('y:').strip()
# if symbol=='+':
#     print(x+y)
# elif symbol=='-':
#     print(x-y)
# elif symbol=='*':
#     print(x*y)
# elif symbol=='/':
#     print(x/y)
# else:
#     print('非法输入')
# # 7.
# # 简述python内存管理
# 垃圾回收机制
# # 8.
# # 编写代码测试
# # 字符串
# # 列表
# # 比较大小的原理
# # 做出总结
# print('abcde'<'bcde')
# print(['a','b','c']<['b','c','d'])
# 只能字符串和字符串,列表和列表对比
# 两个第一个字符比较ASCIIA码,要是相等则比较下一个字符
# # 9.
# # 扩展题
# # 作业：编写登陆接口
# #
# #     基础需求：
# #         让用户输入用户名密码
# #         认证成功后显示欢迎信息
# #         输错三次后退出程序
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
#
#
# # 升级需求：
# #
# # 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# # 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）
# db_txt=r'db.txt'
# dic={
#     '张三':{
#         'pwd':'123',
#         'count':0
#     },
#     '李四': {
#         'pwd': '123',
#         'count': 0
#     },
#     '王五': {
#         'pwd': '123',
#         'count': 0
#     }
# }
# while True:
#     name=input('name:').strip()
#     if not name in dic:
#         print('该用户不存在')
#         continue
#     with open(db_txt,'r',encoding='utf8')as f:
#         info=f.read()
#         info=info.split(',')
#         if name in info:
#             break
#
#     pwd=input('pwd:').strip()
#     if pwd==dic[name]['pwd']:
#         print('登录成功')
#         break
#     else:
#         dic[name]['count']+=1
#         if dic[name]['count']==3:
#             with open(db_txt,'a',encoding='utf8')as f:
#                 f.write(name+',')