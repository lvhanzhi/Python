# import socket
# server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# server.bind(('127.0.0.1',8080))
# while True:
#     data, addr = server.recvfrom(1024)
#     print(data)
#     server.sendto(data.upper(), addr)
# server.close

import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))
while True:
    data,addr=server.recvfrom(1024)
    print(data)
    server.sendto(data.upper(),addr)
server.close()