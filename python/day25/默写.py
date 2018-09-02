class OldboyPeople:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
class Course:
    def __init__(self,c_name,c_price,c_priod):
        self.c_name=c_name
        self.c_prcie=c_price
        self.c_priod=c_priod
    def tell_course_info(self):
        print('<课程名字:%s 价格:%s 时长:%s>'%(self.c_name,self.c_prcie,self.c_priod))
class OldboyStudnet(OldboyPeople):
    def __init__(self,name,age,sex,score=0):
        OldboyPeople.__init__(self,name,age,sex)
        self.score=score
        self.courses=[]
    def choose_course(self):
        print('%s正在选课'%self.name)
    def check_course(self):
        print(('%s的课程'%self.name).center(50,'*'))
        for i in self.courses:
            i.tell_course_info()
        print('*'*60)
class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,revel):
        OldboyPeople.__init__(self,name,age,sex)
        self.revel=revel
        self.courses=[]
    def core(self,stu,num):
        stu.score=num
    def check_course(self):
        print(('%s教授的课'%self.name).center(50,'*'))
        for i in self.courses:
            i.tell_course_info()
        print('*'*60)
python=Course('python全栈开发',1800,'5个月')
stu1=OldboyStudnet('张三',18,'male')
stu1.courses.append(python)
stu1.check_course()

tea1=OldboyTeacher('egon',18,'male','10')
tea1.courses.append(python)
tea1.check_course()




