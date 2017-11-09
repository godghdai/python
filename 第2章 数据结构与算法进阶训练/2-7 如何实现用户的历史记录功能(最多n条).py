#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2-7 如何实现用户的历史记录功能(最多n条)
# 猜数字游戏
from random import randint
from collections import deque
# 对象序列化保存
import pickle

N = randint(0, 100)
history = deque([], 5)

# 对象序列化保存与读取
pickle.dump(history, open('./res/history', 'w'))
pickle.load(open('./res/history'))


def guess(k):
    if k == N:
        print 'right'
        return True
    if k < N:
        print '%s is less-then N' % k
    else:
        print '%s is greater-then N' % k
    return False


while True:
    line = raw_input("please input a number:")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    # 输入h?查看转入历史
    elif line == 'history' or line == 'h?':
        print list(history)
