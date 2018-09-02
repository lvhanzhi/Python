import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect_ex(('127.0.0.1',9000))
s.send('aaa'.encode('utf8'))
msg=s.recv(1024)
print(msg.decode('utf8'))
s.close()