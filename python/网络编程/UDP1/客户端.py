import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input('>>:').strip()
    s.sendto(msg.encode('utf8'),('127.0.0.1',9000))
    demsg,addr=s.recvfrom(1024)
    print(demsg.decode('utf8'))
s.close()