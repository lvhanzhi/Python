from abc import abstractmethod,ABCMeta
class Pet(metaclass=ABCMeta):
    def __init__(self,name):
        self.__name=name
    @abstractmethod
    def eat(self):
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name=new_name
        return self.__name
class Master:
    def __init__(self,name,pet):
        self.__name=name
        self.__pet=pet
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        return self.__name

    @property
    def pet(self):
        return self.__pet

    @pet.setter
    def pet(self, new_pet):
        self.__pet = new_pet
        return self.__pet
    def feed(self):
        print('%s主人准备好宠物粮食'%self.__name)
        print('%s的%s来进食'%(self.__pet.type,self.__pet.name))
        self.__pet.eat()

class Cat(Pet):
    def __init__(self,name,type):
        super(Cat,self).__init__(name)
        self.__type=type
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,new_type):
        self.__type=new_type
        return self.__type
    def eat(self):
        print('吃猫粮')
class Dog(Pet):
    def __init__(self,name,type):
        super(Dog,self).__init__(name)
        self.__type=type
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,new_type):
        self.__type=new_type
        return self.__type
    def eat(self):
        print('吃狗粮')
class Pig(Pet):
    def __init__(self,name,type):
        super(Pig,self).__init__(name)
        self.__type=type
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,new_type):
        self.__type=new_type
        return self.__type
    def eat(self):
        print('吃猪粮')
cat=Cat('cat','cat')
dog=Dog('dog','dog')
pig=Pig('pig','pig')
egon=Master('egon',cat)
alex=Master('alex',dog)
wupeiqi=Master('wupeiqi',pig)
egon.feed()
alex.feed()
wupeiqi.feed()