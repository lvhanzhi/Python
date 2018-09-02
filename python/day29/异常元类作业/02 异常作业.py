# Integer类
# 功能: 从键盘上接收数据,最终给用户(使用者)反馈一个合法的数字(int类型32位)
# 方法: input方法  verifySlopOver方法
# input方法 分析
#   -- 参数列表 可有可无(有就是用户输入的提示)
#   -- 返回值 int类型合法数字
#   -- 方法的类型 类方法
# verifySlopOver方法 分析
#   -- 参数列表 int类型数字
#   -- 返回值 None
#   -- 方法的类型 静态方法
class Integer:
    @classmethod
    def input(cls, msg):
        # print(msg, end="")
        try:
            num = int(input(msg))
        except ValueError as e:
            print(e)
            num = cls.input(msg)
        try:
            cls.verifySlopOver(num)
        except SlopOverError as e:
            print(e)
            num = cls.input(msg)
        return num

    @staticmethod
    def verifySlopOver(num):
        max_num = 2147483647
        min_mun = -2147483648
        if not (max_num >= num >= min_mun):
            raise SlopOverError(num, "越界")

class SlopOverError(BaseException):
    def __init__(self, num, msg):
        super().__init__()
        self.num = num
        self.msg = msg

    def __str__(self):
        return "ErrorMsg：%d - %s" % (self.num, self.msg)

num = Integer.input("请输入一个数字: ")
print(num)











