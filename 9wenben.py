#!/usr/bin/env python
# coding:utf-8

'''
创建website的标签
'''

import time
import hashlib
import re
import os


db=[]
#创建文件
def newuser():
    db.extend(raw_input('input lables : ').split('|'))
    file1=open(os.path.join(r'D:\gitcode\corePython\data',db[0]),'w')
    for d in db[1:]:
        file1.write(d+'\n')
    file1.close()

#编辑文件
def updatelable():
    rowid=raw_input('update which? ').split('|')
    db[int(rowid[0])]=rowid[1]
    file1=open(os.path.join(r'D:\gitcode\corePython\data',db[0]),'w')
    for d in db[1:]:
        file1.write(d+'\n')
    file1.close()


#显示文件
def showusers():
    file1=open(os.path.join(r'D:\gitcode\corePython\data',db[0]),'r')
    print file1.read()


def showmenu():
    prompt = '''
(N)ew User Login
(U)pdate a User
(S)how all Users
(Q)uit
Enter choice: '''
    done = False
    while not done:
        # print db
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\n You picked: [%s]' % choice
            if choice not in 'nuqds':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':
            done =True
            # #将数据存入file中。
            # file1=open(r'D:\gitcode\corePython\data\website.html','w')
            # file1.write('<table>\n')
            # for d in db:
            #     file1.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n'%(db[d][2],d,db[d][0],db[d][1]))
            # file1.write('</table>\n')
            # file1.close()

        if choice == 'n': newuser()
        if choice == 'u': updatelable()
        if choice == 's':showusers()

if __name__ == '__main__':
    showmenu()