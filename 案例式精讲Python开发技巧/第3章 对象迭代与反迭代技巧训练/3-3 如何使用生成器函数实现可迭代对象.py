#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  3-3 如何使用生成器函数实现可迭代对象
def f():
    print 'in f(),1'
    yield 1

    print 'in f(),2'
    yield 2

    print 'in f(),3'
    yield 3


g = f()
print g.next()
print g.next()
for x in g: print x

print g.__iter__() is g


# True

#迭代给定范围内所有素数
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False

        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1,100):print x

"""
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""