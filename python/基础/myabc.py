from abc import ABCMeta,abstractmethod
'''
class MyABC(metaclass=ABCMeta):
    pass
MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
print(issubclass(tuple, MyABC))
'''

class Foo:
    def __getitem__(self, index):
        pass
    def __len__(self):
        pass
    def get_iterator(self):
        return iter(self)

class MyIterable(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass


    @abstractmethod
    def __iter__(self):
        while False:
            yield None
    def get_iterator(self):
        return self.__iter__()

    '''
    @abstractmethod
    def _get_x(self):
        pass
    @abstractmethod
    def _set_x(self, val):
        pass
    x = property(_get_x, _set_x)
    '''


    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

class T(MyIterable):
    def say(self):
        print('gg')
    def __iter__(self):
        pass
    #@property
    #def getx(self):
    #    return self._x
    #@property
    #def setx(self,val):
    #    self._x = val
    #s = property(getx,setx)


    



#MyIterable.register(Foo)
t = T()
t.say()
t.x = 'allen'
print(t.x)





