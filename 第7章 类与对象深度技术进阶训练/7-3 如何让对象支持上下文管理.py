# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 7-3 如何让对象支持上下文管理
"""
#with 结束后，自动关闭文件
with open('demo.txt', 'w') as f:
    f.write('abcdef')
    f.writelines(['xyz\n', '123\n'])
 # f.close()
"""

from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

#模拟远程登录并执行linux命令
class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()

        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self, tn, write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])

    def cleanup(self):
            self.tn.close()
            self.tn = None
            with open(self.addr + '_history.txt', 'w') as f:
                f.writelines(self.history)


client = TelnetClient('127.0.0.1')
print '\nstart...'
client.start()
print  '\ncleanup.'
client.cleanup()





"""
实现上下文管理协议，需定义实例的__enter__,__exit__方法
它们分别在with开始和结束时被调用
"""
class TelnetClient2(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        #注释移动到__enter__方法内
        """
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        """
        #raise Exception('Test')
        """
        抛出异常后，直接调用__exit__方法
        """

        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self, tn, write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])

    def cleanup(self):
        pass
        #移动到__exit__(self, exc_type, exc_val, exc_tb)
        """
            self.tn.close()
            self.tn = None
            with open(self.addr + '_history.txt', 'w') as f:
                f.writelines(self.history)
        """

    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        return self

    #exc_type异常类型，exc_val异常值，exc_tb异常跟踪栈
    def __exit__(self, exc_type, exc_val, exc_tb):
            print  'In __exit__'
            self.tn.close()
            self.tn = None
            with open(self.addr + '_history.txt', 'w') as f:
                f.writelines(self.history)

            #防止往外抛异常，默认return None
            return True


"""
client为调用__enter__后的返回值
而不是TelnetClient2的构造器返回的值
"""
with TelnetClient2('127.0.0.1') as client:
    client.start()
print 'END'

