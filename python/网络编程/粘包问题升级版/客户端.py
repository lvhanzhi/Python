import socket
import json
import struct
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9001))
while True:
    cmd=input('请输入命令:').strip()
    s.send(cmd.encode('utf8'))
    header_len=struct.unpack('i',s.recv(4))[0]
    header_bytes=s.recv(header_len)
    header_json=header_bytes.decode('utf8')
    header_dic=json.loads(header_json)
    total_size=header_dic['total_size']
    file_size=0
    file=b''
    while file_size<total_size:
        msg=s.recv(1024)
        file_size+=1024
        file+=msg
    print(file.decode('gbk'))
s.close()

