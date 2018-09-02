import socket
ip=('127.0.0.1',9000)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect_ex(ip)
while True:
    msg = input('>>:').strip()
    s.send(msg.encode('utf8'))
    demsg = s.recv(BUFSIZE)
    print(demsg.decode('utf8'))
s.close()