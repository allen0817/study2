#!coding=utf-8
'''
metaclass 的理解
类的创建这程
类最终使用type()函数来实例类
type(name of the class, 
    tuple of the parent class (for inheritance, can be empty), 
    dictionary containing attributes names and values)

metaclass 是 type 一个实例（应该可以这样理解）

metaclass 可以改变类

然后返回类
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