# 1.借助shelve模块，完成将数据
# 		"week": ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
# 		"person": {"name": "Zero", "age": 8, "height": 180}
# 		序列化到date.shl文件中
# 		并反序列化来测试文件中的数据：如访问数据	"Tues"及"Zero"
# 	探索：
# 		自定义一个有打印语句的简单函数，将函数序列化到文件中，在反序列化测试函数中的打印语句

# import shelve
# f = shelve.open('date.shl')
# f['week'] = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
# f['person']={"name": "Zero", "age": 8, "height": 180}
# f.close()

# def foo():
#     print('foo')
# import shelve
# f = shelve.open('date.shl')
# f['foo'] = foo
# f.close()
# import shelve
# f=shelve.open('date.shl')
# message=f.get('foo')#print(f.get('a'))
# f.close()
# print(message)
# message()



# 2.有一个people.xml文件，内容如下
# 	<?xml version="1.0" encoding="utf-8" ?>
# 	<Peoples value="人们">
#     	    存放所有嘉宾的xml文件
#     	    <People flag="一号男嘉宾">
# 		<name>张三</name>
# 		<age>20</age>
# 		<gender>男</gender>
# 	    </People>
# 	    <People flag="一号女嘉宾">
# 		<name>李四</name>
# 		<age>18</age>
# 		<gender>女</gender>
# 	    </People>
# 	</Peoples>
# 	遍历输出xml文件中的所有数据

# import xml.etree.ElementTree as et
# tree=et.parse('people.xml')
# root=tree.getroot()
# print(root.tag,root.attrib,root.text)
# for country in root:
#     print(country.tag,country.attrib,country.text)
#     for t in country:
#         print(t.tag,t.attrib,t.text)



# 3.模拟加密过程
# 		1）账号密码有用户键盘输入
# 		2）对得到的账号密码进行md5方式加密处理(采取加盐)
# 		3）提前建立基本的碰撞测试库
# 		4）对于用户输入的账号密码进行反馈
# 			-- 解密成功
# 			-- 解密失败

# name=input('请输入用户名:').strip()
# pwd=input('请输入密码:').strip()
# import hashlib
# md5_obj=hashlib.md5(name.encode('utf8'))
# md5_obj.update(pwd.encode('utf8'))
# pwd_dic = {"123456":"e10adc3949ba59abbe56e057f20f883e","hello":"5d41402abc4b2a76b9719d911017c592"}
# for i in pwd_dic:
#     if pwd_dic[i]==md5_obj:
#         print(i)
#         print('解密成功')
#         break
# else:
#     print('解密失败')

