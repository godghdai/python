#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5-2 如何处理二进制文件
import struct
import array

f = open('./files/demo.wav', 'rb')
info = f.read(44)
# 小端字节序
print  struct.unpack('h', '\x01\x02')
print  struct.unpack('>h', '\x01\x02')
"""
(513,)
(258,)
"""
# NumChannels 声道数 2bytes
print struct.unpack('h', info[22:24])

# SampleRate 采样频率  与int格式读取 4bytes
print struct.unpack('i', info[24:28])

# BitsPersSample 2bytes
print struct.unpack('h', info[34:36])

# 文件指针移到文件末尾
f.seek(0, 2)
f.tell()
n = (f.tell() - 44) / 2
buf = array.array('h', (0 for _ in xrange(n)))
f.seek(44)
f.readinto(buf)
print buf[10]
# 将声音变小
for i in xrange(n): buf[i] /= 8
f2 = open('./files/demo2.wav', 'wb')
f2.write(info)
buf.tofile(f2)
f2.close()
