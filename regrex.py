import re

a='c|c++|java|C#|python|javascript'
print(a.index('python')>-1)
print('python' in a)

# 正则表达式
r=re.findall('python',a)
print(r)

a='c0c++7java9C#6python10javascript'
# ['0', '7', '9', '6', '10']
r=re.findall('\d+',a)
print(r)

# 字符集
s='abc,acc,adc,aec,afc,ahc'
r=re.findall('a[cf]c',s)
#r=re.findall('a[c-f]c',s)
print(r)


'''
常见的概括字符集：
\d：0-9的数字，等价于[0-9]
\D: 非数字，等价于[^0-9]
\w：匹配包括下划线的任何单词字符。类似但不等价于“[A-Za-z0-9_]”，这里的"单词"字符使用Unicode字符集。
\W：匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
\s:匹配任何不可见字符(空白字符), 包括空格,制表符,换行符,回车,换页符等等  [ \t\n\r\f]
\S:匹配任何可见字符(非空白字符。等价于[^ \t\n\r\f]
. 匹配除换行符(\n)之外的其他所有字符
'''

a="python1111java678php"
# 贪婪
r=re.findall('[a-z]+',a)
print(r)
# 非贪婪+?
r=re.findall('[a-z]{3,6}?',a)
print(r)

'''
# 数量词
* 匹配0次或无限多次
+ 匹配1次或无限多次
? 匹配0次或者1次
注：若?前是字符出现次数范围则代表非贪婪
'''
a = 'pytho00python22pythonn'
r = re.findall('python?',a)
print(r)
#仅匹配一次   ('python{1,2}?',a)    或者    ('python{1}',a)    ('python',a)

# 边界匹配
qq='12345678912'
r = re.findall('^\d{4,8}$',qq)
print(r)

# 组
a = 'PythonPythonPythonPythonPythonPython'
r = re.findall('(Python){3}',a)
print(r)

'''
[]是一个或的关系
()是一个且的关系
. 匹配出换行符(\n)之外的其他所有字符
re.S 匹配所有的字符包含换行符
re.I忽率大小写，re.S匹配所有的字符包含换行符
'''
s="PythonC#\nC++"
r=re.findall('c#.{1}',s,re.I|re.S)
print(r)


# 正则替换
lanuage="PythonC#C++JavaPHPC#"
r=re.sub('C#','GO',lanuage,1)
print(r)


def convert(value):
    print(value)
    matched=value.group()
    return '!!'+matched+'!!'

r=re.sub('C#',convert,lanuage)
# Python!!C#!!C++JavaPHP!!C#!!
print(r)


s='A8C3721D86'
def convert2(value):
    matched=int(value.group())
    if matched >=6:
        return '9'
    else:
        return '0'

r=re.sub('\d',convert2,s)
# A9C0900D99
print(r)

'''
re模块中函数：
match函数：从字符串首字母开始匹配。
search函数：搜索整个字符串，返回第一个匹配的结果。
注：这两个函数一旦匹配到结果就立即返回而不继续匹配。
'''
r=re.match('\w',s)
print(r)
print(r.group())
print(r.span())

r=re.search('\d',s)
print(r)


'''
正则表达式中组的概念：
用括号括起来的多个字母，用于一次匹配一个字符串而不是单个字符。如果正则表达式中都是普通字符的话，默认是一个组。
在使用re模块中的search函数时，访问返回的匹配字符串时，可以使用group函数指定要访问的组，如：
注：若组号为0表示整个字符串。也可以使用groups函数以字符串元组形式返回所有匹配字符串。
'''

s = 'life is short,i use python'
r = re.search('life(.*)python', s)
#is short,i use 
print(r.group(1))
#[' is short,i use ']
r = re.findall('life(.*)python', s)
print(r)

s = 'life is short,i use python,i love python'
r = re.search('life(.*)python(.*)python', s)
#('life is short,i use python,i love python', ' is short,i use ', ',i love ')
print(r.group(0,1,2))
#(' is short,i use ', ',i love ')
print(r.groups())

