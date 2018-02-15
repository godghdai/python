#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4-1 如何拆分含有多种分隔符的字符串
import re

s = "hello;word|dfd|fd,ijg\tpop,sfdf\test"
res = s.split(';')
print map(lambda x: x.split('|'), res)
t = [];
map(lambda x: t.extend(x.split('|')), res)
print t
ret = t
t = []
map(lambda x: t.extend(x.split('\t')), res)
print t


def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    # 过滤空字符器
    return [x for x in res if x]


print mySplit(s, ';|,\t')

print re.split('[,;|,\t]+', s)
