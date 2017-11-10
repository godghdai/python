#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5-4 如何将文件映射到内存
"""
#/dev/zero，是一个输入设备，你可你用它来初始化文件。该设备无穷尽地提供0，可以使用任何你需要的数目——设备提供的要多的多。他可以用于向设备或文件写入字符串0。
dd if=/dev/zero of=demo.bin bs=1024 count=1024
"""
import mmap
import os

f = open('files/demo.bin', 'r+b')
f.fileno()

mmap.PAGESIZE
# offset必需为页大小的整数 倍
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRIT, offset=mmap.PAGESIZE * 4)
type(m)

# od -x demo.bin

mp[10:20]
x[0] = '\x88'
m[4:8] = '\xff' * 4

m = mmap.mmap(f.fileno(), mmap.PAGESIZE * 8, access=mmap.ACCESS_WRIT, offset=mmap.PAGESIZE * 4)
m[:0x1000] = '\xaa' + 0x1000
