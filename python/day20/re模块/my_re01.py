import re
# 正则表达式（regex）
# 用途：以一定规则来匹配目标字符串(字符)
# 正则：定义了这样的一套规则

# part1 正则的语法
# part2 re模块的常用方法
# match 正则的匹配方法：从头开始匹配，只匹配一个结果，返回值match对象|None

# 两种方式：
# 第一种：
ts = "+abc" # 字符串(普通)
reg = "\w" # 字符串(有语法)
res = re.match(reg, ts)
print(res)

# 第二种：
ts = "呵呵"
reg = "."
regex = re.compile(reg) # 获得正则规则对象
res = regex.match(ts) # 正则规则对象进行匹配目标字符串，得到匹配结果(re.Match)
print(res)
if res is not None:
    print(res.group())  # 匹配到的内容实体
    print(res.span())  # 匹配到的区间












