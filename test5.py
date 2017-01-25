# coding=utf-8
'''
本章的主题是Python中的数字。我们会详细介绍每一种数字类型，他们使用的各种操作符，以及用于处理数字的内减函数。
在本章的末尾，我们简单介绍了几个标准库中用于处理数字的模块。
'''
from __future__ import division
import math
from decimal import Decimal
import sys
import random


#5-4
def quyu(t):
    if (t % 4 == 0 and t % 100 !=0) or (t % 400 == 0):
        return True
    else:
        return False
#5-5
def yingbi(t):
    yingbilist=[25,10,5,1]
    plan=''
    if (t >= 100) or (t <= 0) :
        return  'Wrong input'
    else:
        for yb in yingbilist:
            ybd=divmod(t,yb)
            if ybd[0]==0:
                continue
            else:
                plan=plan+ str(yb)+':'+str(ybd[0])+' '
                t = t - ybd[0]*yb
        return plan

#5-6
def qisuanqi(t):
    # czflist=['+','-','*','/','%','**']
    # for cl in czflist:
    #     if cl in t:
    #         return int(t.split(cl)[0])+int(t.split(cl)[1])
    if '.' not in t:
        if '+' in t:
            return int(t.split('+')[0]) + int(t.split('+')[1])
        elif '-' in t:
            return int(t.split('-')[0]) - int(t.split('-')[1])
        elif '**' in t:
            return int(t.split('**')[0]) ** int(t.split('**')[1])
        elif '/' in t:
            return int(t.split('/')[0]) / int(t.split('/')[1])
        elif '%' in t:
            return int(t.split('%')[0]) % int(t.split('%')[1])
        elif '*' in t:
            return int(t.split('*')[0]) * int(t.split('*')[1])
        else:
            return 'error input'
    else:
        if '+' in t:
            return float(t.split('+')[0]) + float(t.split('+')[1])
        elif '-' in t:
            return float(t.split('-')[0]) - float(t.split('-')[1])
        elif '**' in t:
            return float(t.split('**')[0]) ** float(t.split('**')[1])
        elif '/' in t:
            return float(t.split('/')[0]) / float(t.split('/')[1])
        elif '%' in t:
            return float(t.split('%')[0]) % float(t.split('%')[1])
        elif '*' in t:
            return float(t.split('*')[0]) * float(t.split('*')[1])
        else:
            return 'error input'

#5-7
def yingyeshui(s):
    yysdict={'jianzhu':Decimal('0.03'),'jinrongbaoxian':Decimal('0.05'), 'wenhuatiyu':Decimal('0.03'), 'yule':Decimal('0.05'), 'fuwu':Decimal('0.05')}
    return Decimal(s[1])*yysdict[s[0]]

#5-8 1 正方形 2 立方体 3 圆 4 球
def mianji(t,r):
    if t=='zheng':
        return r*r
    elif t=='li':
        return r*r*r
    elif t=='yuan':
        return math.pi*r*r
    elif t=='qiu':
        return (4.0/3.0)*math.pi*r**3
    else:
        return 'wrong input'

#5-10
def zhuanhuan(n):
    return (n-32)*(5/9)

#5-11
def qiou():
    oulist=[]
    qilist=[]
    for i in range(0,21):
        if i % 2 ==0:
            oulist.append(str(i))
        else:
            qilist.append(str(i))
    return  ','.join(oulist)+'-'+','.join(qilist)
# 5-11
def zhengchu(x,y):
    if x % y ==0:
        return True
    else:
        return False

#5-12
def fanwei():
    intlist=[-sys.maxint-1,sys.maxint]
    longlist=[]
    floatlist=[-sys.float_info.max-1,sys.float_info.max]
    # return  [-sys.maxint-1,sys.maxint]
    print intlist,longlist,floatlist
#5-13
def time_transfer(s):
    slist=s.split(':')
    return int(slist[0])*60+int(slist[1])
#5-14
def lixi(m,l):
    m=Decimal(m)
    l=Decimal(l)
    dingqi=m+m*l
    ri=l/360
    fuli=m*(1+ri)**365
    return  dingqi,fuli

#5-15
def gongbei1(x, y):
    gongyue = 1
    gongbei = 0
    i = 0

    while True:
        i=i+1
        if i > max(x,y):
            break
        if x % i == 0 and y % i == 0:
            gongyue = i

    while True:
        i=i+1
        if i % x == 0 and i % y == 0:
            gongbei = i
            break
    return gongyue,gongbei

# 5-16
def get_rest(balance,payment):
    loglist=[]
    loglist.append([0,Decimal('0.00'),Decimal(balance)])
    i=0
    while True:
        i=i+1
        # print '===',loglist[-1][2],payment
        if loglist[-1][2] < Decimal(payment):
            loglist.append([i, loglist[-1][2],Decimal('0.00')])
            break
        else:
            loglist.append([i, Decimal(payment), loglist[-1][2]-Decimal(payment)])
    for ll in loglist:
        print ll[0],ll[1],ll[2]
    # print loglist

#5-17
def suijishu(N,M):
    Nlist=[]
    for i in range(0,N):
        Nlist.append(random.randint(0, 2**31))
    Mlist=[]
    Mindex=[]
    for i in range(0,M):
        Mindex.append(random.randint(0,N))

    for mi in Mindex:
        Mlist.append(Nlist[mi])
    print Mlist
    sorted(Mlist)
    print Mlist



if __name__ == '__main__':
    # print quyu(2400)
    # print yingbi(76)
    # print qisuanqi('90.0/4')
    print yingyeshui(['wenhuatiyu','266'])
    # print mianji('yuan',3.4)
    # print zhuanhuan(90)
    # print qiou()
    # print zhengchu(8,3)
    # print fanwei()
    # print time_transfer('3:56')
    # print lixi(81234, 0.0330)
    # print gongbei1(190, 50)
    # get_rest('100.00','16.13')
    # suijishu(79,45)
    # a=1.0
    # b=1.0
    # print (a is b)