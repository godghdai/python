# None 空

a=''
b=False
c=[]

print(a==None)
print(a==None)
print(a==None)

print(a is None)

#<class 'NoneType'>
print(type(None))

def fun():
    return None

a=fun()
if not a:
    print('not a')

if a is None:
    print('is None')

"""
a=None
a=''
a=[]
a=False
"""
#if not a:


class Test():
    def __bool_(self):
        return False
    def __len__(self):
        return 0

test=Test()

# 做先调用__bool_，后调用__len__
print(bool(None))
print(bool([]))
print(bool(test))

if test:
    print('s')
else:
    print('f')



