#!coding=utf-8
# 检查一个函数的输入参数个数,
# 如果调用此函数时提供的参数个数不符合预定义，则无法调用。

# 实例对象版本装饰器
class Checker:
    def __init__(self, require_num):
        self.require_num = require_num

    
    def __call__(self, func):
        self.func = func

        def inner(*args, **kw):
            if len(args) != self.require_num:
                print('函数参数个数不符合预定义，无法执行函数')
                return None

            return self.func(*args, **kw)
        return inner

'''
@Checker(2)
def show(*args):
    print('show函数成功执行!')

show(1)  # 函数参数个数不符合预定义，无法执行函数
show(1,2) # show函数成功执行!
show(1,2,3)  # 函数参数个数不符合预定义，无法执行函数
'''

