import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# from conf import settings
from lib import common

DB_PATH =os.path.join(BASE_DIR,'db','db.txt')
LOG_PATH = os.path.join(BASE_DIR,'log','access.log')


# 获取文本内账户信息
def info():
    user_info = []
    with open('%s' % DB_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split(',')
            user_info.append(line)
        return user_info


# 检测额度是否为数字
def check_balance(bal):
    user_bal_info = []
    if bal.isdigit():
        print('余额输入正确')
        user_bal_info.append(bal)
        user_bal_info.append(False)
        return user_bal_info
    else:
        print('请输入数字')
        user_bal_info.append(bal)
        user_bal_info.append(True)
        return user_bal_info


# 将用户信息写入文件（a模式）
def write_info(name, pwd, bal):
    with open('%s' % DB_PATH, 'a', encoding='utf-8') as f:
        f.write('%s,%s,%s\n' % (name, pwd, bal))
        # print(f.read())

# 商城购物车
def shop():
    import os
    import time
    current_info = []
    shopping = {}
    goods = {'apple': 5000,
             'water': 100,
             }
    if len(current_user_info) == 0:
        print('请先登录！！')
    else:
        gd_info = []
        tag = True
        print('=====================商品信息======================')
        for goods_info in enumerate(goods):
            print('商品编号:%s      商品名：%s     价格：%s   ' % (goods_info[0], goods_info[1], goods[goods_info[1]]))
        while tag:
            choice = input('输入您想要买的商品编号或输入q退出并查看已购商品：')
            if choice in ['0', '1', '2', '3']:
                for goods_info in enumerate(goods):
                    choice = int(choice)
                    current_user_info[2] = int(current_user_info[2])
                    if choice == goods_info[0]:
                        if current_user_info[2] > goods[goods_info[1]]:
                            current_user_info[2] = current_user_info[2] - goods[goods_info[1]]
                            print('尊敬的%s,您本回购买的商品为%s，单价为%s，您的余额为%s。' % (
                                current_user_info[0], goods_info[1], goods[goods_info[1]], current_user_info[2]))
                            if goods_info[1] in shopping:
                                shopping[goods_info[1]]['count'] += 1
                            else:
                                shopping[goods_info[1]] = {'count': 1, 'price': goods[goods_info[1]]}
                        else:
                            print('您的余额不够购买此商品！请重新选择或退出！')
            if choice in ['0', '1', '2', '3'] or choice == 'q':
                print('您已购买的商品为：')
                for k in shopping:
                    print('商品%s,数量：%s,单价：%s' % (k, shopping[k]['count'], shopping[k]['price']))
                print('尊敬的用户%s，您的账户余额为：%s' % (current_user_info[0], current_user_info[2]))
                with open('log.txt', 'a', encoding='utf-8') as f:
                    local_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    f.write('时间%s,增加账户%s,额度%s\n' % (local_time, current_user_info[0], current_user_info[2]))
                with open(r'db.txt', 'r', encoding='utf-8') as p1, \
                        open(r'a', 'w', encoding='utf-8') as p2:
                    data = p1.readlines()
                    for u_line in data:
                        u_line = u_line.strip('\n')
                        u_line = u_line.split(',')
                        if u_line[0] == current_user_info[0]:
                            u_line[2] = '%s' % (current_user_info[2])
                        u_line = '%s,%s,%s\n' % (u_line[0], u_line[1], u_line[2])
                        p2.write(u_line)
                os.remove('db.txt')
                os.rename('a', 'db.txt')
                break
            else:
                print('非法输入！！')


# 用户认证
def auth():
    import time
    while True:
        uname = input('name>>:').strip()
        with open('log.txt', 'a', encoding='utf-8') as f:
            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write('时间%s,账户%s尝试登陆\n' % (str(local_time), uname))
        with open('log.txt', 'r', encoding='utf-8') as f:
            line = f.read().split(',')
            if uname in line:
                print('您的账户已被锁定')
                continue
        pwd = input('请输入密码').strip()
        if pwd.isdigit():
            print('密码格式正确')
        else:
            print('输入有误')
        for user_info in info():
            if uname == user_info[0] and pwd == user_info[1]:
                print('auth success')
                current_user_info.append(uname)
                current_user_info.append(pwd)
                current_user_info.append(user_info[2])
                return
        else:
            print('密码或用户名错误')
            continue


# 退出时写入信息
def wri(account, money):
    import os
    # money = str(money)
    with open(r'db.txt', 'r', encoding='utf-8') as f, \
            open(r'db.swap.txt', 'w', encoding='utf-8') as g:
        data = f.readlines()
        # print(data)
        for w in data:
            # print(data)
            # print(w)
            w = w.strip('\n')
            w = w.split(',')
            if account == w[0]:
                w[2] = money
            g.write('%s,%s,%s\n' % (w[0], w[1], w[2]))
    os.remove('db.txt')
    os.rename('db.swap.txt', 'db.txt')


# 添加账户
def add_account():
    # 输入用户名
    import time
    register_info = []
    while True:
        uname = input('请输入用户名').strip()
        for user_info in info():
            if uname == user_info[0]:
                print('用户名重复')
                break
        else:
            print('恭喜，此用户名可用')
            register_info.append(uname)
            break
    # 输入密码
    while True:
        pwd1 = input('请输入密码').strip()
        pwd2 = input('请再次输入密码').strip()
        if pwd1 == pwd2:
            print('两次密码输入正确')
            print('账户注册成功')
            register_info.append(pwd1)
            break
        else:
            print('两次密码输入不同')
    # 添加账户到数据库
    write_info(register_info[0], register_info[1], bal=15000)
    # 写入用户信息到日志
    with open('log.txt', 'a', encoding='utf-8') as f:
        local_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write('时间%s,增加账户%s,额度%s\n' % (local_time, register_info[0], 15000))


# 修改额度
def change_bal():
    import time
    # 输入余额
    bal = input('请输入余额')
    while check_balance(bal)[1]:
        bal = input('请输入余额')
    wri(current_user_info, bal)
    with open('%s_log.txt' % current_user_info[0], 'a', encoding='utf-8') as f:
        local_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write('时间%s,账户%s,修改余额%s\n' % (local_time, current_user_info[0], bal))
    with open('log.txt', 'a', encoding='utf-8') as f:
        local_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write('时间%s,账户%s,修改余额%s\n' % (local_time, current_user_info[0], bal))
        wri(current_user_info[0], bal)
        print('时间%s,账户%s,修改余额%s\n' % (local_time, current_user_info[0], bal))


# 全局变量
import time

user_info = info()
current_user_info = []
local_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
def run():
    while True:
        print("""
        0.购物
        1.注册
        2.登录
        3.提现
        4.转账
        5.还款
        6.流水
        7.操作日志
        8.管理接口（添加账户get，用户额度get，冻结账户）
        9.退出
        """)
        choice = input('请输入功能编号')
        # 注册
        if choice == '0':
            shop()
        if choice == '1':
            add_account()
        # 登录验证
        if choice == '2':
            auth()
        if choice == '3':
            import time

            tag = True
            if len(current_user_info) == 0:
                print('请先登录')
            else:
                # 提现
                while tag:
                    cash_num = input('请输入取现金额')
                    if cash_num.isdigit():
                        print('输入正确')
                        for user_info in info():
                            if current_user_info[0] in user_info:
                                current_user_info[2] = float(current_user_info[2]) - int(cash_num) * 1.05
                                # 将修改记录写入文件
                                with open('%s_log.txt' % current_user_info[0], 'a', encoding='utf-8') as f:
                                    local_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                                    f.write('时间%s,账户%s,提现%s,余额%s\n' % (
                                        local_time, current_user_info[0], cash_num, current_user_info[2]))
                                with open('log.txt', 'a', encoding='utf-8') as f:
                                    local_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                                    f.write('时间%s,账户%s,提现%s,余额%s\n' % (
                                        local_time, current_user_info[0], cash_num, current_user_info[2]))
                                wri(current_user_info[0], current_user_info[2])
                                print('取现金额%s,剩余余额%s' % (cash_num, current_user_info[2]))
                                tag = False
                    else:
                        print('请输入数字')
        if choice == '4':
            # 账户间转账
            import time

            tag = True
            if len(current_user_info) == 0:
                print('请先登录')
            else:
                src_account = current_user_info[0]
                while tag:
                    dst_account = input('输入转账对象').strip()
                    if dst_account.isspace():
                        print('转账对象不能为空')
                    elif dst_account == current_user_info[0]:
                        print('不能给自己转账')
                        continue
                    for line in info():
                        if dst_account in line:
                            tag = False
                            break
                    else:
                        print('被转账账户不存在')
                src_account_money = float(current_user_info[2])
                while True:
                    transfer_money = input('输入转账金额').strip()
                    if transfer_money.isspace():
                        print('转账对象不能为空')
                    transfer_money = float(transfer_money)
                    if src_account_money < transfer_money:
                        print('余额不足')
                    else:
                        for line in user_info:
                            if dst_account in line:
                                dst_account_money = line[2]
                                wri(dst_account, float(dst_account_money) + transfer_money)
                                break
                        wri(src_account, src_account_money - transfer_money)
                        with open('%s_log.txt' % current_user_info[0], 'a', encoding='utf-8') as f:
                            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            f.write('时间%s,账户%s,转账%s\n' % (local_time, current_user_info[0], transfer_money))
                        with open('log.txt', 'a', encoding='utf-8') as f:
                            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            f.write('时间%s,账户%s,向账户%s，转账%s\n' % (local_time, src_account, dst_account, transfer_money))
                        print('时间%s,账户%s,向账户%s，转账%s,余额%s\n' % (
                            local_time, src_account, dst_account, transfer_money, src_account_money - transfer_money))
        if choice == '5':
            # 还款
            import time

            if len(current_user_info) == 0:
                print('请先登录')
            else:
                repayment = input('输入还款金额')
                current_user_info[2] = float(current_user_info[2])
                repayment = float(repayment)
                current_user_info[2] = current_user_info[2] + repayment
                with open('%s_log.txt' % current_user_info[0], 'a', encoding='utf-8') as f:
                    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    f.write(
                        '时间%s,账户%s,还款%s,余额%s\n' % (local_time, current_user_info[0], repayment, current_user_info[2]))
                with open('log.txt', 'a', encoding='utf-8') as f:
                    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    f.write(
                        '时间%s,账户%s,还款%s,余额%s\n' % (local_time, current_user_info[0], repayment, current_user_info[2]))
                wri(current_user_info[0], current_user_info[2])
                print('时间%s,账户%s,还款%s,余额%s\n' % (local_time, current_user_info[0], repayment, current_user_info[2]))
        if choice == '6':
            #     查看流水
            if len(current_user_info) == 0:
                print('请先登录')
            else:
                with open('%s_log.txt' % current_user_info[0], 'r', encoding='utf-8') as f:
                    print(f.read())
        if choice == '7':
            #     查看流水`
            if len(current_user_info) == 0:
                print('请先登录')
            else:
                with open('log.txt', 'r', encoding='utf-8') as f:
                    print(f.read())
        if choice == '8':
            #     查看流水`
            if len(current_user_info) == 0:
                print('请先登录')
            else:
                msg = '''
                1.添加账户
                2.用户额度
                3.冻结账户
                '''
                print(msg)
                choice = input('选择管理功能,退出q')
                if choice == '1':
                    add_account()
                elif choice == '2':
                    change_bal()
                elif choice == '3':
                    lock_account = input('需要锁定那个账户')
                    with open('lock.txt', 'a', encoding='utf-8') as f:
                        f.write('%s,' % lock_account)
                elif choice == 'q':
                    break
        if choice == '9':
            break
