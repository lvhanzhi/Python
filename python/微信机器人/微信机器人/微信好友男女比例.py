from wxpy import *
from pyecharts import Pie

bot=Bot(cache_path=True) #注意手机确认登录

friends=bot.friends()

attr=['男朋友','女朋友']
value=[0,0]
for friend in friends:
    if friend.sex == 1: # 等于1代表男性
        value[0]+=1
    elif friend.sex == 2: #等于2代表女性
        value[1]+=1

pie = Pie("朋友男女比例")
pie.add("", attr, value, is_label_show=True)
pie.render('sex.html')
import webbrowser
webbrowser.open("sex.html")