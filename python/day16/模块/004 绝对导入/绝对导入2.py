import sys

print("------------------")
# 通过包的.语法导入
# 基于sys.path，指向的就是该文件路径(当前执行文件)
# from folder import m2
# print(m2.mm2)

# import folder.m2
# print(folder.m2.mm2)

# import folder.m2 as m2
# print(m2.mm2)

# 导入模块时出现了A.B...，这种.语法，.前必须是包
# from folder.m2 import mm2
# print(mm2)

# folder就是包了
# import m1.nm1
import folder
# print(folder)
# print(sys.path)


