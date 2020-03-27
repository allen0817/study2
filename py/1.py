#!/usr/bin/python


from tempfile import NamedTemporaryFile
from time import sleep,time

f_2 = NamedTemporaryFile()
print(f_2.name)
f_2.close()



sleep(1)




'''
d = {'x': 'A', 'y': 'B', 'z': 'C' }
n = [k + '=' + v for k, v in d.items()]
print n


c = [x * x for x in range(10)]
print c

l = ["name","age","hobby"]

l1 = [ x.upper() for x in l]
print l1


23:59	No R interpreter defined: Many R related features like completion, code checking and help won't be available. You can set an interpreter under Preferences->Languages->R


def fib(m):
	n,a,b = 0,0,1
	while n < m:
		yield b
		print b 
		a,b = b,a+b
		n = n + 1
	#return 'done'

fib(12)

s = sum([1,1,2])
print s


from operator import itemgetter

t = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# sort by name 
print(sorted(t, key=itemgetter(0)))
# sort by score
print(sorted(t, key=lambda t: t[1]))
#sort by score desc
print(sorted(t, key=itemgetter(1), reverse=True))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)

print f()

a = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print reduce(lambda x,y:x + y, a )

lam = lambda x,y : x+y

print lam(2,9)

def build(x, y):
    return lambda: x * x + y * y

b = build(3,2)
print b()

'''



print('allen')






