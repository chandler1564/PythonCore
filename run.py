#!/usr/bin/env python
#encoding:utf-8
'''
徐翔的代码，用来提取文件列表
'''
import os
from os.path import join, getsize
import pymongo
from hashlib import md5
host = '10.0.60.206'
port = 27017
conn = pymongo.MongoClient(host,port)
db = conn.filelist
filecounter = 0
md5counter = 0
filenamecounter = 0
unknowncounter = 0
jsoncounter = 0
datapath = u'F:\\sgkorigin'
f = file('filerecord.txt','a')
for root,dir,files in os.walk(datapath):
    if files == []:
        continue
    # f.write(root.encode('utf-8'))
    # f.write('\n')
    for ef in files:
        if '._' in ef.encode('utf-8'):
            continue
        if 'DS_Store' in ef.encode('utf-8'):
            continue
        if 'desktop.ini' in ef.encode('utf-8'):
            continue
        if getsize(join(root,ef)) == 0:
            continue
        filecounter = filecounter + 1
        print ef.encode('utf-8')
        m = md5()
        fmd = open(join(root, ef), 'rb')
        m.update(fmd.read())
        fmd.close()
        md5value = str(m.hexdigest())
        # res = db.filelists.find({'_id':md5value})
        # flag = False
        res = db.filelists10.update({'_id': md5value}, {'$set':{'dealInfo': 'yes(md5 verified)'}})
        if res['updatedExisting'] == True:
            md5counter = md5counter + 1
        else:
            res = db.filelists10.update({'filename': ef.encode('utf-8')}, {'$set':{'dealInfo': 'yes(file name verified)'}})
            if res['updatedExisting'] == True:
                filenamecounter = filenamecounter + 1
            else:
                res = db.filelists10.update({'filename': ef.encode('utf-8')+'x'},
                                            {'$set': {'dealInfo': 'yes(file name verified)'}})
                if res['updatedExisting'] == True:
                    filenamecounter = filenamecounter + 1
                else:
                    if not 'json' in ef.encode('utf-8'):
                        f.write(root.encode('utf-8'))
                        f.write('\n')
                        f.write(ef.encode('utf-8'))
                        f.write('\n')
                        unknowncounter = unknowncounter + 1
                    else:
                        jsoncounter = jsoncounter + 1
print('Scanned %d files' % filecounter)
print('MD5 verified %d files' % md5counter)
print('File name verified %d files' % filenamecounter)
print('Unknown %d files' % unknowncounter)
print('%d json files' % jsoncounter)
        # for doc in res:
        #
        #     for resf in res:
        #         if resf == '':
