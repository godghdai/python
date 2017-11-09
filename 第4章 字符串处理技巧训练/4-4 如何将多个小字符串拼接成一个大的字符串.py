#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4-4 如何将多个小字符串拼接成一个大的字符串
s1 = 'abcdefg'
s2 = '12345'
print s1 + s2
print str.__add__(s1, s2)
print str.__gt__(s1, s2)

pl = ["<0112>", "<32>", "<1024*768>", "<60>", "<1>", "<100.0>", "<500.0>"]
s = ''
for p in pl:
    s += p
    print s

print ';'.join(['abc', '123', 'xyz'])
print ''.join(['abc', '123', 'xyz'])

l = ['abc', 123, 45, 'xyx']
#列表解析
print ''.join([str(x) for x in l])

#生成器表达式 开销比列表解析小
print ''.join(str(x) for x in l)
