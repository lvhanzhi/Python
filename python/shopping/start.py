import os, time, json

user_login = {
    'name': None,
    'is_auth': False
}


# 装饰器验证登录:
def get_login(func):
    def wrapper(*args, **kwargs):
        if user_login['is_auth']:
            res = func(*args, **kwargs)
            return res
        else:
            print('您还未登录,请先登录')
            login()

    return wrapper


# 获取用户信息
def get_user_info(name):
    path = '%s.json' % name
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf8')as f:
            return json.load(f)
    else:
        return False


# 写用户信息
def write_user(dic):
    path = '%s.json' % dic['name']
    with open(path, 'w', encoding='utf8')as f:
        json.dump(dic, f)
        f.flush()


# 操作记录
def logger(name,message):
    with open('log.txt','a',encoding='utf8')as f:
        f.write('%s %s,用户名为:%s\n'%(time.strftime('%Y-%m-%d %X'),message,name))
def register():
    while True:
        name = input('请输入用户名:').strip()
        if name == 'q': break
        user_info = get_user_info(name)
        if user_info:
            print('用户名重复')
        else:
            pwd = input('请输入密码:').strip()
            if len(pwd) < 6:
                print('密码至少6位')
            else:
                user_dic = {
                    'name': name,
                    'pwd': pwd,
                    'shopping_car': {},
                    'locked': False,
                    'balance': 15000,
                    'time': 0,
                    'count': 0,
                    'cost': 0
                }
                write_user(user_dic)
                print('恭喜注册成功,您的余额为15000')
                logger(name,message='执行了注册')
                break


def login():
    while True:
        name = input('请输入用户名:').strip()
        if name == 'q': break
        user_info = get_user_info(name)
        if user_info:
            if user_info['count'] >= 3 and not user_info['locked']:
                print('登录次数过多,锁定')
                user_info['time'] = time.time()
                user_info['locked'] = True
                write_user(user_info)
                break
            elif user_info['count'] >= 3 and user_info['locked']:
                if time.time() > user_info['time'] + 5:
                    user_info['time'] = 0
                    user_info['count'] = 0
                    user_info['locked'] = False
                    write_user(user_info)
                else:
                    print('锁定时间还没到')
                    break
            pwd = input('请输入密码:').strip()
            if pwd == user_info['pwd'] and not user_info['locked']:
                print('恭喜登录成功')
                user_login['name'] = name
                user_login['is_auth'] = True
                logger(name, message='执行了登录')
                break
            else:
                print('用户名或密码错误')
                user_info['count'] += 1
                write_user(user_info)
        else:
            print('该用户不存在')


@get_login
def shopping():
    cost = 0
    shopping_car = {}
    menu = {
        '大白菜': 10,
        '咖啡': 50,
        'iphone': 5800
    }
    menu_list = []
    user_info = get_user_info(user_login['name'])
    balance = user_info['balance']
    print('%s您的账户余额为%s' % (user_login['name'], balance))
    if len(user_info['shopping_car']) != 0:
        print('您上次购物的清单还未结算')
        return
    while True:
        print('---------菜单----------')
        print('序号    商品名     价格')
        for index, produce in enumerate(menu):
            print('%s   %s    %s' % (index, produce, menu[produce]))
            menu_list.append([produce, menu[produce]])
        choice = input('请选择或按q退出:').strip()
        if choice.isdigit() or choice in menu:
            if choice.isdigit():
                choice = int(choice)
                if choice >= 0 and choice < len(menu):
                    choice = menu_list[choice][0]
                else:
                    print('没有该商品')
                    continue
            name = choice
            price = menu[choice]
            if balance >= price:
                if choice in shopping_car:
                    shopping_car[name]['count'] += 1
                else:
                    shopping_car[name] = {'price': price, 'count': 1}
                balance -= price
                cost += price
                print('您已把%s加入购物车' % (choice))
            else:
                print('您的余额不足')
                continue
        elif choice == 'q':
            user_info['cost'] = cost
            user_info['shopping_car'] = shopping_car
            write_user(user_info)
            break
        else:
            print('没有这件商品')


@get_login
def see_shopping_car():
    logger(user_login['name'], message='查看了购物车')
    user_info = get_user_info(user_login['name'])
    cost = user_info['cost']
    shopping_car = user_info['shopping_car']
    if len(shopping_car) == 0:
        print('您没有购买任何东西')
        return
    print('---------------购物清单--------------')
    print('编号   商品名    价格     数量    总价')
    for i, produce in enumerate(shopping_car):
        print('%s   %s   %s   %s    %s' % (
            i, produce, shopping_car[produce]['price'], shopping_car[produce]['count'],
            shopping_car[produce]['price'] * shopping_car[produce]['count']))
    print('总价为%s' % cost)
    print("""
        1 结算
        2 清空
        """)
    choice = input('>>:').strip()
    if choice == '1':
        user_info['balance'] = user_info['balance'] - cost
        user_info['shopping_car'] = {}
        user_info['cost'] = 0
        write_user(user_info)
        print('购买成功,您的余额为%s' % user_info['balance'])
    elif choice == '2':
        user_info['shopping_car'] = {}
        user_info['cost'] = 0
        write_user(user_info)
        print('已取消购买')
    else:
        print('错误输入')


@get_login
def update_user_info():
    print("""
        1 修改密码
        2 注销账户
        """)
    choice = input('>>:').strip()
    if choice == '1':
        pwd = input('请输入新密码:').strip()
        if len(pwd) >= 6:
            user_info = get_user_info(user_login['name'])
            user_info['pwd'] = pwd
            write_user(user_info)
            print('修改成功')
            logger(user_login['name'], message='修改了密码')
        else:
            print('修改失败,密码必须是6位')
    elif choice == '2':
        os.remove('%s.json' % user_login['name'])
        user_login ['name']= None
        user_login['is_auth']=False
        print('注销成功')


@get_login
def user_add_money():
    user_info = get_user_info(user_login['name'])
    money = input('请输入充值金额:').strip()
    if money.isdigit():
        money = int(money)
        if money >= 0:
            user_info['balance'] += money
            write_user(user_info)
            print('充值成功')


dic = {
    '1': register,
    '2': login,
    '3': shopping,
    '4': see_shopping_car,
    '5': update_user_info,
    '6': user_add_money,
}
while True:
    print("""
    1 注册
    2 登录
    3 购物
    4 查看购物车
    5 账户信息
    6 账户充值
    """)
    choice = input('>>:').strip()
    if choice in dic:
        dic[choice]()
    elif choice == 'q':
        break
    else:
        print('非法输入')
