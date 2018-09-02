import subprocess
obj=subprocess.Popen(
    r'dir C:\Users\2\Desktop\python\day20\0814作业\0814作业\text >C:\Users\2\Desktop\python\day20\0814作业\0814作业\text\tag.txt',
    shell=True,#
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
stdout_res=obj.stdout.read()
stderr_res=obj.stderr.read()
print(stdout_res.decode('gbk'))
print(stderr_res.decode('gbk'))