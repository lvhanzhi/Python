# 默写:
# 	开闭原则
# 封闭指的是对修改封闭,对扩展开放
# 	什么样的函数称为闭包
# 闭：指的是闭包函数是定义在一个函数内部的函数
# 包：该内部函数包含对外层函数作用域名字的引用
# 	python中什么是装饰器
# 器:指的是具备某一功能的工具
# 装饰:指的是为被装饰器对象添加新功能
# 装饰器就是用来为被装饰器对象添加新功能的工具
# 	装饰器的两个原则
# 不修改被装饰对象的源代码
# 不修改被装饰器对象的调用方式

# user_dic={
#     'name':None
# }
# def login(engine='file'):
#     def outter(func):
#         def wrapper(*args,**kwargs):
#             if user_dic['name']:
#                 print('您已经登录')
#                 res=func(*args,**kwargs)
#                 return res
#             if engine=='file':
#                 name=input('请输入用户名:').strip()
#                 pwd=input('请输入密码:').strip()
#                 if name=='egon' and pwd=='123':
#                     print('恭喜登录成功')
#                     user_dic['name']=name
#                     res=func(*args,**kwargs)
#                     return res
#                 else:
#                     print('用户名或密码错误')
#             elif engine=='mysql':
#                 print('mysql')
#             elif engine=='db..':
#                 print("db..")
#         return wrapper
#     return outter
# @login(engine='file')
# def foo():
#     print('runn...')
# foo()



user_dic={
    'name':None
}
def login(engine='file'):
    def outter(func):
        def wrapper(*args,**kwargs):
            if user_dic['name']:
                print('您已登录')
                res=func(*args,**kwargs)
                return res
            if engine=='file':
                name=input('name:').strip()
                pwd=input('pwd:').strip()
                if name=='egon' and pwd=='123':
                    print('恭喜登录成功')
                    res=func(*args,**kwargs)
                    return res
                else:
                    print('用户名或密码错误')
            elif engine=='mysql':
                print('用Mysql的认证机制')
            elif engine=='dlap':
                print('用dlap的认证机制')
            else:
                print('没有这种机制')
        return wrapper
    return outter
@login(engine='file')
def foo():
    print('running..')
foo()





































