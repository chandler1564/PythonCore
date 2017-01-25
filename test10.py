#encoding:utf-8

'''
本章将介绍什么是异常、异常处理和Python对异常的支持。我们还会介绍如何在
代码里生成异常。最后，我们会涉及如何创建自定义的异常类。
'''

import math
import cmath
#
# def test():
#     try:
#         f=open('abc','r')
#     except IOError,e:
#         print 'could not open file: ',e
#
# def safe_float(obj):
#     try:
#         retval=float(obj)
#     # except ValueError:
#     #     retval='could not convert non-number to float'
#     # except TypeError:
#     #     retval='object type connot be converted to float'
#     # except (ValueError,TypeError):
#     #     retval='argument must be a number or numeric string'
#     # except Exception,e:
#     #     print e
#     except (ValueError,TypeError),diag:
#         retval=str(diag)
#     return retval
#
# def diag1():
#     try:
#         float(['float() does not', 'like lists',2])
#     except TypeError,diag:
#         pass
#     print type(diag),diag
#     print diag.__class__.__doc__
#     print diag.__class__.__name__
#
# def test1():
#     try:
#         float('abc123')
#     except:
#         import sys
#         exc_tuple=sys.exc_info()
#     print exc_tuple

# 10-1 程序执行是引发异常的因素
# a 用户，c 程序

#10-2 哪些因素会在执行交互解释器是引发异常
#b 解释器 c 程序

#10-3 引发异常的关键字
# try  exception raise finally else

# 10-4 try-exception   try-finally的区别
# exception不一定执行，finally一定执行；
# try-finally不是用来捕捉异常的。作为替代，无论异常是否发生，它常常用来
#维持一直的行为。

# 10-5 指出下列语句的异常
def errorexa():
    #if 3<4 then: print '3 is less than 4 !'    没有then关键字
    aList=['Hello','World!','Anyone','Home?']
    print 'the last string in aList is: ',aList[len(aList)]  #索引超出范围
    # x             c 未定义x
    x=4%0   #0不能做除数
    import math
    i=math.sqrt(-1)  # 不能对负数开方

# 10-6 自定义open函数
def myopen(filename1):
    try:
        file1=open(filename1,'r')
    except Exception,args:
        file1=None
    return file1

# 10-7 两个异常的区别。我看不出有什么区别。
def yichang1():

    try:
        a=float('69/')
    except Exception,e:
        a=10.0
    else:
        a=a*100
    return a

def yichang2():

    try:
        a=float('69/')
        a=a*100
    except Exception,e:
        a=10.0
    return a

#10-8 改进的raw_input()函数
def safe_input():
    try:
        ri =raw_input('input: ')
    except (EOFError,KeyboardInterrupt),e:
        ri=None
    return ri

# 10-9 改进的math.sqrt()函数
def safe_sqrt(n):
    try:
        ri=math.sqrt(n)
    except ValueError,e:
        ri=cmath.sqrt(n)
    return ri


if __name__=='__main__':
    # pass
    # test()
    # print safe_float('abc')
    # diag1()
    # test1()
    # for j in myopen(r'D:\gitcode\corePython\data\cardlog1.txt'):
    #     print j
    print yichang1()
    print yichang2()
    # print safe_input()
    # print cmath.sqrt(9)