#2
# student_info=[
#     {
#         'name':'张无忌',
#         'number':'sh01',
#         'math':90,
#         'english':87,
#         'chinese':56
#     },
#     {
#         'name':'武则天',
#         'number':'sh02',
#         'math':40,
#         'english':97,
#         'chinese':67
#     }
# ]
# def update_student_info(student):
#     student_info.append(student)
# def delete_student_info(id=None,name=None):
#     i=get_student_info(name=name,id=id)[1]
#     student_info.pop(i)
# def get_student_info(name=None,id=None):
#     if id==None:
#         """根据名字找到学生的信息"""
#         for i,student in enumerate(student_info):
#             if name == student['name']:
#                 return student,i
#         else:
#             return False
#     else:
#         """根据学号找到学生的信息"""
#         for i,student in enumerate(student_info):
#             if id == student['number']:
#                 return student,i
#         else:
#             return False
# def name_get_score():
#     """获取指定学生的成绩"""
#     name=input('请输入学生的姓名:').strip()
#     student_info=get_student_info(name=name)
#     if student_info==False:
#         print('该同学不存在')
#         return
#     if student_info:
#         student_info=student_info[0]
#         print("""
#         name:%s
#         math:%s
#         english:%s
#         chinese:%s
#         """%(name,student_info['math'],student_info['english'],student_info['chinese']))
#
# def number_get_score():
#     """获取指定学号的成绩"""
#     id=input('请输入学生的学号:').strip()
#     student_info = get_student_info(id=id)
#     if student_info:
#         student_info=student_info[0]
#         print("""
#             number:%s
#             math:%s
#             english:%s
#             chinese:%s
#             """ % (id,student_info['math'], student_info['english'], student_info['chinese']))
#     else:
#         print('该同学不存在')
#
# def number_modification_name():
#     """根据学生的学号修改姓名"""
#     id=input('请输入学号:').strip()
#     student_info =get_student_info(id=id)
#     if student_info:
#         uname=input('请输入姓名:').strip()
#         student_info[0]['name']=uname
#         delete_student_info(name=uname)
#         update_student_info(student_info[0])
#         print('修改成功')
#     else:
#         print('该同学不存在')
# def name_modification_score():
#     """根据学生的姓名修改成绩"""
#     name = input('请输入姓名:').strip()
#     student_info = get_student_info(name=name)
#     if student_info:
#         math=int(input('请输入数学成绩:').strip())
#         english=int(input('请输入英文成绩:').strip())
#         chinese=int(input('请输入语文成绩:').strip())
#         student_info[0]['math'] = math
#         student_info[0]['chinese'] = chinese
#         student_info[0]['english'] = english
#         delete_student_info(name=name)
#         update_student_info(student_info[0])
#         print('修改成功')
#     else:
#         print('该同学不存在')
# def name_delete_score():
#     name=input('请输入名字:').strip()
#     delete_student_info(name=name)
#     print('删除成功')
# dic={
#     '1':name_get_score,
#     '2':number_get_score,
#     '3':number_modification_name,
#     '4':name_modification_score,
#     '5':name_delete_score
# }
# while True:
#     print("""
# 1 获取指定学生的成绩
# 2 获取指定学号的成绩
# 3 根据学生的学号修改姓名
# 4 根据姓名修改指定学科的成绩
# 5 删除指定学生及其成绩
#     """)
#     choice=input('>>:').strip()
#     if choice in dic:
#         dic[choice]()
#3
# 3.1
# import os
# def alter_file(file_path,old,new):
#     with open(file_path,'r',encoding='utf8')as read_f,\
#         open('%s.swap'%file_path,'w',encoding='utf8')as write_f:
#         for line in read_f:
#             line=line.replace(old,new)
#             write_f.write(line)
#     os.remove(file_path)
#     os.rename('%s.swap'%file_path,file_path)
#      print('修改成功')
#
# file_path=input('请输入要修改的文件地址:').strip()
# old=input('请输入原内容:').strip()
# new=input('请输入新内容:').strip()
# alter_file(file_path,old,new)
# 3.2

# def calculate(str1):
#     number_count = 0
#     letter_count=0
#     bank_count=0
#     else_ount=0
#     for i in str1:
#         i=str(i)
#         if i.isdigit():
#             number_count+=1
#         elif i.isalpha():
#             letter_count+=1
#         elif i==' ':
#             bank_count+=1
#         else:
#             else_ount+=1
#     print('数字:%s,字母:%s,空格:%s,其他:%s'%(number_count,letter_count,bank_count,else_ount))
# str1=input('请输入:')
# calculate(str1)

#3.3
# def judge(str):
#     if len(str)>5:
#         print('yes')
#     else:
#         print('no')
# judge(input('请输入:'))

#3.4
# def judge(str):
#     if len(str)>2:
#         str=str[0:2]
#     return str
# print(judge([1,2,3]))

# 3.5
# def foo(l):
#     l=list(l[1::2])
#     return l
# print(foo([1,2,3,4]))

# 3.6
# def foo(dic):
#     for key,value in dic.items():
#         if len(value)>2:
#             value=value[0:2]
#             dic[key]=value
#     return dic
#
# print(foo(dic = {"k1": "v1v1", "k2": [11,22,33,44]}))












