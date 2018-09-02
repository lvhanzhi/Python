import logging
#方式一:只能存到文件里,不能输出到终端
logging.basicConfig(filename='access.log',
                    format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10
                    )
logging.debug('debug日志')#10
logging.info('info日志')#20
logging.warning('warning日志')#30
logging.error('error日志')#40
logging.critical('critical日志')#50

import logging
#1.logger对象:生产日志
logger1=logging.getLogger('用户交易')
#2.filter对象:过滤(不考虑)
#3.handler对象:控制日志输出目标位置(终端还是文件)
fh1=logging.FileHandler('a1.log',encoding='utf8')#放到a1.log文件里
fh2=logging.FileHandler('a2.log',encoding='utf8')#放到a2.log文件里
ch=logging.StreamHandler()#输出到终端上
#4.formmate对象:控制日志格式
formatter1=logging.Formatter(
    fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p'
)
formatter2 = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s :  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p'
)
# 5.绑定logger对象与handler对象
logger1.addHandler(fh1)
logger1.addHandler(fh2)
logger1.addHandler(ch)
# 6.绑定handler对象与formatter对象
fh1.setFormatter(formatter1)
fh2.setFormatter(formatter1)
ch.setFormatter(formatter2)
# 7. 设置日志级别,有logger对象与handler对象两层关卡,必须都放行最终日志才会放行,通常二者级别相同
logger1.setLevel(10)
fh1.setLevel(10)
fh2.setLevel(10)
ch.setLevel(10)
#8. 使用logger对象产生日志
logger1.info('alex给egon转账1个亿')