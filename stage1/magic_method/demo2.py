"""
2019/12/1 20:46
130.【Python魔术方法】比较运算符魔术方法
"""

"""
比较运算符魔术方法：
__eq__(self, other): ==比较运算符，比较两个对象是否相等调用这个方法。如果相等返回True，否则返回False
__ne__(self, other): !=比较运算符，比较两个对象是否不相等会调用这个方法。如果不相等返回True,否则返回False
__lt__(self, other): < 比较运算符，比较两个对象大小的时候会调用这个方法。如果self < other那么返回True,否则返回False
__gt__(self, other): > 比较运算符，比较两个对象大小的时候会调用这个方法。如果self > other那么返回True,否则返回False
__le__(self, other): <= 比较运算符。首先判断 < ,如果返回True那么就返回True。如果为False，那么再执行 == 判断，如果返回
    为True或者False，那么就返回True或者False
__ge__(self, other): >= 比较运算符。首先判断 > ,如果返回True那么就返回True。如果为False，那么再执行 == 判断，如果返回
    为True或者False，那么就返回True或者False
"""


class Person(object):
    def __init__(self, name, age, height):
        """
        判断两个对象大小的条件：
        1. 首先看age，谁的age大，谁就大
        2. 如果age相等，就看height，谁的height大，谁就更大
        """
        self.name = name
        self.age = age
        self.height = height

    def __eq__(self, other):
        return True if self.age == other.age and self.height == other.height else False

    def __ne__(self, other):
        return False if self.age == other.age and self.height == other.height else True

    def __lt__(self, other):
        if self.age < other.age:
            return True
        else:
            if self.age == other.age:
                return True if self.height < other.height else False
            return False

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            if self.age == other.age:
                return True if self.height > other.height else False
            return False

    def __le__(self, other):
        # TODO: 如果self < other为True，那么返回True
        if self.__lt__(other):
            return True
        # TODO: 否则返回 self.eq 结果
        return self.__eq__(other)

    def __ge__(self, other):
        # TODO: 如果self > other为True，那么返回True
        if self.__gt__(other):
            return True
        # TODO: 否则返回 self.__eq__结果
        return self.__eq__(other)


# TODO: __eq__
# p1 = Person('zhiliao', 20, 170)
# p2 = Person('ketang', 20, 170)
# print(p1 == p2)  # TODO: True

# TODO: __ne__
# p1 = Person('zhiliao', 20, 170)
# p2 = Person('ketang', 21, 170)
# print(p1 != p2)  # TODO: True

# TODO: __lt__
# p1 = Person('zhiliao', 21, 169.9)
# p2 = Person('ketang', 21, 170)
# print(p1 < p2)  # TODO: True

# TODO: __gt__
# p1 = Person('zhiliao', 21, 171)
# p2 = Person('ketang', 21, 170)
# print(p1 > p2)  # TODO: True

# TODO: __le__
# p1 = Person('zhiliao', 20, 173)
# p2 = Person('ketang', 21, 172)
# print(p1 <= p2)  # TODO: True

# TODO: __ge__
p1 = Person('zhiliao', 21, 173)
p2 = Person('ketang', 21, 172)
print(p1 >= p2)  # TODO: True
