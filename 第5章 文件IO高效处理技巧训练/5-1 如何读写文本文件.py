#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5-1 如何读写文本文件

s = u'你好'
ord('a')
print s.encode('utf8')
print s.encode('gbk')
# s.decode('utf8')

f = open('./files/py2.txt', 'w')
f.write(s.encode('gbk'))
f.close()

f = open('./files/py2.txt', 'r')
t = f.read()
print t.decode('gbk')

"""
python 3
b'python 3 #字节字符串'
'你好' #python 3 unicode不加u

f = open('py3.txt', 'wt', encoding='utf8')
f.write('你好，我爱编程')
f.close()

f = open('py3.txt', 'rt', encoding='utf8')
s = f.read()
print(s)
"""