#coding:utf-8
'''
在我们的描绘中，类最终解释了面向对象编程（OOP，object-oriented programming）思想。
本章中，我们首先将给出一个总体上的概述，涵盖了Python中使用类和OOP的主要方面。其余部分
针对类，类实例和方法进行详细探讨。我们还将描述Python中有关派生或子类及继承机理。
最后，Python可以在特定功能方面定制类，例如重载操作符，模拟Python类型等。我们将
展示如何实现这些特殊的方法来自定义你的类，以让它们表现得更像Python的內建类型。
'''
import time
from math import fabs
class Devnull1(object):
    def __get__ (self, obj,type=None):
        pass
    def __set__ (self, obj, val):
        pass

class C1(object):
    foo = Devnull1()

# c1=C1()
# c1.foo='bar'
# print 'c1.foo contains:',c1.foo

class DevNull2(object):
    def __get__ (self, obj, type=None):
        print 'Accessing attribute... ignoring'
    def __set__ (self, obj, val):
        print 'Attempt to assign %r ... ignoring' % (val)

class C2(object):
    foo=DevNull2()

# c2=C2()
# c2.foo='bar'
# x=c2.foo
# print 'c2.foo contains:',x

class DevNull3(object):
    def __init__ (self,name=None):
        self.name=name
    def __get__ (self, obj, type=None):
        print 'Accessing [%s] ... ignoring' % (self.name)
    def __set__ (self,obj,val):
        print 'Assigning %r to [%s] ... ignoring' % (val,self.name)

class C3(object):
    foo=DevNull3('foo')

# c3=C3()
# c3.foo='bar'
# x=c3.foo
# print 'c3.foo contains:',x
# print 'Let us try to sneak it into c3 instance...'
# c3.__dict__ ['foo']='bar'
# x=c3.foo
# print 'c3.foo contains:', x
# print 'c3.__dict__ [foo] contains: %r' % (c3.__dict__ ['foo']) , '...why?!?'
class FooFoo(object):
    def foo(self):
        print 'Very important foo() method.'

#13-1 枚举面向对象编程优于传统程序设计形式之处
'''答1 OO更多的是给了你一种能力，一种忽略细节的能力：忽略的越多，人类有限的智力就可以容纳
越多复杂的问题，并因此提高生产效率。
答2 OO三大件：封装，继承，多态。 封装是为了‘去除全局变量’，继承是为了‘去除代码dup’，多态是为了让继承得以成立。
由此可见，OO重要性也就两点，1 去全局变量，2 去代码dup。那么为什么这两点这么重要？亲手写过并且跟踪维护过大规模应用的
人自然明白，或者接收并维护过‘全局变量，代码dup满天飞项目’的人，也能明白。
答3 面向对象编程踏上了进化的阶梯，增强了结构化编程，实现了数据与动作的融合：数据层和逻辑层现在由一个可用以
这些对象的简单抽象层来描述。现实世界中的问题和实体完全暴露了本质，从中提供的一种抽象，可用来进行相似编码，或者
编入能与系统中对象进行交互的对象中。类提供了这样一些对象的定义，实例既是这些定义的实现。二者对面向对象设计来说
都是重要的，面向对象设计是采用面向对象方式架构来创建系统。
'''

# 13-2 函数和方法的区别
#答：函数在声明之后可以随时调用。方法是类的属性，只能由类的实例来调用。

#13-3 编写一个类，把数值转换为美元
class MoneyFmt(object):
    count = 0

    def __init__(self, data1):
        self.count = data1

    def update(self, data1):
        self.count = data1

    def __nonzero__(self):
        if self.count<1:
            return False
        else:
            return True

    def __repr__(self):
        return float(self.count)

    def __str__(self):
        data = self.count
        if isinstance(data, (int, long)):
            if data < 0:
                return '-$' + '{:,}'.format(abs(data)).split('.')[0]
            else:
                return '$' + '{:,}'.format(data).split('.')[0]
        elif isinstance(data, (float)):
            if data < 0:
                return '-$' + '{:,}'.format(abs(data)).split('.')[0] + '.' + '{:,}'.format(abs(data)).split('.')[1][0:2]
            else:
                return '$' + '{:,}'.format(data).split('.')[0] + '.' + '{:,}'.format(data).split('.')[1][0:2]
        else:
            return '$0'

#13-4 用户数据类，登录名，密码，上次登录时间
#代码在13userpw.py中

#13-5 坐标点类
class Point(object):
    x=0
    y=0
    def __init__(self,x1=0,y1=0):
        x=x1
        y=y1

# p=Point(1,3)
# print p.x,p.y

#13-6


























#
# if __name__=='__main__':
#     itd = MoneyFmt(25.36)
#     itd.update(222222.36)
#     print itd.__str__(),itd.__nonzero__(),itd.__repr__()
