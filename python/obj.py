'''
from math import pi

class Circel(object):
	def  __init__(self,radius):
		self.radius = radius
	def getRadius(self):
		return self.radius

	def  setRadius(self,value):
		if not isinstance(value,(int, float) ): #python3 没有long
			raise ValueError('wrong type')
		self.radius = float(value)

	def getArea(self):
		return self.radius ** 2 * pi
	R = property(getRadius,setRadius)

c = Circel(2)
print(c.getArea())
#c.radius = 'asf'
#c.setRadius('asf')
c.R = 2 #可以达到setter 效果
print(c.getArea())
'''

'''
#减少类实例占内存大小
import sys
class stu1(object):
	"""docstring for stu1"""
	def __init__(self, name):
		super(stu1, self).__init__()
		self.name = name

class stu2(object):
	#用__slots__ 定义了类的属性后不能再动态修改类属性
	__slots__ = ['name']
	"""docstring for stu2"""
	def __init__(self, name):
		super(stu2, self).__init__()
		self.name = name
		
		

s1 = stu1('allen')
print(sys.getsizeof(s1))
s1.age = 18
print(s1.__dict__)
s2 = stu2('allen')
print(sys.getsizeof(s2))
#s2.age = 18 #  这是一个错误行为
'''


#类里比较大小 
'''
class Rectangle(object):
	def  __init__(self,w,h):
		self.w = w
		self.h = h
	def area(self):
		return self.w * self.h
	def __lt__(self,obj):
		return self.area() < obj.area()
	def __gt__(self,obj):
		return self.area() > obj.area()
r1 = Rectangle(2,3)
r2 = Rectangle(4,5)

print(r1 < r2) 
#这里实质是调用了 r1.__lt__(r2)方法，把r2当参数传进去，
#如需比较大，也要实现相应的方法
print(r1 > r2)
'''
#=============

'''
from functools import total_ordering
from math import pi
from abc import ABCMeta,abstractmethod

@total_ordering
class Shape(object,metaclass = ABCMeta):
	@abstractmethod
	def area(self,obj):
		pass
	def __lt__(self,obj):
		return self.area() < obj.area()
	def __eq__(self,obj):
		return self.area() == obj.area()
	def __gt__(self,obj):
		return self.area() > obj.area()
		

class Rectangle(Shape):
	def  __init__(self,w,h):
		self.w = w
		self.h = h
	def area(self):
		#print('Rectangle area count')
		return self.w * self.h

class Circle(Shape):
	def __init__(self,r):
		self.r = r
	def area(self):
		#print('Circle area count')
		return self.r ** 2 * pi

r1 = Rectangle(2,3)
r2 = Rectangle(4,5)
#print(r1 < r2)
#print(r1 == r2)
c1 = Circle(3)
print(r1 < c1 )
print(c1 >= r2 )
'''


#metaclass test
#function 
'''
def upper_attr(future_class_name,future_class_parents,future_class_attr):
	uppercase_attr = {}
	for name,val in future_class_attr.items():
		if not name.startswith('__'):
			uppercase_attr[name.upper()] = val
		else:
			uppercase_attr[name] = val
	return type(future_class_name,future_class_parents,uppercase_attr)


class Foo(object,metaclass=upper_attr):
	__name__ = 'GG'
	bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))
print(hasattr(Foo,'__name__'))
'''

'''
class UpperAttrMetaclass(type): 
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

class Foo(object,metaclass=UpperAttrMetaclass):
	__name__ = 'GG'
	bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))
print(hasattr(Foo,'__name__'))
print(Foo.__class__)
print(Foo.__class__.__class__)
'''


#多线程
#python 多线程有一个GIL（全局解析器锁），他不适合用做cpu密集型多线程，可以做IO密集型多线程
#实现两种方法
#1.直接使用Thread(target = handle,args=(x,))
#2.继承Thread类，实现run方法，把自己的方法放到run里实现
from threading import Thread
from time import sleep

#这是cpu密集型操作，所以效果有点差
def handle(name):
	sleep(1)
	print('hello ',name,"\n")

'''
threads = []
for x in range(1,10):
	t = Thread(target = handle,args=(x,))
	threads.append(t)
	t.start()
for t in threads:
	t.join()
'''

class MyThread(Thread):
	def  __init__(self, arg):
		super(MyThread,self).__init__()
		#Thread.__init__(self)
		self.arg = arg
	def  run(self):
		handle(self.arg)
threads = []
for x in range(1,10):
	t = MyThread(x)
	threads.append(t)
	t.start()
for t in threads:
	t.join()







