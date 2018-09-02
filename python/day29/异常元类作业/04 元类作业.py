class CarMeta(type):
    # __init__ | __call__
    def __init__(cls, *args, **kwargs): # 类的名称空间
        pass

    def __call__(cls, *args, **kwargs): # 对象的名称空间
        # 为将要新建的对象开辟空间,返回空间的地址给对象指向
        car_obj = cls.__new__(cls)
        # 实例化对象
        # cls.__init__(car_obj, *args, **kwargs)
        car_obj.__init__(*args, **kwargs)
        for k in ['production_date', 'engine_number', 'capacity']:
            if k not in car_obj.__dict__:
                raise Exception("轿车非法")
        return car_obj
class Audi(metaclass=CarMeta):

    # production_date | engine_number | capacity
    def __init__(self, engine_number, capacity, color):
        # self.production_date = production_date
        self.engine_number = engine_number
        self.capacity = capacity
        self.color = color
a1 = Audi( "AD7345GTL", "2", "红色")
# a2 = Audi("1977-01-8", "AD4568GTL", "2", "银色")
# print(a1, a2.capacity)