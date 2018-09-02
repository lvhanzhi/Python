"""
    元组
	也是一种可以存储多个值的数据容器
	元组中的元素不可以被修改
	可以存储任何类型数据
	可以存储重复元素
元素和列表到底谁快?
	列表在增加和删除元素时都涉及到一个扩充容量和减少容量的操作,二元组没有这个过程,所以元组速度会略快列表
	例如:对列表调用一个pop方法 和 对元组直接取值

	元组的定义方式:
		变量名 = (value1,valu..n)
		注:一旦元组被创建了 他的内容也就固定了
"""
my_tuple = (1, "a", [],98,90,78)
print(my_tuple)
my_tuple[2].append(100)
print(my_tuple)

# 取出元素
print(my_tuple[0])

# 循环取值
for elm in my_tuple:
    print(elm)

# 内容运算
# 想知道一个数据是否存在于元组中
print(1 not in my_tuple)

# 切片
# 拿到第2-3个元素
print(my_tuple[2:4])

# index 可以找出每个元素在元组中的位置 注意如果元素不在元组中会奔溃
# 98在元组第几个?
print(my_tuple.index(98))

# count 统计元素在元组中出现的次数
# 98 有几个?
print(my_tuple.count(98))
print("hello")





