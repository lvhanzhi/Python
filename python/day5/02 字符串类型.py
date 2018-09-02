#一：基本使用
# 1 用途：记录描述性的状态，比如人的名字、地址、性别

# 2 定义方式：在"",'',""""""内包含一系列的字符
# msg='hello' #msg=str('hello')
# res1=str(1)
# res2=str([1,2,3])
# print(type(res1),type(res2))
# info="'xxx'"

# 3 常用操作+内置的方法
#优先掌握的操作：
#1、按索引取值(正向取+反向取) ：只能取
# msg='hello world'
# print(msg[4])
# print(msg[-1])
# msg[3]='A'
# name='egon'


#2、切片(顾头不顾尾，步长)
# msg='hello world' # 就是从一个大的字符串中切分出一个全新的子字符串
# print(msg[0:5])
# print(msg) # 没有改变原值

# print(msg[0:5:1])
# print(msg[0:5])
# print(msg[0:5:2]) #hlo

# 了解：
# print(msg[0:5:1])
# msg='hello world'
# print(msg[5:0:-1])
# print(msg[5::-1])
# print(msg[-1::-1])
# print(msg[::-1])

#3、长度len
# msg='hello world'
# print(len(msg))

#4、成员运算in和not in: 判断一个子字符串是否存在于一个大的字符串中
# print('alex' in 'alex is dsb')
# print('dsb' in 'alex is dsb')
# print('sb' in 'alex is dsb')
# print('xxx' not in 'alex is dsb') # 推荐
# print(not 'xxx' in 'alex is dsb')

#5、去掉字符串左右两边的字符strip，不管中间的

# user='      egon       '
# user='   x   egon       '
# user="*******egon********"
# user=" **+*  */***egon*  **-*****"
# print(user.strip("* +/-"))

# user=input('>>>: ').strip()
# if user == "egon":
#     print('用户名正确')

#6、切分split:针对按照某种分隔符组织的字符串，可以用split将其切分成列表，进而进行取值

# msg="root:123456:0:0::/root:/bin/bash"
# res=msg.split(':')
# print(res[1])

# cmd='dowload|a.txt|3333333'
# cmd_name,filename,filesize=cmd.split('|')

#7、循环
msg='hello'
for item in msg:
    print(item)



#二：该类型总结
# 1 存一个值or存多个值
#     只能存一个值
#     可以存多个值，值都可以是什么类型
#
# 2 有序or无序
#
# 3 可变or不可变
#     ！！！可变：值变，id不变。可变==不可hash
#     ！！！不可变：值变，id就变。不可变==可hash