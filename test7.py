#!/usr/bin/env python
#coding:utf8

import  sys
import string
import random

"""
本章来讨论Python语言中的映射类型和集合类型。
和前面的一章一样，我们首先做一个介绍，再来讨论可用操作符，工厂函数、內建函数和方法，
然后再来看看每种数据类型的详细用法。
"""

#7-1 两个dict相加  使用dict1.update()
#7-2 可以hash的对象才能作为键值。一般来说，str，tuple，int都可以做键值。但是可变的dict，list不行。
#7-3 字典的一些基本函数
def mydict():
    dict1={'ryoko':1, 'hirosue':1980, 'chandler':1987, 'monica':1982}
    dlist = sorted(dict1)
    print dlist
    print '*'*40
    klist = sorted(dict1.iteritems(),key=lambda d:d[0],reverse=False)
    print klist
    print '*'*40
    vlist = sorted(dict1.iteritems(),key=lambda d:d[1],reverse=False)
    print vlist

#7-4 用两个list创建一个对应的dict
def cdict():
    list1=[1,2,3,4,5,6]
    list2=['abc','def','fgh','hij','kml','lmn']
    dict1=dict(zip(list1,list2))
    print dict1

#7-5 在7userpw中进行了修改。
#(a) 已经修改好，加上time的时间戳。
#(b) 做好了
#(c) 使用了md5加密算法
#(e) 要求用户名都是用小写字母
#(f) 用户名不允许出现符号和空白符
#(g) 不存在的用户名可能是老用户么？我不懂这道题目。没办法做。

#7-6 故事证券投资数据系统。
# 样例   ST 白银有色 209.00 100.00   N 凯众股份 2.00 10.90      XD 泰嘉股份 14.00 30.15
def mystock():
    stocklist=[]
    stockdict={}
    while True:
        stockmsg = raw_input('luru: ').strip()
        if stockmsg =='q':
            break
        else:
            stocklist.append(stockmsg.split(' '))
    print 'chose a col: ', stocklist[0]
    stockcol = int(raw_input('your choise: ').strip())
    for sl in stocklist:
        stockdict[sl[stockcol]]=sl
    print stockdict

#7-7 点到字典中的键和值
def reversedict():
    dict1={'ryoko':1980,'chandler':1986,'monica':1984}
    print 'befor: ',dict1
    dict2={}
    for d in dict1:
        dict2[dict1[d]]=d
    print 'after: ',dict2

#7-8 人力资源系统
def hrsystem():
    hrdict={}
    while True:
        hrlist=raw_input('luru: ').strip().split(' ')
        if hrlist[0]=='q':
            break
        else:
            hrdict[hrlist[0]] = hrlist[1]
    print sorted(hrdict.iteritems(),key=lambda s:s[0],reverse=False)
    print sorted(hrdict.iteritems(),key=lambda s:s[1],reverse=False)

#7-9 翻译
def tr():
    srcstr='abc'
    dststr='mno'
    dict1=dict(zip(list(srcstr),list(dststr)))
    instr=raw_input('luru: ').strip()
    s=[]
    for i in instr:#第一题
        if dict1.has_key(i):
            s.append(dict1[i])
        else:
            s.append(i)

    # for i in instr:#第三题什么意思，没看懂。
    #     if dict1.has_key(i):
    #         s.append(dict1[i])
    print'after tr()', ''.join(s)

#7-10 加密
def rot13():
    srcstr=list(string.letters)
    dststr=[]
    roti=''
    for istr in srcstr:
        i=ord(istr)
        if 110 <= i <= 122 or 78 <= i <= 90:
            roti=chr(i+13-26)
            dststr.append(roti)
        else:
            roti=chr(i+13)
            dststr.append(roti)
    rotdict=dict(zip(srcstr, dststr))
    # print sorted(rotdict.iteritems(),key=lambda a:a[0],reverse=False)
    while True:
        string1=raw_input('Enter string to rot13: ').strip()
        if string1=='q':
            break
        string2=[]
        for i in string1:
            if rotdict.has_key(i):
                string2.append(rotdict[i])
            else:
                string2.append(i)
        print 'Your string to en/decrypt was: ',string1
        print 'The rot13 string is :', ''.join(string2)

#7-11 在dict中，可以哈希的值就是合法的键。string tuple frozenset int类型 就是合法的键。
# list dict类型就是非法的键。

#7-12 （a）数学上，集合就是将数个对象归类而分成为一个或数个形态各异的大小整体。
# （b） Python中，集合就是一个数据容器，其中的元素是固定的，无序的。

#7-13 集合A和集合B的交集，并集。
def myset():
    while True:
        num = raw_input('number is ? ')
        if num =='q':
            break
        alist=[]
        blist=[]
        for i in range(int(num)):
            alist.append(random.randint(0,10))
            blist.append(random.randint(0,10))
        aset = frozenset(alist)
        bset= set(blist)
        print 'a: ',aset,'b: ',bset
        print 'a&b: ',aset & bset
        print 'a|b: ',aset | bset

# 7-14 用户计算集合的交集和并集，并判断
def myset1():
    while True:
        num = raw_input('number is ? ')
        if num =='q':
            break
        alist=[]
        blist=[]
        for i in range(int(num)):
            alist.append(str(random.randint(0,10)))
            blist.append(str(random.randint(0,10)))
        aset = frozenset(alist)
        bset= set(blist)
        print 'a: ', aset
        print 'b: ', bset
        for i in range(3):
            jiaoji = raw_input('a&b= :').strip()
            if frozenset(jiaoji.split(' '))==aset & bset:
                print 'jiaoji is right'
                break
        else:
            print 'a&b: ', aset & bset

        for i in range(3):
            bingji = raw_input('a|b= :').strip()
            if frozenset(bingji.split(' ')) == aset | bset:
                print 'bingji is right'
                break
        else:
            print 'a|b: ', aset | bset

# 7-14 创建某个集合的潜在子集，给用户判断
def myset2():
    while True:
        alist=[]
        sonlist=[]
        for i in range(6):#固定为6个元素
            alist.append(str(random.randint(0,10)))
        aset = set(alist)
        print 'aset is : ',aset
        # raw_input()
        num= random.randint(0, 5)#子集的个数比原集合小，而且是随机的。
        for i in range(num):
            sonlist.append(str(random.randint(0,10)))
        sonset = set(sonlist)
        print 'sonset is : ',sonset
        s1=raw_input('is sonset right: ').strip()
        # s2=''
        if sonset < aset :
            s2='y'
        else:
            s2='n'
        #这里不给用户更改答案了，因为判断题只有一次机会的。
        if s1==s2:
            print 'you are right'
        else:
            print 'wrong'

# 7-15 集合的计算器
def setcompute():
    a = set(raw_input('A: ').split(' '))
    b = set(raw_input('B: ').split(' '))
    compute = raw_input('fuhao: ').strip()
    print a,compute,b,':  '
    if compute =='in':
        print a in b
    elif compute =='&':
        print a & b
    elif compute =='^':
        print a ^ b
    elif compute =='<':
        print a < b
    elif compute =='<=':
        print a <= b
    elif compute =='==':
        print a == b
    else:
        print 'invalid fuhao '



if __name__=='__main__':
    # mydict()
    # cdict()
    # mystock()
    # reversedict()
    # hrsystem()
    # tr()
    # rot13()
    # myset2()
    setcompute()