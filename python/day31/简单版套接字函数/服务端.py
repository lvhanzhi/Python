import socket
#1.买手机
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)#是用来接收链接请求,从而建立链接的
#2.插手机卡
s.bind(('127.0.0.1',9000))
#3.开机
s.listen(5)
#4.等待电话请求
conn,addr=s.accept()#(双向链接的套接字对象,存放客户端ip和端口的小元组)
# conn代表双向链接,用来收发消息
print('正在接听来自%s的电话'%addr[0])
#5.收\发消息
msg=conn.recv(1024)#1024接收的最大字节数bytes
print(msg.decode('utf8'))
conn.send(msg.upper())
#6.挂电话链接
conn.close()
#7.关机
s.close()