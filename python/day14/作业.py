# 今日作业：
# 	1.简述
# 	什么是迭代器
#可以重复取值的工具,这次的循环是基于上一次结果而来的
# 	什么是可迭代对象
#有__iter__就是可迭代对象
# 	什么是面向过程编程
#复杂的问题简单化,先干什么再干什么
# 	2.自定义生成器 实现 range功能
# def foo(start,end,bu):
#     while start<end:
#         yield start
#         start+=bu
# foo=foo(1,11,1)
# for i in foo:
#     print(i)

# 	3、文件shopping.txt内容如下
# 		mac,2000,3
# 		lenovo,3000,10
# 		tesla,1000000,10
# 		chicken,200,1
# 		求总共花了多少钱？
# 		打印出所有的商品信息，格式为
# 		[{'name':'xxx','price':'3333','count':3},....]
# 		求单价大于10000的商品信息，格式同上

# l=[]
# with open('shopping.txt','r',encoding='utf8')as f:
#     for line in f:
#         dic = {}
#         info=line.strip('\n').split(',')
#         dic['name']=info[0]
#         dic['price']=info[1]
#         dic['count']=info[2]
#         l.append(dic)
# print(l)
# res=filter(lambda i:int(i['price'])>10000,l)
# for i in res:
#     print(i)
# 	4、文件内容如下,标题为:姓名,性别,年纪,薪资
# 		egon male 18 3000
# 		alex male 38 30000
# 		wupeiqi female 28 20000
# 		yuanhao female 28 10000
#
# 		要求:
# 		从文件中取出每一条记录放入列表中,
# 		列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
# l=[]
# def foo():
#     with open('db.txt', 'r', encoding='utf8')as f:
#         for line in f:
#             dic = {}
#             info = line.strip('\n').split(' ')
#             dic['name'] = info[0]
#             dic['sex'] = info[1]
#             dic['age'] = info[2]
#             dic['salary'] = info[3]
#             yield dic
# foo=foo()
# for i in foo:
#     l.append(i)
# 	5 根据1得到的列表,取出薪资最高的人的信息
# dic2={}
# for i in l:
#     name=i['name']
#     salary=i['salary']
#     dic2[name]=salary
# print(dic2)
# print(max(dic2,key=lambda x:dic2[x]))
# 	6 根据1得到的列表,取出最年轻的人的信息
# dic2={}
# for i in l:
#     name=i['name']
#     age=i['age']
#     dic2[name]=age
# people=min(dic2,key=lambda x:dic2[x])
# for i in l:
#     if i['name']==people:
#         print(i)
# 	7 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
# l2=[]
# for i in l:
#     name=i['name'].capitalize()
#     i['name']=name
#     l2.append(i)
# print(l2)



# res=map(lambda x:x['name'].capitalize(),l)
# for i in res:
#     print(i)
# 	8 根据1得到的列表,过滤掉名字以a开头的人的信息
#方式一:
# for i in l:
#     if i['name'].startswith('a'):
#         l.remove(i)
# print(l)
#方式二:
# res=filter(lambda i:not i['name'].startswith('a'),l)
# for i in res:
#     print(i)