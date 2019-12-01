"""
2019/12/1 22:08
132.【Python魔术方法】二元运算符魔术方法
"""

"""
二元运算符魔术方法

普通运算操作符：
__add__(self, other): 在两个对象相加的时候执行的方法。
__sub__(self, other): 在两个对象相减的时候执行的方法。
__mul__(self, other): 在两个对象相乘的时候执行的方法。
__floordiv__(self, other): 在两个对象使用 // 整除运算的时候执行的方法。
__truediv__(self, other): 在两个对象使用 / 真除运算的时候执行的方法。
__mod__(self, other): 在两个对象使用 % 取模运算的时候执行的方法。
"""


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Position(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other):
        return Position(self.x // other.x, self.y // other.y)

    def __truediv__(self, other):
        return Position(self.x / other.x, self.y / other.y)

    def __mod__(self, other):
        return Position(self.x % other.x, self.y % other.y)

    def __str__(self):
        return 'Person (%s, %s)' % (self.x, self.y)


p1 = Position(24, 36)
p2 = Position(12, 18)

# TODO: __add__
print('__add__...')
p3 = p1 + p2
print(p3)

# TODO: __sub__
print('__sub__...')
p4 = p1 - p2
print(p4)

# TODO: __mul__
print('__mul__...')
p5 = p1 * p2
print(p5)

# TODO: __floordiv__
print('__floordiv__...')
p6 = p1 // p2
print(p6)

# TODO:__truediv__
print('__truediv__...')
p7 = p1 / p2
print(p7)

# TODO: __mod__
print('__mod__...')
p8 = p1 % p2
print(p8)
