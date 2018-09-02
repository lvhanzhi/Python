import socket
import json
import struct
import subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('127.0.0.1',9001))
s.listen(5)
while True:
    conn,addr=s.accept()
    print('%s正在连接'%addr[0])
    while True:
        cmd=conn.recv(1024)
        res=subprocess.Popen(cmd.decode('utf8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout=res.stdout.read()
        stderr=res.stderr.read()
        header_dic={
            'total_size':len(stdout)+len(stderr),
            'filename':None,
            'md5':None
        }
        header_json=json.dumps(header_dic)
        header_bytes=header_json.encode('utf8')
        conn.send(struct.pack('i',len(header_bytes)))
        conn.send(header_bytes)
        conn.send(stdout)
        conn.send(stderr)
    conn.close()
s.close()

