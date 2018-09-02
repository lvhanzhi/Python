# 最初的导入：同目录下的绝对导入
# import m1
# print(m1.mm1)

# 借助sys.path完成不在同目录下模块的导入
import sys
# 将m2所在的目录添加到sys.path中，操作后就可以直接导入m2
sys.path.append("/Users/wer_chen/Desktop/辅导/模块/004 绝对导入/folder")
import m2
print(m2.mm2)

# eg:使用 003 搜索路径 目录下的 module.py
sys.path.append("/Users/wer_chen/Desktop/辅导/模块/003 搜索路径")
import module
print(module.x)