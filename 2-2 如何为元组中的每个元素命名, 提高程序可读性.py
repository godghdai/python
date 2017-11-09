#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2-2 如何为元组中的每个元素命名, 提高程序可读性 tuple
"""
NAME=0
AGE=1
SEX=2
EMAIL=3
"""
NAME, AGE, SEX, EMAIL = xrange(4)
student = ('jim', 16, 'male', 'jim@gmail.com')
# print student[0]

print student[NAME]

# age
if student[1] >= 18:
   print 'hello'

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('jim', 16, 'male', 'jim@gmail.com')
s = Student(name='jim', age=16, sex='male', email='jim@gmail.com')
print s.name
print isinstance(s, tuple)
