# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 7-8 如何通过实例方法名字的字符串调用方法
from Shape.Triangle import Triangle
from Shape.Circle import Circle
from Shape.Rectangle import Rectangle


def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()
    pass


shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)

shapes = [shape1, shape2, shape3]
print map(getArea, shapes)


from operator import methodcaller
s='abc123abc456'
s.find('abc',4)

print methodcaller('find','abc',4)(s)
