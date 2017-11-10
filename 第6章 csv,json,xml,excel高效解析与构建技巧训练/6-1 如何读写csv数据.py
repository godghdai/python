#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 6-1 如何读写csv数据
from urllib import urlretrieve
import csv

# urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz','pingan.csv')
# 二进制模式打开
rf = open('./files/demo.csv', 'rb')
reader = csv.reader(rf)
# for line in reader: print  line

wf = open('./files/demo_copy.csv', 'wb')
writer = csv.writer(wf)
writer.writerow(['姓名'',生日', '年龄', '家庭电话', '地址', '备注'])
reader.next();
writer.writerow(reader.next())
writer.writerow(reader.next())
wf.flush()

with open('./files/demo.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('./files/demo2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        # 标题
        headers = reader.next()
        writer.writerow(headers)
        for line in reader:
            print line
            if line[1] < '1984-01-04':
                break
            if int(line[2]) >= 20:
                writer.writerow(line)

print 'end'
