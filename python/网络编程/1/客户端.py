import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect_ex(('127.0.0.1',9000))
while True:
    msg=input('>>:').strip()
    s.send(msg.encode('utf8'))
    demsg=s.recv(1024)
    print(demsg.decode('gbk'))
s.close()