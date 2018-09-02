def timmer(func):                  #1.return wrapper
    print('timmer')               #     foo=wrapper
    def wrapper(*args,**kwargs):
        print('timmer inner')
        res=func(*args,**kwargs)
        return res
    return wrapper
def timmer2(func):                 #1.return wrapper2
    print('timmer2')              #     foo=timmer(wrapper2)
    def wrapper2(*args,**kwargs):
        print('timmer2 inner')
        res=func(*args,**kwargs)
        return res
    return wrapper2
def timmer3(func):                  #1.return wrapper3
    print('timmer3')               #     foo=timmer(timmer2(wrapper3))
    def wrapper3(*args,**kwargs):
        print('timmer3 inner')
        res=func(*args,**kwargs)
        return res
    return wrapper3
@timmer   # foo=timmer(foo)  -----> foo=timmer(timmer2(timmer3(foo)))
@timmer2  #foo=timmer2(foo)
@timmer3  #foo=timmer3(foo)
#还没有调用foo就已经开始调用装饰器
def foo():
    pass
foo()
#开始调用返回的函数