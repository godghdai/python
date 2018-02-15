## !/usr/bin/env python
# -*- coding: utf-8 -*-
# 9-1 如何使用函数装饰器

def fun(a, *b):
    print a
    for x in b:
        print '*%s' % x


fun(1, 1, 2, 3)
print '-------------'
fun(2, *[1, 2, 3])
print '-------------'


def fun2(a, **b):
    print b["c"]
    for key in b:
        print '**%s:%s' % (key, b[key])


print '-------------'
fun2(3, b=2, c=3, d=5)
print '-------------'
fun2(4, **{'b': 3, 'c': 4, 'd': 5})

print '-------------'


class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print self.name

    @staticmethod
    def staticTest():
        print "word"

    @classmethod
    def classTest(cls,**kwargs):
         return cls(**kwargs)

class Student(Person):
    def __init__(self,name, num):
        #Person.__init__(self,name)
        super(Student, self).__init__(name)
        self.num = num

    def say(self):
        print self.name+self.num

p = Person('hello')
p.say()
s = Student('stu',"2001")
s.say()

Person.staticTest()
s.staticTest()

Person.classTest(name="myPerson").say()

dic={
    "name":"dic",
    "num":"3"
}
s.classTest(**dic).say()