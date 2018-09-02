import socket
ip=('127.0.0.1',9000)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
s.bind(ip)
s.listen(5)
while True:
    conn, addr = s.accept()
    print('正在接收%s的电话' % addr[0])
    while True:
        msg = conn.recv(BUFSIZE)
        print(msg.decode('utf8'))
        conn.send(msg.upper())
    conn.close()
s.close()