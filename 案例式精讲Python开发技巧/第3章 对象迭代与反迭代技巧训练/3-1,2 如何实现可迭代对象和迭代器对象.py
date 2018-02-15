#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3-1 如何实现可迭代对象和迭代器对象(1)(2)
import requests

l = [1, 2, 3, 4]
s = 'abcde'
for x in l: print x
for x in s: print x
"""
#迭代器接口
l.__iter__()
#序列接口
s.__getitem__()
"""


def getWeather(city):
    r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['forecast'][0]
    return '%s:%s,%s' % (city, data['low'], data['high'])


# [u'北京',u'上海',u'广州',u'长春']
"""
print getWeather(u'北京')
print getWeather(u'长春')
#北京:低温 7℃,高温 13℃
#长春:低温 0℃,高温 10℃
"""

from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            # 抛异常
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable([u'北京', u'上海', u'广州', u'长春']):
    print x
"""
北京:低温 7℃,高温 13℃
上海:低温 15℃,高温 21℃
广州:低温 19℃,高温 27℃
长春:低温 0℃,高温 10℃
"""
