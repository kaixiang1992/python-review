"""
2019/12/1 21:23
131.【Python魔术方法】一元运算符魔术方法
"""

"""
一元运算符魔术方法：
__pos__(self)魔术方法： 在这个对象前面使用正号 + 的时候执行的方法.
__neg__(self)魔术方法： 在这个对象前面使用负号 - 的时候执行的方法.
__abs__(self)魔术方法： 在这个对象前面使用 abs函数（求绝对值） 的时候执行的方法.
__invert__(self)魔术方法： 在这个对象前面使用 ~ 的时候执行的方法.
"""


class Position(object):
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __pos__(self):
        return Position(self.lat + 1, self.lng + 1)

    def __neg__(self):
        return Position(self.lat - 1, self.lng - 1)

    def __abs__(self):
        return Position(abs(self.lat), abs(self.lng))

    def __invert__(self):
        return Position(255 - self.lat, 255 - self.lng)

    def __str__(self):
        return 'Position (%s, %s)' % (self.lat, self.lng)


p1 = Position(44.33795, -73.24821)
print(p1)

# TODO: __pos__
print('__pos__...')
p2 = +p1
print(p2)

# TODO: __neg__
print('__neg__...')
p3 = -p1
print(p3)

# TODO: __abs__
print('__abs__...')
p4 = abs(p1)
print(p4)

# TODO: __invert__
print('__invert__...')
p5 = ~p1
print(p5)
