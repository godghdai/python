#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4-3 如何调整字符串中文本的格式
import re

log = open('./files/log.txt').read();
print re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
"""
 11/10/2017 hello
 12/23/2017 word
"""
print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)
