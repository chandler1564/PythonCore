#!/usr/bin/env python
# coding:utf-8

'''
这是一个例子，检测用户名是否存在。新建用户名。
'''

import time
import hashlib
import pickle
import shelve

# db=pickle.loads(open(r'D:\gitcode\corePython\data\userpw.txt','r').read())

db=shelve.open(r'D:\gitcode\corePython\data\userpw')
#注册新用户
def newuser():
    prompt ='login desired: '
    while True:
        name = raw_input(prompt)
        #name字符串中必须全是小写字母，否则不通过。
        if not name.islower():
            prompt = 'no upper word, try another: '
            continue
        if set(name) & set(['+','-','*','/','[',']','(',')','{','}','\\','\'','\n','\t','\r','\f','\"','\b']):
            prompt = 'no blank or fuhao, try another'
            continue
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    db[name] = [hashlib.md5(pwd).hexdigest(), time.time()]

    # #将数据存入file中。
    # file1=open(r'D:\gitcode\corePython\data\userpw.txt','w')
    # # for d in db:
    # #     file1.write('%s:%s:%s\n'%(d,db[d][0],db[d][1]))
    # file1.write(pickle.dumps(db))
    # file1.close()
#登录已有账号
def olduser():
    name=raw_input('login: ').lower()
    pwd = raw_input('passwd: ')
    passwd=db.get(name)

    if passwd != None and passwd[0] == hashlib.md5(pwd).hexdigest():
        print
        if time.time() - passwd[1] > 30:
            db[name][1]=time.time()
            # print 'welcome back',name
            wel='''
***********************
***
*** welcome back %s
***
***********************
            ''' % name
            print wel
        else:
            print 'You already logged in at :<%f>' % passwd[1]
    else:
        print 'login incorrect '
    #  #将数据存入file中。
    # file1=open(r'D:\gitcode\corePython\data\userpw.txt','w')
    # for d in db:
    #     file1.write('%s:%s:%s\n'%(d,db[d][0],db[d][1]))
    # file1.close()
#删除用户
def deluser():
    name=raw_input('del who? ')
    if db.has_key(name):
        del db[name]
        print '%s is deleted ' % name
    else:
        print 'there is no %s ' % name
    # #将数据存入file中。
    # file1=open(r'D:\gitcode\corePython\data\userpw.txt','w')
    # for d in db:
    #     file1.write('%s:%s:%s\n'%(d,db[d][0],db[d][1]))
    # file1.close()
#展示所有用户
def showusers():
    print 'all user: ', db


def showmenu():
    prompt = '''
(N)ew User Login
(E)xisting User Login
(D)elete a User
(S)how all Users
(Q)uit
Enter choice: '''
    done = False
    while not done:
        print db
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\n You picked: [%s]' % choice
            if choice not in 'neqds':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':
            done =True
            db.close()
        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'd':deluser()
        if choice == 's':showusers()

if __name__ == '__main__':
    showmenu()#问题在于登录时间没有进一步修改，是shelve的问题吗？不能修改value是list的元素。