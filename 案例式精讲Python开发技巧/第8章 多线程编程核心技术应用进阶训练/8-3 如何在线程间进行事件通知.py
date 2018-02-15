# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 8-3 如何在线程间进行事件通知

from Queue import Queue
from threading import Event,Thread
"""
def f(e):
    print 'f 0'
    e.wait()
    print 'f 1'

e=Event()
t=Thread(target=f,args=(e,))
t.start()
e.set()
e.clear()


def tarXML(tfname):
    tf = tarfile.open(tfname, 'w:gz')
    for fname in os.listdir('.'):
        if fname.endswith('.xml'):
            tf.add(fname)
            os.remove(fname)
    tf.close()

    #空包删除
    if not tf.members:
        os.remove(tfname)

#mkdir tmp
#tar zxfv test.tgz -C tmp
tarXML('test.tgz')
"""


def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level


import tarfile
import os


class TarThread(Thread):
    def __init__(self,cEvent,tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent=cEvent
        self.tEvent=tEvent
        self.setDaemon(true)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()
        # 空包删除
        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()
            self.tEvent.set()

# I/O操作
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


# CPU密集型操作
class ConvertThread(Thread):
    def __init__(self, sid, queue,cEvent,tEvent):
        Thread.__init__(self)
        self.cEvent=cEvent
        self.tEvent=tEvent
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
    count=0
    while True:
        sid, data = self.queue.get()
        print 'Convert', sid
        if sid == -1:
            self.cEvent.set()
            self.tEvent.wait()
            break
        if data:
            fname = str(sid).rjust(6, '0') + '.xml'
            with open(fname, 'wb') as wf:
                self.csvToXml(data, wf)
            count+=1
            #可以打包
            if count==5:
                self.cEvent.set()
                self.tEvent.wait()
                self.tEvent.clear()
                count=0



q = Queue()


cEvent=Event()
tEvent=Event()

dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]
cThread = ConvertThread(q,cEvent,tEvent)
tThread = TarThread(cEvent,tEvent)
tThread.start()


for t in dThreads:
    t.start()
cThread.start()

# 所有下载线程下载完成后，
for t in dThreads:
    t.join()
# 主线程 通知转换线程退出
q.put(-1, None)
