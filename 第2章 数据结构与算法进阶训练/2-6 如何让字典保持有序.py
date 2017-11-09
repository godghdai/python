#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2-6 如何让字典保持有序
d = {}
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d: print k
print '-----------------------------'
from collections import OrderedDict

d = OrderedDict()
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d: print k

from time import time
from random import randint

store = OrderedDict()
players = list('ABCDEFGH')
start = time()
for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start,
    store[p] = (i + 1, end - start)

print
print '_' * 20
for k in store:
    print k, store[k];
