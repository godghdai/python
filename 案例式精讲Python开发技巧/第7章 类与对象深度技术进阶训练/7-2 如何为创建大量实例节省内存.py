# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 7-2 如何为创建大量实例节省内存

class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


# 阻止动态属性绑定，节省内存，
# 去掉 __dict__，属性已固定，赋值其它属性报错
class Player2(object):
    __slots__ = ['uid', 'name', 'status', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


p1 = Player('0001', 'Jim')
p2 = Player2('0001', 'Jim')

# 两个实例属性差积，Player比Player2多两个属性
print set(dir(p1)) - set(dir(p2))
# set(['__dict__', '__weakref__'])

# 默认支持动态属性
print p1.__dict__
p1.x = 123
p1.__dict__['y'] = 99
del p1.__dict__['x']

# 计算对象占用内存空间
import sys

print sys.getsizeof(p1.__dict__)

# __slots__  后不允许动态增加属性
p2.x = 123
# AttributeError: 'Player2' object has no attribute 'x'
