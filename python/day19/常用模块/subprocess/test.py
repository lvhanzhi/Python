import subprocess
obj=subprocess.Popen(#相当于开启了一个子进程
    'tasklist',#命令
    shell=True,#相当于调了一个shell命令解释器
    stdout=subprocess.PIPE,#命令正常运行的结果 往管道丢
    stderr=subprocess.PIPE#命令出错运行的结果
    #调用了两个管道
)
stdout_res=obj.stdout.read()#从正确的管道里拿结果
print(stdout_res.decode('gbk'))#拿到的是二进制,需要进行解码
