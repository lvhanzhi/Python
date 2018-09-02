import re
while True:
    phone_number = input('请输入手机号:').strip()
    if re.match('^(13|16|19|15)[0-9]{9}$', phone_number):
        print('该号码合法')
    else:
        print('该号码不合法')