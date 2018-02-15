#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 统计序列中元素出现的频度
from random import randint

data = [randint(0, 20) for _ in xrange(30)]
print data
c = dict.fromkeys(data, 0)
for x in data:
    c[x] += 1
print c

from collections import Counter

c2 = Counter(data)
print c2.most_common(3)

# 正则 统计2-3.txt中单词出现的频度
import re

txt = open('./res/2-3.txt').read()
c3 = Counter(re.split('\W+', txt))
print c3.most_common(10)
