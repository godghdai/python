'''
匿名函数需要使用lambda表达式，lambda表达式格式：
lambda parameter_list: expression
注：此处的expression只能是简单的B表达式，而不能实现像函数内部的代码块。
例：lambda x,y: x+y
'''

def add(x,y):
    return x+y

print(add(1,2))

f=lambda x,y:x+y
print(f(1,2))


#x>y?x:y
x=2
y=1
# 条件
r=x if x>y else y
print(r)


'''
三元表达式格式：
条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果
例：x if x > y else y

三元表达式常用于lambada表达式的表达式部分
三元表达式：
x=3
y=10
res=x if x>y else y
print(res)

三元表达式经常用于lambada表达式部分 例如：
res=lambda x,y:x if x>y else y
print(res(5,4))

'''


# map
list_x=[1,2,3,4,5,6,7,8]
list_y=[1,2,3,4,5,6,7,8]

def square(x):
    return x*x

r=map(square,list_x)
print(list(r))

r=map(lambda x:x*2,list_x)
print(list(r))

r=map(lambda x,y:x*2+y,list_x,list_y)
print(list(r))

# reduce
from functools import reduce

r=reduce(lambda sum,y:sum+y,list_x,0)
#(((1+2)+3)+4)+5
print(r)

list_x=[1,12,24,5,36,7,8]
# 三元表达式
r=filter(lambda x:True if x%2==0 else False,list_x)
print(list(r))

list_u=['a','B','c','F','e']
min_ord=ord('a')
max_ord=ord('z')
r=filter(lambda x:ord(x)>=min_ord and ord(x)<=max_ord,list_u)
print(list(r))

r=filter(lambda x:not str(x).islower(),list_u)
print(list(r))

import re
r=filter(lambda x:re.match('[a-z]',x),list_u)
print(list(r))

