import re
# print(re.findall('\w','hello 123_*/-='))#匹配字母/数字/下划线
# print(re.findall('\W','hello 123_*/-='))
# print(re.findall('\s','hell\no 12\t3_*/-='))
# print(re.findall('\S','hell\no 12\t3_*/-='))
# print(re.findall('\d','hell\no 12\t3_*/-='))
# print(re.findall('\D','hell\no 12\t3_*/-='))
# print(re.findall('\n','hell\no 12\t3_*/-='))
# print(re.findall('\t','hell\no 12\t3_*/-='))
# print(re.findall('1','hell\no 12\t3_*/-='))
# print(re.findall('a.c','abc alc aac asd aaaaac a*c'))#.匹配任意一个字符(除换行符)
# #[]:匹配一个在中括号里的字符
# print(re.findall('a[0-|]c','AAA abc alc aac asd aaaaac a*ca<c'))#a到z
# #要减号,就把-放到两边
# #`取反
# print(re.findall('a[`a-z]c','abc alc aac asd aaaaac a*c'))
# print(re.findall('ab*','abc alc aac asd aaaaac bbbabcabaaaabbbbba*c'))
# print(re.findall('ab?','abc alc aac asd aaaaac a*cabb'))
# print(re.findall('ab+','abc alc aac asd aaaaac abbb a*c'))
# print(re.findall('aaa{2}','aaabbb aab abbb,aaaaaa'))
# print(re.findall('ab{1,3}','abc alc aac asd aaaaac a*c'))
# print(re.findall('a+b{2}','a+ba+b a+b'))
#
# class OldboyStudent():
#     school='oldboy'  #共有属性
#     def __init__(self,name,sex,age):  #私有属性
#         self.name=name
#         self.sex=sex
#         self.age=age
#     def attack(self):  #功能
#         print('%s is learning' %self.name) #新增self.name
#
#
#
# s1=OldboyStudent('李坦克','男')
# s2=OldboyStudent('王大炮','女',38)
# s3=OldboyStudent('牛榴弹','男',78)
#
# print(s1.school)
# print(s1.name)
# print(s1.age)
# print(s1.sex)
#
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getsize(path) 返回path的大小
#
#
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
#
# import hashlib
# m=hashlib.md5()
# m.update('hello'.encode('utf8'))

# print(re.findall('ab?','bbbabbbbb')) #['a']
# print(re.findall('ab?','abbb')) #['ab']
print(re.findall('a.*?b','a12345b222nb22b222b'))
                           # a.*?b
                           # a.*b
# print(re.findall('a.','a123b22222222baaaaa'))
# print(re.findall('a.*','a123b22222222baaaaa'))
# print(re.findall('a.*?','a123b22222222baaaaa'))
# print(re.findall('a.*?b','a123b22222222baaaaa'))