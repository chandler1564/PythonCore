#!/ust/bin/env python
#coding:utf8

'''
本章的主要内容是Python的条件和循环语句以及它们相关的部分。
我们会深入探讨if、while、for及与它们相搭配的else、elif、break、
continue和pass语句。
'''
import string
import time
import random
# print 'abc'
# namelist=['ryoko','hirosue','chandler']
# e = enumerate(namelist)
# print e.next()
# valid=False
# count =3
# passwdList=['ryoko','1234','hirosue']
# while count >0:
#     input =raw_input('enter password: ')
#     for eachPasswd in passwdList:
#         if input == eachPasswd:
#             valid = True
#             break
#     if not valid:
#         print 'invalid input'
#         count -= 1
#         continue
#     else:
#         break
#
# def showMaxFactor(num):
#     count = num/2
#     while count > 1:
#         if num % count ==0:
#             print 'largest factor of %d is %d' % (num, count)
#             break
#         count-=1
#     else:
#         print num, 'is prime'
#
# for eachNum in range(10, 21):
#         showMaxFactor(eachNum)

#8-1 a x<0 A C E
#b  x==0  A D E
# c x>0 A B E

#8-2 循环
def myrange():
    f1=int(raw_input('f: '))
    t1=int(raw_input('t: '))
    i1=int(raw_input('i: '))
    print range(f1,t1,i1)

# 8-3 range()
def range1():
    print range(0,10)
    print range(3,19,3)
    print range(-20,861,220)

# 8-4 判断是否素数,一个数只能被1和自己整除，就是素数。
def isprime(luru):
    num=int(luru)
    for i in range(2,num):
        if num % i ==0:
            return False
    else:
        return True

#8-5 返回整数的约数列表
def getfactors(luru):
    num = int(luru)
    flist=[]
    for i in range(1,num+1):
        if num % i ==0:
            flist.append(i)
    return flist

#8-6 素因子分解，为什么后面会跟着一个None？
def getsu(luru):
    num= int(luru)
    ylist=getfactors(num)
    if isprime(num):
        print ylist[-1]
    # print '-'*10,ylist
    for i in (ylist[1], ylist[-2]):
        # print i,'-'*10
        if isprime(i):
            print i,
        else:
            getsu(i)

#8-7 是否是完全数，6的约数1 2 3 并且1+2+3=6
def isperfect():
    for j in range(1,1001):
        # num = int(raw_input('luru: '))
        num = j
        alist=getfactors(num)[0:-1]
        tmp=0
        for i in alist:
            tmp+=i
        if num==tmp:
            print j,1
        # else:
        #     print j,0

# 8-8 阶乘的计算
def jiecheng():
    num = int(raw_input('luru: '))
    re_num=1
    for i in range(num,1,-1):
        re_num=re_num*i
    print re_num

#8-9 斐波那契数列函数1,1,2,3,5,8,13
def fbnq():
    while True:
        num=int(raw_input('luru: '))
        flist=[]
        for i in range(num):
            flist.append(1)
        # print flist
        for i in range(2,num):
            flist[i]=flist[i-1]+flist[i-2]
        print flist

#8-10 统计一句话中的元音，辅音及单词的个数。
def strsum():
    linestr=raw_input('luru: ').strip()
    ylist=set(['a','e','i','o','u'])
    f=set(string.letters.lower())
    flist=f-ylist
    wordlist=linestr.split(' ')
    print 'words number: ',len(wordlist)
    ynum=0
    fnum=0
    for i in linestr:
        iset=set(str(i))
        if iset & ylist:
            ynum+=1
        elif iset & flist:
            fnum+=1
        else:
            pass
    print 'yuanyin number: ',ynum
    print 'fuyin number: ',fnum

def sgkfile(filename1):
    f=open(filename1,'r')
    f1=open(filename1[0:-4]+'_decode.txt','w')
    f1.write(f.next())
    for line in f:


        linestr=line.strip('\r\n').split('\t')
        if len(linestr[1])!=18 and len(linestr[1])!=15:
            lstr='%s****%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (linestr[0][0:3],linestr[0][-5:-1],linestr[1],linestr[2],linestr[3],
                                                                 linestr[4],linestr[5],linestr[6],linestr[7],
                                                                 linestr[8],linestr[9],linestr[10],linestr[11],linestr[12],linestr[13],
                                                                 linestr[14],linestr[15],linestr[16])
        else:
            # lstr='%s\t%s****%s\t%s\t%s****\t%s\n' % (linestr[0],linestr[7][0:3], linestr[7][-5:-1], linestr[8],linestr[10][0:15],linestr[11])
            lstr='%s****%s\t%s****\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (linestr[0][0:3],linestr[0][-5:-1],linestr[1][0:13],linestr[2],linestr[3],
                                                                 linestr[4],linestr[5],linestr[6],linestr[7],
                                                                 linestr[8],linestr[9],linestr[10],linestr[11],linestr[12],linestr[13],
                                                                 linestr[14],linestr[15],linestr[16])
        f1.write(lstr)
    f.close()
    f1.close()

#8-11 按格式输入姓名
def namestrack():
    num=int(raw_input('Enter total number of names: '))
    i=0
    j=0
    names=[]
    while i < num:
        namestr='Enter total number of name %s: ' % str(i)
        namelist=raw_input(namestr).split(',')
        if len(namelist)!=2:
            j=j+1
            print 'Wrong format...should be Last, First.'
            print 'You have done this %s time(s) already. Fixing input...' % str(j)
        else:
            names.append(namelist)
            i=i+1
            # print names,'-'*20
        # i=i+1
    print sorted(names,key=lambda a:a[0],reverse=False)

# 8-12 随意整数，输出其二进制，八进制，十进制，十六进制和asc码。
def intmap():
    num1=int(raw_input('from: '))
    num2=int(raw_input('to: '))
    print 'dec bin oct hex asc11'
    print '-'*30
    for i in range(num1,num2+1):
        print i,bin(i),oct(i),hex(i),chr(i)

#8-13 序列的迭代方式的效率。1迭代序列项，2 迭代索引
#测试结果是1.9倍。
def xunhuan():
    testlist=[]
    num=int(raw_input('num: '))
    for i in range(num):
        testlist.append(random.randint(1,100000))
    time1=time.time()
    for tl in testlist:
        tl-1
    xiangtime=time.time()-time1
    print 'xiang die dai',xiangtime

    time2=time.time()
    for i in range(0,num):
        testlist[i]-1
    suoyintime=time.time()-time2
    print 'suo yin die dai',suoyintime

    print suoyintime/xiangtime

if __name__=='__main__':
    # sgkfile(r'D:\mission\stratifyd4000\sgk1000.txt')
    # myrange()
    # range1()
    # isprime()
    # getfactors()
    # print getsu('20')
    # isperfect()
    # jiecheng()
    # fbnq()
    # strsum()
    # namestrack()
    # intmap()
    xunhuan()