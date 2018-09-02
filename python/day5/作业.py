# 默写:
#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s "%(i,j,i*j),end='')
#     print()
#金字塔
# n=int(input('n:').strip())
# for x in range(1,n+1):
#     for i in range(n-x):
#         print(' ',end='')
#     for j in range(2*x-1):
#         print('*',end='')
#     print()
# 1.
# # 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
# name = " aleX"
# # 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip())
# # 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
# print(name.startswith('al'))
# # 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# print(name.endswith('X'))
# # 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# print(name.replace('l','p'))
# # 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# print(name.split('l'))
# # 6)    将 name 变量对应的值变大写,并输出结果 
# print(name.upper())
# # 7)    将 name 变量对应的值变小写,并输出结果 
# print(name.lower())
# # 8)    请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# # 9)    请输出 name 变量对应的值的前 3 个字符?
# print(name[0:3])
# # 10)    请输出 name 变量对应的值的后 2 个字符? 
# print(name[-2:])
# # 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# print(name.index('e'))
# # 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# name='oldboy'
# print(name[0:-1])
# 2.要求用户输入五个数字存储到列表中, 然后提供三个功能
l=[]
# for i in range(5):
#     while True:
#         try:
#             l.append(float(input('>>:').strip()))
#             break
#         except Exception as e:
#             print('请重新输入')
#             continue
# 2.1打印最大值
# l.sort()
# print(l[-1])
# 2.2打印最小值
# l.sort()
# print(l[0])
# 2.3打印平均数
# sum=0
# for i in l:
#     sum+=i
# print(sum/len(l))
# 3.交换两个列表中的元素, (两个列表元素个数相同)
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# l3=l1.copy()
# l1=l2
# l2=l3
# print(l1,l2)
# 4.有以下列表["python", "java", "C++", "PHP", "HTML", "python", "C++", "Ruby"]编写代码去除列表中重复的元素
# l=["python", "java", "C++", "PHP", "HTML", "python", "C++", "Ruby"]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l2)

# 5.查看提供的(待处理文本.txt)文件,编写代码取出所有图片的网址,不需要直接读取文件,把内容复制到代码找中定义为变量即可
# with open(r'C:\Users\2\Desktop\python\day5\0724作业待处理文本.txt','r',encoding='utf8')as f:
#     for line in f:
#         star_http=line.find('http')
#         end_jpg=line.find('.jpg')
#         print(line[star_http:end_jpg+4])
#         star_http1=line.rfind('http')
#         end_jpg1=line.rfind('.jpg')
#         print(line[star_http1:end_jpg1+4])

# 6.有如下字符串("language,is,perfect,hello,i am jack,python")编写代码,将其修改为,"hello i am jack python is perfect language"字符串
# str="language,is,perfect,hello,i am jack,python"
# l=str.split(',')
# print(l)
# str=[l[3],l[4],l[5],l[1],l[2],l[0]]
# print(' '.join(str))

# 选做
#
# 7.
# 有如下列表
# [5, 2, 1, 4, 3]
# 编写代码实现从大到小排序(百度搜索冒泡排序)
# l=[5, 2, 1, 4, 3]
# l.sort(reverse=True)
# print(l)
nums=[5, 2, 1, 4, 3]
for i in range(len(nums)-1):
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)
# 8.
# 简单购物车
# 博客题http: // www.cnblogs.com / linhaifeng / articles / 7133357.
# html  # _label8
#简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　

# msg_dic={
# 'apple':10,
# 'tesla':100000,
# 'mac':3000,
# 'lenovo':30000,
# 'chicken':10,
# }
