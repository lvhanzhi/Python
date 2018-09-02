# 1.书写验证身份证、手机号码、网易邮箱的正则表达式
import re
# print(len('33032119970125445x'))
src='33032119970125445x'
print(re.findall('^[0-6]\d{5}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])(?:\d{4}|\d{3}x)',src))
# 如果要做手机号的验证，那么我们需要知道手机号码的号段。
# //移动号码归属地支持号段:134 135 136 137 138 139 147 150 151 152 157 158 159 178  182 183 184 187 188
# //联通号码归属地支持号段:130 131 132  145 155 156 176  186
# //电信号码归属地支持号段:133 153 177 180 181 189
# //移动运营商:170
print(re.findall('^(?:134|135|136|137|138|139|147|150|151|152|157|158|159|178|182|183|184|187|188|130|131|132|145|155|156|176|186|133|153|177|180|181|189)\d{8}$','18667383023'))
#网易邮箱:6~18个字符，可使用字母、数字、下划线，需以字母开头@163.com/126.com/yeah.net
print(re.findall('^[a-zA-Z]\w{7,17}@163.com|126.com|yeah.net','a1234565589987@163.com'))

# 2.遍历book.xml文件，通过正则匹配，将所有书名存放到book.txt文件中
import xml.etree.ElementTree as et
tree=et.parse('book.xml')
root=tree.getroot()
str1=''
for country in root:
    str1+=country.text
with open('book.txt','w',encoding='utf8')as f:
    f.write(str1)
# 3.现有一个text目录下有a.txt,b.txt,c.py三个文件，利用subprocess模块，将三个文件的文件名存放到tag.txt文件中
# 	思考：执行文件在text目录下与不在text目录下两种情况
import subprocess
obj=subprocess.Popen(
    r'dir C:\Users\2\Desktop\python\day20\0814作业\0814作业\text >C:\Users\2\Desktop\python\day20\0814作业\0814作业\text\tag.txt',
    shell=True,#
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
stdout_res=obj.stdout.read()
stderr_res=obj.stderr.read()
print(stdout_res.decode('gbk'))
print(stderr_res.decode('gbk'))