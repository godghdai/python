# 列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8]

b = [i**2 for i in a]
print(b)

b = [i**2 for i in a if i >= 5]
print(b)

# set 也可以被推导
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {i+2 for i in a if i >= 5}
print(b)

#　dict
a = {"name": "hello", "age": 18}
b = { vlaue:key for key,vlaue in a.items()}
print(b)

b = (key for key,vlaue in a.items())
for x in b:
    print(x)

b = [key for key,vlaue in a.items()]
print(b)

b = { key for key in a}
print(b)