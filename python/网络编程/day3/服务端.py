import socket
import subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9000))
s.listen(5)
while True:
    conn,addr=s.accept()
    print("正在接听%s的电话"%addr[0])
    while True:
        msg=s.recv(1024)
        print(msg.decode('utf8'))
        p=subprocess.Popen(msg.decode('utf8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout=p.stdout.read()
        stuerr=p.stderr.read()
        conn.send(stdout+stuerr)
    conn.close()
phone.close()
