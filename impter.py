#coding:utf-8
from imptee import foo, show
# import imptee
# imptee.show()
# imptee.foo=123
# print 'foo from impter: ', imptee.foo
# imptee.show()

def foo():
    print '\ncalling foo()...'
    aString ='bar'
    anInt=42
    print "foo()'s golbals: ",globals().keys()
    print "foo()'s locals: ", locals().keys()

print "__main__'s globals: ",globals().keys()
print "__main__'s locals:" , locals().keys()
foo()