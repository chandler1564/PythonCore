#!/usr/bin/env python
# coding=utf-8
'''
第六章，我们要研究这样一些Python类型，它们的成员时有序排列的，并且可以通过下标偏移量访问到它的一个
或者几个成员，这类Python类型统称为序列，包括字符串（普通字符串和unicode字符串）、列表
和元组类型。
'''

###例子
import string
import keyword
import random
import test5
import datetime

def example1():
    alphas = string.letters + '_'
    nums = string.digits
    print 'Welcom to the Identifier Checker v1.0'
    print 'Testees must be at least 2 chars long.'
    myInput = raw_input('Identifier to test? ')
    if len(myInput) > 1:
        if myInput[0] not in alphas:
            print 'invalid: first symbol must be alphabetic'
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print 'invalid: remaining symbols must be alphanumeric'
                    break
            else:
                print 'okay as an identifier'

def readfile():
    motd = ['ryoko hirosue']
    f = open(r'F:\sgkorigin\data.txt'.decode('utf8').encode('gbk'), 'r')
    motd.extend(f)
    f.close()
    print motd
    # for line in f:
    #     motd.extend(line)
    #     break

'''
An example of reading and writing Unicode strings:Writes a Unicode string to
a file in utf8 and reads it back in.
'''
def unicode_example():
    hello_out = u'Hello world\n'
    bytes_out = hello_out.encode('utf8')
    f = open('unicode.txt', 'w')
    f.write(bytes_out)
    f.close()

    f = open('unicode.txt', 'r')
    bytes_in = f.read()
    f.close()
    hello_in = bytes_in.decode('utf8')
    print hello_in

#6.1 in
#6.2 识别字符串表示符
def kown_biaoshifu():
    alphas = string.letters + '-'
    nums = string.digits
    keywords = keyword.kwlist
    myInput = raw_input('luru: ')
    if len(myInput) == 1:
        if myInput[0] not in alphas:
            print 'invalid: first symbol must be alphabetic'
        else:
            print 'okay as an identifier'
    if len(myInput) > 1:
        if myInput.lower() in keywords:
            print 'this is a keyword'
        elif myInput[0] not in alphas:
            print 'invalid: first symbol must be alphabetic'
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print 'invalid: remaining symbols must be alphanumeric'
                    break
            else:
                print 'okay as an identifier'

#6-3 排序
def sort_num():
    while True:
        inlist = raw_input('luru: ').strip().split(' ')
        inlist.sort()
        print 'zidianxu: ', ' '.join(inlist)

        inlist1 = [int(i) for i in inlist]
        inlist1.sort()
        print 'suanshuxu: ',' '.join([str(i) for i in inlist1])

# 6-4 计算平均分
def avrage_score():
    inlist = raw_input('luru: ').strip().split()
    outlist = [float(i) for i in inlist]
    print 'pingjunzhi: ', str(sum(outlist)/len(outlist))

# 6-5 循环读出头尾的字符
def xunhuan():
    inlist = raw_input('luru: ').strip()
    inlen = len(inlist)
    if inlen % 2 ==0:
        for i in range(0,inlen/2):
            print inlist[i]
            print inlist[-(i+1)]
    else:
        for i in range(0,inlen/2):
            print inlist[i]
            print inlist[-(i+1)]
        print inlist[inlen/2]

# 6-5 判断两个字符串是否相等
def match_str():
    str1 = raw_input('luru: ').strip()
    str2 = raw_input('luru: ').strip()
    for i,j in zip(str1,str2):
        if i == j:
            continue
        elif i > j:
            print 'str1 > str2'
            break
        else:
            print 'str1 < str2'
            break

# 6-5 判断字符串中是否出现回文现象。
def huiwen():
    while True:
        inlist = raw_input('luru: ').strip()
        inlen = len(inlist)
        for i in range(0, inlen/2):
            if inlist[i] != inlist[-(i+1)]:
                print 'not the same'
                break
        else:
            print 'this is a huiwen word'

# 6-5 给字符串加上回文字符串
def addhuiwen():
    inlist = raw_input('luru: ').strip()
    inlist1 = inlist[::-1]
    print inlist + inlist1

# 6-6 strip函数的替代品
def newstrip():
    while True:
        str1 = raw_input('luru: ')
        flag = [0, 0]
        for i in range(0, len(str1)):
            if str1[i] != ' ':
                flag[0] = i
                print i
                break
        for j in range(len(str1)-1, -1, -1):
            if str1[j] != ' ':
                flag[1] = j
                print j
                break
        print str1[flag[0]:flag[1]+1]

# 6-7 调试buggy.py程序 .感觉没有问题啊，这个函数就是除以一个数字中可以除以的数
def buggy():
    while True:
        # 接收一个字符串类型的数字
        num_str = raw_input('Enter a number: ')
        # 字符串转换为数字
        num_num = int(num_str)
        # 生成一个列表
        fac_list = range(1, num_num+1)
        print 'BEFORE', fac_list
        #哨兵
        i = 0
        # 循环列表
        while i < len(fac_list):
            # 删除可以正除以的数字
            if num_num % fac_list[i] == 0:
                del fac_list[i]
            # 哨兵加一
            i = i + 1
        # 输出结果
        print 'AFTER: ', fac_list

# 6-8 由数字返回英文
def num2engish():
    while True:
        num_str = raw_input('luru: ').strip()
        maplist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten' , 'eleven' , 'twelve' , 'thirteen' , 'fourteen' , 'fifteen' , 'sixteen' , 'seventeen' , 'eighteen' , 'nineteen' ]
        tenmaplist = ['zero', 'teen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        num_int = int(num_str)
        if 0 <= num_int <= 19:
            print maplist[int(num_str)]
        elif 20 <= num_int < 100:
            print tenmaplist[int(num_str[0])] + '-' + maplist[int(num_str[1])]
        elif 100 <= num_int < 1000:
            print maplist[int(num_str[0])].capitalize() + ' hundred and ' + tenmaplist[int(num_str[1])] + '-' + maplist[int(num_str[2])]
        else:
            print 'invalid input '

# 6-9 把分钟数转化为小时+分钟
def m2h():
    mins = int(raw_input('luru:  ').strip())
    s = divmod(mins, 60)
    print '%s mins could be changes to %s hour %s mins' % (mins, s[0], s[1])

# 6-10 字母大小写反转
def oppsitechar():
    instr = raw_input('luru: ').strip()
    outstr = ''
    for i in instr:
        if i.islower():
            outstr = outstr + i.upper()
        else:
            outstr = outstr + i.lower()
    print outstr

# 6-11 整型到ip地址的转换程序
def ip2int():
    iplist = raw_input('luru: ').strip().split('.')
    ipint = int(iplist[0]) * pow(256,3) + int(iplist[1]) * pow(256,2) + int(iplist[2]) * pow(256,1) + int(iplist[3])
    print ipint
def int2ip():
    num = int(raw_input('luru: ').strip())
    s = []
    for i in range(3, -1, -1):
        s.append(str(divmod(num, pow(256, i))[0]))
        num = divmod(num, pow(256, i))[1]
    print '.'.join(s)

# 6-12
def findchr():
    while True:
        string1 = raw_input('string: ').strip()
        chr = raw_input('char: ').strip()
        for i in range(len(string1)):
            if chr == string1[i]:
                print i
                break
def findchrback():
    while True:
        string1 = raw_input('string: ').strip()
        chr = raw_input('char: ').strip()
        for i in range(len(string1)-1,-1,-1):
            if chr == string1[i]:
                print i
                break
def subchr(string, origchar, newchar):
    newstring = ''
    for i in string:
        if origchar == i:
            newstring = newstring + newchar
        else:
            newstring = newstring + i
    print newstring

# 6-13 string类型转complex类型   -1.23e+4-5.67j
def atoc():
    num_str = raw_input('luru: ').strip()
    for i in range(1,len(num_str)):
        if ('+' == num_str[i] and 'e' != num_str[i-1]) or ('-' == num_str[i] and 'e' != num_str[i-1]):
            real = float(num_str[:i])
            imag = float(num_str[i:-1])
            break
    print complex(real, imag)

# 6-14 剪刀石头布
def gambling():
    while True:
        gdict = {'jiandao':0,'shitou':1,'bu':2}
        jiqilist = ['jiandao','shitou','bu']
        user_str = raw_input('luru: ').strip()
        jiqi = random.randint(0,2)
        yh = gdict[user_str]
        print 'yonghu: ',user_str,'jiqi: ',jiqilist[jiqi]
        if abs(yh - jiqi) == 2:
            res= -(yh - jiqi)
        elif abs(yh - jiqi) ==1 or abs(yh - jiqi) ==0:
            res= yh -jiqi
        else:
            print 'invalid input'

        if res ==0:
            print '平局'
        elif res > 0:
            print '赢了'
        else:
            print '输了'

# 6-15 日期转换，考虑闰月  YY/MM/DD的格式
def get_days():
    riqi1 = raw_input('rulu: ').strip()
    riqi2 = raw_input('luru: ').strip()
    rq1 = [int(i) for i in riqi1.split('/')]
    rq2= [ int(i) for i in riqi2.split('/')]
    print abs(rq1[2]-rq2[2] + 30*(rq1[1] - rq2[1]) + 360*(rq1[0]-rq2[0]))
def get_births():
    bir = raw_input('shengri: ').strip().split('/')
    bir_year = int(bir[0])
    bir_month = int(bir[1])
    bir_day = int(bir[2])
    birlist = []
    for i in range(bir_year+1,2016):
        if test5.quyu(i):
            birlist.append([i,365])
        else:
            birlist.append([i,366])

    runlist= [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]
    burunlist = [[1,31],[2,29],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]
    m =0
    if test5.quyu(bir_year):
        for j in range(0,bir_month-1):
            m = m +runlist[j][1]
    else:
        for j in range(0, bir_month-1):
            m = m + burunlist[j][1]
    birlist.append([bir_year,m+bir_day])
    birlist.append(([2016,359]))
    sumday=0
    for bl in birlist:
        sumday=sumday+bl[1]
    # print birlist
    print sumday
def next_birth():
    while True:
        bir = raw_input('shengri: ').strip().split('/')
        bir_month = bir[1]
        bir_day = bir[2]
        today_date=datetime.date.today()
        bir_date = datetime.date(2016,int(bir_month),int(bir_day))
        if  today_date <= bir_date :
            print bir_date - today_date
        else:
            nextbir_date = datetime.date(2017,int(bir_month),int(bir_day))
            print nextbir_date - today_date

# 6-16 矩阵的加和乘
def juzhenjia():
    a_str = raw_input('luru: ').strip().split(' ')
    b_str = raw_input('luru: ').strip().split(' ')
    a=[]
    b=[]
    for ast in a_str:
        a.append(ast.split(','))
    for bst in b_str:
        b.append(bst.split(','))
    c =[]
    for i in range(len(a)):
        tmp=[]
        for j in range(len(a[i])):
            tmp.append(int(a[i][j])+int(b[i][j]))
        c.append(tmp)
    print c
def juzhencheng():#乘操作挺难的。
    while True:
        a_str = raw_input('luru: ').strip().split(' ')
        b_str = raw_input('luru: ').strip().split(' ')
        a=[]
        b=[]
        for ast in a_str:
            a.append(ast.split(','))
        for bst in b_str:
            b.append(bst.split(','))
        c =[]
        print a,b
        for i in range(len(a)):
            tmp=[]
            for j in range(len(b[0])):
                cv = 0
                for k in range(len(b)):#矩阵计算的列*行
                    cv = cv + int(a[i][k])*int(b[k][j])
                tmp.append(cv)
            c.append(tmp)
        print c

#6-17 实现pop函数，input是一个列表，然后删除它的第一个元素，并返回它
def mypop():
    inlist = raw_input('luru: ').strip().split(',')
    returnstr = inlist[-1]
    del inlist[-1]
    return returnstr,inlist

#6-18 返回的是fn和ln的元素组成的新元组。(ian,Bairnson), (Stuart,Elliott) ,(David, paton)

#6-19 字符输出样式空值，真浮夸。
def printstyle():
    outlist = []
    for i in range(100):
        outlist.append(str(random.randint(0,1000)))
    tmpstr=''
    for i in range(len(outlist)):
        j=i+1
        tmpstr = tmpstr + outlist[i]+ ' '*5
        if j % 3 ==0:
            print tmpstr
            tmpstr=''
    print tmpstr


if __name__ == '__main__':
    printstyle()
    # print mypop()
    # gambling()
    # juzhenjia()
    # next_birth()
    # juzhencheng()
    # get_days()
    # readfile()
    # get_births()
    # unicode_example()
    # kown_biaoshifu()
    # sort_num()
    # avrage_score()
    # xunhuan()
    # match_str()
    # huiwen()
    # addhuiwen()
    # newstrip()
    # buggy()
    # num2engish()
    # num2engish()
    # m2h()
    # oppsitechar()
    # int2ip()
    # ip2int()
    # findchr()
    # findchrback()
    # subchr('ryokohirosue','o','O')
    # atoc()