#!/usr/bin/env python
# coding:utf-8

'''
创建website的标签
'''

import time
import hashlib
import re


db={}
file1=open(r'D:\gitcode\corePython\data\website.html','r')
for line in file1:
    if '<tr' in line:
        dblist=re.findall('<td>([^</>]*)</td>',line)
        db[dblist[1]]=[dblist[2],dblist[3],dblist[0]]
file1.close()

#添加新的书签
def newuser():
    labellist=raw_input('input lables : ').split(',')
    db[labellist[0]]=labellist[1],labellist[2],labellist[3]


#删除书签
def deluser():
    name=raw_input('del who? ')
    if db.has_key(name):
        del db[name]
        print '%s is deleted ' % name
    else:
        print 'there is no %s ' % name


#修改书签
def updatelable():
    name=raw_input('update which? and message').split(',')
    if db.has_key(name[0]):
        db[name[0]]=[name[1], name[2],name[3]]
        print '%s is updated ' % name[0]
    else:
        print 'there is no %s ' % name[0]


#展示所有用户
def showusers():
    print 'all user: ', db


def showmenu():
    prompt = '''
(N)ew User Login
(U)pdate a User
(D)elete a User
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
            #将数据存入file中。
            file1=open(r'D:\gitcode\corePython\data\website.html','w')
            file1.write('<table>\n')
            for d in db:
                file1.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n'%(db[d][2],d,db[d][0],db[d][1]))
            file1.write('</table>\n')
            file1.close()

        if choice == 'n': newuser()
        if choice == 'u': updatelable()
        if choice == 'd':deluser()
        if choice == 's':showusers()

if __name__ == '__main__':
    showmenu()#问题在于登录时间没有进一步修改，是shelve的问题吗？不能修改value是list的元素。