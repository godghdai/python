
# 序列解包
a = 1
b = 2
a, b = 1, 2

d = 1, 4, 8
print(type(d))  # <class 'tuple'>
a, b, c = d
print(b)

d = [11, 12, 13]
print(type(d))  # <class 'list'>
a, b, c = d
print(c)

# 函数返回多个结果


def fname(x, y):
    return x+1, y*2


x, y = fname(a, b)
print(x, y)


# 关键字参数　
# 方便调用， 调用时实参顺序可以不按函数定义的形参顺序
c = fname(y=3, x=2)
print(c)


# 默认参数
def print_user_info(name, sex='boy', age=18):
    print('name:', name)
    print('sex:', sex)
    print('age:', age)


print_user_info("joho", 'girl', 17)
print('--------------------')
print_user_info("peter")
print('--------------------')
print_user_info("test", age=22, sex='abc')


# 可变参数
def sum(*numbers):
    #<class 'tuple'>
    print(type(numbers))
    total = 0
    for num in numbers:
        total += num
    return total


print(sum(1, 2, 3, 4))
a = (1, 2, 3, 4)
# *a把元组类形的参数平铺
print(sum(*a))
b = [1, 2, 3, 4, 5]
print(sum(*b))


def demo(param1, *param, param2=2):
    print(param1)
    print(param)
    print(param2)


demo("a", 1, 2, 3, param2='test')


# 关键字可变参数
def city_temp(**param):
    #<class 'dict'>
    print(type(param))
    print(param)
    for key, value in param.items():
        print(key, ":", value)


city_temp(bj="32c", xm="23c", sh="31c")
a = {'yn': "32c", 'xm': "23c", 'sh': "31c"}
city_temp(**a)
city_temp()


# 变量的作用域
c = 33


def add(x, y):
    c = x+y
    print(c)


add(1, 2)
print(c)  # 33


def demo2():
    c = 50
    # 没有块级作用域
    for i in range(0, 9):
        a = 'a'
        c += 1
    print(c)
    # 可以打印a,python没有块级作用域
    print(a)


demo2()


# 作用域具有链式特性，逐级寻找
c = 1


def func1():
    c = 2

    def func2():
        # c=3
        print(c)
    func2()


func1()


# 局部变量转全局变量
def globalVar():
    global c
    c = 2


globalVar()
print(c)
