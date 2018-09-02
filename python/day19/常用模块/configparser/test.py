import configparser
config=configparser.ConfigParser()#得到一个对象
config.read('config.ini')#可以读a.cfg a.ini a.cnf
res=config.options('egon')#取某一个标题下面的所有配置项(取kye值)
age=config.get('egon','age')
print(type(age))#从文件里面取出来都是字符串类型
age=config.getint('egon','age')#getfloat getboolean
print(type(age))
print(config.items('egon'))#取key和value都取出来