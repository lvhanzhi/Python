import socket
ip=('127.0.0.1',9000)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ip)
s.listen(5)
conn,addr=s.accept()
print('正在接收来自%s的电话'%addr[0])
msg=conn.recv(BUFSIZE)
print(msg.decode('utf8'))
conn.send('hello'.encode('utf8'))
conn.close()
s.close()
