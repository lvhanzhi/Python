import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9000))
s.listen(5)
while True:
    conn,addr=s.accept()
    print('%s正在连接'%addr[0])
    while True:
        msg=conn.recv(1024)
        print('接收的数据是:%s'%msg.decode('utf8'))
        conn.send(msg.upper())
    conn.close()
s.close()