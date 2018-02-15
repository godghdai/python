import time
# AOP 思想
def f1():
    print("This is a f1")

def f2():
    print("This is a f2")


def print_time(func):
    print(time.time())
    func()

# 太不优雅
print_time(f1)

def time_decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

f=time_decorator(f2)
f()

@time_decorator
def f3():
    print("This is a f3")

f3()

# 解决参数个数不一切的问题
def time_decorator2(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@time_decorator2
def pf1(p1):
    print("This is a "+p1)

@time_decorator2
def pf2(p1,p2):
    print("This is a "+p1)
    print("This is a "+p2)

pf1("pf1")
pf2("pf21","pf22")


def time_decorator3(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

def pf3(p1,p2,**kw):
    print("This is a "+p1)
    print("This is a "+p2)
    print(kw)

pf3('pa','pb',j=1,d=2)

@time_decorator3
def pf4(p1,p2,**kw):
    print("This is a "+p1)
    print("This is a "+p2)
    print(kw)

pf4('pa','pb',a=1,b=2)

# flask


#　装饰器的副作用
# 文档注释和函数名改变了
def pf55():
    '''
      This is pf55
    '''
    print(pf55.__name__)

print(help(pf55))


from functools import wraps

def time_decorator4(func):
    @wraps(func)
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@time_decorator4  
def pf56():
    '''
      This is pf56
    '''
    print(pf56.__name__)

help(pf56)