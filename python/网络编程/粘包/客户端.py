from socket import *
import time
s=socket(AF_INET,SOCK_STREAM)
s.connect_ex(('127.0.0.1',9000))
s.send('hello'.encode('utf8'))
time.sleep(5)
s.send('helloword'.encode('utf8'))
s.close()