while True:
    tell_number=input('请输入手机号:').strip()
    if tell_number.isdigit() and len(tell_number)==11 and (tell_number.startswith('13')\
            or tell_number.startswith('15')\
            or tell_number.startswith('17')\
            or tell_number.startswith('14')\
            or tell_number.startswith('18')\
            ):
        print('这是合法的手机号')
    else:
        print('这不是合法的手机号')



