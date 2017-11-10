# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 7-7 如何在环状数据结构中管理内存
import sys


class A(object):
    def __del__(self):
        print('in A.__del__')


a = A()
# 引用计数 包含 sys.getrefcount的引用，所以一般比想象的大1
print sys.getrefcount(a) - 1
a2 = a
print sys.getrefcount(a) - 1
del a2
print sys.getrefcount(a) - 1


class Data(object):
    def __init__(self, value, owner):
        self.owner = owner
        self.value = value

    def __str__(self):
        return "%s's data,value is %s" % (self.owner, self.value)

    def __del__(self):
        print 'in Data.__del___'


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print 'in Node.__del___'


# 循环引用
node = Node(100)
# 删除后也没有回收，没用调用虚构函数__del__
del node

# 强制回收，也不行
import gc

gc.collect()

a = A()
print sys.getrefcount(a) - 1
# 弱引用，weakref,它可以创建一个能访问对象但不增加引用计数的对象
import weakref

a_wref = weakref.ref(a)
a2 = a_wref()
print a is a2
del a
del a2
"""
弱引用，对象存在返回对象，不存在，返回None
"""
print a_wref is None


class Data2(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner)
        self.value = value

    def __str__(self):
        return "%s's data,value is %s" % (self.owner, self.value)

    def __del__(self):
        print 'in Data.__del___'


class Node2(object):
    def __init__(self, value):
        self.data = Data2(value, self)

    def __del__(self):
        print 'in Node.__del___'


# 循环引用，引入软引用后，可以正常回收
node = Node2(100)
del node
"""
in Node.__del___
in Data.__del___
"""

raw_input('wait....')
