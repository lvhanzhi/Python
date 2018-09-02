with open('db.txt','r',encoding='utf8')as f:
    message=f.read()
    end=int(f.tell())
    start=int(message.index('\n')+1)
    text=message[start:end]
    print(text)