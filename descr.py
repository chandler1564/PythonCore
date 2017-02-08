#coding:utf-8

import os
import pickle

class FileDescr(object):
    saved=[]
    def __init__ (self,name=None):
        self.name=name

    def __get__ (self,obj,type=None):
        if self.name not in FileDescr.saved:
            raise AttributeError, '%r used before assignment' % self.name
        try:
            f=open(self.name,'r')
            val=pickle.load(f)
            f.close()
            return val
        except(pickle.UnpicklingError,IOError,EOFError,AttributeError,ImportError,IndexError),e:
            raise AttributeError, 'could not read %r: %s' % self.name

    def __set__ (self,obj,val):
        f=open(self.name, 'w')
        try:
                pickle.dump(val,f)
                FileDescr.saved.append(self.name)
        except (TypeError,pickle.PicklingError),e:
            raise AttributeError,'could not pickle %r' % self.name
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError), e:
            pass

class MyFileVarClass(object):
    foo=FileDescr('foo')
    bar = FileDescr('bar')

# fvc=MyFileVarClass()
# # print fvc.foo
# fvc.foo=42
# fvc.bar='leanna'
# print fvc.foo,fvc.bar
#
# del fvc.foo,fvc.bar
# print fvc.foo,fvc.bar
# fvc.foo=__builtins__

class ProtectAndHideX(object):
    def __init__ (self,x):
        assert isinstance(x,int),'"x" must be an integer!'
        self.__x=~x

    def get_x(self):
        return ~self.__x

    x=property(get_x)

# inst=ProtectAndHideX('foo')
# inst=ProtectAndHideX(10)
# print 'inst.x=',inst.x
# inst.x=20

class HideX(object):
    def __init__(self,x):
        self.x=x
    def get_x(self):
        return ~self.__x
    def set_x(self,x):
        assert isinstance(x,int),'"x" must be an integer!'
        self.__x=~x
    x=property(get_x,set_x)
# inst=HideX(20)
# print inst.x
# inst.x='30'
# print inst.x
from math import pi
def get_pi(dummy):
    return pi
class PI(object):
    pi=property(get_pi,doc='Constant "pi"')

# inst=PI()
# # print inst.pi
# print '---',inst.pi. __doc__ ,'---'

# from time import ctime
#
# print '*** Welcome to Metaclasses!'
# print '\tMeteclass declaration first.'
#
# class MetaC(type):
#     def __init__(cls, name, bases, attrd):
#         super(MetaC,cls).__init__(name, bases, attrd)
#         print '*** Created class %r at: %s' % (name,ctime())
# print '\tClass "Foo" declaration next.'
#
# class Foo(object):
#     __metaclass__ = MetaC
#     def __init__(self):
#         print '*** Instantiated class %r at: %s' % (self.__class__.__name__, ctime())
#
# print '\tClass "Foo" instantiation next.'
# f=Foo()
# print '\tDONE'

def foo(data):
    if isinstance(data,int):
        print 'you entered an integer'
    elif isinstance(data,str):
        print 'you entered a string'
    else:
        raise TypeError, 'only integers or strings!'

# foo(['a','b'])
# foo(1)
from operator import *
vec1=[12,24]
vec2=[2,3,4]
opvec=(add,sub,mul,div)
for eachOp in opvec:
    for i in vec1:
        for j in vec2:
            print '%s(%d,%d) = %d' % (eachOp.__name__,i,j,eachOp(i,j))






