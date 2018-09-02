# import json
# # dic={
# #     'name':'111',
# #     'age':18,
# #     'sex':'male'
# # }
# # with open('db.json','wt',encoding='utf8')as f:
# #     json.dump(dic,f)
# # with open('db.json','rt',encoding='utf8')as f:
# #     data=json.load(f)
# # print(data)
import json

dic = {'a': 1, 'b': 'B'}
with open('a.txt', 'a', encoding='utf8') as f:
    json.dump(dic, f)

# print(json.dumps(dic))
a = json.dumps(dic)  # a传输给其他机器  2.其他函数需要这个结果,传参给对应的函数
print(a)






