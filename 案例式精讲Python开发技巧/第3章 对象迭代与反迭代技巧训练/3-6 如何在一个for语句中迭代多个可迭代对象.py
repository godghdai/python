#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3-6 如何在一个for语句中迭代多个可迭代对象
from random import randint
from itertools import chain

chinese = [randint(60, 100) for _ in xrange(40)]
math = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]

for i in xrange(len(math)):
    print  chinese[i] + math[i] + english[i]

print  zip([1, 2, 3, 4], ('a', 'b', 'c', 'd'), [13, 14, 15, 16])

total = [];
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)

for x in chain([1, 2, 3, 4], ['a', 'b', 'c', 'd']):
    print x

e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(42)]
e3 = [randint(60, 100) for _ in xrange(42)]
e4 = [randint(60, 100) for _ in xrange(39)]
count = 0
for s in chain(e1, e2, e3, e4):
    if s > 90:
        count += 1

print count
