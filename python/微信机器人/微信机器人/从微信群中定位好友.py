
from wxpy import *
bot=Bot(cache_path=False)

company_group=bot.groups().search('玩转Python')[0]

boss=company_group.search('kevin')[0]

@bot.register(chats=company_group) #接收从指定群发来的消息，发送者即recv_msg.sender为组
def recv_send_msg(recv_msg):
    print('收到的消息：',recv_msg.text)
    if recv_msg.member == boss:
        recv_msg.forward(bot.file_helper,prefix='老板发言: ')
        return '老板说的好有道理，深受启发'

embed()