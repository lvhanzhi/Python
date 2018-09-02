import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9000))
while True:
    qq_msg,addr=s.recvfrom(1024)
    print('来自%s的一条消息:%s'%(addr,qq_msg.decode('utf8')))
    back_msg=input('回复消息:').strip()
    s.sendto(back_msg.encode('utf8'),addr)
s.close()