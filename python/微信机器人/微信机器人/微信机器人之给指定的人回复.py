import json
import requests
from wxpy import *
bot = Bot(cache_path=True)

girl_friend=bot.search('刘sir')[0]

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "9d602fe417464cd18beb2083d064bee6"
    payload = {
        "key": api_key,
        "info": text,
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[微信测试，请忽略] " + result["text"]


@bot.register()
def forward_message(msg):
    if msg.sender == girl_friend:
        return auto_reply(msg.text)

embed()