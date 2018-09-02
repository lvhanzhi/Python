# 元祖的特点：
# 1.与列表相似，但是列表用的是[]元祖用的是()
# 2.元祖的元素不能修改
# 3.元祖中只有一个数的时候，需要在这个数后面加上逗号。如：zu=(1,)
yuan=(1,2,3)
print(yuan[0])
print(yuan[1:3])
zu=(1,)
print(zu[0])

#对元组进行连接组合
c=yuan+zu
print(c)

len((1,2,3))  #长度
(1, 2, 3) + (4, 5, 6)#连接
('Hi!',) * 4#复制
3 in (1, 2, 3)#元素是否存在
for x in (1, 2, 3):
    print(x)#迭代
# 1	cmp(tuple1, tuple2)
# 比较两个元组元素。
# 2	len(tuple)
# 计算元组元素个数。
# 3	max(tuple)
# 返回元组中元素最大值。
# 4	min(tuple)
# 返回元组中元素最小值。
# 5	tuple(seq)
# 将列表转换为元组。
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
goods_l=[]
while True:
    for key,item in msg_dic.items():
        print('name:{name} price:{price}'.format(price=item,name=key))
    choice=input('商品>>: ').strip()
    if not choice or choice not in msg_dic:continue
    count=input('购买个数>>: ').strip()
    if not count.isdigit():continue
    goods_l.append((choice,msg_dic[choice],count))

    print(goods_l)