#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4-6 如何去掉字符串中不需要的字符
import re
import string
s = ' abc  123   '
# 去除两端字符
print s.strip()

s = '+++abc  123---'
print s.strip('+-')

s = 'abc:123'
print s[:3]+s[4:]

s='\tabc\t123\txyz'
print s.replace('\t','')

s='\tabc\t123\txyz\rhello\r'
print re.sub('[\t\r]','',s)

#一个字符映射成另外一个字符
s='abc1230323xyz'
#构造映射表
#translate(table, deletechars=None)
print s.translate(string.maketrans('abcxyz','xyzabc'))
#xyz1230323abc

s='abc\refg\n\2342\t'
#删除\t
print s.translate(None,'\t\r\n')

#unicode
u=u'ni\u0301 ha\u030co, chi\u0304 fa\u0300n'
print u
print u.translate(dict.fromkeys([0x0301,0x030c,0x0304,0x0300]))
"""
ní hǎo, chī fàn
ni hao, chi fan
"""