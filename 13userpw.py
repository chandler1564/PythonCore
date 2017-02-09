# coding:utf-8

import shelve
import hashlib
import time
import pickle
import json
from os import listdir

class UserMsg(object):
    userdict={}
    def __init__(self):
        if 'userfile.txt' in listdir(r'D:\gitcode\PythonCore1\data'):
            file1=open(r'D:\gitcode\PythonCore1\data\userfile.txt','r')
            # print type(file1.readline())
            self.userdict=json.loads('{"ryoko":"1234"}')
            file1.close()
        else:
            pass

    def __del__(self):
        if self.userdict=={}:
            pass
        else:
            file1=open(r'D:\gitcode\PythonCore1\data\userfile.txt','w')
            print self.userdict
            file1.write(json.dumps(self.userdict))
            file1.close()

    def updateuser(self,username):
        name=username
        if self.userdict.has_key(name):
            del self.userdict[name]
            print '%s is deleted ' % name
        else:
            print 'there is no %s ' % name

    def userlogin(self,user,pwd):
        name=user.lower()
        pwd = pwd
        passwd=self.userdict.get(name)
        if passwd != None and passwd[0] == hashlib.md5(pwd).hexdigest():
            print
            if time.time() - passwd[1] > 30:
                self.userdict[name][1]=time.time()
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

    def showall(self):
        return self.userdict

    def newuser(self,name,pwd):
        self.userdict[name] = [hashlib.md5(pwd).hexdigest(), time.time()]
inst=UserMsg()
inst.newuser('ryoko','1234')
inst.newuser('hirosue','1234')
# print inst.showall()
