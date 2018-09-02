# import hashlib
# user='egon'
# pwd='123'
# md5_obj=hashlib.md5(user.encode('utf8'))
# md5_obj.update(pwd.encode('utf8'))
# print(md5_obj.hexdigest())


# import hashlib,os
# md5_obj=hashlib.md5()
# file_size=os.path.getsize('db.txt')
# f=open('db.txt','rb')
# while file_size>0:
#     if file_size>1024:
#         content=f.read(1024)
#         file_size-=1024
#     else:
#         content=f.read(file_size)
#         file_size-=file_size
#     md5_obj.update(content)
# print(md5_obj.hexdigest())

import hmac
m=hmac.new('小鸡炖蘑菇'.encode('utf8'))
m.update('hello'.encode('utf8'))
print(m.hexdigest())