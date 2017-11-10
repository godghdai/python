# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 7-5 如何让类支持比较操作
from math import pi
from functools import total_ordering

"""
相当于运算符重载
total_ordering根据小于，等于实现
〉，>=
"""
@total_ordering
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        print 'in  ___it___'
        return self.area() < other.area()

    def __eq__(self, other):
        print 'in  ___eq___'
        return self.area() == other.area()

    """
    def __le__(self, obj):
        return self < obj or self == obj

    def _gt__(self, obj):
        return not (self < obj or self == obj)
    """

class Circle(object):
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r ** 2 * pi


r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)
c1 = Circle(3.2)
print r1 < r2  # r1.___lt(r2)







from abc import ABCMeta,abstractmethod
@total_ordering
class Shape(object):
    @abstractmethod
    def area(self):
        pass

    def __lt__(self, other):
        print 'in  ___it___'
        if not isinstance(other,Shape):
            raise TypeError('other is not Shape')
        return self.area() < other.area()

    def __eq__(self, other):
        print 'in  ___eq___'
        if not isinstance(other,Shape):
           raise TypeError('other is not Shape')
        return self.area() == other.area()


class Rectangle2(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle2(Shape):
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r ** 2 * pi

r11 = Rectangle2(5, 3)
c11 = Circle2(3.2)

print c11<=r11
print r11>c11
print r11>1
