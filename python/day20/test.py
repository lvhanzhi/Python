# import re
# src='abcdefg\r\t\f12ghg3548'
# #查找所有满足条件的
# print(re.findall('a',src))
# print(re.findall('\w',src))#字母数字下划线
# print(re.findall('\s',src))#任意空白字符
# print(re.findall('.',src))#匹配任意字符(除了\n)
# print(re.findall('\d{3}',src))
# print(re.findall('\d*',src))#*[0,无穷)
# print(re.findall('\d+',src))#+[1,无穷)
# print(re.findall('\d?',src))#?[0,1]
# print(re.findall('\d{0,1}',src))#{n,m} [n,m]
# print(re.findall('\d{2}',src))#{n}指定n次
# #匹配范围
# #a|b 或
# print(re.findall('1|5|2',src))
# #[]字符集合
# print(re.findall('[125]',src))
# #找出所有数字和字母
# print(re.findall('[0-9]|[a-z]|[A-Z]',src))
# print(re.findall('[0-9|a-z|A-Z]',src))
# print(re.findall('[0-9a-zA-Z]',src))
#
# #^行首
# print(re.findall('^hello','hello hello'))
# #&行尾
# print(re.findall('h$','hello hello'))
# print(re.findall('o$','hello hello'))
#
# #取反
# print(re.findall('[^0-9]',src))
#
# #边界单词(单词的末尾)
# print(re.findall(r'o\b','hello word'))
# print(re.findall('\\bw','hello word'))
#
# #验证密码 不能少于8位,智能是数字字母下划线 最长16位
# pwd='12345678'
# print(re.findall('\w{8,16}',pwd))
#
# #验证手机号码 长度11 全是数字 前三位是固定范围[189 131 10]
# phone='13162998165'
# print(re.findall('^(?:189|131|150)\d{8}',phone))
#
# #用正则取图片地址
# src="<img src='www.baidu.jpg'><img src='www.baidu.jpg'>"
# print(re.findall("src='.+?'",src))
# print(re.findall("src='(.+?)'",src))
# #()用于给正则表达式分组,优先取出括号内的内容
# #?:取消()的优先级
#
# src="c|java|python|shell"
# a=re.findall('([a-zA-Z]+)',src)[0]
# b=re.findall('([a-zA-Z]+)',src)[-1]
# # print(re.sub('a'))
#
# print(re.findall('.','1a-*\n\t\r'))
#
#
#
#
#
# print(re.findall('[^0-9]','123'))
#
# import re
# src = "c++|java|python|shell"
# res=re.sub('(.+?)(\|.+?\|.+?\|)(.+)',r'\3\2\1',src)
# print(res)

# import re
# def fn(match):
#     res=match.group()
#     return str(int(res)+1)
# res=re.sub(r'\d+',fn,'我的日薪:88888,你的日薪1')
# print(res)#我的日薪:88889,你的日薪2





























