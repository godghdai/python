#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

data = [randint(-10, 10) for _ in xrange(10)]
print data

res = []
for x in data:
    if x >= 0:
        res.append(x)
print res

print filter(lambda x: x >= 0, data)

# 列表解析 执行更快
print [x for x in data if x >= 0]
"""
timeit filter(lambda x:x>=0,data)
timeit [x for x in data if x>=0]
"""

{x: randint(60, 100) for x in xrange(1, 21)}
d = {x: randint(60, 100) for x in xrange(1, 21)}
print d
# 字典解析
print {k: v for k, v in d.iteritems() if v > 90}

# 集合解析
s = set(data)
print {x for x in s if x % 3 == 0}
