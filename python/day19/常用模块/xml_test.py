#查
import xml.etree.ElementTree as et
#得到节点树
tree=et.parse('test.xml')
#获取根标签
root=tree.getroot()
#获取所有的country(查找标签find/findall)
print(root.find('country'))
#获取year
print(root.iter('year'))#在全文中查找,返回迭代器(找的是标签)

#遍历整个xml 标签名 属性 文本
for country in root:
    print(country.tag,country.attrib,country.text)
    for t in country:
        print(t.tag, t.attrib, t.text)

print(root.find('country').get('name'))#得到country中name的属性内容

#改
import xml.etree.ElementTree as et
#读到内存
tree=et.parse('test.xml')
for country in tree.findall('country'):
    yeartag=country.find('year')
    yeartag.text=str(int(yeartag.text)+1)
#写到硬盘中(xml_declaration=False)文档声明
tree.write("test.xml",encoding='utf8',xml_declaration=False)


#删
import xml.etree.ElementTree as et
#读到内存
tree=et.parse('test.xml')
for country in tree.findall('country'):
    country.remove(country.find('year'))
tree.write("test.xml",encoding='utf8',xml_declaration=False)

#添加子标签
import xml.etree.ElementTree as et
#读到内存
tree=et.parse('test.xml')
for country in tree.findall('country'):
    #一个新标签
    newtag=et.Element('newTag')#添加标签
    newtag.text='123'#文本
    newtag.attrib['name']='DSB'
    #添加到country便签里面
    country.append(newtag)

tree.write("test.xml",encoding='utf8',xml_declaration=False)


#用代码生成xml
import xml.etree.ElementTree as et
#创建根标签
root=et.Element('root')
#创建节点树
t1=et.ElementTree(root)
#创建一个peron标签
person=et.Element('person')
person.attrib['name']="yyh"
person.attrib['sex']="man"#注意:只能写字符串
person.text="这是一个person标签"
root.append(person)
#写入文件
t1.write('newXML.xml',encoding='utf8',xml_declaration=True)