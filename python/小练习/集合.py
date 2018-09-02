#空集合
msg=set()
print(msg,type(msg))
#不空的集合
msg={'张三','赵四'}
print(msg,type(msg))

x={1,2,3,2}
y={2,3,4}
print(x)#重复的会被删除
print(x&y)#交集
print(x|y)#并集
print(x-y)#差集（x有的y没有的）
print(x^y)#对称差集


# 一.关系运算
# 　　有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
# 　　pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# 　　linuxs={'wupeiqi','oldboy','gangdan'}
# 　　1. 求出即报名python又报名linux课程的学员名字集合
pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
linuxs={'wupeiqi','oldboy','gangdan'}
print(pythons&linuxs)
# 　　2. 求出所有报名的学生名字集合
print(pythons|linuxs)
# 　　3. 求出只报名python课程的学员名字
print(pythons-linuxs)
# 　　4. 求出没有同时这两门课程的学员名字集合
print((pythons-linuxs)|(linuxs-pythons))
print(pythons ^ linuxs)

# 1. 有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序
l=['a','b',1,'a','a']
l=set(l)
ccc=[]
for u in l:
    ccc.append(u)
print(ccc)

# 2.在上题的基础上，保存列表原来的顺序
l=['a','b',1,'a','a']
mm=[]
for g in l:
    if not g in mm:
        mm.append(g)
print(mm)