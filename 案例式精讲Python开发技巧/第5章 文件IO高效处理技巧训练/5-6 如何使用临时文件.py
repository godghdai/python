#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5-6 如何使用临时文件
from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write('abcdef' * 1000)

f.seek(0)

print f.read(100)

ntf = NamedTemporaryFile()
print ntf.name
# c:\users\yzd\appdata\local\temp\tmpdvg6ow
# 不会自动删除
ntf = NamedTemporaryFile(delete=False)
