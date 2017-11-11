# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 8-5 如何使用线程池
# python3
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(3)


def f(a, b):
    print('f', a, b)
    return a ** b


future = executor.submit(f, 2, 3)
future.result()

# 2^4  3^5
executor.map(f, [2, 3, 5], [4, 5, 6])


def f2(a, b):
    print('f', a, b)
    time.sleep(10)
    return a ** b


executor.map(f2, [2, 3, 5, 6, 7], [4, 5, 6, 7, 8])
