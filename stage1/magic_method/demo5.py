"""
2019/12/1 22:36
133.【Python魔术方法】增量赋值魔术方法
"""

"""
增量赋值魔术方法：
__iadd__(self, other): 在给对象做 += 运算的时候会执行的方法.
__isub__(self, other): 在给对象做 -= 运算的时候会执行的方法.
__imul__(self, other): 在给对象做 *= 运算的时候会执行的方法.
__itruediv__(self, other): 在给对象做 /= 运算的时候会执行的方法.
__imod__(self, other): 在给对象做 %= 运算的时候会执行的方法.
"""


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other
        self.y += other
        return self

    def __isub__(self, other):
        self.x -= other
        self.y -= other
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __imod__(self, other):
        self.x %= other
        self.y %= other
        return self

    def __str__(self):
        return 'Position (%s, %s)' % (self.x, self.y)


p1 = Position(23, 24)
print(p1)

# TODO: __iadd__
print('__iadd__ += 2')
p1 += 2
print(p1)

# TODO: __isub__
print('__isub__... -= 15')
p1 -= 15
print(p1)

# TODO: __imul__
print('__imul__... *= 5')
p1 *= 5
print(p1)

# TODO: __itruediv__
print('__itruediv__... /= 3')
p1 /= 3
print(p1)

# TOOD: __imod__
print('__imod__... %= 5')
p1 %= 5
print(p1)
