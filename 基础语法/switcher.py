#  用字典映射代替switch case语句 

def getOne():
    return 'one'

def getTwo():
    return 'two'

def default():
    return 'defalut'

switcher={
    0:getOne,
    1:getTwo
}

index=3
name=switcher.get(index,default)()
print(name)