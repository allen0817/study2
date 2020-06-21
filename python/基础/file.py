#!/usr/bin/env python3
#!coding=utf-8

import os





############# csv start  ##################
import csv
baseDir = os.path.dirname(os.path.abspath(__name__))

filePath = baseDir + '/1.csv'

if os.path.isfile(filePath):
    with open(filePath,'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=':', quotechar='|')
        for row in spamreader:
            #print(', '.join(row))
            print(row)

    with open(filePath,'r') as csvfile:
        f = csv.DictReader(csvfile,delimiter=':',fieldnames=['no','name','age','hobby','other'])
        for x in f:
            print(x)


#如果数据里包含分隔符，会用quotechar 把所在字段隔起来 如  |字符；字符|
filePath =  baseDir + '/2.csv'
with open(filePath,'a+') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely; Spam', 'Wonderful Spam','abc'])


print(csv.list_dialects())
print(csv.field_size_limit())
############# csv end  ##################
'''

############# json start  ##################
import json

#字符串转python对象
s = '[1,3,"abc",{"name":"allen","age":17}]'
j = json.loads(s)
print(j)
print(type(j))

#python 转json字符串  
l = [1,3,'abc',{'name':'allen','age':17}]
j = json.dumps(l,separators=[',',':']) #默认分隔符
print(j)
print(type(j))

#读取文件操作用dump,load

############# json end  #################












