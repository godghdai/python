#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2-5 如何快速找到多个字典中的公共键(key)
from random import randint, sample

print sample('abcdefg', randint(3, 6))
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print s1, s2, s3
print res
# 集合交集
print s1.viewkeys() & s2.viewkeys() & s3.viewkeys()

print reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))
