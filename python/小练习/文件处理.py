# f=open(file='a.txt',mode='r',encoding='utf-8')
# data=f.read()
# print(data)
# f.close()


# 确定自己文件是什么编码
# import  chardet
# f=open('a.txt','rb')
# data=f.read()
# result=chardet.detect(open('a.txt','rb').read())
# print(result)
# f.close()

#循环输出
# f=open('a.txt','r',encoding='utf-8')
# for line in f:
#     print(line,end="")
# f.close()


#seek
f=open('a.txt','r+',encoding='utf-8')
f.seek(6)
f.write("hahaha")
f.close()