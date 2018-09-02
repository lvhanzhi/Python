menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

tag = True
while tag:
    for key in menu:
        print(key)
    city1 = input("第一级:").strip()
    if city1 == 'b':
        continue
    elif city1 == 'q':
        break
    elif not city1 in  menu:
        continue
    menu1 = menu[city1]
    for key in menu1:
        print(key)
    city2 = input("第二级:").strip()
    if city2 == 'b':
        continue
    elif city2 == 'q':
        break
    elif not city2 in  menu[city1]:
        continue
    menu2 = menu1[city2]
    for key in menu2:
        print(key)
    city3 = input("第三级:").strip()
    if city2 == 'b':
        continue
    elif city2 == 'q':
        break
    elif not city3 in  menu[city2]:
        continue
    menu3 = menu2[city3]
    for key in menu3:
        print(key)
    city4 = input().strip()
    if city3 == 'b':
        continue
    elif city3 == 'q':
        break
    elif not city4 in  menu[city3]:
        continue
