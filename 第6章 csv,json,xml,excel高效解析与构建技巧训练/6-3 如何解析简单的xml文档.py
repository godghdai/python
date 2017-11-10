# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 6-3 如何解析简单的xml文档
from xml.etree.ElementTree import parse

f = open('./files/demo.xml')
et = parse(f)
root = et.getroot()
print root.tag
print root.attrib
print root.text.strip()

for chlid in root:
    print chlid.get('name')

#只能找下一层子节点
root.find('country')
root.findall('country')
root.findall('rank')
#[]

for e in root.iterfind('country'):
    print e.get('name')

print list(root.iter())

print list(root.iter('rank'))

print list(root.findall('country/*'))

print list(root.findall('.//rank'))

print list(root.findall('.//rank/..'))
"""
[<Element 'country' at 0x2507350>, <Element 'country' at 0x2507630>, <Element 'country' at 0x2507810>]
"""
print list(root.findall('country[@name]'))

print list(root.findall('country[@name="Liedhtenstein"]'))

#查看包含特定子元素tag的节点
print list(root.findall('country[rank]'))

print list(root.findall('country[rank="5"]'))

print list(root.findall('country[2]'))

#position从1开始
print list(root.findall('country[last()]'))

print list(root.findall('country[last()-1]'))