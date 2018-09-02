#增 append
name=[]#空列表
name.append('张三')# 使用 append() 添加元素
print(name)
#删 del
del name[0]
print(name)
#len()长度
print(len(name))
print(len([1,2,3]))
#组合
print([1,2]+[1,2])
#重复
print([1]*3)
#in 元素是否存在
print(1 in [1,2,3])
#迭代
for x in [1,2,3]:
    print(x)
#cmp()方法，比较列表
#max()最大值
list1=[1,2,3,4]
print(max(list1))
#min()最小值
print(min(list1))
# list(seq)将元祖转换成列表
# .count()统计次数
print(list1.count(1))#统计1在list1中出现的次数
#extend()相当于两个列表相加
list2=[1,2]
list1.extend(list2)
print(list1)
# index()查找位置
print(list1.index(1))
#insert()将对象插入列表的指定位置
list2.insert(0,555)
print(list2)
#pop()移除列表中的第几个元素
shan=list2.pop(0)
print(shan)#查看删除的元素
print(list2)
#remove()移除列表中的某一项
list2.remove(1)
print(list2)
#reverse()反向列表中的元素
list3=[1,2,3,4,5,6]
list3.reverse()
print(list3)
#sort()排序
list4=[1,5,8,6,4,5]
list4.sort()
print(list4)
#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
list4.sort(reverse=True)
print(list4)

