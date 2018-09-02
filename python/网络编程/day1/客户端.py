import socket
ip=('127.0.0.1',9000)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect_ex(ip)
s.send('hi'.encode('utf8'))
msg=s.recv(BUFSIZE)
print(msg.decode('utf8'))
s.close()