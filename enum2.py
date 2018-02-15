from enum import Enum
'''
用字典类型和类表示枚举值的缺点：
1.可变
2.没有防止相同标签的功能
枚举类型中的值不能更改。
'''
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW)
print(VIP.GREEN.value)
print(VIP.GREEN.name)
# <enum 'VIP'>
print(type(VIP.GREEN))
print(VIP["GREEN"])

for v in VIP:
    print(v)


class Common(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4

# 默认值相等是不会全部遍历出来的
# 没有YELLOW_ALIAS
for v in Common:
    print(v)

for v in Common.__members__.items():
    print(v)

# 数值转枚举
a=1
print(VIP(a))



from enum import IntEnum,unique
# 值必需为int,且唯一
@unique
class CommonUnique(IntEnum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4