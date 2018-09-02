class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


class Course:
    def __init__(self,name,price,time):
        self.name=name
        self.price=price
        self.time=time
    def run(self):
        print('<%s %s %s>'%(self.name,self.price,self.time))

class Teacher(People):
    def __init__(self,name,age,sex,job_title):
        People.__init__(self,name,age,sex)
        self.job_title=job_title
        self.course=[]
        self.student=[]

class Student(People):
    def __init__(self,name,age,sex):
        People.__init__(self,name.age,sex)
        self.course=[]



t1=Teacher('张老师',55,'男','金牌讲师')
python=Course('python',111111,'3个月')
t1.course.append(python)
t1.course=python
t1.course.run()