#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2-4 如何根据字典中值的大小, 对字典中的项排序
from random import randint

print sorted([9, 2, 2, 4])
dic = {x: randint(60, 100) for x in 'xyzabc'}
print dic
# iter(dic)
print (97, "a") > (33, "b")
print zip(dic.values(), dic.keys())
print sorted(zip(dic.itervalues(), dic.iterkeys()))

print dic.items()
# [('a', 60), ('c', 88), ('b', 94), ('y', 96), ('x', 69), ('z', 100)]
print sorted(dic.items(), key=lambda x: x[1])
