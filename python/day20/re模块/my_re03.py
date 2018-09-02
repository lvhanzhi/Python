# 方法
# match
# search
# findall
# sub
# split
import re
# 从头开始，匹配一次(没有匹配到返回None)
# res = re.match(r'a', "abc")
# print(res)

# 匹配一次，无关位置，从前往后索引匹配(没有匹配到返回None)
res = re.search(r'a', "baca")
print(res)

# 从前往后索引匹配，匹配所有，返回列表(没有匹配到返回[])
res = re.findall(r'a', "baca")
print(res)

# 正则 替换字符串 目标字符串
# 不修改目标字符串，返回替换后的字符串
# ts = "abcdea"
# res = re.sub(r'[0-9]', "呵", "a2b12e9a")
# print(res)

# 以正则拆分成数据列表
# ts = "老男孩：python，Linux、H5、Java GO C++ AR VR"
# res = re.split(r' |：|，|、', ts)
# print(res)




