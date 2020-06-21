#!/usr/bin/env python3
# coding = utf-8



class IntTuple(tuple):
	
	def __new__(cls,iterable):
		g = (x for x in iterable if isintance(x,int) and x > 0 )
		print(type(iterable))
		print(type(g))

		c = super(IntTuple,cls).__new__(cls)
		return c
		#return super(IntTuple,cls).__new__(cls,g)
	

	"""docstring for IntTuple"""
	def __init__(self, iterable):
		super(IntTuple, self).__init__()
		self.iterable = iterable



t =  IntTuple([-1,1,'abc',['x','y'],6,2])

print(t)
		