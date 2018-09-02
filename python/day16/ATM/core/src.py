
from lib import common

def register():
    print('\033[45m注册\033[0m')

def login():
    print('\033[44m登录\033[0m')

def shopping():
    print('\033[43m购物\033[0m')

def pay():
    print('\033[42m支付\033[0m')

def transfer():
    print('\033[41m转账\033[0m')
    common.logger('alex给egon转了1个亿')


func_dic={
    '1':register,
    '2':login,
    '3':shopping,
    '4':pay,
    '5':transfer
}

def run():
    while True:
        print("""
        0 退出
        1 注册
        2 登录
        3 购物
        4 支付
        5 转账
        """)
        choice=input('请输入您的操作: ').strip()
        if choice == '0':break
        if choice not in func_dic:
            print('输入错误指令')
            continue
        func_dic[choice]()

