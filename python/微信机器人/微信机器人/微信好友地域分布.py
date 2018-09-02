from wxpy import *
from pyecharts import Map

bot=Bot(cache_path=False)

friends=bot.friends()


area_dic={}
for friend in friends:
    if friend.province not in area_dic:
        area_dic[friend.province]=1
    else:
        area_dic[friend.province]+=1

attr = area_dic.keys()
value = area_dic.values()



map = Map("好朋友们的地域分布", width=1200, height=600)
map.add(
    "好友地域分布",
    attr,
    value,
    maptype='china',
    is_visualmap=True, #结合体VisualMap
    visual_text_color='#000'
)
map.render('area.html')

import webbrowser
webbrowser.open("area.html")