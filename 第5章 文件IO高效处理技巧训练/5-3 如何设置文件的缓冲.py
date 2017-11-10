#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5-3 如何设置文件的缓冲
f = open('./files/demo5-3.txt', 'w')
f.write('abc')
# 默认缓冲区大小跟设备相关 4096
f.write('+' * 4093)
f.write('-')

# 观测是否从缓冲区写入磁盘
# tail -f demo.txt

# 全缓冲
f = open('./files/demo5-3-2.txt', 'w', buffering=2048)
f.write('+' * 1024)
f.write('+' * 1023)
f.write('_' * 2)

# 行缓冲
f = open('./files/demo5-3-3.txt', 'w', buffering=1)
f.write('abcd')
f.write('\n')
f.write('xyz\n')

# 无缓冲
f = open('./files/demo5-3-4.txt', 'w', buffering=0)
f.write('a')
