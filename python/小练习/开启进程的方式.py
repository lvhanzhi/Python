# 方式一:
# from multiprocessing import Process
# # def task(x):
# #     pass
# # def func():
# #     pass
# # if __name__=='__main__':
# #     p=Process(target='task',args=(1,))
# #     p.start()
# #     func()

# 方式二:
# from multiprocessing import Process
# class Process:
#     def start(self):
#         self.run()
# class Myprocess(Process):
#     def run(self):
#         pass
# if __name__=='__main__':
#     p=Myprocess()
#     p.start()
#     func()


# 开启线程的两种方式(*****)
# 线程vs进程(*****)

# 方式一
# import time
# from threading import Thread
# def task(name):
#     print('%s is running '%name)
#     time.sleep(3)
#     print('%s is done'%name)
# if __name__=='__main__':
#     t=Thread(target=task,args=('子进程',))
#     t.start()
#     print('主')


# 方式二:
import time
from threading import Thread


class Mythread(Thread):
    def run(self):
        print('%s is running ' % self.name)
        time.sleep(3)
        print('%s is done' % self.name)


if __name__ == '__main__':
    t = Mythread()
    t.start()
    print('主')
