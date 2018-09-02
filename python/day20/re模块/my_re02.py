# 语法
import re
# 1）普通的字符
# res = re.match(r'a', 'abc')
# print(res.group())

# 2）单个(非换行\n)任意字符 .
# res = re.match(r'.', 'abc')
# print(res.group())

# 3）字符集(单个) [...] eg: [abc] [a-z] [a-zA-Z0-9_]
# res = re.match(r'[a-zA-Z0-9_]', 'babc') #a-z或A-Z或0-9或_ == \w
# print(res.group())

# 4）非\w的所有字符\W  拓展：\d \D \s \S
# res = re.match(r'\W', '$babc')
# print(res.group())

# 5）开头、结尾(只适用于单行匹配) ^ $
ts = """abc
123
a1d"""
# res = re.match(r'^a', ts)
# print(res)
# match 不与 $结合使用：匹配整个字符串的开头，只匹配一次
# search 可以与 $结合使用：匹配整个字符串(不限定从头开始)，只匹配一次
# res = re.search(r'd$', ts)
# print(res)

# res = re.match(r'^a[\w]c$', "a_c")
# print(res)

# 6) 次数
# *[0, +œ) 尽可能多的匹配
# *? 尽可能少的匹配
# +[1, +œ) | ?[0, 1] | +? | ??
# res = re.match(r'ab*?', "abbbbbc")
# print(res)
# {m} 匹配m次 {m,n} 匹配m~n  {m,n}?
# res = re.match(r'ab{2,5}', "abbbbb")
# print(res)

# 7）或 |  a|b == [ab]
# res = re.match(r'a|b', "cbabc")
# print(res)





