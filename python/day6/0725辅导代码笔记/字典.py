"""
    字典是什么:
        可以存储多个键值对的数据容器
        键值对是:以 key  value形式存在的一对数据
        特点:
        key必须是不可变的数据类型
        value可以是任意类型
        字典是可变(内容可以被修改而且id不会变)
        key不可以重复
        value可以重复
        字典中的键值对是无序的
    字典定义的方式:
        1. 变量名 = {key1:value1,key n:value n}
        2. 变量名 = {}     # 一个空字典

        3. 变量名 = dict() # 一个空字典
        4. 变量名 = dict([(key1,value1),(key2,value2...)])
        5. 变量名 = dict(key=value,....)
"""
# "yyh 20 man" 不方便存取
# ["yyh", 20, "man"] 可读性差

my_dic = {"name": "yyh", "age": 20, "sex": "man"}

my_dic2 = dict([("name", "yyh"),("sex","man") ])
# 错误示范 [这里可以使元组 也可以是列表但是必须只有两个元素]
# my_dic2 = dict([("name")])
print(my_dic2)

my_dic3 = dict(name="yyh",sex="girl")
print(my_dic3)

# 存储键值对到字典中
# 在创建同时就可以指定
# 加入新的键值对 [这是key] = value
# 如果这个键已经存在就更新对应的值
my_dic3["age"] = 20
print(my_dic3)

# 更新 将原来的sex的值替换为了man
my_dic3["sex"] = "man"

# 如果字典中已经存在相同的key则什么都不做,否则就添加
my_dic3.setdefault("sex", "man")
print(my_dic3)

# 取值 通过key
# 取出key为name的值
# print(my_dic3.get("names")) #没有这个key时返回空
# print(my_dic3["names"])     # 没有这个key崩溃


# 循环取值  每一次取到的是key 通过key可以取出value
# for i in my_dic3:
#     print("%s : %s" % (i, my_dic3[i]))

# items 用于取出键值对 这些键值对被打包在一起
# for item in my_dic3.items():
#     print(item)

# keys 用于取出所有键 key
# print(type(my_dic3.keys()))
# for key in my_dic3.keys():
#     print(key)
#     print(my_dic3[key])

# values 用于取出所有的值
# print(my_dic3.values())


# 删除键值对 根据键删除指定的键值对
# 通用删除方法 没有任何返回
# del my_dic3["name"]
# 自带的删除方法 会返回被删除的值
# age = my_dic3.pop("age")
# print(my_dic3)
# print(age)

# 随机删除一个键值对 会返回被删除键值对
# test = my_dic3.popitem()
# print(test)
# print(my_dic3)


# 如果原始的字典中有同样的key,就更新它的值,如果没有则添加
# my_dic4 = {"name":"yyh","height":180}
# my_dic5 = {"sex":"man","age":20,"name":"hhh"}
# my_dic4.update(my_dic5)
# print(my_dic4)

my_dic10 = {1:"123"}
print(my_dic10)