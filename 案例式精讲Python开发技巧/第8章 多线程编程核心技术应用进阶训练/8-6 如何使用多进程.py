# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 8-6 如何使用多进程

from multiprocessing import Process
def f(s):print s

p=Process(target=f,args=('hello',))
p.start()



from multiprocessing import Queue,Pipe
q=Queue()

def f2(q):
    print 'start'
    print q.get()
    print 'end'

Process(target=f,args=(q,)).start()

q.put(100)


c1,c2=Pipe()
c1.send('abc')
c2.recv()


def f3(c):
   c.send(c.recv()*2)

c2,c3=Pipe()
Process(target=f3,args=(c2,)).start()
c1.send(55)
c1.recv()
#110



