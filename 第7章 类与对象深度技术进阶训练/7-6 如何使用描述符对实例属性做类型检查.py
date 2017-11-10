# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 7-6 如何使用描述符对实例属性做类型检查
#类似代理
class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        print 'in  __get__', instance, owner
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        print 'in  __set__'
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print 'in  __del__'
        del instance.__dict__[self.name]

#默认 name并不存在实例的.__dict__中，说明不是实例的属性
class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)

p = Person()
print p.__dict__

p = Person()
p.name = 'Bob'
print p.name


