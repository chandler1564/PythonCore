#encoding:utf-8
'''
本章将集中介绍Python模块和如何把数据从模块中导入到编程环境中。同时也会
涉及包的相关概念。模块是用来组织Python代码的方法，而包是用来组织模块的。
本章最后还会讨论一些与模块有关的其他方面的问题。
'''

import Tkinter as tk
import time
#
# class MyUltimatePythonStorageDevice(object):
#     pass
# bag=MyUltimatePythonStorageDevice()
# bag.x=100
# bag.y=200
# bag.version=0.1
# bag.completed=False
#
# print bag.x

#12-1 路径搜索和搜索路径的不同点
#路径搜索是指查找某个文件的操作；搜索路径是去查找一组目录。

#12-2 两种不同的引用方式
#a from mymodule import foo
#a import mymodule
# b 名称空间是名称到对象的映射。第一种只引用了foo，第二种引用了全部的模块。

#12-3 不同在于第一种必须要module.X来引用，但是第二种可直接调用X

#12-4 名称空间和变量作用域有什么不同？
# 命名空间是纯粹意义上的名字和对象间的映射关系，而作用域还指出了
#从用户代码的哪些物理位置可以访问到这些名字。

#12-5 a 使用__import__引用模块。
sys=__import__('sys')
# print sys.path
#12-5 b 使用__import__()从指定模块导入名字
time1=__import__('time',fromlist=['time'])
print time1.time()

# 12-6
def importAS(mymod):
    b=__import__(mymod)
    return b

# 12-7 导入钩子。研究PEP302的导入钩子机制
# 不会






if __name__=='__main__':
    c=importAS('time')
    c.time()








