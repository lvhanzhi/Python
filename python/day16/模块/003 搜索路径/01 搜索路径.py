# 搜索路径有哪些
# 内存 > 内置模块 > sys.path （存在优先级）

# 1.认识sys.path
# 是内置模块sys中名字
# 本质：存在字符串形式路径的链表，第一位就是当前执行文件的路径
# import sys
# print(sys.path)

# 2.验证优先级
"""
import module, time
time.sleep(10)
# 导入模块会优先搜索内存
import module
print(module.x)
"""
"""
# 内存中没有时，优先查找内置模块
import time
time.sleep(2)
print("睡了2s")
"""

# 3.认识sys.modules：已被加载到内存中的模块
import sys
print("sys" in sys.modules)
print("time" in sys.modules)
import module
print("module" in sys.modules)





