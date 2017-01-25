#encoding:utf8

import sys


def jisuanqi():
    # writelist=[]
    restr=''
    t=''.join(sys.argv[1:])
    if 'print' in t:
        file2=open(r'D:\gitcode\corePython\data\cal.txt','r')
        restr=file2.read()
        file2.close()
    elif '.' not in t:
        if '+' in t:
            restr= int(t.split('+')[0]) + int(t.split('+')[1])
        elif '-' in t:
            restr= int(t.split('-')[0]) - int(t.split('-')[1])
        elif '**' in t:
            restr= int(t.split('**')[0]) ** int(t.split('**')[1])
        elif '/' in t:
            restr= int(t.split('/')[0]) / int(t.split('/')[1])
        elif '%' in t:
            restr= int(t.split('%')[0]) % int(t.split('%')[1])
        elif '*' in t:
            restr= int(t.split('*')[0]) * int(t.split('*')[1])
        else:
            restr= 'error input'
    else:
        if '+' in t:
            restr= float(t.split('+')[0]) + float(t.split('+')[1])
        elif '-' in t:
            restr= float(t.split('-')[0]) - float(t.split('-')[1])
        elif '**' in t:
            restr= float(t.split('**')[0]) ** float(t.split('**')[1])
        elif '/' in t:
            restr= float(t.split('/')[0]) / float(t.split('/')[1])
        elif '%' in t:
            restr= float(t.split('%')[0]) % float(t.split('%')[1])
        elif '*' in t:
            restr= float(t.split('*')[0]) * float(t.split('*')[1])
        else:
            restr= 'error input'
    file1=open(r'D:\gitcode\corePython\data\cal.txt','a')
    file1.write('9calc.py '+' '.join(sys.argv[1:])+'\n')
    file1.write(str(restr)+'\n')
    file1.close()
    return restr


if __name__=='__main__':
    print jisuanqi()
