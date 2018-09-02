import settings
class Mysql:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
obj=Mysql(settings.IP,settings.PORT)