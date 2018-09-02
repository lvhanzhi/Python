# 默写:
# 	列表冒泡排序
#
# 必做:
# 	1.简述什么是字符编码,为什么出现
#     人操作计算机使用人类认识的字符，而计算机存放都是二进制数字
#     所以人在往计算机里输入内容的时候，必然发生：
#         人类的字符------（字符编码表）--------》数字
# 	2.使用字典实现三级菜单题目要求参考博客http://www.cnblogs.com/linhaifeng/articles/7133357.html#_label11
# menu = {
#     '北京':{
#         '海淀':{
#             '五道口':{
#                 'soho':{},
#                 '网易':{},
#                 'google':{}
#             },
#             '中关村':{
#                 '爱奇艺':{},
#                 '汽车之家':{},
#                 'youku':{},
#             },
#             '上地':{
#                 '百度':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '北航':{},
#             },
#             '天通苑':{},
#             '回龙观':{},
#         },
#         '朝阳':{},
#         '东城':{},
#     },
#     '上海':{
#         '闵行':{
#             "人民广场":{
#                 '炸鸡店':{}
#             }
#         },
#         '闸北':{
#             '火车战':{
#                 '携程':{}
#             }
#         },
#         '浦东':{},
#     },
#     '山东':{},
# }
# dic=[menu,]
# while True:
#     now_menu = dic[-1]
#     for city in now_menu:
#         print(city)
#     choice=input('>>:').strip()
#     if choice=='q':break
#     if choice=='b':
#         dic.pop(-1)
#         continue
#     if choice in now_menu:
#         dic.append(now_menu[choice])
#     else:
#         print('非法输入')
#         continue
# 	3.编写文件复制工具 输入源文件路径 输入目标文件路径 完成copy
# old_path=input('请输入源文件路径:').strip()
# new_path=input('请输入目标文件路径:').strip()
# with open(r'%s'%old_path,'r',encoding='gbk')as read_f,\
#     open(r'%s'%new_path,'w',encoding='gbk')as write_f:
#     for line in read_f:
#         write_f.write(line)

# 	4.登录注册购物车 提供以下功能
# 		1.注册
# 			用户名不能重复
# 			密码需二次确认
# 		2.登录读取数据判断是否登录成功
#
# 		3.修改密码
#
# 		4.查看商品列表
#
# 		5.将商品添加至购物车
#
# 		6.购物车中的商品结算

# 扩展:
# 	1.将作业2升级文文件版  使用户在退出程序后重新运行 依然可以访问自己的账户信息 购物车信息
# 	2.文档压缩工具
# 		可将多个文本文件合并为一个大文件
# 		可将合并后的大文件在切割为原本的小文件
import os
path_list = []
while True:
    choice=input('请选择打包还是解压(0or1),q退出:').strip()
    if choice=='0':
        while True:
            path = input('>>:')
            if path == 'q': break
            path_list.append(path)
        in_path=input('请输入要打包到哪个路径:').strip()
        for path in path_list:
            with open(r'%s'%path,'r',encoding='gbk')as read_f,\
                    open('%s'%in_path, 'a', encoding='gbk')as write_f:
                write_f.write(read_f.read() + '****')
            # os.remove(path)
        path_list.append(in_path)
        path_list=str(path_list)
        with open('db.txt','a',encoding='utf8')as f:
            f.write(path_list)
        path_list=list(path_list)
        path_list.clear()
        print('打包成功')
    elif choice=='1':
        all_path=input('请输入要解压的路径:').strip()
        with open(r'db.txt', 'r', encoding='utf8')as f:
            for line in f:
                line=line[0:-2]
                if line[-1]==all_path:
                    line.pop(-1)
                    path_list=list(line)
        with open(r'%s'%all_path, 'r', encoding='utf8')as f:
            info=f.read().split('****')
            for i in range(len(path_list)):
                with open(r'%s' % path_list[i], 'w', encoding='utf8')as write_in_f:
                    write_in_f.write(info[i])
            print('解压成功')
        path_list.append(all_path)
        print(path_list)
        os.remove(all_path)

    elif choice=='q':
        break
    path_list=str(path_list)
    with open('db.txt','a',encoding='utf8')as f:
        f.write(path_list)
    path_list=list(path_list)