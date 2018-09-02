# # 　　 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
#
# l=[
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'alex','age':73,'sex':'male'},
#     {'name':'egon','age':20,'sex':'female'},
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'egon','age':18,'sex':'male'},
# ]
# # 定义函数,既可以针对可以hash类型又可以针对不可hash类型
# def func(items,key=None):
#     s=set()
#     for item in items:
#         val=item if key is None else key(item)
#         if val not in s:
#             s.add(val)
#             yield item
#
# print(list(func(l,key=lambda dic:(dic['name'],dic['age'],dic['sex']))))





menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
dic=[menu,]
while True:
    dic_menu = dic[-1]
    for i in dic_menu:
        print(i)
    choice = input('>>:').strip()
    if choice=='q':
        break
    elif choice=='b':
        dic.pop(-1)
        continue
    dic.append(dic_menu[choice])















