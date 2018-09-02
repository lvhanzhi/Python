import socket
#1.买手机
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.拨号
s.connect_ex(('127.0.0.1',9000))
#3.发\收消息
s.send('aaa'.encode('utf8'))# 只能发bytes类型
msg=s.recv(1024)
print(msg.decode('utf8'))
#4.挂电话链接
s.close()