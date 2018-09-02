import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))
while True:
    msg = input(">>:")
    if len(msg)==0:continue
    if msg=='q':break
    phone.send(msg.encode('utf8'))
    print(phone.recv(1024))

phone.close()
