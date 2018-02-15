#闭包 = 函数 + 环境变量
# 函数一定要在被包含的函数外部，并且不能是全局变量


def curve_pre():
    # 环境变量
    a = 25

    def curve(x):
        return a*x*x
    return curve


f = curve_pre()
print(f.__closure__)
# 25
print(f.__closure__[0].cell_contents)
print(f(2))


def f1():
    a = 10

    def f2():
        # a为局部变量
        a = 20
        print(a)
    print(a)
    f2()
    print(a)


f1()
# 10
# 20
# 10





origin = 0
def go(step):
    global origin
    origin += step
    return origin

print(go(2))
print(go(3))
print(go(6))


def factory(origin):
    def go(step):
       nonlocal origin
       origin += step
       return origin
    return go

go2 = factory(0)
print(go2(2))
print(go2.__closure__[0].cell_contents)
print(go2(3))
print(go2.__closure__[0].cell_contents)
print(go2(6))
print(go2.__closure__[0].cell_contents)
