# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 6-4 如何构建xml文档
from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import tostring
import csv


#解决UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xe5 in position 108: ordinal not in range(128
import sys
reload(sys)
sys.setdefaultencoding('utf8')



"""
e = Element('Data')
e.set('name', 'abc')
# e.text=None
e2 = Element('Open')
e2.text = '8.80'
e.append(e2)
print tostring(e)
et = ElementTree(e)
et.write('./files/demo6-4.xml')
"""

def pretty(e,level=0):
    if len(e)>0:
        e.text='\n'+'\t'*(level+1)
        for child in e:
            pretty(child,level+1)
        child.tail=child.tail[:-1]
    e.tail='\n'+'\t'*level


def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('Data')
        for line in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, line):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    pretty(root)
    return ElementTree(root)


et = csvToXml('./files/demo.csv')
et.write('./files/csv2xml.xml',encoding="utf-8")
