#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
from socket import *
import subprocess

ip_port=('192.168.13.41',8080)#127.0.0.1
BUFSIZE=1024

tcp_socket_server=socket(AF_INET,SOCK_STREAM)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

while True:
    conn,addr=tcp_socket_server.accept()
    print('客户端',addr)

    while True:
        cmd=conn.recv(BUFSIZE)
        if len(cmd) == 0:break

        res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE)

        stderr=res.stderr.read()
        stdout=res.stdout.read()
        conn.send(stderr)
        conn.send(stdout)
