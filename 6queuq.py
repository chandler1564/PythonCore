#!/usr/bin/env python
# coding = utf8

queue1 = []

def enQ():
    global queue1
    queue1.append(raw_input('luru:').strip())

def deQ():
    global queue1
    if queue1:
        tmp=[]
        for q in queue1[1:]:
            tmp.append(q)
        print 'del ', queue1[0]
        queue1 = tmp
    else:
        print 'lenth of queue is 0'

def showQ():
    global queue1
    print queue1

CMDs ={'e': enQ, 'd': deQ, 's': showQ}

def queuemenu():
    while True:
        while True:
            try:
                choice = raw_input('choice types: ').strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'edsq':
                print 'Invalid option, try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    # print '-'
    queuemenu()







