# 需求：
"""
1）进度条总长度固定
2）会刷新打印
3）完成字符串的格式化操作
4）模拟现实中的文件下载环境
5）定义进度条函数
    -- 参数：进度值
    -- 返回值：功能就是展示，不需要返回值
问题：字符串各种格式化组合
"""

import time

def progress(percent):
    # 功能：将进度值转换为可视化的进度条
    width = 50
    ss = "%d" % width
    ss = ("%%-%ss" % ss) % ('#' * int(percent * width))
    ss = "\r[%s] %d%%" % (ss, percent * 100)
    print(ss, end="")

curr_size = 0
total_size = 10241
while curr_size < total_size:
    # 剩余未下载量
    last_size = total_size - curr_size
    time.sleep(0.1)
    if last_size > 1024:
        curr_size += 1024
    else: # 最后一次下载量
        curr_size += last_size
    progress(curr_size / total_size)

"""
# 如何完成刷新打印
# print("%d" %1, end="")
# print("\r%d" %2, end="")

# %号的转义问题
# 需要占位，前置%会被认为为转义符
# 不需要占位，%就代表自身
# print("%") # %
# print("%%") # %%
# print("%%d") # %%d
# # print("%%d" %10) # 报错
# print("%d%%") # %d%%
# print("%d%%" %10) # 10%
# # %10
# print("%%%d" %10)
# print("%" + ("%d" %10))

# 最终结果
# [*******************     ] 85%
p = 0.85
w = 50 # %-50s 50->w->%d
# (%-50s) -> '#' * p * w
# 85% -> %d%% -> p * 100
# [%%-%ds] %d%% 占位符分析
# [(%%-(%d %w)s %('#' * p * w))] %d%% %(p * 100)
# print("[################    ] 85%")
# "[(%%-(%d %w)s %('#' * p * w))] %d%% %(p * 100)"
ss = "%d" %w
ss = ("%%-%ss" %ss) %('#' * int(p * w))
ss = "\r[%s] %d%%" %(ss, p * 100)
# print(("%%-%ds" %50) %"#")
print(ss, end="")
"""

