x = 100

# 在包内可以使用相对导入的.语法
# .该文件的当前目录
# ..该文件的上一级目录，依次类推
# 住：不可以出包
from . import m2
print(m2.y)

# 出错：出包
# from .. import mmm
# print(mmm.mmm)