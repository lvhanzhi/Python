# import socket
# client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#     aaa = input('请输入:')
#     client.sendto(aaa.encode('utf8'), ('127.0.0.1', 8080))
#     back_msg, addr = client.recvfrom(1024)
#     print(back_msg.decode('utf8'), addr)
# # data.sercer_addr=client.recvfrom()
# client.close()

import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    aaa=input("请输入:")
    client.sendto(aaa.encode('utf8'),('127.0.0.1',8080))
    data,addr=client.recvfrom(1024)
    print(data.decode('utf8'))
client.close
