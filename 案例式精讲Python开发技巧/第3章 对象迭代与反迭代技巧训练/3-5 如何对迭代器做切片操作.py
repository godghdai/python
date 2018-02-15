#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  3-5 如何对迭代器做切片操作
from itertools import islice

f = open('./res/3-5.txt')
# f[100:300]

lines = f.readlines()
print lines[10:50]

f.seek(0)
for line in f:
   print line

#10->23行
for line in islice(f,10, 23):
    print line

"""
#前500行
islice(f,500)
#100到末尾
islice(f,100，None)
"""

l=range(20)
t=iter(l)
for x in islice(t,5,10):print x
print '--------------'
for x in t:print x