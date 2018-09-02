import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9000))
while True:
    msg,addr=s.recvfrom(1024)
    print(msg.decode('utf8'))
    s.sendto(msg.upper(),addr)
s.close()
