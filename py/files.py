#!/usr/bin/env python3
# coding=utf8


'''
#csv 简单使用
import csv 
f = open('./test.csv')
c = csv.reader(f)
print(c.__next__())

print('*'*20)

for x in c:
	print(x[1],x)
'''

'''
#json 
import json

s = '{"name":"allen","age":18,"hobby":"study"}'
#str to json(dict)
obj = json.loads(s)
print(obj)
print(type(obj))
#json to str 
s1 = json.dumps(obj,sort_keys=True)
print(s1)
print(type(s1))
'''

#xml

'''
from xml.etree.ElementTree import parse
f = open('./1.xml')
e = parse(f)

#print(e.getroot())
root = e.getroot()

'''

'''
for  x in root:
	print(x.get('a_name'))
'''
#print('*'*50)

#print('root-tag:',root.tag,',root-attrib:',root.attrib,',root-text:',root.text)

'''
for x in root.iterfind('class'):
	#print(x.get('a_name'))
	for i in x:
		for j in i:
			print('tag:',j.tag,'attrib:',j.attrib,'text:',j.text)
	print('*'*50)
	print(x[0][0].text)
	print('*'*50)


	for l in x:
		print( 'name:',l[0].text,'age:',l[1].text,'sex:',l[2].text )
'''

'''
stu = root.findall('class/*')
print(len(stu))
for l in stu:
	print( 'name:',l[0].text,'age:',l[1].text,'sex:',l[2].text )
'''

# .// 任意节点
'''
names = root.findall('.//name')
for x in names:
	print(x.text)
'''

#包含属性
'''
c = root.findall('class[@a_name]')
print(c)
c = root.findall('.//name[@n]')
print(c)
c = root.findall('.//name[@n="b"]')
print(c[0].text)
'''

# 有@是属性，没有@是元素(标签)
#包含子元素
'''
stu = root.findall('class[gg]')
print(stu)

# 通个包含有gg子元素查找他的上一级
stu =  root.findall('.//gg/..')
for x in stu:
	for l in x:
		if l.tag == 'student':
			print( 'name:',l[0].text,'age:',l[1].text,'sex:',l[2].text )
'''

# 查找子元素值等于某一值的元素
'''
stu = root.find('class/student[name="张三"]')
print(stu[0].text,stu[1].text,stu[2].text)
'''


'''
#按位置 , 如果不是从根节点开始，会匹配多个节点下的机同位置。像这个例子，匹配两个节点下的第三个 student 位置
stu = root.findall('class/student[3]')
print(len(stu))
print(stu[0][0].text,stu[0][1].text,stu[0][2].text)
print(stu[1][0].text,stu[1][1].text,stu[1][2].text)

print('*'*50)
#倒数第二个 倒数第一个 last()
stu = root.findall('class/student[last() -1 ]')
print(stu[0][0].text,stu[0][1].text,stu[0][2].text)
print(stu[1][0].text,stu[1][1].text,stu[1][2].text)
'''

'''
n = root.findtext('class/student/name')
print(n)
'''
'''
stu = root.findall('class/student')
for x in stu:
	print(x.findtext('./name'),"\t",x.findtext('./age'),"\t",x.findtext('./sex')  )
'''



'''
# csv to xml
import csv
from  xml.etree.ElementTree import ElementTree,Element

#美化xml格式 
def pretty(e,level=0):
	if(len(e)) > 0:
		e.text = '\n' + '\t' *(level + 1)
		for child in e:
			pretty(child,level+1)
		child.tail = child.tail[:-1]
	e.tail = '\n' + '\t' * level

def csvToXml(name):
	with open(name)  as f:
		c = csv.reader(f)
		headers = c.__next__()
		root =  Element('data')
		for row in c:
			erow = Element('student')
			root.append(erow)
			for tag,text in zip(headers,row):
				e = Element(tag)
				e.text = text
				erow.append(e)
	pretty(root)
	return ElementTree(root)

et = csvToXml('./test.csv')
et.write('./test.xml')
'''

#读写excel

import xlrd,xlwt

book = xlrd.open_workbook('stu.xlsx')
#print(book.sheets())
sheet = book.sheet_by_index(0) #表对象 
print(sheet.nrows) #行数
print(sheet.ncols) #列数
print(sheet.cell(0,0).value) #访问单元格
print(sheet.row(1)  )
print(sheet.row_values(1,1)  )
print(sheet.col(1)  )

print('*'*20,'写','*'*20)


nc = sheet.ncols  #列数
sheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,u'总分',None) #第一行最后一列写入总分

for row in range(1,sheet.nrows):	#循环每一行
	t = sum(sheet.row_values(row,1))  #从第二列开始，每列相加
	sheet.put_cell(row,nc,xlrd.XL_CELL_NUMBER,t,None) #最后一列写入总分

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(sheet.name) # 表名
style = xlwt.easyxf('align: vertical center, horizontal center')

for r in range(sheet.nrows):
	for c in range(sheet.ncols):
		wsheet.write(r,c,sheet.cell_value(r,c),style)



wbook.save('./new.xlsx')









