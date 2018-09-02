today=input("今天星期几？")
if today in ["星期一","星期二","星期三","星期四","星期五"]:
    print("今天上班")
elif today in ["星期六","星期天"]:
    print("今天休息")
else :
    print('''
    必须输入其中一种:
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
    ''')