#encoding:utf-8

'''
这一章，我们将在前面内容的基础上，详细的讲解函数的方方面面。
除了预期特性之外，Python中的函数嗨支持多种调用方式以及参数类型
并实现了一些函数式编程接口。最后我们将以对Python变量的作用域和
递归函数的讨论来结束本章的学习
'''
from time import ctime,sleep
from operator import add,sub
from decimal import Decimal
import time

# 11-1 比较下面三个函数，填空
'''
input    f1                       f2              f3
2        0 1 2 3 4               2 3 4           2 3 4
4        0 1 2 3 4               4               4
5        0 1 2 3 4               None            None
'''

# 11-2 我是没看懂题目啥意思。就当做自动选择加减法吧。
def addandsub():
    odict={'+':add,'-':sub}
    instr=raw_input('luru: ').split(' ')
    print odict[instr[1]](int(instr[0]),int(instr[2]))

#11-3 a 重写内减函数  min和max
def min2(x,y):
    if x<=y:
        return x
    else:
        return y

#11-3 b 重写内减函数  min和max
def my_min(*nkw):
    tmplist=list(nkw)
    for i in range(len(tmplist)-1):#循环list，将最小值放在最右边
        if min2(tmplist[i],tmplist[i+1])==tmplist[i]:
            tmp=tmplist[i+1]
            tmplist[i+1]=tmplist[i]
            tmplist[i]=tmp
    return tmplist[-1]

#11-4 总时间的格式转换，分 变成 时：分
def min2hourmin(time1):
    hourstr=int(time1) / 60
    minstr=int(time1) % 60
    return '%d:%d' % (hourstr,minstr)

# 11-5 默认函数
def yingyeshui(shuliang,leixing='wenhuatiyu'):
    yysdict={'jianzhu':Decimal('0.03'),'jinrongbaoxian':Decimal('0.05'), 'wenhuatiyu':Decimal('0.03'), 'yule':Decimal('0.05'), 'fuwu':Decimal('0.05')}
    return Decimal(shuliang)*yysdict[leixing]

# 11-6 哪个傻逼翻译的，根本就是语义不通！完全不知道啥意思。

# 11-7 函数式编程
def mymap():
    print map((lambda x,y:(x,y)),[1,2,3],['abc','def','ghi'])

# 11-8 filter函数编程,从列表中挑出闰年的年份
def myfilter():
    print filter(lambda x:(x % 4 == 0 and x % 100 !=0) or (x % 400 == 0),range(1987,2016))

# 11-9 reduce函数编程。求列表集合的平均值
def myreducer():
    print reduce((lambda x,y:x+y),range(10))/10.0

# 11.10 描述下面的代码的含义
# files= filter(lambda x:x and x[0] !='.', os.listdir(folder))
# 代码是遍历文件夹中的文件的意思。

# 11.11 map的函数式编程，读文件，处理文件，写入新文件中。
def mapfilter():
    a= map(lambda x:x.replace(' ',''), open(r'D:\gitcode\corePython\data\cardlog.txt', 'r').readlines())
    file2=open(r'D:\gitcode\corePython\data\cardlog.txt', 'w')
    for i in a:
        file2.write(i+'\n')
    file2.close()

#11.12 传递函数的应用
def timeit(func,timestr):
    time1=time.time()
    totaltime=func(timestr)
    time2=time.time()
    return time2-time1,totaltime

#11.13 a reduce函数式编程
def mult(x,y):
    return x*y
# 11.13 b 计算阶乘
def jiecheng(x):
    print reduce(lambda x,y:mult(x,y),range(x,1,-1))

# 11.13 c 计算阶乘
def jiecheng1(x):
    print reduce(lambda x,y:x*y,range(x,1,-1))

# 11.13 d 给三个函数计时
def jishi():
    for i in [jiecheng,jiecheng1]:
        print timeit(i(10),'120')#计时的程序有点问题

# 11.14 斐波那契数列f3=f1+f2
fib=lambda n:1 if n<2 else fib(n-1)+fib(n-2)

#11.15 循环打印字符串的第一个，第-1个。
def getfirst(inputstr):
    inputstr1=inputstr[::-1]#逆序输出
    # print inputstr1
    inlist= map(lambda x,y:(x,y),inputstr,inputstr1)#输出一半就可以。
    print inlist[0:len(inlist)/2]

# 11.16 easyMath.py 增加 乘法 和除法，不明白题目要求除法达到什么目的。

# 11.17 a 不明白偏函数和currying的区别
# b 偏函数和闭包的区别也不明白
# c 迭代器 迭代出一个list               生成器，yield产生，只要是生成器，就一定是迭代器。

# 11.18 同步 函数的调用。知识点：装饰器和threading模块的同步指令。
# 这个感觉很难啊。暂时不写

if __name__=='__main__':
    # addandsub()
    # print my_min('chandler','bing','ryoko','hirosue')#参数可以写任意个
    # print min2hourmin('578')
    # print yingyeshui('266','jinrongbaoxian')
    # mymap()
    # myfilter()
    # myreducer()
    # mapfilter()
    # print timeit(min2hourmin,'12345')
    # print jiecheng(6)
    # jishi()
    # print [fib(i) for i in range(10)]
    getfirst('chandler')