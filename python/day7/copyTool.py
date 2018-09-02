# 系统提供的模块  现在用它来接收用户从cmd中输入的参数
import  sys

# argv 返回一个数组 里面是cmd中接收的参数 空格分隔
# print(sys.argv)



src = sys.argv[1]
dis = sys.argv[2]
if src == dis:
    print("源文件与目标文件相同 再见")

# 以读取二进制的模式打开源文件
srcf = open(src, "rb")
# 以写入二进制的模式打开目标文件
disf = open(dis, "wb")

# 从源文件读取 写入到目标文件
for line in srcf:
    disf.write(line)
# 关闭资源
srcf.close()
disf.close()
