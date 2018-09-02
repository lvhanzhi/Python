import configparser
config=configparser.ConfigParser()#得到一个对象
config.read('test.ini')#可以读a.cfg a.ini a.cnf
print(config.sections())#获取所有分区
print(config.options('egon'))#获取所有选项
res=config.options('egon')#取某一个标题下面的所有配置项(取kye值)
age=config.get('egon','age')
print(type(age))#从文件里面取出来都是字符串类型
age=config.getint('egon','age')#getfloat getboolean
print(type(age))
print(config.items('egon'))#取key和value都取出来
config.add_section('wupeiqi')
config.set('wupeiqi','age','18')
print(config.sections())