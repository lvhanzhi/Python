# 1、买手机
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp称为流式协议,udp称为数据报协议SOCK_DGRAM
# print(phone)

# 2、插入/绑定手机卡
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1', 8080))




# 3、开机
phone.listen(5)  # 半连接池，限制的是请求数

# 4、等待电话连接
print('start....')
while True:  # 连接循环
    conn, client_addr = phone.accept()  # （三次握手建立的双向连接，（客户端的ip，端口））
    # print(conn)
    print('已经有一个连接建立成功', client_addr)

    # 5、通信：收\发消息
    while True:  # 通信循环
        try:
            print('服务端正在收数据...')
            data = conn.recv(1024)  # 最大接收的字节数，没有数据会在原地一直等待收，即发送者发送的数据量必须>0bytes
            # print('===>')
            if len(data) == 0: break  # 在客户端单方面断开连接，服务端才会出现收空数据的情况
            print('来自客户端的数据', data)
            conn.send(data.upper())
        except ConnectionResetError:
            break
    # 6、挂掉电话连接
    conn.close()

# 7、关机
phone.close()



print('aaa')
def foo():
    pass

from b import foo
foo()

圣诞快乐国际旅客的世界观的雷锋精神的理解老师是DLGKLFDNHJGLADF

IF

报头



