import logging.config
# import test
logging.config.dictConfig(LOGGING_DIC)
logger1=logging.getLogger('用户交易')
logger1.info('alex给egon转账1个亿')

logger2=logging.getLogger('用户权限')
logger2.error('egon没有执行权限')