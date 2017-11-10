#!/usr/bin/env python
# -*- coding: utf-8 -*-
#5-5 如何访问文件的状态
import os
os.stat('./files/py2.txt')
# like stat(path),but do not follow symbolic links.
os.lstat('./files/py2.txt')
# like stat(path),but for an open file descriptor..
#os.fstat()

s= os.stat('./files/py2.txt')
print s
#nt.stat_result(st_mode=33206, st_ino=0L, st_dev=0L, st_nlink=0, st_uid=0, st_gid=0, st_size=4L, st_atime=1510297940L, st_mtime=1510299146L, st_ctime=1510297940L)

#转为二进制
print bin(s.st_mode)

import stat

#是否是一个文件夹
print stat.S_ISDIR(s.st_mode)
#是否是一个普通文件
print stat.S_ISREG(s.st_mode)
"""
S_IRUSR = 00400
S_IWUSR = 00200
S_IXUSR = 00100
S_IXGRP = 00010
S_IXOTH = 00001
"""
#文件访问权限
print s.st_mode&stat.S_IRUSR
print s.st_mode&stat.S_IXUSR

#文件最后访问时间
import time
print time.localtime(s.st_atime)
#time.struct_time(tm_year=2017, tm_mon=11, tm_mday=10, tm_hour=15, tm_min=12, tm_sec=20, tm_wday=4, tm_yday=314, tm_isdst=0)
#ll a.txt

#文件大小
print s.st_size

print os.path.isdir('./files/py2.txt')
print os.path.islink('./files/py2.txt')
print os.path.isfile('./files/py2.txt')
print os.path.getatime('./files/py2.txt')
print os.path.getsize('./files/py2.txt')