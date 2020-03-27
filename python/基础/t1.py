# -*- coding: utf-8 -*-
# @Author: allen
# @Date:   2020-03-14 16:06:38
# @Last Modified by:   allen
# @Last Modified time: 2020-03-15 10:09:41
# @Email: 1009336683@qq.com

'''
#将func注册为要在解释器终止时执行的功能
print(1)
import atexit
def goodbye(name):
	print('Goodbye,%s ,it was happy to meet you!'%(name))

def hi():
	atexit.register(goodbye,'allen')
	print('hi func')

print(2)
#goodbye('allen')
#atexit.register(goodbye,'allen')
hi()
print(3)
'''

'''
import base64
f2 = open('./2','r')
f3 = open('./3','w+')
base64.encode(f2,f3)
f3 = open('./3','r')
f4 = open('./4','a+')
base64.decode(f3,f4) 
'''

'''
#二分算法简单应用
import bisect
#二分查找index   计算分数等级
def grade(score,breakpoints=[60, 70, 80, 90], grades='FDCBA'):
	i = bisect.bisect(breakpoints,score)
	return grades[i]
#print( [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]] )

#二分查找
def binary_search_bisect(lst, x):
	from bisect import bisect_left
	i = bisect_left(lst, x)
	if i != len(lst) and lst[i] == x:
		return i
	return None
#print(binary_search_bisect([1,5,7,9,11],5))
'''



