import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
qq_name_dic={
    '房得成':('127.0.0.1',9000),
    '陈凤琴':('127.0.0.1',9000),
    '王雅玲':('127.0.0.1',9000),
    '喜洋洋':('127.0.0.1',9000)
}
while True:
    name=input('请输入聊天对象:').strip()
    if name not in qq_name_dic:continue
    while True:
        msg=input('请输入消息,回车发送:').strip()
        if msg=='q':break
        if not msg or not name in qq_name_dic:
            continue
        s.sendto(msg.encode('utf8'),qq_name_dic[name])
        back_msg,addr=s.recvfrom(1024)
        print('来自%s的一条消息:%s'%(addr,back_msg.decode('utf8')))
s.close()
