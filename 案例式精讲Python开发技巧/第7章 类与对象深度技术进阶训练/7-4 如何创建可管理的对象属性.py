# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 7-4 如何创建可管理的对象属性

from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
        #四舍五入
        #return round(self.radius)

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError('wrong type.')
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi
    #R来调用get和set方法
    R = property(getRadius,setRadius)

c = Circle(3.2)
"""
#没有类型检查，错误
c.radius = 'abc'
d = c.radius * 2
print d
# abcabc
"""
print c.R
c.R=5.9
print c.R
