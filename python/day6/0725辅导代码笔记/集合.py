"""
    集合是什么
        可以存储多个值的数据容器
        特点:
            元素是无序的
            是可变的
            不可以存储重复元素(id相同)
            只能存储不可变数据类型

    集合的定义方式:
        变量名 = {值1,值2....}
    集合更多用在需要计算两个集合之间的关系的场景
"""

# my_set = {1, 2, "abc", "bde","pop","class","A"}
# print(my_set)

# 删除 并返回被删除的元素
# res = my_set.pop()
# print(res)
# print(my_set)

# 添加元素
# my_set.add("abc")
# my_set.add("abcd")
# print(my_set)


# 获取元素
# for i in my_set:
#     print(i)


# 交集 两个集合中同时存在的元素
my_set1 = {1, 2, 3, 8}
my_set2 = {1, 2, 3, 4}
# print(my_set1 & my_set2)
# 调用方法求交集
# print(my_set1.intersection(my_set2))
# 求两个集合的交集 并将结果赋值给my_set1
# print(my_set1.intersection_update(my_set2))
print("注意: my_set1:%s" % my_set1)
#
# 并集(合集) 两个集合中所有元素
# print(my_set1 | my_set2)
# 方法求合集
# print(my_set1.union(my_set2))


# 差集 后者相比前者 差了什么 差的数据成为差集
print(my_set2 - my_set1)
print(my_set2.difference(my_set1))
print(my_set2.difference_update(my_set1))
print(my_set2)

# 对称差集  不同时存才与两边的数据(除了交集都是对称差集)
print(my_set2 ^ my_set1)
print(my_set2.symmetric_difference(my_set1))
print(my_set2.symmetric_difference_update(my_set1))

my_set3 = {1, 2, 3, 4} #b
my_set4 = {1, 2, }  #a
# 子集 a集合中的所有元素都出现在了b集合 a就是b的子集 b是a父集
print(my_set4.issubset(my_set3))
# 父集 a集合完全包含b集合 a 就是b的父集
print(my_set3.issuperset(my_set4))


