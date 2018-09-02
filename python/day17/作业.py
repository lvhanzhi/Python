# 1.掌握课堂案例：验证码
# import random
# def foo(n):
#     str_all=''
#     for i in range(4):
#         str1=str(random.randint(0,9))
#         str2=chr(random.randint(65,90))
#         str_all+=random.choice([str1,str2])
#     print(str_all)
# foo(4)
#2.掌握课堂案例：进度条
# import time
# def foo(percent,width=50):
#     if percent>1:percent=1
#     res=('[%%-%ds]'%width)%('#'*int(percent*width))
#     print('\r%s%d%%'%(res,percent*100),end='')
# file_size=15555
# rece_size=0
# while rece_size<file_size:
#     time.sleep(.1)
#     rece_size+=1024
#     percent=rece_size/file_size
#     foo(percent)
# 扩展：
# 	3.控制台模拟发送验证码
# 	提示：
# 	1）验证码为6位纯数字
# 	2）两次获取的间隔为60s
# 	3）倒计时为一秒减一次
# 	4）流程中的?是实际数字，#为临时填充字符
# 	流程：
# 	1）控制台提示用户是否发送验证码[1:是 0:否]
# 	2）取消发送验证码则提示"取消发送"并直接退出程序
# 	3）发送成功后，提示用户"验证码发送成功"，但3s后才可以获取到验证码
# 	4）一旦发送成功后，控制台会刷新打印倒计时多少秒后可以重新发送验证码
# 	5）未接收到验证码的前3s，控制台刷新打印的内容是：验证码:######，?s后可以重新发送
# 	6）验证码获取后，5中的打印内容会替换为：验证码:??????，?s后可以重新发送
# 	7）只有等"?s后可以重新发送"的?从60变到0，才可以重新执行整个过程


import time,random
def get_verification_code():
    res=''
    for i in range(6):
        res+=str(random.randint(0,9))
    return res
def progress_bar():
    for i in range(5):
        if i==4:
            verification_code=get_verification_code()
            for j in range(57):
                time.sleep(1)
                print('\r验证码:%s，%ds后可以重新发送' % (verification_code,56-j), end='')
        else:
            time.sleep(1)
            print('\r验证码:######，%ds后可以重新发送' % (60-i), end='')


while True:
    choice = input('是否发送验证码[1:是 0:否]:').strip()
    if choice == '1':
        print('验证码发送成功')
        progress_bar()
        print()
    elif choice == '0':
        print('取消发送')
        break
