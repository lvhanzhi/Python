# 默写:
# 	1.元组 字典 集合 列表 各自的特点

# 元祖:tuple,存多个值/有序/不可变
#     不能改,只能取
#     记录多个值，当多个值没有改的需求，此时用元组更合适
# 字典:dict,存多个值/无序/可变
# value可以是任意类型，而key必须是不可变的类型
# 记录多个值，每一个值都对应的key用来描述value的作用
# 集合:set,存多个值/无序/set可变
#     每一个值都必须是不可变类型,元素不能重复,集合内元素无序
# 列表:list存多个值,有序,可变,存放多个值，可以根据索引存取值,值可以是任意类型



# 	2.字典添加 删除 修改 循环
dic={
    'name':'小明',
    'age':18,
}
dic2={
    'name':'***',
    'sex':'male',
    'hobby':'eat'
}
# dic2=dic2.fromkeys(['aaa','bbb'],None)
# dic['sex']='male'
# res=dic.pop('age')
# res=dic.popitem()
# dic.clear()
# del dic['name']
# del dic
# dic.update(dic2)
# dic.setdefault('sex','male')
# for key,value in dic.items():
#     print(key,value)

print(dic2)