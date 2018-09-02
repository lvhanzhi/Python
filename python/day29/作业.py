# 1.
# 异常作业
# 自定义一个Integer类
# -- 该类有个input方法，调用该方法一定会得到一个合法的数字(非数字为不合法，越界为不合法)
# ---- 如果是非数字不合法，需要打印不合法消息，然后用户需要重新输入
# -- 如输入
# 'abc'，不合法消息就为：invalid
# literal
# for int() with base 10: 'abc'
# ---- 如果是越界不合法，需要打印不合法消息，然后用户需要重新输入
# -- 如输入
# '2147483648'，不合法消息就为：ErrorMsg：2147483648 - 越界
# 提示：
# 1)该方法需要捕获并处理两次异常(内置异常ValueError，自定义异常SlopOverError)
# 2)该方法运用到递归方式处理更简单，如果用不到递归也可以
#
#                   - - 该类有个verifySlopOver方法，可以判断传入的数字是否越界(非 - 2147483648
# ~ 2147483647
# 为越界)
# ---- 如果数字越界，会主动抛出自定义SlopOverError异常，并传入数字和异常消息
# 自定义异常SlopOverError类
# - - 该类需要重写__init__方法
# - --- 有num、msg两个参数，num是数字类型的数，msg是字符串类型的异常消息
#                               - - 该类需要重写__str__方法
#                               - --- 通过num、msg两个属性格式化异常信息
class SlopOverError(BaseException):
    def __init__(self,num,msg):
        self.msg=msg
        self.num=num
    def __str__(self):
        return '%s:%s   - 越界'%(self.msg ,self.num)

class Integer:
    def input(self):
        try:
            num=input('请输入数字:').strip()
            num=int(num)
            self.num = num
        except ValueError:
            print("""invalid
literal
for int() with base 10: '%s'""" % num)
            self.input()
        else:self.verifySlopOver()
    def verifySlopOver(self):
        if self.num>2147483647 or self.num<-2147483648:
            print( SlopOverError(self.num,'ErrorMsg'))
            self.input()

n=Integer()
n.input()
print(n.num)



# 2.元类作业
#     自定义轿车元类CarMeta
# 	-- 实现元类为CarMeta的类至少有生产日期(production_date)、发动机编号(engine_number)及载客量(capacity)三个基本属性
# class CarMeta(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         super().__init__(class_name,class_bases,class_dic)
#     def __call__(self, *args, **kwargs):
#         obj=self.__new__(self)
#         self.__init__(obj,*args,**kwargs)
#         if not obj.__dict__.get('production_date') or not obj.__dict__.get('engine_number') or not obj.__dict__.get('capacity'):
#             raise TypeError('至少有生产日期(production_date)、发动机编号(engine_number)及载客量(capacity)三个基本属性')
#         return obj
# class Car(object,metaclass=CarMeta):
#     def __init__(self,production_date,engine_number,capacity):
#         self.production_date=production_date
#         self.engine_number = engine_number
#         self.capacity = capacity
# car=Car('1','1','1')
# print(car.production_date)








