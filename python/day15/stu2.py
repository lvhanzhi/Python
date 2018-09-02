# 4.在stu2.py文件中导入cuboid模块时为模块起简单别名，利用别名完成第3题中完成的操作
# import cuboid as foo
# print(foo.perimeter())
# print(foo.area())

from cuboid import perimeter as p
from cuboid import area as a
print(p())
print(a())
# print(perimeter)#注意:改了之后原名就不能用了