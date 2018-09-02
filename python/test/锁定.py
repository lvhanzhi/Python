'''
3、这一项为选做功能：锁定的账号，在五分钟内无法再次登录
提示：一旦用户锁定，则将用户名与当前时间写入文件,例如: egon:1522134383.29839
实现方式如下：
import time
current_time=time.time()
current_time=str(current_time) #当前的时间是浮点数，要存放于文件，需要转成字符串
lock_user='%s:%s\n' %('egon',current_time)
然后打开文件
f.write(lock_user)
以后再次执行用户验证功能，先判断用户输入的用户名是否是锁定的用户，如果是，再用当前时间time.time()减去锁定的用户名后
的时间，如果得出的结果小于300秒，则直接终止函数，无法认证，否则就从文件中清除锁定的用户信息，并允许用户进行认证
'''

db_file = r'user_info.txt'
src_file = db_file
dst_file = r'%s.swap' %db_file
lock_db_file = r'lock.txt'
lock_src_file = lock_db_file
lock_dst_file = r'%s.swap' %lock_db_file
l_list = []

import time
import os

def login():
    count = 0
    while True:
        name = input('请输入用户名:').strip()
        if check_lock(name) == 0:
            return
        if count == 3:
            print('错误次数过多，锁定!')
            lock(name)
            return
        with open(src_file,'r',encoding='utf-8') as read_f:
            for line in read_f:
                l = line.strip('\n').split(',')
                if name == l[0]:
                    pwd = input('请输入密码:').strip()
                    if pwd == l[1]:
                        print('登录成功!')
                        return None
                    else:
                        print('密码错误，请重新输入!')
                        count += 1
                        break
            else:
                print('该用户未注册，请注册!')

def lock(name):
    current_time=time.time()
    current_time=str(current_time) #当前的时间是浮点数，要存放于文件，需要转成字符串
    lock_user='%s:%s\n' %(name,current_time)
    with open(lock_src_file,'a',encoding='utf-8') as write_lock:
        write_lock.write(lock_user)
        return

def check_lock(name):
    i = 0
    with open(lock_src_file,'r',encoding='utf-8') as lock_read,\
        open(lock_dst_file,'w',encoding='utf-8') as lock_write:
        for line in lock_read:
            line = line.strip('\n')
            l_list.append(line)
            l = line.split(':')
            # print(l)
            if name in l:
                if name == l[0]:
                    current_time = time.time()
                    if current_time - float(l[1])  < 300:
                        print('该用户处于锁定阶段!')
                        return 0
                    else:
                        print('用户已解锁!')
                        l_list.pop(i)
                    i += 1
        for item in l_list:
            lock_write.write(item)

    os.remove(lock_src_file)
    os.rename(lock_dst_file,lock_src_file)

login()





























