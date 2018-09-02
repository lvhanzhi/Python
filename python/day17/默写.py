#随机验证码
import random
def foo(n):
    str_all=''
    for i in range(n):
        str1=str(random.randint(0,9))
        str2=chr(random.randint(65,90))
        str_all+=random.choice([str1,str2])
    print(str_all)
foo(4)
#进度条
import time
def make_progress(percent,width=50):
    if percent > 1:percent=1
    show_str=('[%%-%ds]' % width) % (int(percent * width) * '#')
    print('\r%s %s%%' %(show_str,int(percent * 100)),end='')
total_size=25555
recv_size=0
while recv_size < total_size:
    time.sleep(0.1)
    recv_size+=1024
    percent=recv_size / total_size
    make_progress(percent)