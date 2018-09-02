# # 1.strip去首位空格
# name="***123***"
# print(name.strip('*'))#去首位
# print(name.lstrip('*'))#去首
# print(name.rstrip('*'))#去尾
# # 2.lower大小写转换
# name="TOM"
# name2="tom"
# print(name.lower())#大转小
# print(name2.upper())#小转大/
# # 3.startswith,endswith字符串是否已***开头或结尾,返回Ture或Flase
# name="tom_aaa"
# print(name.startswith("t"))
# print(name.endswith("b"))
# #4.format的三种玩法
# aaa="{}{}".format("tom","lisi")
# print(aaa)
# bbb="{2}{1}{0}".format(1,2,3)
# print(bbb)
# ccc="{name}{age}{sex}".format(name="张三",age=16,sex="女")
# print(ccc)
# #5.split 切片
# name='root:x:0:0::/root:/bin/bash'
# print(name.split("/"))
# print(name.split("/",2))#从右开始切分
# # 6.join连接   （返回通过指定字符连接序列中元素后生成的新字符串。）
# tag="_"
# aaa=['zhan','lisi','王五']
# print(tag.join(aaa))
# #7.replace 替换
# name="我是一只小青蛙小青蛙"
# print(name.replace("小青蛙","小青龙",1))
# #8.isdigit：可以判断bytes和unicode类型,是最常用的用于于判断字符是否为"数字"的方法
# # age=input("请输入数字：")
# # print(age.isdigit())
#
#
#





#
#
#
#
#
#
#
# # 9.find,rfind,index,rindex,count
# name="66abbbccc"
# print(name.find('a',1,3))#[1,3),find找不到不会报错
# # print(name.index('e',2,4)) #同上,但是找不到会报错
# print(name.count('c'))#查找存在的个数
# #10.center,ljust,rjust,zfill填充
# name="hello word"
# print(name.center(30,"*"))#name在中间，数字表示name+*的总长度，只有一个*，则*在右边
# print(name.ljust(30,"*"))#字在左边
# print(name.rjust(30,"*"))#字在右边
# print(name.zfill(50))#用0填充，并且0在左边
# #11.expandtabs把字符串中的tab符号（'\t')转为空格
# name="vewvwe\tgw\te"
# print(name.expandtabs(1))#这里为空格数
# #12.captalize,swapcase,title大小写
# name="tOm"
# print(name.capitalize())#首字母大写
# print(name.swapcase())#大小写翻转
# name="tom aaa bbb"
# print(name.title())#每个单词的首字母大写
# #13.is
# num="4"
# print(num.isdigit())#检测字符串是否只由数字组成。
# print(num.isdecimal())#isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
# #注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
# print(num.isnumeric())#检测字符串是否只由数字组成（中文数字,罗马数字）
# #注：以上三者不能判断浮点数
# print(name.isalnum()) #字符串由字母或数字组成
# print(name.isalpha()) #字符串只由字母组成
#
#
#
# # 练习
# name = " aleX"
# # 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip())
# # 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
# print(name.startswith("al"))
# # 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# print(name.endswith("X"))
# # 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# print(name.replace("l","p"))
# # 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# print(name.split("l"))
# # 6)    将 name 变量对应的值变大写,并输出结果 
# print(name.upper())
# # 7)    将 name 变量对应的值变小写,并输出结果 
# print(name.lower())
# # 8)    请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# # 9)    请输出 name 变量对应的值的前 3 个字符?
# print(name[2])
# # 10)    请输出 name 变量对应的值的后 2 个字符? 
# print(name[-2:])
# # 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# print(name.index('e'))
# # 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# name="oldboy"
# print(name[0:-1])



#进出队
# l=[]
# l.append('p1')
# l.append('p2')
# l.append('p3')
# print(l)
# print(l.pop(0))
# print(l)

#进出栈
# l=[]
# l.append('a1')
# l.append('a2')
# l.append('a3')
# print(l)
# print(l.pop())
# print(l.pop())
# print(l.pop())
# print(l)



l=[
    {'name':'alex','age':84},
    {'name':'oldboy','age':73},
    {'name':'egon','age':18},
]
l.sort(key=lambda item:item['age'])
print(l)


















