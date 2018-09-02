

myset1 = {1,2,3,4,5}
myset2 = {1,2,3}

# 是否无交集 无交集返回True
print(myset1.isdisjoint(myset2))

# 添加一个
myset1.add(100)
# 添加一堆
myset1.update({99,88,77})
print(myset1)

# 随机删除
# myset1.pop()
# 删除指定的元素  没有则崩溃
# myset1.remove(100)
# print(myset1)

# 没有找到这个元素也不会崩溃
myset1.discard(1001)

print(myset1)
