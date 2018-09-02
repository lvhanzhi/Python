# 作业：
# 	编写用户注册函数，实现功能
# 		1、在函数内接收用户输入的用户名、密码、余额
# 			要求用户输入的用户名必须为字符串，并且保证用户输入的用户名不与其他用户重复
# 			要求用户输入两次密码，确认输入一致
# 			要求用户输入的余额必须为数字
# 		2、要求注册的用户信息全部存放于文件中


# def register():
#     tag=True
#     while tag:
#         name = input('请输入用户名:').strip()
#         with open('db.txt', 'r', encoding='utf8')as f:
#             for line in f:
#                 info = line.strip('\n').split(',')
#                 if name == info[0]:
#                     print('该用户已存在')
#                     break
#             else:
#                 tag=False
#                 break
#     while True:
#         pwd1=input('请输入密码:').strip()
#         pwd2=input('请再次输入密码:').strip()
#         if pwd2==pwd1:
#             balance=input('请输入充值金额:').strip()
#             if balance.isdigit():
#                 break
#             else:
#                 print('非法输入')
#         else:
#             print('两次密码不一致,请重新输入')
#     with open('db.txt','a',encoding='utf8')as f:
#         f.write('%s,%s,%s\n'%(name,pwd1,balance))
#     print('恭喜注册成功')
# register()




                # 	编写用户转账函数，实现功能
# 		1、传入源账户名（保证必须为str）、目标账户名（保证必须为str）、转账金额（保证必须为数字）
# 		2、实现源账户减钱，目标账户加钱
# import os
# def user_info(name):
#     with open('db.txt', 'r', encoding='utf8')as f:
#         for line in f:
#             info = line.strip('\n').split(',')
#             if name==info[0]:
#                 return info
#         else:
#             return False
# def update_user_info(name,balance):
#     with open('db.txt','r',encoding='utf8')as read_f,\
#         open('db.txt.swap','w',encoding='utf8')as write_f:
#         for line in read_f:
#             info=line.strip('\n').split(',')
#             if name==info[0]:
#                 info[2]=str(balance)
#             line=','.join(info)+'\n'
#             write_f.write(line)
#     os.remove('db.txt')
#     os.rename('db.txt.swap','db.txt')
#
# def transfer():
#     while True:
#         out_name = input('请输入你的姓名:').strip()
#         if user_info(out_name):
#             out_money=int(user_info(out_name)[2])
#         else:
#             print('用户不存在')
#             continue
#         in_name=input('请输入要转账的用户姓名:').strip()
#         if user_info(in_name):
#             in_money=int(user_info(in_name)[2])
#         else:
#             print('用户不存在')
#             continue
#         add_money=input('请输入要转账的金额:').strip()
#         if add_money.isdigit():
#             add_money=int(add_money)
#             out_money-=add_money
#             in_money+=add_money
#             update_user_info(out_name,out_money)
#             update_user_info(in_name,in_money)
#             print('转账成功')
#         else:
#             print('转账金额必须是数字')
# transfer()






# 	编写用户验证函数，实现功能
# 		1、用户输入账号，密码，然后与文件中存放的账号密码验证
# 		2、同一账号输错密码三次则锁定
#
# 		3、这一项为选做功能：锁定的账号，在五分钟内无法再次登录
# 			提示：一旦用户锁定，则将用户名与当前时间写入文件,例如: egon:1522134383.29839
# 				实现方式如下：
#
# 				import time
#
# 				current_time=time.time()
# 				current_time=str(current_time) #当前的时间是浮点数，要存放于文件，需要转成字符串
# 				lock_user='%s:%s\n' %('egon',current_time)
#
# 				然后打开文件
# 				f.write(lock_user)
#
# 				以后再次执行用户验证功能，先判断用户输入的用户名是否是锁定的用户，如果是，再用当前时间time.time()减去锁定的用户名后
# 				的时间，如果得出的结果小于300秒，则直接终止函数，无法认证，否则就从文件中清除锁定的用户信息，并允许用户进行认证
import os,time
def update_user_info(name,count):
    with open('db.txt','r',encoding='utf8')as read_f,\
        open('db.txt.swap','w',encoding='utf8')as write_f:
        for line in read_f:
            info=line.strip('\n').split(',')
            if name==info[0]:
                    info[3]=str(count)
            line=','.join(info)+'\n'
            write_f.write(line)
    os.remove('db.txt')
    os.rename('db.txt.swap','db.txt')
def user_info(name):
    with open('db.txt', 'r', encoding='utf8')as f:
        for line in f:
            info = line.strip('\n').split(',')
            if name==info[0]:
                return info
        else:
            return False
def login():
    while True:
        name=input('请输入用户名:').strip()
        info=user_info(name)
        if info:
            if int(info[3])==3:
                if time.time()>float(info[-1])+5:
                    with open('db.txt', 'r', encoding='utf8')as read_f, \
                            open('db.txt.swap', 'w', encoding='utf8')as write_f:
                        for line in read_f:
                            info = line.strip('\n').split(',')
                            if name == info[0]:
                                info.pop(-1)
                                info[3]='0'
                            line = ','.join(info) + '\n'
                            write_f.write(line)
                    os.remove('db.txt')
                    os.rename('db.txt.swap', 'db.txt')
                else:
                    print('账户已锁定')
                    break
            pwd=input('请输入密码:').strip()
            if info[1]==pwd:
                print('登录成功')
                break
            else:
                count=int(info[3])+1
                update_user_info(name,count)
                print('用户名或密码错误,请重新输入')
                if count==3:
                    with open('db.txt', 'r', encoding='utf8')as read_f, \
                            open('db.txt.swap', 'w', encoding='utf8')as write_f:
                        for line in read_f:
                            info = line.strip('\n').split(',')
                            if name == info[0]:
                                info.append(time.time())
                                info[-1]=str(info[-1])
                            line = ','.join(info) + '\n'
                            write_f.write(line)
                    os.remove('db.txt')
                    os.rename('db.txt.swap', 'db.txt')
        else:
            print('该用户不存在')
login()
