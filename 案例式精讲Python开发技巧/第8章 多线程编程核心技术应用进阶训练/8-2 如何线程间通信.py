# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 8-2 如何线程间通信
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO

# from collections import deque
# 带锁安全队列
"""
标准库中的Queue.Queue是一个线程安全的队列，
Download线程把下载数据放入队列，Convert线程从队列里提取数据
"""
from Queue import Queue


# q = deque()


def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

#I/O操作
class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue

    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print 'Download', sid
        data = self.download(self.url)
        # 2 (sid,data)
        # q.append((sid, data))
        self.queue.put((self.sid, data))

#CPU密集型操作
class ConvertThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue


def csvToXml(self, scsv, fxml):
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


def run(self):
    while True:
        sid, data = self.queue.get()
        print 'Convert', sid
        if sid == -1:
            break
        if data:
            fname = str(sid).rjust(6, '0') + '.xml'
            with open(fname, 'wb') as wf:
                self.csvToXml(data, wf)


q = Queue()
dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()

# 所有下载线程下载完成后，
for t in dThreads:
    t.join()
# 主线程 通知转换线程退出
q.put(-1, None)
