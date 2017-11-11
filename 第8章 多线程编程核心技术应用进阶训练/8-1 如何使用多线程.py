# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 8-1 如何使用多线程
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO


def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level


def download(url):
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)


def csvToXml(scsv, fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h: h.replace(' ', ''), headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text
            eRow.append(e)
    pretty(root)
    et = ElementTree(root)
    et.write(fxml)


if __name__ == '__main__':
    """
    url='http://table.finance.yahoo.com/table.csv?s=000001.sz'
    rf=download(url)
    if rf:
        with open('000001.xml','wb') as wf:
            csvToXml(rf,wf)
    """

    for sid in xrange(1, 11):
        print 'Download...(%d)' % sid
        url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        url %= str(sid).rjust(6, '0')
        rf = download(url)
        if rf is None: continue

        print 'Convert to XML...(%d)' % sid
        fname = str(sid).rjust(6, '0') + '.xml'
        with open(fname, 'wb') as wf:
            csvToXml(rf, wf)


def handle(sid):
    print 'Download...(%d)' % sid
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None: return

    print 'Convert to XML...(%d)' % sid
    fname = str(sid).rjust(6, '0') + '.xml'
    with open(fname, 'wb') as wf:
        csvToXml(rf, wf)


"""
from threading import Thread
t=Thread(target=handle,args=(1,))
t.start()
"""


class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        handle(self.sid)
        pass


threads = []
for i in xrange(1, 11):
    t = MyThread(i)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

"""
t=MyThread(1)
t.start()

t.join()
"""
print 'main thread'
