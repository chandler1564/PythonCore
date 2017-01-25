#!/usr/bin/env python
#encoding:utf-8
'''
本章将深入介绍Python的文件处理和相关输入输出能力。我们将介绍文件对象
（它的內建函数、內建方法和属性）、标准文件，同时讨论文件系统的访问方法、
文件执行、最后简洁的介绍持久存储和标准库中与文件有关的模块。
'''
import os
import sys
import json
import time
import shutil
import re
import random
import string
import struct
import gzip
import zipfile
import tarfile



# fp=open('F://read.txt','r')
# print repr(fp.readline())
# fp.seek(0)
# print repr(fp.readline())

# filename=raw_input('Enter file name: ')
# f=open(filename,'r')
# # allLines=f.readlines()
# # f.close()
# # for eachLine in allLines:
# #     print eachLine,
# for eachLine in f:
#     print repr(eachLine)
# f.close()
# filename=raw_input('Enter file name: ')
# fobj=open(filename,'w')
# while True:
#     aLine = raw_input('Enter a line ("." to quit): ')
#     if aLine !='.':
#         fobj.write('%s\n' % (aLine))
#     else:
#         break
# fobj.close()
# f=file('ryoko.txt','w+')
# print f.tell()
# f.write('test line 1 \n')
# print f.tell()
# f.write('test line 1\n')
# print f.tell()
# f.seek(-12,1)
# f.tell()

#9-1 文件过滤
def filterexplain(filename1):
    f = open(filename1,'r')
    i='closed'
    for line in f:
        if line.strip()[0]=='#':
            continue
        elif line.strip()[0]=="'":
            if i=='opened':
                i='closed'
            else:
                i='opened'
        elif i=='opened':
            continue
        else:
            print line.rstrip()
    f.close()

#9-2 文件访问访问文件的前F的前N行
def showfile():
    filename1=raw_input('filename: ').strip()
    num=int(raw_input('first N rows: '))
    f=open(filename1,'r')
    for line,i in zip(f,range(num)):
        print line.strip()
    f.close()

#9-3 求文件的行数
def lenfile():
    filename1=raw_input('filename: ').strip()
    f=open(filename1,'r')
    print len(f.readlines())
    f.close()

# 9-4 文件访问，翻页访问
def fanye():
    filename1=raw_input('filename: ').strip()
    f=open(filename1,'r')
    while True:
        for i in range(25):
            print i,f.next()
        raw_input('continue: ')
    f.close()

# 9-5 读多文件
def scorefile():
    filedir=r'D:\gitcode\corePython\data'
    slist={}
    for i in os.listdir(filedir):
        f=open(os.path.join(filedir,i),'r')
        for line in f:
            llist=line.strip('\n').split('\t')
            if slist.has_key(llist[0]):
                slist[llist[0]].append(int(llist[1]))
            else:
                slist[llist[0]]=[int(llist[1])]
        f.close()
    for j in slist:
        print j,sum(slist[j])
    # print slist

#9-6 比较文件
def cmpfile():
    filename1=raw_input('file1: ')
    filename2=raw_input('file2: ')
    f1=open(filename1,'r')
    f2=open(filename2,'r')
    for i,j,num in zip(f1,f2,range(10000)):
        if i == j:
            continue
        else:
            print 'rows: ',num
            for a,b,n in zip(i,j,range(1000000)):
                if a==b:
                    continue
                else:
                    print 'cols: ',n
                    break
            break
    f1.close()
    f2.close()

#9-7 解析win.ini
def jiexi():
    fdict={}
    f=open(r'c:\Windows\win.ini','r')
    for line in f:
        if '=' in line:
            flist=line.rstrip('\n').split('=')
            fdict[flist[0]]=flist[1]
    f.close()
    print fdict

#9-8 模块研究
def mokuai():
    mname=raw_input('luru: ')
    print dir(mname)

#9-9 进入Python标准库所在的目录
def getdoc():
    docdict={}
    filedir=r'C:\Python27\Lib'
    for i in os.listdir(filedir):
        if i[-3:]=='.py':
            f=open(os.path.join(filedir,i),'r')
            for line in f:
                if '__doc__' in line:
                    docdict[i]=1
                    break
            else:
                docdict[i]=0
            f.close()
    print sorted(docdict.iteritems(),key=lambda a:a[1],reverse=True)

#9-9 提取标准库的所有类和函数(需要进一步修订)
def getclassdef():
    cddict={}
    filedir=r'C:\Python27\Lib'
    for i in os.listdir(filedir):
        if i[-3:]=='.py':
            f=open(os.path.join(filedir,i),'r')
            for line in f:
                # print line[0:3]
                if line[0:3]=='def' and line[-2]==':':
                    if not cddict.has_key(i):
                        cddict[i]=[line.split('(')[0]]
                        # print line.split('(')[0]
                    else:
                        cddict[i].append(line.split('(')[0])
                elif line[0:5]=='class' and line[-2]==':':
                    if not cddict.has_key(i):
                        cddict[i]=[line.split(':')[0]]
                    else:
                        cddict[i].append(line.split(':')[0])
                else:
                    pass
            f.close()
    print cddict

#9-10 家庭理财，有储蓄账户，信用卡账户，金融账户。
def licai():
    flag=0
    file2=open(r'D:\gitcode\corePython\data\licai.json','r')
    moneydict=json.loads(file2.next())
    file2.close()
    while flag==0:
        print moneydict
        caozuo=raw_input('write caozuo  :').split(',')
        if caozuo[0]=='qu':
            moneydict['chuxu']=moneydict['chuxu']-int(caozuo[1])
        elif caozuo[0] =='cun':
            moneydict['chuxu']=moneydict['chuxu']+int(caozuo[1])
        elif caozuo[0]=='jie':
            moneydict['xinyongka']=moneydict['xinyongka']-int(caozuo[1])
        elif caozuo[0]=='dai':
            moneydict['jinrong']=moneydict['jinrong']+int(caozuo[1])
        elif caozuo[0]=='q':
            file1=open(r'D:\gitcode\corePython\data\licai.json','w')
            file1.write(json.dumps(moneydict))
            file1.close()
            flag=1
            shutil.copyfile(r'D:\gitcode\corePython\data\licai.json',r'D:\gitcode\corePython\data\licai.json'+str(time.time()))
        else:
            print 'invalid input. try agin'

# 9-11 编写一个URL书签管理工具
#9website.py

# 9-12 用户名和密码
#9userpw.py

# 9-13 命令行参数
#a 什么是命令行参数，他们有什么用？
# 在执行python命令时输入的参数。它们可以在灵活的利用py程序。
#b 写一个程序，打印出所有的命令行参数。
#print 'all agr',sys.argv[1:]

#9-14 修改计算器程序
#9calc.py

#9-15 复制文件
def cpfile(filename1,filename2):
    shutil.copyfile(filename1,filename2)

#9-16 打断超过80字的行。
def dadaun():
    file1=open(r'D:\gitcode\corePython\data\ryoko.txt','r')
    file2=open(r'D:\gitcode\corePython\data\ryoko1.txt','w')
    for line in file1:
        linenum=len(line)/80
        if linenum==0:
            file2.write(line)
        else:
            linesplit=[0]
            for i in range(linenum):
                for i in range((i+1)*80,0,-1):
                    if line[i] == ' ':
                        linesplit.append(i)
                        break
            for j in range(len(linesplit)-1):
                file2.write(line[linesplit[j]:linesplit[j+1]]+'\n')
            file2.write(line[linesplit[-1]:])
    file1.close()
    file2.close()

# 9-17 文本处理
#9wenben.py

# 9-18 搜索文件
def sswenjian(i,filename1):
    istr=chr(i)
    file1=open(filename1,'r')
    print len(re.findall(istr,file1.read()))

# 9-19 创建一个符合条件的文件
def createfile(i,inum,len):
    file1=open(r'D:\gitcode\corePython\data\createfile','wb')
    numlist=range(0,257)
    numlist.remove(i)

    inumlist=random.sample(range(0,len),inum)#预先制定设定字节值出现的位置

    for j in range(len):
        if j in inumlist:
            file1.write(struct.pack('i',i))
        else:
            file1.write(struct.pack('i',random.choice(numlist)))
    file1.close()

# 9-20 压缩文件，压缩gzip格式的文件。
def gzipfile():
    with open(r'D:\gitcode\corePython\data\ryoko1.txt','rb') as f_in, gzip.open(r'D:\gitcode\corePython\data\ryoko1.txt.gz','wb') as f_out:
        shutil.copyfileobj(f_in,f_out)

#9-21 zip归档文件。
def zipf():
    with zipfile.ZipFile(r'D:\gitcode\corePython\data\ryoko1.zip','w') as myzip:
        myzip.write(r'D:\gitcode\corePython\data\ryoko.txt','ryoko.txt')
        myzip.write(r'D:\gitcode\corePython\data\ryoko1.txt','ryoko1.txt')

#9-21 zip提取文件
def zipread():
    with zipfile.ZipFile(r'D:\gitcode\corePython\data\ryoko\ryoko1.zip','r') as myzip:
        # for i in myzip.namelist():
        #     myzip.extract(i)
        myzip.extractall(r'D:\gitcode\corePython\data\ryoko\1')

# 9-22 枚举zip归档文件中的所有文件，及其属性值
def lszip():
    with zipfile.ZipFile(r'D:\gitcode\corePython\data\ryoko\ryoko.zip','r') as myzip:
        for i in myzip.namelist():
            # print zipfile.ZipInfo(i).date_time
            print myzip.getinfo(i).filename, myzip.getinfo(i).date_time, myzip.getinfo(i).compress_size

# 9-23 TAR归档文件,没有压缩的功能。
def tarfile1():
    tar=tarfile.open('./data/ryoko2.tar','w')
    tar.add('./data/ryoko1.txt','ryoko1.txt')
    tar.add('./data/ryoko11.txt','ryoko11.txt')
    tar.close()

# 9-24  归档文件转换。从zip归档中移动【ryoko.txt】到tar归档文档中
def zip2tar():
    with zipfile.ZipFile(r'D:\gitcode\corePython\data\ryoko\ryoko1.zip','r') as myzip:
        myzip.extractall(r'D:\gitcode\corePython\data\ryoko\2')
    tar=tarfile.open('./data/ryoko2.tar', 'a')
    tar.add(r'D:\gitcode\corePython\data\ryoko\2\ryoko.txt', 'ryoko.txt')
    tar.close()

# 9-25  解压所有的压缩文件，通用解压程序
def zipall(filedir1,filedir2):
    for fd in os.listdir(filedir1):
        if '.tar' in fd[-5:]:
            tar=tarfile.open(os.path.join(filedir1,fd),'r')
            tar.extractall(filedir2)
            tar.close()
        elif '.zip' in fd[-5:]:
            with zipfile.ZipFile(os.path.join(filedir1,fd),'r') as myzip:
                myzip.extractall(filedir2)
        else:
            print fd


if __name__=='__main__':
    # filterexplain('run.py')
    # showfile()
    # lenfile()
    # fanye()
    # scorefile()
    # cmpfile()
    # jiexi()
    # mokuai()
    # getdoc()
    # getclassdef()
    # licai()
    # cpfile(r'E:\list.txt',r'E:\list1.txt')
    # dadaun()
    # sswenjian(99,r'D:\gitcode\corePython\data\ryoko1.txt')
    # createfile(100,9,800)
    # gzipfile()
    # zipf()
    # zipread()
    # lszip()
    # tarfile1()
    # zip2tar()
    zipall(r'D:\gitcode\corePython\data\test', r'D:\gitcode\corePython\data\test1')