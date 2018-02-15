#!/usr/bin/env python
# -*- coding: utf-8 -*-
#4-5 如何对字符串进行左, 右, 居中对齐
s='abc'
print s.ljust(20)
print s.ljust(20,'=')
print s.rjust(20,'_')
print s.center(20,'_')
"""
abc
abc=================
_________________abc
________abc_________
"""
#左对齐
print format(s,'<20')
#右对齐
print format(s,'>20')
#居中对齐
print format(s,'^20')

dic={
    'DistCull':500.0,
    'SmaillCull':0.04,
    'farclip':477,
    'lodDist':100.0,
    'trilinear':40
}
w=max(map(len,dic.keys()))
for k in dic:
    print k.ljust(w),':',dic[k]
"""
SmaillCull : 0.04
farclip    : 477
DistCull   : 500.0
lodDist    : 100.0
trilinear  : 40
"""