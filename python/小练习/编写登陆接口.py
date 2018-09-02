dic={
    'egon1':{
        'password':'1',
        'count':0
    },
    'egon2':{
        'password':'2',
        'count':0
    },
    'egon3':{
        'password':'3',
        'count':0
    }
}
while True:
    name = input("请输入用户名：")
    if not name in dic:
        print("请输入注册过的用户名！！！")
    else:
        if dic[name]['count']>2:
            print("您的机会已用完")
            break
        else:
            password=input("请输入密码：")
            if password==dic[name]['password']:
                print("欢迎登陆！！！")
                break
            else:
                dic[name]['count']+=1
                print("密码错误")
                print(dic[name]['count'])
