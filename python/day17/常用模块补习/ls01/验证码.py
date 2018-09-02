# 需求：
"""
1）产生指定位数的随机数
2）产生的随机数包含数字大小写字母 0-9 65-90 97-122
3）从函数角度考虑问题(定义为一个产生随机数的功能)
    -- 有参：指定位数
    -- 返回值：产生的验证码
问题：一次只能产生一个，所以要涉及到字符串拼接 "" + "10" + char
"""
# print("" + chr(65))

import random

# 产生随机数的函数
def make_code(limt):
    res = ""
    for i in range(limt):
        # 产生数字、大小写字母并转换为字符串可拼接对象
        n = str(random.randint(0, 9))
        l = chr(random.randint(97, 122))
        L = chr(random.randint(65, 90))
        # 完成字符串拼接
        res += random.choice([n, l, L])
    return res

for i in range(5):
    limt = random.randint(5, 10)
    res = make_code(limt)
    print(res)

