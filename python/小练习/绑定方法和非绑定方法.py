class people:
    @classmethod
    def f1(cls):
        print(cls)
    def f2(self):
        print(self)
obj=people()
people.f1()
obj.f1()