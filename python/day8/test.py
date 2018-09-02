# x='上'
# res=x.encode('utf8')
# print(res,type(res))

# f=open(r'test.txt',mode='rt',encoding='utf8')
# msg=f.read()
# print(type(msg))
# f.close()

# f=open(r'test.txt',mode='wt',encoding='utf8')
# f.write('你好')
# f.close()

# with open(r'test.txt','wb')as f:
#     f.write('哈哈哈'.encode('gbk'))

# with open(r'test.txt','a+t',encoding='utf8')as f:
#      f.read()
#      f.write('bbb')

# with open(r'test.txt','rb')as f:
#      msg=f.read(3)
#      print(msg.decode('utf8'))

# with open('test.txt','rt',encoding='utf8')as f:
#      f.seek(2,0)
#      msg=f.read()
#      print(msg)

# with open('test.txt','rb')as f:
#      f.seek(2,2)
#      print(f.tell())

# with open('test.txt','rb')as f:
#      f.seek(0,2)
#      while True:
#           message=f.read()
#           if len(message) !=0:
#                print(message.decode('utf8'),end='')


# with open(r'test.txt','r',encoding='utf8')as f:
#      info=f.read()
# with open(r'test.txt','w',encoding='utf8')as f:
#      f.write(info.replace('alax','dsb'))

import os
with open(r'test.txt','r',encoding='utf8')as read_f,\
     open(r'test.txt.swap','w',encoding='utf8')as write_f:
     for line in read_f:
          line=line.replace('dsb','alax')
          write_f.write(line)
os.remove('test.txt')
os.rename('test.txt.swap','test.txt')