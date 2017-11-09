#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4-2 如何判断字符串a是否以字符串b开头或结尾
import os, stat

files = os.listdir('./files')
s = "g.sh"
print s.endswith('.sh')
print s.endswith(('.sh', '.py'))

print [name for name in files if name.endswith(('.sh', '.py'))]
# 查看文件权限
print os.stat('./files/e.py').st_mode
# 转换为八进制数
print oct(os.stat('./files/e.py').st_mode)

# 增加用户的执行权限
os.chmod('./files/e.py', os.stat('./files/e.py').st_mode | stat.S_IXUSR)
