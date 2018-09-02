# 2.定义一个cuboid模块，模块中有三个变量长(long)宽(wide)高(high)，数值自定义，有一个返回值为周长的perimeter方法，
# 一个返回值为表面积的area方法
long_size=1
with_size=1
height_size=1
def perimeter():
    return (with_size+long_size+height_size)*4
def area():
    return (long_size*with_size+with_size*height_size+long_size*height_size)*2