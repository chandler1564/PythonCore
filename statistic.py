#coding=utf-8
import os
from os.path import join, getsize
import pymongo
from hashlib import md5
host = '10.0.60.206'
port = 27017
conn = pymongo.MongoClient(host,port)
db = conn.filelist
f = file('file_record.csv','a')
res = db.filelists10.find()
f.write('文件路径'+'\t'+'文件名'+'\t'+'处理信息')
f.write('\n')
for doc in res:
    if len(doc['root']) == 1:
        f.write(doc['root'][0].encode('utf-8'))
        f.write('\t')
        f.write(doc['filename'][0].encode('utf-8'))
        f.write('\t')
        try:
            f.write(doc['dealInfo'])
        except Exception, e:
            f.write('未处理')
        finally:
            f.write('\n')
    else:
        for i in range(len(doc['root'])):
            f.write(doc['root'][i].encode('utf-8'))
            f.write('\t')
            f.write(doc['filename'][i].encode('utf-8'))
            f.write('\t')
            try:
                f.write(doc['dealInfo'])
            except Exception, e:
                f.write('未处理')
            finally:
                f.write('\n')
f.close()