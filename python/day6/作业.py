# 1.餐厅提供了五种不同的菜,使用元组来存储他们,并循环打印出所有菜名,要求用户输入新加的菜名,加入到菜单中,并重新输出
# menu=('芹菜','白菜','萝卜','西红柿','土豆')
# l=[]
# for i in menu:
#     l.append(i)
#     print(i)
# while True:
#     greens=input('请输入要添加的菜名or输入q退出:').strip()
#     if greens=='q':break
#     l.append(greens)
# print(tuple(l))
# 2.使用列表存储1-10所有的平方数
# l=[]
# for i in range(1,11):
#     l.append(i**2)
# print(l)
# 3.使用三种不同的语法 创建内容包含name和age的字典
# dic={
#     'name':'egon',
#     'age':18
# }
# print(dic)
# dic=dict((['name','egon'],['age',18]))
# print(dic)
# dic=dic.fromkeys(['name','age'],None)
# print(dic)
# 4.在使用字典存储你和你左右同学的信息然后将它们存储在一个列表中最后循环输出所有信息
# dic={
#     '我':{
#         'name':'tom',
#         'age':18
#     },
#     '你':{
#         'name':'Mr zhang',
#         'age':15
#     },
#     '他':{
#         'name':'Mr lv',
#         'age':12
#     }
# }
# l=[]
# for key,value in dic.items():
#     l.append([key,value])
# for i in l:
#     print(i)
# 5.请写出代码验证 交集 合计 对称差集 差集 子集 父集的效果
# pythons={'李二丫','张金蛋','李银弹','赵铜蛋','张锡蛋','alex','oldboy'}
# linuxs={'lxx','egon','张金蛋','张锡蛋','alex','陈独秀'}
# print(pythons|linuxs)
# print(pythons&linuxs)
# print(pythons^linuxs)
# print(pythons-linuxs)
# print(pythons<=linuxs)
# print(pythons>=linuxs)
# 6.举例子说明元组 列表 集合 的使用场景
# 元祖:不改变里面值的
# 列表:需要用到多个值
# 集合:用来做逻辑运算,去重
# 7.对于字典 有多重方式可以删除一个键值对
# 	dic.pop("key")
# del dic['key']
# 	两种方法有什么不同
# 是否有返回值
# res=dic.pop('name')#返回要删除的value值,没有要删除的值则报错
# print(res)
# print(dic)
# 尝试:
# 	编写程序实现以下功能
# 		要求用户输入音乐数据 包括 类型,名字,作者,时长,发布时间
# 		每种类型可以有多个音曲目信息(循环录入多个曲目)
# 		输入指定命令可以退出输入
# 		输入完成后
# 			可以按照类型查看音乐
# 			可以按照名称查看音乐
# 			拓展,按照名称查看时 可以模糊查找 例如 输入 气球 可以查看到 告白气球
#
# 	注:先完成录入部分 在完成查看信息部分
# dic = {}
# while True:
#     muse_type = input('请输入音乐类型或输入q退出:').strip()
#     if muse_type == 'q': break
#     if muse_type not in dic:
#         dic[muse_type] = []
#     title = input('请输入歌名:').strip()
#     auth = input('请输入作者:').strip()
#     time = input('请输入时长:').strip()
#     data = input('请输入发布时间:').strip()
#     dic_music_info = {
#         'title': title,
#         'auth': auth,
#         'time': time,
#         'data': data,
#     }
#     dic[muse_type].append(dic_music_info)
#
# while True:
#     print("""
#     1 按照类型查看音乐
#     2 按照名称查看音乐
#     3 按照名称查看(可以模糊查找)
#     """)
#     choice=input('>>:').strip()
#     if choice=='1':
#         muse_type=input('请输入类型:').strip()
#         if muse_type not in dic:
#             print('不存在这个类型')
#             continue
#         muser_sum=dic[muse_type]
#         for i in muser_sum:
#             print(i['title'])
#     elif choice=='2':
#         muse_name=input('请输入歌曲名称:').strip()
#         for key,value in dic.items():
#             for i in value:
#                 if i['title']==muse_name:
#                     print(i)
#     elif choice=='3':
#         muse_name = input('请输入歌曲名称:').strip()
#         for key, value in dic.items():
#             for i in value:
#                 if muse_name in i['title']:
#                     print(i)
