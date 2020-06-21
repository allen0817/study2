#coding:utf8
import time


#装饰器函数
def memo(func):
	cache = {}
	def run(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return run


@memo
def fibonacci(n):
	if n <= 1:
		return 1
	return fibonacci(n -1) + fibonacci(n -2)

#print(fibonacci(50))

from random import randint
from functools import wraps


def find(num):
	if not isinstance(num,int):
		raise 'type error'
	for x in range(1,num):
		print(x)


def logBug(func):
	@wraps(func) #保持原来函数的属性
	def run(*args):
		print('methon: {methon} is run at {time}'.format(methon=func.__name__,time= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())   ))
		func(*args)
	return run

@logBug
def a(a,b):
	print('this is a fun')
	print("%s\t%s"%(a,b))

@logBug
def b():
	print('this is b fun')

a("hello ","allen")
b()
print(b.__name__)





