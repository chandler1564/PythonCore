#encoding:utf-8
# foo='abc'
# def show():
#     print 'foo from imptee:', foo

class MyDataWithMethod(object):
    def printFoo(self):
        print 'You invoked printFoo()! '

# myObj=MyDataWithMethod()
# myObj.printFoo()

class AddrBookEntry(object):
    '''address book entry class'''
    def __init__(self,nm,ph):
        self.name=nm
        self.phone=ph
        print 'Created instance for: ',self.name

    def updatePhone(self,newph):
        self.phone=newph
        print 'Updated phone# for: ', self.name

# john=AddrBookEntry('John Doe','408-555-1212')
# jane=AddrBookEntry('Jane Doe','650-555-1212')
# print john.name,john.phone
# john.updatePhone('18862130511')
# print john.phone

class EmplAddrBookEntry(AddrBookEntry):
    ''' Employee Address Book Entry class'''
    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid=id
        self.email=em

    def updateEmail(self,newem):
        self.email=newem
        print 'Updated e-mail address for: ',self.name

john=EmplAddrBookEntry('John Doe','408-555-1212',42,'john@spam.doe')
print john.name
print john.phone,john.email
john.updatePhone('18862130511')
print john.phone
john.updateEmail('704158028@qq.com')
print john.email





















