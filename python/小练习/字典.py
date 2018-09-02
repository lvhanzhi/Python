# # #键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
# # #键不可变
# # msg={
# # 'apple':10,
# # 'tesla':100000,
# # 'mac':3000,
# # 'lenovo':30000,
# # 'chicken':10,
# # }
# # print(msg['apple'])
# #
# # msg['apple']=12
# # print(msg['apple'])
# #
# # #删键
# # del msg['apple']
# # print(msg)
# # #清除字典里面的所有条目
# # msg.clear()
# # #删字典
# # # del msg
# #
# # print(len(msg))#键的总数
# # print(str(msg))
# #
#
#
# # 1 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
# #
# # 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# aaa=[11,22,33,44,55,66,77,88,99,90]
# bbb={
#     'k1':[],
#     'k2':[]
# }
# for i in aaa:
#     if i>66:
#         bbb['k1'].append(i)
#     else :
#         bbb['k2'].append(i)
# print(bbb)
#
# # 2 统计s='hello alex alex say hello sb sb'中每个单词的个数
# #
# # 结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
# s='hello alex alex say hello sb sb'
# l=s.split()
# dic={}
# for item in l:
#     if item in dic:
#         dic[item]+=1
#     else:
#         dic[item]=1
# print(dic)
#
# s='hello alex alex say hello sb sb'
# dic={}
# words=s.split()
# for word in words: #word='alex'
#     dic.setdefault(word,s.count(word))
# print(dic)

