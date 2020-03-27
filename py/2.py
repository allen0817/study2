#!/usr/bin/python
#coding:utf8




#nametempro

"""
f = open('./tmp.txt','w')
for x in  xrange(1,601):
	x = str(x) + '\n'
	f.write(x)

f.close()
"""
f = open('./tmp.txt','r')
from tempfile import NamedTemporaryFile
lines =  f.readlines()
l = len(lines) -1
i = 3
for k,x in enumerate(lines):
	if k%i == 1 or k==0:
		f_2 = NamedTemporaryFile(delete=False)
	
	f_2.write(str(x))
	if k%i == 0 or k==l:
		f_2.close()
		print f_2.name
		#sender
		#delete





"""
	if i == 0:
		f_2 = NamedTemporaryFile(delete=False)
	if (i%3 == 0  and k>0 ) or k == l:
		f_2.write(str(x))
		print f_2.name
		print i,k,l
		i = 0		
		f_2.close()
	elif i % 3 != 0:
		i = i +1
		f_2.write(str(x))
	
"""
 

 
# delete默认删除，为True则关闭临时文件时候不删除，








"""
while f:
	for lines in f.readlines(250):
	    if not lines:
        	break
    #for line in lines:
        #pass # do something
    	g.write(lines.strip())
    	print '=' * 50
    	print "\n"
"""

f.close()
