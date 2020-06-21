#!coding=utf-8
'''
#9x9S
for i in range(1,10):
    for j in range(1,10):
        if j <=i:
            print('%d * %d = %d \t'%(j,i,i*j),end='')
    print()
'''

'''
#9x9 生成器形式
def mul9x9():
    i = 1
    while i<10:
        t = ''
        j = 1
        while j < 10 and j <=i:
            t = t +  '%d * %d = %d \t'%(j,i,i*j)
            j = j + 1
        yield t
        i = i +1
    return 'done'
a = mul9x9()
print(type(a))
for x in a:
    print(x)
'''