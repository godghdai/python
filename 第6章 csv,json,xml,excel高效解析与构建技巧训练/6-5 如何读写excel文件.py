# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 6-5 如何读写excel文件
# pid install xlrd xlwt
import xlrd
import xlwt
"""
book = xlrd.open_workbook('./files/student.xlsx')
sheet = book.sheet_by_index(0)

sheet.nrows
sheet.ncols

cell = sheet.cell(0, 0)
print cell.ctype == xlrd.XL_CELL_TEXT
print cell.value
# xlrd.XL_CELL_TEXT

cell = sheet.cell(1, 1)
print cell.ctype == xlrd.XL_CELL_NUMBER
print cell.value

print sheet.row(1)
# [text:u'\u674e\u96f7', number:95.0, number:99.0, number:96.0]

print sheet.row_values(1)
# [u'\u674e\u96f7', 95.0, 99.0, 96.0]

print sheet.row_values(1, 1)
# [95.0, 99.0, 96.0]

# sheet.put_cell()


wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')
wsheet.write()
"""

rbook = xlrd.open_workbook('./files/student.xlsx')
rsheet = rbook.sheet_by_index(0)

#增加总分列
nc=rsheet.ncols
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,u'总分',None)

for row in xrange(1,rsheet.nrows):
    #跳过第一列
    t=sum(rsheet.row_values(row,1))
    rsheet.put_cell(row,nc,xlrd.XL_CELL_NUMBER,t,None)

wbook=xlwt.Workbook()
wsheet= wbook.add_sheet(rsheet.name)
style=xlwt.easyxf('align:vertical center,horizontal center ')
for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)

wbook.save('./files/student_output.xls')

