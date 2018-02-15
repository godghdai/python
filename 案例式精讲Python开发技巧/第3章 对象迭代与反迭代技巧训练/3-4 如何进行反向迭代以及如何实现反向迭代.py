#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  3-4 如何进行反向迭代以及如何实现反向迭代
l = [1, 2, 3, 4, 5]
l.reverse()
print l
l = [1, 2, 3, 4, 5]
# 切片操作
print l[::-1]

for x in reversed(l):
    print  x

"""
l.__iter__()
l.__reversed__()
"""


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for x in FloatRange(1.0, 4.0, 0.5): print x
print '--------------'
for x in reversed(FloatRange(1.0, 4.0, 0.5)):print x