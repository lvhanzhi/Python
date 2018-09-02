import os
menu=[
    ['白菜',100],
    ['红豆',200],
    ['土豆',500],
    ['芝麻',2]
]
shopping_car={}
def modification(name,pwd,balance):
    for user_info in user():
        if name==user_info[0]:
            old_pwd=user_info[1]
            old_balance=user_info[2]
    if pwd==None:pwd=old_pwd
    if balance==None:balance=old_balance
    with open(r'db.txt', 'r', encoding='utf8')as read_f, \
        open(r'db.txt.swap', 'w', encoding='utf8')as write_f:
            for line in read_f:
                info=line.strip('\n').split(',')
                if name==info[0]:
                    info[1]=pwd
                    info[2]=str(balance)
                line=','.join(info)+'\n'
                write_f.write(line)
    os.remove(r'db.txt')
    os.rename(r'db.txt.swap',r'db.txt')



def write_user(name,pwd,balance):
    with open(r'db.txt', 'a', encoding='utf8')as f:
        f.write('%s,%s,%s\n'%(name,pwd,balance))
def user():
    user_info=[]
    with open(r'db.txt','r',encoding='utf8')as f:
        for line in f:
            info=line.strip('\n').split(',')
            user_info.append(info)
    return user_info
def register():
    while True:
        name=input('请输入用户名:').strip()
        for user_info in user():
            if name == user_info[0]:
                print('该用户名已被占用')
                break
        else:
            break
    while True:
        pwd1=input('请输入密码:').strip()
        pwd2=input('请再次输入密码:').strip()
        if pwd1==pwd2:
            balance=int(input('请输入充值金额:').strip())
            break
        else:
            print('两次密码不一致')
    write_user(name,pwd2,balance)
def login():
    count=0
    while True:
        if count >= 3:
            print('登录次数过多,退出')
            break
        name=input('请输入用户名:').strip()
        pwd=input('请输入密码:').strip()
        for user_info in user():
            if user_info[0]==name and pwd==user_info[1]:
                current_user.append(name)
                current_user.append(user_info[-1])
                print('登录成功')
                return
        else:
            print("用户名或密码错误,请重新输入")
            count+=1


def change_pwd():
    if len(current_user)==0:
        print('请先登录')
    else:
        new_pwd = input('请输入新的密码:').strip()
        modification(current_user[0], new_pwd, None)
        print('修改成功')

def shop():
    shopping_car = {}
    if len(current_user)==0:
        print('请先登录')
    else:
        balance=float(current_user[1])
        name=current_user[0]
        print('%s余额为%s'%(name,balance))
        tag=True
        while tag:
            print('菜单'.center(20, '-'))
            for index,product in enumerate(menu):
                print(index,product[0],product[1])
            choice=input('请选择,或q退出:').strip()
            if choice.isdigit():
                choice=int(choice)
                if choice>=0 and choice<len(menu):
                    pprice=menu[choice][1]
                    pname = menu[choice][0]
                    if pprice<=balance:
                        if pname in shopping_car:
                            shopping_car[pname]['count']+=1
                        else:
                            shopping_car[pname]={'pprice':pprice,'count':1}
                        balance -= pprice
                        current_user[-1] = balance
                        print('%s价格%s已加入购物车,余额%s'%(pname,pprice,balance))
                    else:
                        print('余额不足')
                else:
                    print('非法输入')
            elif choice=='q':
                if not shopping_car:
                    tag=False
                    break
                else:
                    zprice=0
                    while True:
                        for index,product in enumerate(shopping_car):
                            print('%s %s %s %s %s '%(
                                index,
                                product,
                                shopping_car[product]['pprice'],
                                shopping_car[product]['count'],
                                float(shopping_car[product]['pprice'])*shopping_car[product]['count']
                            ))
                            zprice+=float(shopping_car[product]['pprice'])*shopping_car[product]['count']
                        print('总价为%s'%zprice)
                        choice = input('是否确认购买(y/n):').strip()
                        if choice in ['y','n']:
                            if choice=='y':
                                modification(current_user[0],None,current_user[-1])
                                print('购买成功,您的账户余额为%s'%current_user[-1])
                            shopping_car={}
                            tag=False
                            break
                        else:
                            print('非法输入')
            else:
                print('非法输入')


dic={
    '1':register,
    '2':login,
    '3':change_pwd,
    '4':shop
}
current_user=[]
user_info=user()
while True:
    print("""
    1 注册
    2 登录
    3 修改密码
    4 购物
    5 退出
    """)
    choice=input('>>').strip()
    if choice in dic:
        dic[choice]()
    elif choice=='5':
        current_user=[]
        break
    else:
        print('非法输入')