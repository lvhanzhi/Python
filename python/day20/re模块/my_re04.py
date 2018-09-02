# 分组()
# 1）分组不影响匹配结果 ((a(b)c)d(efg)) ==> abcdefg
# 2）0分组代表整体，第几个(就是第几位分组
import re
reg = r"((a(b)c)d(efg))"
ts = "abcdefg"
res = re.match(reg, ts)
print(res.group()) # abcdefg
print(res.group(0)) # abcdefg
print(res.group(1)) # abcdefg
print(res.group(2)) # abc
print(res.group(3)) # b
print(res.group(4)) # efg

# \num：num为分组号 \1 == book>
# reg = r"<(book>)(\w+)</\1"
# ts = "<book>语文</book>"
# res = re.match(reg, ts)
# print(res)

# (?P<mark>主体) (?P=mark)不占有分组
# reg = r"<(?P<tag>book>)(\w+)</(?P=tag)"
# ts = "<book>语文</book>"
# res = re.match(reg, ts)
# print(res.group(2))

# (?:) 取消分组
# [('语文', '</book>'), ('数学', '</book>')]
reg = r"(?:<book>)(\w+)(</book>)"
ts = "<book>语文</book><book>数学</book>"
res = re.findall(reg, ts)
print(res)

