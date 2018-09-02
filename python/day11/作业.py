# 一：编写函数，（函数执行的时间是随机的）
# import random,time
# def foo():
#     time.sleep(random.randint(0,5))
#     print('running...')
# foo()

# 二：编写装饰器，为函数加上统计时间的功能
# import time,random
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         end_time=time.time()
#         print(end_time-start_time)
#         return res
#     return wrapper
# @timmer
# def foo():
#     time.sleep(random.randint(0, 5))
#     print('running...')
# foo()


# 三：编写装饰器，为函数加上认证的功能
# def authentication(func):
#     def wrapper(*args,**kwargs):
#         name=input('请输入用户名:').strip()
#         pwd=input('请输入密码:').strip()
#         if name=='egon' and pwd=='123':
#             print('恭喜登录成功')
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print('用户名或密码错误')
#     return wrapper
# @authentication
# def run():
#     print('running...')
# run()


# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式
# current_user={
#     'name':None
# }
# def authentication(engine='file'):
#     def approve(func):
#         def wrapper(*args,**kwargs):
#             if current_user['name']:
#                 print('您已登录')
#                 res=func(*args,**kwargs)
#                 return res
#             if engine=='file':
#                 name=input('请输入姓名:').strip()
#                 pwd=input('请输入密码:').strip()
#                 with open('db.txt','r',encoding='utf8')as f:
#                     for line in f:
#                         line=eval(line)
#                         if line['name']==name and line['password']==pwd:
#                             print('恭喜登录成功')
#                             current_user['name']=name
#                             res=func(*args,**kwargs)
#                             return res
#                     else:
#                         print('用户名或密码错误')
#             elif engine=='mysql':
#                 pass
#             elif engine=='ldap':
#                 pass
#             else:
#                 print('没有这种机制')
#         return wrapper
#     return approve
# @authentication()
# def foo():
#     print('running...')
# foo()
# 五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
# import time
# current_user={
#     'name':None,
#     'time':None
# }
# def authentication(engine='file'):
#     def approve(func):
#         def wrapper(*args,**kwargs):
#             now_time=time.time()
#             if current_user['name'] and now_time-current_user['time']<=100:
#                 print('您已登录')
#                 res=func(*args,**kwargs)
#                 return res
#             if engine=='file':
#                 name=input('请输入姓名:').strip()
#                 pwd=input('请输入密码:').strip()
#                 with open('db.txt','r',encoding='utf8')as f:
#                     for line in f:
#                         line=eval(line)
#                         if line['name']==name and line['password']==pwd:
#                             print('恭喜登录成功')
#                             now_time=time.time()
#                             current_user['name']=name
#                             current_user['time']=now_time
#                             res=func(*args,**kwargs)
#                             return res
#                     else:
#                         print('用户名或密码错误')
#             elif engine=='mysql':
#                 pass
#             elif engine=='ldap':
#                 pass
#             else:
#                 print('没有这种机制')
#         return wrapper
#     return approve
# @authentication()
# def foo():
#     print('running...')
# foo()
# time.sleep(1)
# foo()

#
# 六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# import requests
# def outter(url):
#     def inner():
#         response = requests.get(url)
#         print(response.text)
#     return inner
# baidu=outter('http://www.baidu.com')
# baidu()


# 七：为题目五编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中
# import requests,os
# def cache(func):
#     def wrapper(*args, **kwargs):
#         info=os.path.getsize('url.txt')
#         if info == 0:
#             url = args[0]
#             res = requests.get(url).text
#             with open('url.txt', 'w', encoding='utf8')as f:
#                 f.write(res)
#             res=func(*args, **kwargs)
#             return res
#         else:
#             res = func(*args, **kwargs)
#             return res
#     return wrapper
# @cache
# def outter(url):
#     def inner():
#         response = requests.get(url)
#         print(response.text)
#     return inner
# baidu=outter('http://www.baidu.com')
# qq=outter('http://www.qq.com/')
# baidu()
# qq()
# 扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中


# 八：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
# dic={}
# def create_dic(func):
#     def wrapper(*args,**kwargs):
#         l=len(dic)
#         dic['%s'%(l+1)]=func
#         res=func(*args,**kwargs)
#         return res
#     return wrapper
# @create_dic
# def login():
#     print('登录...')
# login()
# print(dic)

# 九 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取
# import time
# time.strftime('%Y-%m-%d %X')
# import time
# def get_log(func):
#     def wrapper(*args,**kwargs):
#         with open('log.txt','a',encoding='utf8')as f:
#             f.write('%s %s run'%(time.strftime('%Y-%m-%d %X'),func))
#         res=func(*args,**kwargs)
#         return res
#     return wrapper
# @get_log
# def f1():
#     print('f1 running...')
#
# f1()